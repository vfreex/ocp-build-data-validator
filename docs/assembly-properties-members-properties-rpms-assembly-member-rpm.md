# Assembly Member RPM Schema

```txt
member_rpm.schema.json#/properties/members/properties/rpms/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly.schema.json\*](../out/assembly.schema.json "open original schema") |

## items Type

`object` ([Assembly Member RPM](assembly-properties-members-properties-rpms-assembly-member-rpm.md))

# items Properties

| Property                     | Type     | Required | Nullable       | Defined by                                                                                                   |
| :--------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------- |
| [distgit\_key](#distgit_key) | `string` | Required | cannot be null | [Assembly Member RPM](member_rpm-properties-distgit_key.md "member_rpm.schema.json#/properties/distgit_key") |
| [why](#why)                  | `string` | Required | cannot be null | [Assembly Member RPM](member_rpm-properties-why.md "member_rpm.schema.json#/properties/why")                 |
| [metadata](#metadata)        | `object` | Optional | cannot be null | [Assembly Member RPM](member_rpm-properties-metadata.md "member_rpm.schema.json#/properties/metadata")       |

## distgit\_key



`distgit_key`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Member RPM](member_rpm-properties-distgit_key.md "member_rpm.schema.json#/properties/distgit_key")

### distgit\_key Type

`string`

### distgit\_key Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## why



`why`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Member RPM](member_rpm-properties-why.md "member_rpm.schema.json#/properties/why")

### why Type

`string`

### why Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](member_rpm-properties-metadata.md))

*   cannot be null

*   defined in: [Assembly Member RPM](member_rpm-properties-metadata.md "member_rpm.schema.json#/properties/metadata")

### metadata Type

`object` ([Details](member_rpm-properties-metadata.md))
