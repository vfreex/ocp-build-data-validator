# Untitled object in Assembly Issues Schema

```txt
assembly_issues.schema.json#/properties/include/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly\_issues.schema.json\*](../out/assembly_issues.schema.json "open original schema") |

## items Type

`object` ([Details](assembly_issues-properties-include-items.md))

# items Properties

| Property  | Type   | Required | Nullable       | Defined by                                                                                                                                         |
| :-------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id) | Merged | Required | cannot be null | [Assembly Issues](assembly_issues-properties-include-items-properties-id.md "assembly_issues.schema.json#/properties/include/items/properties/id") |

## id

Bug ID (integer) or JIRA issue key (string)

`id`

*   is required

*   Type: merged type ([Details](assembly_issues-properties-include-items-properties-id.md))

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include-items-properties-id.md "assembly_issues.schema.json#/properties/include/items/properties/id")

### id Type

merged type ([Details](assembly_issues-properties-include-items-properties-id.md))

one (and only one) of

*   [Untitled string in Assembly Issues](assembly_issues-properties-include-items-properties-id-oneof-0.md "check type definition")

*   [Untitled integer in Assembly Issues](assembly_issues-properties-include-items-properties-id-oneof-1.md "check type definition")
