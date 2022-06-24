# Untitled object in Assembly Schema

```txt
assembly.schema.json#/properties/permits/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly.schema.json\*](../out/assembly.schema.json "open original schema") |

## items Type

`object` ([Details](assembly-properties-permits-items.md))

# items Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                  |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| [code](#code)           | `string` | Required | cannot be null | [Assembly](assembly-properties-permits-items-properties-code.md "assembly.schema.json#/properties/permits/items/properties/code")           |
| [component](#component) | `string` | Required | cannot be null | [Assembly](assembly-properties-permits-items-properties-component.md "assembly.schema.json#/properties/permits/items/properties/component") |

## code

The error code to permit

`code`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly](assembly-properties-permits-items-properties-code.md "assembly.schema.json#/properties/permits/items/properties/code")

### code Type

`string`

### code Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## component

Name of the component that this permit applies to. Use '\*' to permit all components.

`component`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly](assembly-properties-permits-items-properties-component.md "assembly.schema.json#/properties/permits/items/properties/component")

### component Type

`string`

### component Constraints

**minimum length**: the minimum number of characters for this string is: `1`
