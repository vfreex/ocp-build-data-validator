# Assembly Basis Schema

```txt
assembly_basis.schema.json
```

Basis ties the release to a particular moment, existing release, or another release.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly\_basis.schema.json](../out/assembly_basis.schema.json "open original schema") |

## Assembly Basis Type

`object` ([Assembly Basis](assembly_basis.md))

# Assembly Basis Properties

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                                      |
| :-------------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| [brew\_event](#brew_event)                    | `integer`     | Optional | cannot be null | [Assembly Basis](assembly_basis-properties-brew_event.md "assembly_basis.schema.json#/properties/brew_event")                   |
| [assembly](#assembly)                         | `string`      | Optional | cannot be null | [Assembly Basis](assembly_basis-properties-assembly.md "assembly_basis.schema.json#/properties/assembly")                       |
| [reference\_releases](#reference_releases)    | `object`      | Optional | cannot be null | [Assembly Basis](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/reference_releases")    |
| [reference\_releases!](#reference_releases-1) | `object`      | Optional | cannot be null | [Assembly Basis](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/reference_releases!")   |
| [reference\_releases?](#reference_releases-2) | `object`      | Optional | cannot be null | [Assembly Basis](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/reference_releases?")   |
| [reference\_releases-](#reference_releases-)  | Not specified | Optional | cannot be null | [Assembly Basis](assembly_basis-properties-reference_releases-.md "assembly_basis.schema.json#/properties/reference_releases-") |

## brew\_event

A Brew event that ties the release to a particular moment. Images and rpms will be assembled relative to This basis event.

`brew_event`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Assembly Basis](assembly_basis-properties-brew_event.md "assembly_basis.schema.json#/properties/brew_event")

### brew\_event Type

`integer`

### brew\_event Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## assembly

The parent assembly to inherit from

`assembly`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Basis](assembly_basis-properties-assembly.md "assembly_basis.schema.json#/properties/assembly")

### assembly Type

`string`

### assembly Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## reference\_releases

Indicates this release should be assembled with specified existing release images

`reference_releases`

*   is optional

*   Type: `object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

*   cannot be null

*   defined in: [Assembly Basis](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/reference_releases")

### reference\_releases Type

`object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

## reference\_releases!

Indicates this release should be assembled with specified existing release images

`reference_releases!`

*   is optional

*   Type: `object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

*   cannot be null

*   defined in: [Assembly Basis](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/reference_releases!")

### reference\_releases! Type

`object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

## reference\_releases?

Indicates this release should be assembled with specified existing release images

`reference_releases?`

*   is optional

*   Type: `object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

*   cannot be null

*   defined in: [Assembly Basis](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/reference_releases?")

### reference\_releases? Type

`object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

## reference\_releases-



`reference_releases-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Basis](assembly_basis-properties-reference_releases-.md "assembly_basis.schema.json#/properties/reference_releases-")

### reference\_releases- Type

unknown
