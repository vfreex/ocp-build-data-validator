# Assembly Issues Schema

```txt
assembly_issues.schema.json#/properties/issues
```

Bugs and JIRA issues to included or exclude for advisories

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [assembly.schema.json\*](../out/assembly.schema.json "open original schema") |

## issues Type

`object` ([Assembly Issues](assembly-properties-assembly-issues.md))

# issues Properties

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                   |
| :-------------------------------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------- |
| [include](#include)                           | `array`       | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/include")   |
| [include!](#include-1)                        | `array`       | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/include!")  |
| [include?](#include-2)                        | `array`       | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/include?")  |
| [include-](#include-)                         | Not specified | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-include-.md "assembly_issues.schema.json#/properties/include-") |
| [exclude](#exclude)                           | `array`       | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/exclude")   |
| [exclude!](#exclude-1)                        | `array`       | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/exclude!")  |
| [exclude?](#exclude-2)                        | `array`       | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/exclude?")  |
| [exclude-](#exclude-)                         | Not specified | Optional | cannot be null | [Assembly Issues](assembly_issues-properties-exclude-.md "assembly_issues.schema.json#/properties/exclude-") |
| [additionalProperties](#additionalproperties) | Not specified | Optional | cannot be null | [Untitled schema](undefined.md "undefined#undefined")                                                        |

## include

Bugs or JIRA issues to include

`include`

*   is optional

*   Type: `object[]` ([Details](assembly_issues-properties-include-items.md))

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/include")

### include Type

`object[]` ([Details](assembly_issues-properties-include-items.md))

## include!

Bugs or JIRA issues to include

`include!`

*   is optional

*   Type: `object[]` ([Details](assembly_issues-properties-include-items.md))

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/include!")

### include! Type

`object[]` ([Details](assembly_issues-properties-include-items.md))

## include?

Bugs or JIRA issues to include

`include?`

*   is optional

*   Type: `object[]` ([Details](assembly_issues-properties-include-items.md))

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/include?")

### include? Type

`object[]` ([Details](assembly_issues-properties-include-items.md))

## include-



`include-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include-.md "assembly_issues.schema.json#/properties/include-")

### include- Type

unknown

## exclude

Bugs or JIRA issues to include

`exclude`

*   is optional

*   Type: `object[]` ([Details](assembly_issues-properties-include-items.md))

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/exclude")

### exclude Type

`object[]` ([Details](assembly_issues-properties-include-items.md))

## exclude!

Bugs or JIRA issues to include

`exclude!`

*   is optional

*   Type: `object[]` ([Details](assembly_issues-properties-include-items.md))

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/exclude!")

### exclude! Type

`object[]` ([Details](assembly_issues-properties-include-items.md))

## exclude?

Bugs or JIRA issues to include

`exclude?`

*   is optional

*   Type: `object[]` ([Details](assembly_issues-properties-include-items.md))

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-include.md "assembly_issues.schema.json#/properties/exclude?")

### exclude? Type

`object[]` ([Details](assembly_issues-properties-include-items.md))

## exclude-



`exclude-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Issues](assembly_issues-properties-exclude-.md "assembly_issues.schema.json#/properties/exclude-")

### exclude- Type

unknown

## additionalProperties

no description

`additionalProperties`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Untitled schema](undefined.md "undefined#undefined")

### Untitled schema Type

unknown
