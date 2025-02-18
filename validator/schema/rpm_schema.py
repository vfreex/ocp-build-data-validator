from schema import Schema, Optional, And, Or, Regex, SchemaError

valid_modes = [
    'auto',
    'disabled',
    'wip',
]

rpm_schema = Schema({
    'content': {
        Optional('build'): {
            'use_source_tito_config': bool,
            'tito_target': And(str, len),
            'push_release_commit': bool,
        },
        Optional('source'): {
            Optional('alias'): And(str, len),
            Optional('git'): {
                'branch': {
                    'fallback': And(str, len),
                    'target': And(str, len),
                },
                'url': And(str, len),
            },
            'specfile': Regex(r'.+\.spec$'),
        },
    },
    Optional('enabled_repos'): [
        And(str, len),
    ],
    Optional('mode'): Or(*valid_modes),
    'name': And(str, len),
    'owners': [
        And(str, len)
    ],
})


def validate(_, data):
    try:
        rpm_schema.validate(data)
    except SchemaError as err:
        return '{}'.format(err)
