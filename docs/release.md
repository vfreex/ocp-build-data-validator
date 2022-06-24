# Release Schema

```txt
release.schema.json
```

A release

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [release.schema.json](../out/release.schema.json "open original schema") |

## Release Type

`object` ([Release](release.md))

# Release Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                            |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------ |
| [assembly](#assembly) | `object` | Required | cannot be null | [Release](release-properties-assembly.md "assembly.schema.json#/properties/assembly") |

## assembly

An assembly represents unambiguous, programmatic instructions on how to build and rebuild a release payload at any point in the future.

`assembly`

*   is required

*   Type: `object` ([Assembly](release-properties-assembly.md))

*   cannot be null

*   defined in: [Release](release-properties-assembly.md "assembly.schema.json#/properties/assembly")

### assembly Type

`object` ([Assembly](release-properties-assembly.md))
