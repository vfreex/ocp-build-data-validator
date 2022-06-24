# RHCOS Schema

```txt
rhcos.schema.json#/properties/rhcos
```

RHCOS images for the assembly.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly.schema.json\*](../out/assembly.schema.json "open original schema") |

## rhcos Type

`object` ([RHCOS](assembly-properties-rhcos.md))

any of

*   [Untitled undefined type in RHCOS](rhcos-anyof-0.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-anyof-1.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-anyof-2.md "check type definition")

# rhcos Properties

| Property                                     | Type          | Required | Nullable       | Defined by                                                                                                                         |
| :------------------------------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| [machine-os-content](#machine-os-content)    | Merged        | Optional | cannot be null | [RHCOS](rhcos-properties-machine-os-content.md "rhcos.schema.json#/properties/machine-os-content")                                 |
| [machine-os-content!](#machine-os-content-1) | Merged        | Optional | cannot be null | [RHCOS](rhcos-properties-machine-os-content.md "rhcos.schema.json#/properties/machine-os-content!")                                |
| [machine-os-content?](#machine-os-content-2) | Merged        | Optional | cannot be null | [RHCOS](rhcos-properties-machine-os-content.md "rhcos.schema.json#/properties/machine-os-content?")                                |
| [dependencies](#dependencies)                | Merged        | Optional | cannot be null | [RHCOS](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies")  |
| [dependencies!](#dependencies-1)             | Merged        | Optional | cannot be null | [RHCOS](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies!") |
| [dependencies?](#dependencies-2)             | Merged        | Optional | cannot be null | [RHCOS](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies?") |
| [dependencies-](#dependencies-)              | Not specified | Optional | cannot be null | [RHCOS](rhcos-properties-dependencies-.md "rhcos.schema.json#/properties/dependencies-")                                           |

## machine-os-content



`machine-os-content`

*   is optional

*   Type: `object` ([Details](rhcos-properties-machine-os-content.md))

*   cannot be null

*   defined in: [RHCOS](rhcos-properties-machine-os-content.md "rhcos.schema.json#/properties/machine-os-content")

### machine-os-content Type

`object` ([Details](rhcos-properties-machine-os-content.md))

any of

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-0.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-1.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-2.md "check type definition")

## machine-os-content!



`machine-os-content!`

*   is optional

*   Type: `object` ([Details](rhcos-properties-machine-os-content.md))

*   cannot be null

*   defined in: [RHCOS](rhcos-properties-machine-os-content.md "rhcos.schema.json#/properties/machine-os-content!")

### machine-os-content! Type

`object` ([Details](rhcos-properties-machine-os-content.md))

any of

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-0.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-1.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-2.md "check type definition")

## machine-os-content?



`machine-os-content?`

*   is optional

*   Type: `object` ([Details](rhcos-properties-machine-os-content.md))

*   cannot be null

*   defined in: [RHCOS](rhcos-properties-machine-os-content.md "rhcos.schema.json#/properties/machine-os-content?")

### machine-os-content? Type

`object` ([Details](rhcos-properties-machine-os-content.md))

any of

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-0.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-1.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-properties-machine-os-content-anyof-2.md "check type definition")

## dependencies



`dependencies`

*   is optional

*   Type: `object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

*   cannot be null

*   defined in: [RHCOS](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies")

### dependencies Type

`object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

any of

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-0.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-1.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-2.md "check type definition")

## dependencies!



`dependencies!`

*   is optional

*   Type: `object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

*   cannot be null

*   defined in: [RHCOS](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies!")

### dependencies! Type

`object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

any of

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-0.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-1.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-2.md "check type definition")

## dependencies?



`dependencies?`

*   is optional

*   Type: `object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

*   cannot be null

*   defined in: [RHCOS](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies?")

### dependencies? Type

`object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

any of

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-0.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-1.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-2.md "check type definition")

## dependencies-



`dependencies-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [RHCOS](rhcos-properties-dependencies-.md "rhcos.schema.json#/properties/dependencies-")

### dependencies- Type

unknown
