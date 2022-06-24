# Assembly Dependencies Schema

```txt
assembly_dependencies.schema.json
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                            |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly\_dependencies.schema.json](../out/assembly_dependencies.schema.json "open original schema") |

## Assembly Dependencies Type

`object` ([Assembly Dependencies](assembly_dependencies.md))

any of

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-0.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-1.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-2.md "check type definition")

# Assembly Dependencies Properties

| Property         | Type    | Required | Nullable       | Defined by                                                                                                                          |
| :--------------- | :------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| [rpms](#rpms)    | `array` | Optional | cannot be null | [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies.md "assembly_dependencies.schema.json#/properties/rpms")  |
| [rpms!](#rpms-1) | `array` | Optional | cannot be null | [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies.md "assembly_dependencies.schema.json#/properties/rpms!") |
| [rpms?](#rpms-2) | `array` | Optional | cannot be null | [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies.md "assembly_dependencies.schema.json#/properties/rpms?") |

## rpms



`rpms`

*   is optional

*   Type: `object[]` ([Details](assembly_dependencies-properties-rpm-dependencies-items.md))

*   cannot be null

*   defined in: [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies.md "assembly_dependencies.schema.json#/properties/rpms")

### rpms Type

`object[]` ([Details](assembly_dependencies-properties-rpm-dependencies-items.md))

## rpms!



`rpms!`

*   is optional

*   Type: `object[]` ([Details](assembly_dependencies-properties-rpm-dependencies-items.md))

*   cannot be null

*   defined in: [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies.md "assembly_dependencies.schema.json#/properties/rpms!")

### rpms! Type

`object[]` ([Details](assembly_dependencies-properties-rpm-dependencies-items.md))

## rpms?



`rpms?`

*   is optional

*   Type: `object[]` ([Details](assembly_dependencies-properties-rpm-dependencies-items.md))

*   cannot be null

*   defined in: [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies.md "assembly_dependencies.schema.json#/properties/rpms?")

### rpms? Type

`object[]` ([Details](assembly_dependencies-properties-rpm-dependencies-items.md))
