# Assembly Member Image Schema

```txt
member_image.schema.json
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [member\_image.schema.json](../out/member_image.schema.json "open original schema") |

## Assembly Member Image Type

`object` ([Assembly Member Image](member_image.md))

# Assembly Member Image Properties

| Property                     | Type     | Required | Nullable       | Defined by                                                                                                                   |
| :--------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| [distgit\_key](#distgit_key) | `string` | Required | cannot be null | [Assembly Member Image](member_image-properties-distgit_key.md "member_image.schema.json#/properties/distgit_key")           |
| [why](#why)                  | `string` | Required | cannot be null | [Assembly Member Image](member_image-properties-why.md "member_image.schema.json#/properties/why")                           |
| [metadata](#metadata)        | `object` | Optional | cannot be null | [Assembly Member Image](member_image-properties-image-configuration.md "image_config.base.schema.json#/properties/metadata") |

## distgit\_key



`distgit_key`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Member Image](member_image-properties-distgit_key.md "member_image.schema.json#/properties/distgit_key")

### distgit\_key Type

`string`

### distgit\_key Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## why



`why`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Member Image](member_image-properties-why.md "member_image.schema.json#/properties/why")

### why Type

`string`

### why Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## metadata

Image configuration

`metadata`

*   is optional

*   Type: `object` ([Image Configuration](member_image-properties-image-configuration.md))

*   cannot be null

*   defined in: [Assembly Member Image](member_image-properties-image-configuration.md "image_config.base.schema.json#/properties/metadata")

### metadata Type

`object` ([Image Configuration](member_image-properties-image-configuration.md))
