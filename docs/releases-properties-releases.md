# Untitled object in Releases Schema

```txt
releases.schema.json#/properties/releases
```

An object containing all releases in a group.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [releases.schema.json\*](../out/releases.schema.json "open original schema") |

## releases Type

`object` ([Details](releases-properties-releases.md))

# releases Properties

| Property                                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                       |
| :---------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `^stream$\|^test$\|^art\d+$\|^\d+\.\d+\.\d+$\|^[fr]c\.\d+$` | `object` | Optional | cannot be null | [Releases](releases-properties-releases-patternproperties-release.md "release.schema.json#/properties/releases/patternProperties/^stream$\|^test$\|^art\d+$\|^\d+\\.\d+\\.\d+$\|^\[fr]c\\.\d+$") |

## Pattern: `^stream$|^test$|^art\d+$|^\d+\.\d+\.\d+$|^[fr]c\.\d+$`

A release

`^stream$|^test$|^art\d+$|^\d+\.\d+\.\d+$|^[fr]c\.\d+$`

*   is optional

*   Type: `object` ([Release](releases-properties-releases-patternproperties-release.md))

*   cannot be null

*   defined in: [Releases](releases-properties-releases-patternproperties-release.md "release.schema.json#/properties/releases/patternProperties/^stream$|^test$|^art\d+$|^\d+\\.\d+\\.\d+$|^\[fr]c\\.\d+$")

### ^stream$|^test$|^art\d+$|^\d+\\.\d+\\.\d+$|^\[fr]c\\.\d+$ Type

`object` ([Release](releases-properties-releases-patternproperties-release.md))
