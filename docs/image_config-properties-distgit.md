# Untitled object in Image Configuration Schema

```txt
image_config.base.schema.json#/properties/distgit?
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [image\_config.base.schema.json\*](../out/image_config.base.schema.json "open original schema") |

## distgit? Type

`object` ([Details](image_config-properties-distgit.md))

# distgit? Properties

| Property                                  | Type          | Required | Nullable       | Defined by                                                                                                                                                              |
| :---------------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [namespace](#namespace)                   | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-namespace.md "image_config.base.schema.json#/properties/distgit/properties/namespace")                 |
| [namespace!](#namespace-1)                | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-namespace.md "image_config.base.schema.json#/properties/distgit/properties/namespace!")                |
| [namespace?](#namespace-2)                | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-namespace.md "image_config.base.schema.json#/properties/distgit/properties/namespace?")                |
| [namespace-](#namespace-)                 | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-namespace-.md "image_config.base.schema.json#/properties/distgit/properties/namespace-")               |
| [component](#component)                   | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-component.md "image_config.base.schema.json#/properties/distgit/properties/component")                 |
| [component!](#component-1)                | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-component.md "image_config.base.schema.json#/properties/distgit/properties/component!")                |
| [component?](#component-2)                | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-component.md "image_config.base.schema.json#/properties/distgit/properties/component?")                |
| [component-](#component-)                 | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-component-.md "image_config.base.schema.json#/properties/distgit/properties/component-")               |
| [bundle\_component](#bundle_component)    | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-bundle_component.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component")   |
| [bundle\_component!](#bundle_component-1) | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-bundle_component.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component!")  |
| [bundle\_component?](#bundle_component-2) | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-bundle_component.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component?")  |
| [bundle\_component-](#bundle_component-)  | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-bundle_component-.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component-") |
| [branch](#branch)                         | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-branch.md "image_config.base.schema.json#/properties/distgit/properties/branch")                       |
| [branch!](#branch-1)                      | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-branch.md "image_config.base.schema.json#/properties/distgit/properties/branch!")                      |
| [branch?](#branch-2)                      | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-branch.md "image_config.base.schema.json#/properties/distgit/properties/branch?")                      |
| [branch-](#branch-)                       | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-properties-branch-.md "image_config.base.schema.json#/properties/distgit/properties/branch-")                     |

## namespace



`namespace`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-namespace.md "image_config.base.schema.json#/properties/distgit/properties/namespace")

### namespace Type

`string`

### namespace Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"apbs"`       |             |
| `"containers"` |             |
| `"rpms"`       |             |

## namespace!



`namespace!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-namespace.md "image_config.base.schema.json#/properties/distgit/properties/namespace!")

### namespace! Type

`string`

### namespace! Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"apbs"`       |             |
| `"containers"` |             |
| `"rpms"`       |             |

## namespace?



`namespace?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-namespace.md "image_config.base.schema.json#/properties/distgit/properties/namespace?")

### namespace? Type

`string`

### namespace? Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"apbs"`       |             |
| `"containers"` |             |
| `"rpms"`       |             |

## namespace-



`namespace-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-namespace-.md "image_config.base.schema.json#/properties/distgit/properties/namespace-")

### namespace- Type

unknown

## component



`component`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-component.md "image_config.base.schema.json#/properties/distgit/properties/component")

### component Type

`string`

### component Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## component!



`component!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-component.md "image_config.base.schema.json#/properties/distgit/properties/component!")

### component! Type

`string`

### component! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## component?



`component?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-component.md "image_config.base.schema.json#/properties/distgit/properties/component?")

### component? Type

`string`

### component? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## component-



`component-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-component-.md "image_config.base.schema.json#/properties/distgit/properties/component-")

### component- Type

unknown

## bundle\_component



`bundle_component`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-bundle_component.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component")

### bundle\_component Type

`string`

### bundle\_component Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## bundle\_component!



`bundle_component!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-bundle_component.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component!")

### bundle\_component! Type

`string`

### bundle\_component! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## bundle\_component?



`bundle_component?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-bundle_component.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component?")

### bundle\_component? Type

`string`

### bundle\_component? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## bundle\_component-



`bundle_component-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-bundle_component-.md "image_config.base.schema.json#/properties/distgit/properties/bundle_component-")

### bundle\_component- Type

unknown

## branch



`branch`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-branch.md "image_config.base.schema.json#/properties/distgit/properties/branch")

### branch Type

`string`

### branch Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## branch!



`branch!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-branch.md "image_config.base.schema.json#/properties/distgit/properties/branch!")

### branch! Type

`string`

### branch! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## branch?



`branch?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-branch.md "image_config.base.schema.json#/properties/distgit/properties/branch?")

### branch? Type

`string`

### branch? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## branch-



`branch-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-properties-branch-.md "image_config.base.schema.json#/properties/distgit/properties/branch-")

### branch- Type

unknown
