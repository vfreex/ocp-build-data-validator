# Untitled object in Image Content Schema

```txt
image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs!
```

Configuration for creating PRs to align upstream dockerfiles w/ ART

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [image\_content.base.schema.json\*](../out/image_content.base.schema.json "open original schema") |

## streams\_prs! Type

`object` ([Details](image_content-properties-source-properties-ci_alignment-properties-streams_prs.md))

# streams\_prs! Properties

| Property                             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :----------------------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ci\_build\_root](#ci_build_root)    | `object`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root")   |
| [ci\_build\_root?](#ci_build_root-1) | `object`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root?")  |
| [ci\_build\_root!](#ci_build_root-2) | `object`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root!")  |
| [ci\_build\_root-](#ci_build_root-)  | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root-") |
| [enabled](#enabled)                  | `boolean`     | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled")               |
| [enabled?](#enabled-1)               | `boolean`     | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled?")              |
| [enabled!](#enabled-2)               | `boolean`     | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled!")              |
| [enabled-](#enabled-)                | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled-")             |
| [auto\_label](#auto_label)           | `array`       | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label")         |
| [auto\_label?](#auto_label-1)        | `array`       | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label?")        |
| [auto\_label!](#auto_label-2)        | `array`       | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label!")        |
| [auto\_label-](#auto_label-)         | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label-")       |
| [from](#from)                        | `array`       | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from")                     |
| [from?](#from-1)                     | `array`       | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from?")                    |
| [from!](#from-2)                     | `array`       | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from!")                    |
| [from-](#from-)                      | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from-")                   |
| [merge\_first](#merge_first)         | `boolean`     | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first")       |
| [merge\_first?](#merge_first-1)      | `boolean`     | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first?")      |
| [merge\_first!](#merge_first-2)      | `boolean`     | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first!")      |
| [merge\_first-](#merge_first-)       | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first-")     |
| [commit\_prefix](#commit_prefix)     | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix")   |
| [commit\_prefix?](#commit_prefix-1)  | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix?")  |
| [commit\_prefix!](#commit_prefix-2)  | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix!")  |
| [commit\_prefix-](#commit_prefix-)   | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix-") |

## ci\_build\_root

Explicitly override the buildroot to be used for CI tests

`ci_build_root`

*   is optional

*   Type: `object` ([Details](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md))

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root")

### ci\_build\_root Type

`object` ([Details](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md))

## ci\_build\_root?

Explicitly override the buildroot to be used for CI tests

`ci_build_root?`

*   is optional

*   Type: `object` ([Details](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md))

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root?")

### ci\_build\_root? Type

`object` ([Details](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md))

## ci\_build\_root!

Explicitly override the buildroot to be used for CI tests

`ci_build_root!`

*   is optional

*   Type: `object` ([Details](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md))

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root!")

### ci\_build\_root! Type

`object` ([Details](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root.md))

## ci\_build\_root-



`ci_build_root-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-ci_build_root-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/ci_build_root-")

### ci\_build\_root- Type

unknown

## enabled

Whether to create PRs to align upstream dockerfiles w/ ART. Default value: true

`enabled`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled")

### enabled Type

`boolean`

## enabled?

Whether to create PRs to align upstream dockerfiles w/ ART. Default value: true

`enabled?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled?")

### enabled? Type

`boolean`

## enabled!

Whether to create PRs to align upstream dockerfiles w/ ART. Default value: true

`enabled!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled!")

### enabled! Type

`boolean`

## enabled-



`enabled-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-enabled-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/enabled-")

### enabled- Type

unknown

## auto\_label

automatically add labels to alignment PRs when created

`auto_label`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label")

### auto\_label Type

`string[]`

## auto\_label?

automatically add labels to alignment PRs when created

`auto_label?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label?")

### auto\_label? Type

`string[]`

## auto\_label!

automatically add labels to alignment PRs when created

`auto_label!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label!")

### auto\_label! Type

`string[]`

## auto\_label-



`auto_label-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-auto_label-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/auto_label-")

### auto\_label- Type

unknown

## from

Explicitly override the FROMs to be used upstream

`from`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from")

### from Type

`string[]`

## from?

Explicitly override the FROMs to be used upstream

`from?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from?")

### from? Type

`string[]`

## from!

Explicitly override the FROMs to be used upstream

`from!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from!")

### from! Type

`string[]`

## from-



`from-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-from-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/from-")

### from- Type

unknown

## merge\_first

`merge_first` means that child images will not get PRs opened until this image is aligned. This helps prevent images like OpenShift's base image from having 100s of PRs referencing its PR.

`merge_first`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first")

### merge\_first Type

`boolean`

## merge\_first?

`merge_first` means that child images will not get PRs opened until this image is aligned. This helps prevent images like OpenShift's base image from having 100s of PRs referencing its PR.

`merge_first?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first?")

### merge\_first? Type

`boolean`

## merge\_first!

`merge_first` means that child images will not get PRs opened until this image is aligned. This helps prevent images like OpenShift's base image from having 100s of PRs referencing its PR.

`merge_first!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first!")

### merge\_first! Type

`boolean`

## merge\_first-



`merge_first-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-merge_first-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first-")

### merge\_first- Type

unknown

## commit\_prefix

`commit_prefix` will add a prefix to the commit msg in ART alignment PRs

`commit_prefix`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix")

### commit\_prefix Type

`string`

## commit\_prefix?

`commit_prefix` will add a prefix to the commit msg in ART alignment PRs

`commit_prefix?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix?")

### commit\_prefix? Type

`string`

## commit\_prefix!

`commit_prefix` will add a prefix to the commit msg in ART alignment PRs

`commit_prefix!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix!")

### commit\_prefix! Type

`string`

## commit\_prefix-



`commit_prefix-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-ci_alignment-properties-streams_prs-properties-commit_prefix-.md "image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/commit_prefix-")

### commit\_prefix- Type

unknown
