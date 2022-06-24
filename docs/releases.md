# Releases Schema

```txt
releases.schema.json
```

Releases object contains information on every release that ART promotes as GA and every custom hotfix it delivers to customers.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [releases.schema.json](../out/releases.schema.json "open original schema") |

## Releases Type

`object` ([Releases](releases.md))

# Releases Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                              |
| :-------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------- |
| [releases](#releases) | `object` | Required | cannot be null | [Releases](releases-properties-releases.md "releases.schema.json#/properties/releases") |

## releases

An object containing all releases in a group.

`releases`

*   is required

*   Type: `object` ([Details](releases-properties-releases.md))

*   cannot be null

*   defined in: [Releases](releases-properties-releases.md "releases.schema.json#/properties/releases")

### releases Type

`object` ([Details](releases-properties-releases.md))
