import json
from pathlib import Path
from jsonschema import RefResolver, Draft202012Validator, ValidationError
from jsonschema.validators import validator_for
from validator.schema.image_schema import IMAGE_CONTENT_SCHEMA
from validator.schema.rpm_schema import RPM_CONTENT_SCHEMA
from validator.schema.streams_schema import STREAMS_SCHEMA

from schema import And, Optional, Or, Regex, Schema, SchemaError

GIT_SSH_URL_REGEX = r'((git@[\w\.]+))([\w\.@\:/\-~]+)(\.git)(/)?'
UPGRADE_EDGES_REGEX = r'\d+\.\d+\.\d+(?:-[fr]c\.\d+)?(,\d+\.\d+\.\d+(?:-[fr]c\.\d+)?)*'

ASSEMBLY_DEPENDENCIES = {
    'rpms': [
        And({
            Regex(r'el\d+'): str,  # Each RHEL version can have its own
            'why': str,  # Human description of why this is being added for historical purposes
            'non_gc_tag': str,  # Artist should provide tag they know will prevent this NVR from garbage collection.
        })
    ]
}

ASSEMBLY_NAME_REGEX = Or(Regex(r'^art\d+$'), Regex(r'^\d+\.\d+\.\d+$'), Regex(r'^rc\.\d+$'), Regex(r'^fc\.\d+$'))
ARCHES = Or('x86_64', 'ppc64le', 's390x', 'aarch64')
ARCHES_DICT = {
    Optional('x86_64'): str,
    Optional('s390x'): str,
    Optional('ppc64le'): str,
    Optional('aarch64'): str,
}

def releases_schema(file):
    return Schema({
        'releases': {
            Optional(Or('stream', 'test', ASSEMBLY_NAME_REGEX)): {
                'assembly': {
                    Optional('type'): Or('standard', 'custom', 'candidate', 'stream'),
                    Optional('basis'): {
                        Optional('brew_event'): int,
                        Optional('assembly'): ASSEMBLY_NAME_REGEX,

                        # If specified, when generating a release payload, "oc adm release new" will be run with from-release.
                        # However, the basis brew_event is still king and all images found in the nightlies
                        # must align perfectly with the basis & machine-os-content images of the assembly
                        # or an error will be thrown. Why? Nightly records can be lost. We need to be able to
                        # reconstruct from a source of truth.
                        # If not specified, oc release new will not be passed from-release.
                        Optional('reference_releases'): ARCHES_DICT,  # per-arch nightly names
                    },
                    Optional('permits'): [  # A list of issues that this assembly permits during payload generation.
                        And({
                            'code': Regex('[A-Z0-9_]+'),
                            'component': str,  # A component name or '*'
                        })
                    ],
                    Optional('rhcos'): {
                        'machine-os-content': {
                            'images': ARCHES_DICT,  # pullspecs for arch specific images
                        },
                        Optional('dependencies'): ASSEMBLY_DEPENDENCIES,
                    },
                    Optional('streams'): STREAMS_SCHEMA,
                    Optional('group'): {
                        Optional('arches'): [ARCHES],
                        Optional('repos'): {
                            Regex('[a-z0-9.-]+'): {
                                'conf': {
                                    'baseurl': {
                                        ARCHES: str,
                                    }
                                }
                            }
                        },
                        Optional('advisories'): {
                            Optional('image'): int,
                            Optional('rpm'): int,
                            Optional('extras'): int,
                            Optional('metadata'): int,
                        },
                        Optional('dependencies'): ASSEMBLY_DEPENDENCIES,
                        Optional('release_jira'): str,
                        Optional('upgrades'): Regex(UPGRADE_EDGES_REGEX),
                    },
                    Optional('members'): {
                        Optional('rpms'): [
                            And({
                                'distgit_key': str,
                                'why': str,  # Human description of why this is being added for historical purposes
                                Optional('metadata'): {
                                    Optional('content'): RPM_CONTENT_SCHEMA,
                                    Optional('is'): {
                                        Regex(r'el\d+'): str
                                    }
                                },
                            })
                        ],
                        Optional('images'): [
                            And({
                                'distgit_key': str,
                                'why': str,  # Human description of why this is being added for historical purposes
                                Optional('metadata'): {
                                    Optional('container_yaml'): object,
                                    Optional('content'): IMAGE_CONTENT_SCHEMA,
                                    Optional('dependencies'): ASSEMBLY_DEPENDENCIES,
                                    Optional('is'): {
                                        'nvr': str
                                    },
                                },
                            })
                        ]
                    },
                    Optional('issues'): {
                        Optional('include'): [
                            And({
                                'id': Or(int, Regex(r'[A-Z]+-\d+'))  # bugzilla or Jira
                            })
                        ],
                        Optional('exclude'): [
                            And({
                                'id': Or(int, Regex(r'[A-Z]+-\d+'))  # bugzilla or Jira
                            })
                        ],
                    },
                },
            }
        }
    })


def _demerge(data):
    # recursively turn dict meta-attrs ("!?-") that are merged for inheritance into regular attrs just for schema validation
    if type(data) in [bool, int, float, str, bytes, type(None)]:
        return data

    if type(data) is list:
        return [_demerge(item) for item in data]

    if type(data) is dict:
        new_data = {}
        for name, value in data.items():
            if name[-1] in ("!", "?", "-"):
                merged_name = name[:-1]
                if merged_name in data:
                    raise SchemaError(f"Cannot specify '{name}' and '{merged_name}' attrs in same dict")
                name = merged_name

            new_data[name] = _demerge(value)

        return new_data

    raise TypeError(f"Unexpected value type: {type(data)}: {data}")

import sys

if sys.version_info < (3, 9):
    # importlib.resources either doesn't exist or lacks the files()
    # function, so use the PyPI version:
    import importlib_resources
else:
    # importlib.resources has files(), so use that:
    import importlib.resources as importlib_resources

def validate(file, data):
    pkg = importlib_resources.files("validator")
    schemas = {source.name: json.load(open(source)) for source in (pkg / "schemas").iterdir() if source.name.endswith(".json")}
    schema_store = {schema.get("$id", filename): schema for filename, schema in schemas.items()}
    schema = schema_store["releases.schema.json"]
    resolver = RefResolver.from_schema(schema, store=schema_store)
    #validator = Draft202012Validator(schema, resolver=resolver)
    validator = validator_for(schema)(schema, resolver=resolver)
    try:
        validator.validate(data)
    except ValidationError as err:
        return str(err)
