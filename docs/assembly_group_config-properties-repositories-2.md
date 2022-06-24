# Repositories Schema

```txt
repos.schema.json#/properties/repos
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                               |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [assembly\_group\_config.schema.json\*](../out/assembly_group_config.schema.json "open original schema") |

## repos Type

`object` ([Repositories](assembly_group_config-properties-repositories-2.md))

# repos Properties

| Property | Type   | Required | Nullable       | Defined by                                                                     |
| :------- | :----- | :------- | :------------- | :----------------------------------------------------------------------------- |
| `^.+$`   | Merged | Optional | cannot be null | [Repositories](repos-defs-repo.md "repos.schema.json#/patternProperties/^.+$") |

## Pattern: `^.+$`



`^.+$`

*   is optional

*   Type: `object` ([Details](repos-defs-repo.md))

*   cannot be null

*   defined in: [Repositories](repos-defs-repo.md "repos.schema.json#/patternProperties/^.+$")

### ^.+$ Type

`object` ([Details](repos-defs-repo.md))

any of

*   [Untitled undefined type in Repositories](repos-defs-repo-anyof-0.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-anyof-1.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-anyof-2.md "check type definition")

# Repositories Definitions

## Definitions group repo

Reference this group by using

```json
{"$ref":"repos.schema.json#/$defs/repo"}
```

| Property         | Type   | Required | Nullable       | Defined by                                                                                          |
| :--------------- | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------- |
| [conf](#conf)    | Merged | Optional | cannot be null | [Repositories](repos-defs-repo-properties-conf.md "repos.schema.json#/$defs/repo/properties/conf")  |
| [conf!](#conf-1) | Merged | Optional | cannot be null | [Repositories](repos-defs-repo-properties-conf.md "repos.schema.json#/$defs/repo/properties/conf!") |
| [conf?](#conf-2) | Merged | Optional | cannot be null | [Repositories](repos-defs-repo-properties-conf.md "repos.schema.json#/$defs/repo/properties/conf?") |

### conf



`conf`

*   is optional

*   Type: `object` ([Details](repos-defs-repo-properties-conf.md))

*   cannot be null

*   defined in: [Repositories](repos-defs-repo-properties-conf.md "repos.schema.json#/$defs/repo/properties/conf")

#### conf Type

`object` ([Details](repos-defs-repo-properties-conf.md))

any of

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-0.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-1.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-2.md "check type definition")

### conf!



`conf!`

*   is optional

*   Type: `object` ([Details](repos-defs-repo-properties-conf.md))

*   cannot be null

*   defined in: [Repositories](repos-defs-repo-properties-conf.md "repos.schema.json#/$defs/repo/properties/conf!")

#### conf! Type

`object` ([Details](repos-defs-repo-properties-conf.md))

any of

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-0.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-1.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-2.md "check type definition")

### conf?



`conf?`

*   is optional

*   Type: `object` ([Details](repos-defs-repo-properties-conf.md))

*   cannot be null

*   defined in: [Repositories](repos-defs-repo-properties-conf.md "repos.schema.json#/$defs/repo/properties/conf?")

#### conf? Type

`object` ([Details](repos-defs-repo-properties-conf.md))

any of

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-0.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-1.md "check type definition")

*   [Untitled undefined type in Repositories](repos-defs-repo-properties-conf-anyof-2.md "check type definition")
