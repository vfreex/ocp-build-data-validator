# Untitled object in Assembly Schema

```txt
assembly.schema.json#/properties/members
```

Members of the assembly

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly.schema.json\*](../out/assembly.schema.json "open original schema") |

## members Type

`object` ([Details](assembly-properties-members.md))

# members Properties

| Property          | Type    | Required | Nullable       | Defined by                                                                                                                |
| :---------------- | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------ |
| [images](#images) | `array` | Optional | cannot be null | [Assembly](assembly-properties-members-properties-images.md "assembly.schema.json#/properties/members/properties/images") |
| [rpms](#rpms)     | `array` | Optional | cannot be null | [Assembly](assembly-properties-members-properties-rpms.md "assembly.schema.json#/properties/members/properties/rpms")     |

## images



`images`

*   is optional

*   Type: `object[]` ([Assembly Member Image](assembly-properties-members-properties-images-assembly-member-image.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-members-properties-images.md "assembly.schema.json#/properties/members/properties/images")

### images Type

`object[]` ([Assembly Member Image](assembly-properties-members-properties-images-assembly-member-image.md))

## rpms



`rpms`

*   is optional

*   Type: `object[]` ([Assembly Member RPM](assembly-properties-members-properties-rpms-assembly-member-rpm.md))

*   cannot be null

*   defined in: [Assembly](assembly-properties-members-properties-rpms.md "assembly.schema.json#/properties/members/properties/rpms")

### rpms Type

`object[]` ([Assembly Member RPM](assembly-properties-members-properties-rpms-assembly-member-rpm.md))
