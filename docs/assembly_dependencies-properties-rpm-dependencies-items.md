# Untitled object in Assembly Dependencies Schema

```txt
assembly_dependencies.schema.json#/properties/rpms/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly\_dependencies.schema.json\*](../out/assembly_dependencies.schema.json "open original schema") |

## items Type

`object` ([Details](assembly_dependencies-properties-rpm-dependencies-items.md))

## items Constraints

**minimum number of properties**: the minimum number of properties for this object is: `3`

# items Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                             |
| :-------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [why](#why)                 | `string` | Required | cannot be null | [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies-items-properties-why.md "assembly_dependencies.schema.json#/properties/rpms/items/properties/why")                           |
| [non\_gc\_tag](#non_gc_tag) | `string` | Required | cannot be null | [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies-items-properties-non_gc_tag.md "assembly_dependencies.schema.json#/properties/rpms/items/properties/non_gc_tag")             |
| `^el\d+[!?-]?$`             | `string` | Optional | cannot be null | [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies-items-patternproperties-eld-.md "assembly_dependencies.schema.json#/properties/rpms/items/patternProperties/^el\d+\[!?-]?$") |

## why



`why`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies-items-properties-why.md "assembly_dependencies.schema.json#/properties/rpms/items/properties/why")

### why Type

`string`

## non\_gc\_tag



`non_gc_tag`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies-items-properties-non_gc_tag.md "assembly_dependencies.schema.json#/properties/rpms/items/properties/non_gc_tag")

### non\_gc\_tag Type

`string`

## Pattern: `^el\d+[!?-]?$`



`^el\d+[!?-]?$`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Dependencies](assembly_dependencies-properties-rpm-dependencies-items-patternproperties-eld-.md "assembly_dependencies.schema.json#/properties/rpms/items/patternProperties/^el\d+\[!?-]?$")

### ^el\d+\[!?-]?$ Type

`string`
