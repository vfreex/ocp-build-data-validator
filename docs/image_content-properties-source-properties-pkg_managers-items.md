# Untitled string in Image Content Schema

```txt
image_content.base.schema.json#/properties/source/properties/pkg_managers/items
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [image\_content.base.schema.json\*](../out/image_content.base.schema.json "open original schema") |

## items Type

`string`

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"gomod"`         |             |
| `"pip"`           |             |
| `"npm"`           |             |
| `"yarn"`          |             |
| `"git-submodule"` |             |
