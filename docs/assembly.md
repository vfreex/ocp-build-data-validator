# Assembly Schema

```txt
assembly.schema.json
```

An assembly represents unambiguous, programmatic instructions on how to build and rebuild a release payload at any point in the future.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly.schema.json](../out/assembly.schema.json "open original schema") |

## Assembly Type

`object` ([Assembly](assembly.md))

# Assembly Properties

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                            |
| :--------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                            | `string` | Optional | cannot be null | [Assembly](assembly-properties-type.md "assembly.schema.json#/properties/type")                                       |
| [basis](#basis)                          | `object` | Optional | cannot be null | [Assembly](assembly-properties-assembly-basis.md "assembly_basis.schema.json#/properties/basis")                      |
| [group](#group)                          | `object` | Optional | cannot be null | [Assembly](assembly-properties-assembly-group-configuration.md "assembly_group_config.schema.json#/properties/group") |
| [members](#members)                      | `object` | Optional | cannot be null | [Assembly](assembly-properties-members.md "assembly.schema.json#/properties/members")                                 |
| [rhcos](#rhcos)                          | Merged   | Optional | cannot be null | [Assembly](assembly-properties-rhcos.md "rhcos.schema.json#/properties/rhcos")                                        |
| [streams](#streams)                      | `object` | Optional | cannot be null | [Assembly](assembly-properties-streams.md "streams.schema.json#/properties/streams")                                  |
| [permits](#permits)                      | `array`  | Optional | cannot be null | [Assembly](assembly-properties-permits.md "assembly.schema.json#/properties/permits")                                 |
| [promotion\_permits](#promotion_permits) | `array`  | Optional | cannot be null | [Assembly](assembly-properties-promotion_permits.md "assembly.schema.json#/properties/promotion_permits")             |
| [issues](#issues)                        | `object` | Optional | cannot be null | [Assembly](assembly-properties-assembly-issues.md "assembly_issues.schema.json#/properties/issues")                   |

## type

Type of the assembly. Default value: stream

`type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly](assembly-properties-type.md "assembly.schema.json#/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | :---------- |
| `"stream"`    |             |
| `"standard"`  |             |
| `"candidate"` |             |
| `"custom"`    |             |

## basis

Basis ties the release to a particular moment, existing release, or another release.

`basis`

*   is optional

*   Type: `object` ([Assembly Basis](assembly-properties-assembly-basis.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-assembly-basis.md "assembly_basis.schema.json#/properties/basis")

### basis Type

`object` ([Assembly Basis](assembly-properties-assembly-basis.md))

## group

Group configuration overrides for the assembly

`group`

*   is optional

*   Type: `object` ([Assembly Group Configuration](assembly-properties-assembly-group-configuration.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-assembly-group-configuration.md "assembly_group_config.schema.json#/properties/group")

### group Type

`object` ([Assembly Group Configuration](assembly-properties-assembly-group-configuration.md))

## members

Members of the assembly

`members`

*   is optional

*   Type: `object` ([Details](assembly-properties-members.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-members.md "assembly.schema.json#/properties/members")

### members Type

`object` ([Details](assembly-properties-members.md))

## rhcos

RHCOS images for the assembly.

`rhcos`

*   is optional

*   Type: `object` ([RHCOS](assembly-properties-rhcos.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-rhcos.md "rhcos.schema.json#/properties/rhcos")

### rhcos Type

`object` ([RHCOS](assembly-properties-rhcos.md))

any of

*   [Untitled undefined type in RHCOS](rhcos-anyof-0.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-anyof-1.md "check type definition")

*   [Untitled undefined type in RHCOS](rhcos-anyof-2.md "check type definition")

## streams



`streams`

*   is optional

*   Type: `object` ([Streams](assembly-properties-streams.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-streams.md "streams.schema.json#/properties/streams")

### streams Type

`object` ([Streams](assembly-properties-streams.md))

## permits

Permits assembly errors. See <https://github.com/openshift-eng/art-docs/blob/master/content/assemblies.md#permissible-issues> for more information.

`permits`

*   is optional

*   Type: `object[]` ([Details](assembly-properties-permits-items.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-permits.md "assembly.schema.json#/properties/permits")

### permits Type

`object[]` ([Details](assembly-properties-permits-items.md))

## promotion\_permits

Permits promotion errors. See <https://github.com/openshift/aos-cd-jobs/tree/master/jobs/build/promote-assembly#permit-certain-validation-failures> for more information.

`promotion_permits`

*   is optional

*   Type: `object[]` ([Details](assembly-properties-promotion_permits-items.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-promotion_permits.md "assembly.schema.json#/properties/promotion_permits")

### promotion\_permits Type

`object[]` ([Details](assembly-properties-promotion_permits-items.md))

## issues

Bugs and JIRA issues to included or exclude for advisories

`issues`

*   is optional

*   Type: `object` ([Assembly Issues](assembly-properties-assembly-issues.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-assembly-issues.md "assembly_issues.schema.json#/properties/issues")

### issues Type

`object` ([Assembly Issues](assembly-properties-assembly-issues.md))
