# Untitled object in RHCOS Schema

```txt
rhcos.schema.json#/properties/machine-os-content?
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [rhcos.schema.json\*](../out/rhcos.schema.json "open original schema") |

## machine-os-content? Type

`object` ([Details](rhcos-properties-machine-os-content.md))

any of

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-0.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-1.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-2.md "check type definition")

# machine-os-content? Properties

| Property             | Type     | Required | Nullable       | Defined by                                                                                                                             |
| :------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| [images](#images)    | `object` | Optional | cannot be null | [RHCOS](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/machine-os-content/properties/images")  |
| [images!](#images-1) | `object` | Optional | cannot be null | [RHCOS](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/machine-os-content/properties/images!") |
| [images?](#images-2) | `object` | Optional | cannot be null | [RHCOS](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/machine-os-content/properties/images?") |

## images

Indicates this release should be assembled with specified existing release images

`images`

*   is optional

*   Type: `object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

*   cannot be null

*   defined in: [RHCOS](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/machine-os-content/properties/images")

### images Type

`object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

## images!

Indicates this release should be assembled with specified existing release images

`images!`

*   is optional

*   Type: `object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

*   cannot be null

*   defined in: [RHCOS](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/machine-os-content/properties/images!")

### images! Type

`object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

## images?

Indicates this release should be assembled with specified existing release images

`images?`

*   is optional

*   Type: `object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))

*   cannot be null

*   defined in: [RHCOS](assembly_basis-properties-architectures-dict-2.md "arches_dict.schema.json#/properties/machine-os-content/properties/images?")

### images? Type

`object` ([Architectures Dict](assembly_basis-properties-architectures-dict-2.md))
