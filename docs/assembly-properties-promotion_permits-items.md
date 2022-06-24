# Untitled object in Assembly Schema

```txt
assembly.schema.json#/properties/promotion_permits/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly.schema.json\*](../out/assembly.schema.json "open original schema") |

## items Type

`object` ([Details](assembly-properties-promotion_permits-items.md))

# items Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                            |
| :------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [code](#code) | `string` | Required | cannot be null | [Assembly](assembly-properties-promotion_permits-items-properties-code.md "assembly.schema.json#/properties/promotion_permits/items/properties/code") |
| [why](#why)   | `string` | Required | cannot be null | [Assembly](assembly-properties-promotion_permits-items-properties-why.md "assembly.schema.json#/properties/promotion_permits/items/properties/why")   |

## code

The error code to permit

`code`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly](assembly-properties-promotion_permits-items-properties-code.md "assembly.schema.json#/properties/promotion_permits/items/properties/code")

### code Type

`string`

### code Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## why

The reason why this error should be permitted. Note this text is public. Don't include customer related or confidential information.

`why`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly](assembly-properties-promotion_permits-items-properties-why.md "assembly.schema.json#/properties/promotion_permits/items/properties/why")

### why Type

`string`

### why Constraints

**minimum length**: the minimum number of characters for this string is: `1`
