# Image Configuration Schema

```txt
image_config.base.schema.json#/properties/metadata
```

Image configuration

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [member\_image.schema.json\*](../out/member_image.schema.json "open original schema") |

## metadata Type

`object` ([Image Configuration](member_image-properties-image-configuration.md))

# metadata Properties

| Property                                       | Type          | Required | Nullable       | Defined by                                                                                                                                       |
| :--------------------------------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| [additional\_tags](#additional_tags)           | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-additional_tags.md "image_config.base.schema.json#/properties/additional_tags")                    |
| [additional\_tags!](#additional_tags-1)        | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-additional_tags.md "image_config.base.schema.json#/properties/additional_tags!")                   |
| [additional\_tags?](#additional_tags-2)        | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-additional_tags.md "image_config.base.schema.json#/properties/additional_tags?")                   |
| [additional\_tags-](#additional_tags-)         | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-additional_tags-.md "image_config.base.schema.json#/properties/additional_tags-")                  |
| [arches](#arches)                              | `array`       | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches")                               |
| [arches!](#arches-1)                           | `array`       | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches!")                              |
| [arches?](#arches-2)                           | `array`       | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches?")                              |
| [arches-](#arches-)                            | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-arches-.md "image_config.base.schema.json#/properties/arches-")                                    |
| [base\_only](#base_only)                       | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-base_only.md "image_config.base.schema.json#/properties/base_only")                                |
| [base\_only!](#base_only-1)                    | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-base_only-1.md "image_config.base.schema.json#/properties/base_only!")                             |
| [base\_only?](#base_only-2)                    | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-base_only-2.md "image_config.base.schema.json#/properties/base_only?")                             |
| [base\_only-](#base_only-)                     | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-base_only-.md "image_config.base.schema.json#/properties/base_only-")                              |
| [cachito](#cachito)                            | `object`      | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito")                                   |
| [cachito!](#cachito-1)                         | `object`      | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito!")                                  |
| [cachito?](#cachito-2)                         | `object`      | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito?")                                  |
| [cachito-](#cachito-)                          | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-cachito-.md "image_config.base.schema.json#/properties/cachito-")                                  |
| [container\_yaml](#container_yaml)             | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-container_yaml.md "image_config.base.schema.json#/properties/container_yaml")                      |
| [container\_yaml!](#container_yaml-1)          | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-container_yaml.md "image_config.base.schema.json#/properties/container_yaml!")                     |
| [container\_yaml?](#container_yaml-2)          | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-container_yaml.md "image_config.base.schema.json#/properties/container_yaml?")                     |
| [container\_yaml-](#container_yaml-)           | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-container_yaml-.md "image_config.base.schema.json#/properties/container_yaml-")                    |
| [content](#content)                            | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-image-content.md "image_content.base.schema.json#/properties/content")                             |
| [content!](#content-1)                         | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-image-content-1.md "image_content.base.schema.json#/properties/content!")                          |
| [content?](#content-2)                         | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-image-content-2.md "image_content.base.schema.json#/properties/content?")                          |
| [content-](#content-)                          | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-content-.md "image_config.base.schema.json#/properties/content-")                                  |
| [dependencies](#dependencies)                  | Merged        | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies")  |
| [dependencies!](#dependencies-1)               | Merged        | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies!") |
| [dependencies?](#dependencies-2)               | Merged        | Optional | cannot be null | [Image Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies?") |
| [dependencies-](#dependencies-)                | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-dependencies-.md "image_config.base.schema.json#/properties/dependencies-")                        |
| [dependents](#dependents)                      | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-dependents.md "image_config.base.schema.json#/properties/dependents")                              |
| [dependents!](#dependents-1)                   | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-dependents.md "image_config.base.schema.json#/properties/dependents!")                             |
| [dependents?](#dependents-2)                   | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-dependents.md "image_config.base.schema.json#/properties/dependents?")                             |
| [dependents-](#dependents-)                    | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-dependents-.md "image_config.base.schema.json#/properties/dependents-")                            |
| [distgit](#distgit)                            | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit.md "image_config.base.schema.json#/properties/distgit")                                    |
| [distgit!](#distgit-1)                         | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit.md "image_config.base.schema.json#/properties/distgit!")                                   |
| [distgit?](#distgit-2)                         | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-distgit.md "image_config.base.schema.json#/properties/distgit?")                                   |
| [distgit-](#distgit-)                          | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-distgit-.md "image_config.base.schema.json#/properties/distgit-")                                  |
| [final\_stage\_user](#final_stage_user)        | Merged        | Optional | cannot be null | [Image Configuration](image_config-properties-final_stage_user.md "image_config.base.schema.json#/properties/final_stage_user")                  |
| [final\_stage\_user!](#final_stage_user-1)     | Merged        | Optional | cannot be null | [Image Configuration](image_config-properties-final_stage_user-1.md "image_config.base.schema.json#/properties/final_stage_user!")               |
| [final\_stage\_user?](#final_stage_user-2)     | Merged        | Optional | cannot be null | [Image Configuration](image_config-properties-final_stage_user-2.md "image_config.base.schema.json#/properties/final_stage_user?")               |
| [final\_stage\_user-](#final_stage_user-)      | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-final_stage_user-.md "image_config.base.schema.json#/properties/final_stage_user-")                |
| [enabled\_repos](#enabled_repos)               | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-enabled_repos.md "image_config.base.schema.json#/properties/enabled_repos")                        |
| [enabled\_repos!](#enabled_repos-1)            | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-enabled_repos.md "image_config.base.schema.json#/properties/enabled_repos!")                       |
| [enabled\_repos?](#enabled_repos-2)            | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-enabled_repos.md "image_config.base.schema.json#/properties/enabled_repos?")                       |
| [enabled\_repos-](#enabled_repos-)             | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-enabled_repos-.md "image_config.base.schema.json#/properties/enabled_repos-")                      |
| [non\_shipping\_repos](#non_shipping_repos)    | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_repos.md "image_config.base.schema.json#/properties/non_shipping_repos")              |
| [non\_shipping\_repos!](#non_shipping_repos-1) | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_repos.md "image_config.base.schema.json#/properties/non_shipping_repos!")             |
| [non\_shipping\_repos?](#non_shipping_repos-2) | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_repos.md "image_config.base.schema.json#/properties/non_shipping_repos?")             |
| [non\_shipping\_repos-](#non_shipping_repos-)  | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_repos-.md "image_config.base.schema.json#/properties/non_shipping_repos-")            |
| [non\_shipping\_rpms](#non_shipping_rpms)      | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_rpms.md "image_config.base.schema.json#/properties/non_shipping_rpms")                |
| [non\_shipping\_rpms!](#non_shipping_rpms-1)   | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_rpms.md "image_config.base.schema.json#/properties/non_shipping_rpms!")               |
| [non\_shipping\_rpms?](#non_shipping_rpms-2)   | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_rpms.md "image_config.base.schema.json#/properties/non_shipping_rpms?")               |
| [non\_shipping\_rpms-](#non_shipping_rpms-)    | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-non_shipping_rpms-.md "image_config.base.schema.json#/properties/non_shipping_rpms-")              |
| [from](#from)                                  | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-from.md "image_config.base.schema.json#/properties/from")                                          |
| [from!](#from-1)                               | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-from.md "image_config.base.schema.json#/properties/from!")                                         |
| [from?](#from-2)                               | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-from.md "image_config.base.schema.json#/properties/from?")                                         |
| [from-](#from-)                                | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-from-.md "image_config.base.schema.json#/properties/from-")                                        |
| [labels](#labels)                              | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-labels.md "image_config.base.schema.json#/properties/labels")                                      |
| [labels!](#labels-1)                           | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-labels.md "image_config.base.schema.json#/properties/labels!")                                     |
| [labels?](#labels-2)                           | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-labels.md "image_config.base.schema.json#/properties/labels?")                                     |
| [labels-](#labels-)                            | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-labels-.md "image_config.base.schema.json#/properties/labels-")                                    |
| [image\_build\_method](#image_build_method)    | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-image_build_method.md "image_config.base.schema.json#/properties/image_build_method")              |
| [image\_build\_method!](#image_build_method-1) | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-image_build_method-1.md "image_config.base.schema.json#/properties/image_build_method!")           |
| [image\_build\_method?](#image_build_method-2) | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-image_build_method-2.md "image_config.base.schema.json#/properties/image_build_method?")           |
| [image\_build\_method-](#image_build_method-)  | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-image_build_method-.md "image_config.base.schema.json#/properties/image_build_method-")            |
| [mode](#mode)                                  | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-mode.md "image_config.base.schema.json#/properties/mode")                                          |
| [mode!](#mode-1)                               | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-mode-1.md "image_config.base.schema.json#/properties/mode!")                                       |
| [mode?](#mode-2)                               | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-mode-2.md "image_config.base.schema.json#/properties/mode?")                                       |
| [mode-](#mode-)                                | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-mode-.md "image_config.base.schema.json#/properties/mode-")                                        |
| [name](#name)                                  | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-name.md "image_config.base.schema.json#/properties/name")                                          |
| [name!](#name-1)                               | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-name-1.md "image_config.base.schema.json#/properties/name!")                                       |
| [name?](#name-2)                               | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-name-2.md "image_config.base.schema.json#/properties/name?")                                       |
| [name-](#name-)                                | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-name-.md "image_config.base.schema.json#/properties/name-")                                        |
| [odcs](#odcs)                                  | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-odcs.md "image_config.base.schema.json#/properties/odcs")                                          |
| [odcs!](#odcs-1)                               | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-odcs.md "image_config.base.schema.json#/properties/odcs!")                                         |
| [odcs?](#odcs-2)                               | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-odcs.md "image_config.base.schema.json#/properties/odcs?")                                         |
| [odcs-](#odcs-)                                | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-odcs-.md "image_config.base.schema.json#/properties/odcs-")                                        |
| [no\_oit\_comments](#no_oit_comments)          | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-no_oit_comments.md "image_config.base.schema.json#/properties/no_oit_comments")                    |
| [no\_oit\_comments!](#no_oit_comments-1)       | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-no_oit_comments-1.md "image_config.base.schema.json#/properties/no_oit_comments!")                 |
| [no\_oit\_comments?](#no_oit_comments-2)       | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-no_oit_comments-2.md "image_config.base.schema.json#/properties/no_oit_comments?")                 |
| [no\_oit\_comments-](#no_oit_comments-)        | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-no_oit_comments-.md "image_config.base.schema.json#/properties/no_oit_comments-")                  |
| [owners](#owners)                              | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-owners.md "image_config.base.schema.json#/properties/owners")                                      |
| [owners!](#owners-1)                           | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-owners.md "image_config.base.schema.json#/properties/owners!")                                     |
| [owners?](#owners-2)                           | `array`       | Optional | cannot be null | [Image Configuration](image_config-properties-owners.md "image_config.base.schema.json#/properties/owners?")                                     |
| [owners-](#owners-)                            | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-owners-.md "image_config.base.schema.json#/properties/owners-")                                    |
| [payload\_name](#payload_name)                 | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-payload_name.md "image_config.base.schema.json#/properties/payload_name")                          |
| [payload\_name!](#payload_name-1)              | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-payload_name-1.md "image_config.base.schema.json#/properties/payload_name!")                       |
| [payload\_name?](#payload_name-2)              | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-payload_name-2.md "image_config.base.schema.json#/properties/payload_name?")                       |
| [payload\_name-](#payload_name-)               | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-payload_name-.md "image_config.base.schema.json#/properties/payload_name-")                        |
| [push](#push)                                  | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-push.md "image_config.base.schema.json#/properties/push")                                          |
| [push!](#push-1)                               | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-push.md "image_config.base.schema.json#/properties/push!")                                         |
| [push?](#push-2)                               | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-push.md "image_config.base.schema.json#/properties/push?")                                         |
| [push-](#push-)                                | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-push-.md "image_config.base.schema.json#/properties/push-")                                        |
| [required](#required)                          | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-required.md "image_config.base.schema.json#/properties/required")                                  |
| [required!](#required-1)                       | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-required-1.md "image_config.base.schema.json#/properties/required!")                               |
| [required?](#required-2)                       | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-required-2.md "image_config.base.schema.json#/properties/required?")                               |
| [required-](#required-)                        | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-required-.md "image_config.base.schema.json#/properties/required-")                                |
| [scan\_sources](#scan_sources)                 | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-scan_sources.md "image_config.base.schema.json#/properties/scan_sources")                          |
| [scan\_sources!](#scan_sources-1)              | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-scan_sources.md "image_config.base.schema.json#/properties/scan_sources!")                         |
| [scan\_sources?](#scan_sources-2)              | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-scan_sources.md "image_config.base.schema.json#/properties/scan_sources?")                         |
| [scan\_sources-](#scan_sources-)               | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-scan_sources-.md "image_config.base.schema.json#/properties/scan_sources-")                        |
| [update-csv](#update-csv)                      | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-update-csv.md "image_config.base.schema.json#/properties/update-csv")                              |
| [update-csv!](#update-csv-1)                   | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-update-csv.md "image_config.base.schema.json#/properties/update-csv!")                             |
| [update-csv?](#update-csv-2)                   | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-update-csv.md "image_config.base.schema.json#/properties/update-csv?")                             |
| [update-csv-](#update-csv-)                    | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-update-csv-.md "image_config.base.schema.json#/properties/update-csv-")                            |
| [wait\_for](#wait_for)                         | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-wait_for.md "image_config.base.schema.json#/properties/wait_for")                                  |
| [wait\_for!](#wait_for-1)                      | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-wait_for-1.md "image_config.base.schema.json#/properties/wait_for!")                               |
| [wait\_for?](#wait_for-2)                      | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-wait_for-2.md "image_config.base.schema.json#/properties/wait_for?")                               |
| [wait\_for-](#wait_for-)                       | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-wait_for-.md "image_config.base.schema.json#/properties/wait_for-")                                |
| [maintainer](#maintainer)                      | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-maintainer.md "image_config.base.schema.json#/properties/maintainer")                              |
| [maintainer!](#maintainer-1)                   | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-maintainer.md "image_config.base.schema.json#/properties/maintainer!")                             |
| [maintainer?](#maintainer-2)                   | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-maintainer.md "image_config.base.schema.json#/properties/maintainer?")                             |
| [maintainer-](#maintainer-)                    | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-maintainer-.md "image_config.base.schema.json#/properties/maintainer-")                            |
| [for\_payload](#for_payload)                   | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-for_payload.md "image_config.base.schema.json#/properties/for_payload")                            |
| [for\_payload!](#for_payload-1)                | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-for_payload-1.md "image_config.base.schema.json#/properties/for_payload!")                         |
| [for\_payload?](#for_payload-2)                | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-for_payload-2.md "image_config.base.schema.json#/properties/for_payload?")                         |
| [for\_payload-](#for_payload-)                 | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-for_payload-.md "image_config.base.schema.json#/properties/for_payload-")                          |
| [for\_release](#for_release)                   | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-for_release.md "image_config.base.schema.json#/properties/for_release")                            |
| [for\_release!](#for_release-1)                | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-for_release-1.md "image_config.base.schema.json#/properties/for_release!")                         |
| [for\_release?](#for_release-2)                | `boolean`     | Optional | cannot be null | [Image Configuration](image_config-properties-for_release-2.md "image_config.base.schema.json#/properties/for_release?")                         |
| [for\_release-](#for_release-)                 | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-for_release-.md "image_config.base.schema.json#/properties/for_release-")                          |
| [name\_in\_bundle](#name_in_bundle)            | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-name_in_bundle.md "image_config.base.schema.json#/properties/name_in_bundle")                      |
| [name\_in\_bundle!](#name_in_bundle-1)         | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-name_in_bundle-1.md "image_config.base.schema.json#/properties/name_in_bundle!")                   |
| [name\_in\_bundle?](#name_in_bundle-2)         | `string`      | Optional | cannot be null | [Image Configuration](image_config-properties-name_in_bundle-2.md "image_config.base.schema.json#/properties/name_in_bundle?")                   |
| [name\_in\_bundle-](#name_in_bundle-)          | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-name_in_bundle-.md "image_config.base.schema.json#/properties/name_in_bundle-")                    |
| [is](#is)                                      | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-is.md "image_config.base.schema.json#/properties/is")                                              |
| [is!](#is-1)                                   | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-is.md "image_config.base.schema.json#/properties/is!")                                             |
| [is?](#is-2)                                   | `object`      | Optional | cannot be null | [Image Configuration](image_config-properties-is.md "image_config.base.schema.json#/properties/is?")                                             |
| [is-](#is-)                                    | Not specified | Optional | cannot be null | [Image Configuration](image_config-properties-is-.md "image_config.base.schema.json#/properties/is-")                                            |

## additional\_tags



`additional_tags`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-additional_tags.md "image_config.base.schema.json#/properties/additional_tags")

### additional\_tags Type

`string[]`

## additional\_tags!



`additional_tags!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-additional_tags.md "image_config.base.schema.json#/properties/additional_tags!")

### additional\_tags! Type

`string[]`

## additional\_tags?



`additional_tags?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-additional_tags.md "image_config.base.schema.json#/properties/additional_tags?")

### additional\_tags? Type

`string[]`

## additional\_tags-



`additional_tags-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-additional_tags-.md "image_config.base.schema.json#/properties/additional_tags-")

### additional\_tags- Type

unknown

## arches



`arches`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches")

### arches Type

`string[]`

## arches!



`arches!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches!")

### arches! Type

`string[]`

## arches?



`arches?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches?")

### arches? Type

`string[]`

## arches-



`arches-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-arches-.md "image_config.base.schema.json#/properties/arches-")

### arches- Type

unknown

## base\_only



`base_only`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-base_only.md "image_config.base.schema.json#/properties/base_only")

### base\_only Type

`boolean`

## base\_only!



`base_only!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-base_only.md "image_config.base.schema.json#/properties/base_only!")

### base\_only! Type

`boolean`

## base\_only?



`base_only?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-base_only.md "image_config.base.schema.json#/properties/base_only?")

### base\_only? Type

`boolean`

## base\_only-



`base_only-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-base_only-.md "image_config.base.schema.json#/properties/base_only-")

### base\_only- Type

unknown

## cachito

Cachito integration configuration

`cachito`

*   is optional

*   Type: `object` ([Cachito](assembly_group_config-properties-cachito-2.md))

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito")

### cachito Type

`object` ([Cachito](assembly_group_config-properties-cachito-2.md))

## cachito!

Cachito integration configuration

`cachito!`

*   is optional

*   Type: `object` ([Cachito](assembly_group_config-properties-cachito-2.md))

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito!")

### cachito! Type

`object` ([Cachito](assembly_group_config-properties-cachito-2.md))

## cachito?

Cachito integration configuration

`cachito?`

*   is optional

*   Type: `object` ([Cachito](assembly_group_config-properties-cachito-2.md))

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito?")

### cachito? Type

`object` ([Cachito](assembly_group_config-properties-cachito-2.md))

## cachito-



`cachito-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-cachito-.md "image_config.base.schema.json#/properties/cachito-")

### cachito- Type

unknown

## container\_yaml



`container_yaml`

*   is optional

*   Type: `object` ([Details](image_config-properties-container_yaml.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-container_yaml.md "image_config.base.schema.json#/properties/container_yaml")

### container\_yaml Type

`object` ([Details](image_config-properties-container_yaml.md))

## container\_yaml!



`container_yaml!`

*   is optional

*   Type: `object` ([Details](image_config-properties-container_yaml.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-container_yaml.md "image_config.base.schema.json#/properties/container_yaml!")

### container\_yaml! Type

`object` ([Details](image_config-properties-container_yaml.md))

## container\_yaml?



`container_yaml?`

*   is optional

*   Type: `object` ([Details](image_config-properties-container_yaml.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-container_yaml.md "image_config.base.schema.json#/properties/container_yaml?")

### container\_yaml? Type

`object` ([Details](image_config-properties-container_yaml.md))

## container\_yaml-



`container_yaml-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-container_yaml-.md "image_config.base.schema.json#/properties/container_yaml-")

### container\_yaml- Type

unknown

## content

Image content configuration

`content`

*   is optional

*   Type: `object` ([Image Content](image_config-properties-image-content-2.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-image-content-2.md "image_content.base.schema.json#/properties/content")

### content Type

`object` ([Image Content](image_config-properties-image-content-2.md))

## content!

Image content configuration

`content!`

*   is optional

*   Type: `object` ([Image Content](image_config-properties-image-content-2.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-image-content-2.md "image_content.base.schema.json#/properties/content!")

### content! Type

`object` ([Image Content](image_config-properties-image-content-2.md))

## content?

Image content configuration

`content?`

*   is optional

*   Type: `object` ([Image Content](image_config-properties-image-content-2.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-image-content-2.md "image_content.base.schema.json#/properties/content?")

### content? Type

`object` ([Image Content](image_config-properties-image-content-2.md))

## content-



`content-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-content-.md "image_config.base.schema.json#/properties/content-")

### content- Type

unknown

## dependencies



`dependencies`

*   is optional

*   Type: `object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies")

### dependencies Type

`object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

any of

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-0.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-1.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-2.md "check type definition")

## dependencies!



`dependencies!`

*   is optional

*   Type: `object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies!")

### dependencies! Type

`object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

any of

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-0.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-1.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-2.md "check type definition")

## dependencies?



`dependencies?`

*   is optional

*   Type: `object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

*   cannot be null

*   defined in: [Image Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies?")

### dependencies? Type

`object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

any of

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-0.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-1.md "check type definition")

*   [Untitled undefined type in Assembly Dependencies](assembly_dependencies-anyof-2.md "check type definition")

## dependencies-



`dependencies-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-dependencies-.md "image_config.base.schema.json#/properties/dependencies-")

### dependencies- Type

unknown

## dependents



`dependents`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-dependents.md "image_config.base.schema.json#/properties/dependents")

### dependents Type

`string[]`

## dependents!



`dependents!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-dependents.md "image_config.base.schema.json#/properties/dependents!")

### dependents! Type

`string[]`

## dependents?



`dependents?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-dependents.md "image_config.base.schema.json#/properties/dependents?")

### dependents? Type

`string[]`

## dependents-



`dependents-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-dependents-.md "image_config.base.schema.json#/properties/dependents-")

### dependents- Type

unknown

## distgit



`distgit`

*   is optional

*   Type: `object` ([Details](image_config-properties-distgit.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit.md "image_config.base.schema.json#/properties/distgit")

### distgit Type

`object` ([Details](image_config-properties-distgit.md))

## distgit!



`distgit!`

*   is optional

*   Type: `object` ([Details](image_config-properties-distgit.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit.md "image_config.base.schema.json#/properties/distgit!")

### distgit! Type

`object` ([Details](image_config-properties-distgit.md))

## distgit?



`distgit?`

*   is optional

*   Type: `object` ([Details](image_config-properties-distgit.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit.md "image_config.base.schema.json#/properties/distgit?")

### distgit? Type

`object` ([Details](image_config-properties-distgit.md))

## distgit-



`distgit-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-distgit-.md "image_config.base.schema.json#/properties/distgit-")

### distgit- Type

unknown

## final\_stage\_user

When doozer injects USER 0 to do a yum update, this field instructs doozer to set this user afterwards in the final stage of the build.

`final_stage_user`

*   is optional

*   Type: merged type ([Details](image_config-properties-final_stage_user.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-final_stage_user.md "image_config.base.schema.json#/properties/final_stage_user")

### final\_stage\_user Type

merged type ([Details](image_config-properties-final_stage_user.md))

one (and only one) of

*   [Untitled string in Image Configuration](image_config-properties-final_stage_user-oneof-0.md "check type definition")

*   [Untitled integer in Image Configuration](image_config-properties-final_stage_user-oneof-1.md "check type definition")

## final\_stage\_user!

When doozer injects USER 0 to do a yum update, this field instructs doozer to set this user afterwards in the final stage of the build.

`final_stage_user!`

*   is optional

*   Type: merged type ([Details](image_config-properties-final_stage_user.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-final_stage_user.md "image_config.base.schema.json#/properties/final_stage_user!")

### final\_stage\_user! Type

merged type ([Details](image_config-properties-final_stage_user.md))

one (and only one) of

*   [Untitled string in Image Configuration](image_config-properties-final_stage_user-oneof-0.md "check type definition")

*   [Untitled integer in Image Configuration](image_config-properties-final_stage_user-oneof-1.md "check type definition")

## final\_stage\_user?

When doozer injects USER 0 to do a yum update, this field instructs doozer to set this user afterwards in the final stage of the build.

`final_stage_user?`

*   is optional

*   Type: merged type ([Details](image_config-properties-final_stage_user.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-final_stage_user.md "image_config.base.schema.json#/properties/final_stage_user?")

### final\_stage\_user? Type

merged type ([Details](image_config-properties-final_stage_user.md))

one (and only one) of

*   [Untitled string in Image Configuration](image_config-properties-final_stage_user-oneof-0.md "check type definition")

*   [Untitled integer in Image Configuration](image_config-properties-final_stage_user-oneof-1.md "check type definition")

## final\_stage\_user-



`final_stage_user-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-final_stage_user-.md "image_config.base.schema.json#/properties/final_stage_user-")

### final\_stage\_user- Type

unknown

## enabled\_repos



`enabled_repos`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-enabled_repos.md "image_config.base.schema.json#/properties/enabled_repos")

### enabled\_repos Type

`string[]`

## enabled\_repos!



`enabled_repos!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-enabled_repos.md "image_config.base.schema.json#/properties/enabled_repos!")

### enabled\_repos! Type

`string[]`

## enabled\_repos?



`enabled_repos?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-enabled_repos.md "image_config.base.schema.json#/properties/enabled_repos?")

### enabled\_repos? Type

`string[]`

## enabled\_repos-



`enabled_repos-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-enabled_repos-.md "image_config.base.schema.json#/properties/enabled_repos-")

### enabled\_repos- Type

unknown

## non\_shipping\_repos



`non_shipping_repos`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_repos.md "image_config.base.schema.json#/properties/non_shipping_repos")

### non\_shipping\_repos Type

`string[]`

## non\_shipping\_repos!



`non_shipping_repos!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_repos.md "image_config.base.schema.json#/properties/non_shipping_repos!")

### non\_shipping\_repos! Type

`string[]`

## non\_shipping\_repos?



`non_shipping_repos?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_repos.md "image_config.base.schema.json#/properties/non_shipping_repos?")

### non\_shipping\_repos? Type

`string[]`

## non\_shipping\_repos-



`non_shipping_repos-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_repos-.md "image_config.base.schema.json#/properties/non_shipping_repos-")

### non\_shipping\_repos- Type

unknown

## non\_shipping\_rpms



`non_shipping_rpms`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_rpms.md "image_config.base.schema.json#/properties/non_shipping_rpms")

### non\_shipping\_rpms Type

`string[]`

## non\_shipping\_rpms!



`non_shipping_rpms!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_rpms.md "image_config.base.schema.json#/properties/non_shipping_rpms!")

### non\_shipping\_rpms! Type

`string[]`

## non\_shipping\_rpms?



`non_shipping_rpms?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_rpms.md "image_config.base.schema.json#/properties/non_shipping_rpms?")

### non\_shipping\_rpms? Type

`string[]`

## non\_shipping\_rpms-



`non_shipping_rpms-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-non_shipping_rpms-.md "image_config.base.schema.json#/properties/non_shipping_rpms-")

### non\_shipping\_rpms- Type

unknown

## from



`from`

*   is optional

*   Type: `object` ([Details](image_config-properties-from.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-from.md "image_config.base.schema.json#/properties/from")

### from Type

`object` ([Details](image_config-properties-from.md))

## from!



`from!`

*   is optional

*   Type: `object` ([Details](image_config-properties-from.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-from.md "image_config.base.schema.json#/properties/from!")

### from! Type

`object` ([Details](image_config-properties-from.md))

## from?



`from?`

*   is optional

*   Type: `object` ([Details](image_config-properties-from.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-from.md "image_config.base.schema.json#/properties/from?")

### from? Type

`object` ([Details](image_config-properties-from.md))

## from-



`from-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-from-.md "image_config.base.schema.json#/properties/from-")

### from- Type

unknown

## labels



`labels`

*   is optional

*   Type: `object` ([Details](image_config-properties-labels.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-labels.md "image_config.base.schema.json#/properties/labels")

### labels Type

`object` ([Details](image_config-properties-labels.md))

## labels!



`labels!`

*   is optional

*   Type: `object` ([Details](image_config-properties-labels.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-labels.md "image_config.base.schema.json#/properties/labels!")

### labels! Type

`object` ([Details](image_config-properties-labels.md))

## labels?



`labels?`

*   is optional

*   Type: `object` ([Details](image_config-properties-labels.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-labels.md "image_config.base.schema.json#/properties/labels?")

### labels? Type

`object` ([Details](image_config-properties-labels.md))

## labels-



`labels-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-labels-.md "image_config.base.schema.json#/properties/labels-")

### labels- Type

unknown

## image\_build\_method



`image_build_method`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-image_build_method.md "image_config.base.schema.json#/properties/image_build_method")

### image\_build\_method Type

`string`

### image\_build\_method Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## image\_build\_method!



`image_build_method!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-image_build_method.md "image_config.base.schema.json#/properties/image_build_method!")

### image\_build\_method! Type

`string`

### image\_build\_method! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## image\_build\_method?



`image_build_method?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-image_build_method.md "image_config.base.schema.json#/properties/image_build_method?")

### image\_build\_method? Type

`string`

### image\_build\_method? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## image\_build\_method-



`image_build_method-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-image_build_method-.md "image_config.base.schema.json#/properties/image_build_method-")

### image\_build\_method- Type

unknown

## mode



`mode`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-mode.md "image_config.base.schema.json#/properties/mode")

### mode Type

`string`

### mode Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"auto"`     |             |
| `"disabled"` |             |
| `"wip"`      |             |

## mode!



`mode!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-mode.md "image_config.base.schema.json#/properties/mode!")

### mode! Type

`string`

### mode! Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"auto"`     |             |
| `"disabled"` |             |
| `"wip"`      |             |

## mode?



`mode?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-mode.md "image_config.base.schema.json#/properties/mode?")

### mode? Type

`string`

### mode? Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"auto"`     |             |
| `"disabled"` |             |
| `"wip"`      |             |

## mode-



`mode-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-mode-.md "image_config.base.schema.json#/properties/mode-")

### mode- Type

unknown

## name



`name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name.md "image_config.base.schema.json#/properties/name")

### name Type

`string`

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## name!



`name!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name.md "image_config.base.schema.json#/properties/name!")

### name! Type

`string`

### name! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## name?



`name?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name.md "image_config.base.schema.json#/properties/name?")

### name? Type

`string`

### name? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## name-



`name-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name-.md "image_config.base.schema.json#/properties/name-")

### name- Type

unknown

## odcs



`odcs`

*   is optional

*   Type: `object` ([Details](image_config-properties-odcs.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-odcs.md "image_config.base.schema.json#/properties/odcs")

### odcs Type

`object` ([Details](image_config-properties-odcs.md))

## odcs!



`odcs!`

*   is optional

*   Type: `object` ([Details](image_config-properties-odcs.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-odcs.md "image_config.base.schema.json#/properties/odcs!")

### odcs! Type

`object` ([Details](image_config-properties-odcs.md))

## odcs?



`odcs?`

*   is optional

*   Type: `object` ([Details](image_config-properties-odcs.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-odcs.md "image_config.base.schema.json#/properties/odcs?")

### odcs? Type

`object` ([Details](image_config-properties-odcs.md))

## odcs-



`odcs-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-odcs-.md "image_config.base.schema.json#/properties/odcs-")

### odcs- Type

unknown

## no\_oit\_comments



`no_oit_comments`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-no_oit_comments.md "image_config.base.schema.json#/properties/no_oit_comments")

### no\_oit\_comments Type

`boolean`

## no\_oit\_comments!



`no_oit_comments!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-no_oit_comments.md "image_config.base.schema.json#/properties/no_oit_comments!")

### no\_oit\_comments! Type

`boolean`

## no\_oit\_comments?



`no_oit_comments?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-no_oit_comments.md "image_config.base.schema.json#/properties/no_oit_comments?")

### no\_oit\_comments? Type

`boolean`

## no\_oit\_comments-



`no_oit_comments-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-no_oit_comments-.md "image_config.base.schema.json#/properties/no_oit_comments-")

### no\_oit\_comments- Type

unknown

## owners



`owners`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-owners.md "image_config.base.schema.json#/properties/owners")

### owners Type

`string[]`

## owners!



`owners!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-owners.md "image_config.base.schema.json#/properties/owners!")

### owners! Type

`string[]`

## owners?



`owners?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-owners.md "image_config.base.schema.json#/properties/owners?")

### owners? Type

`string[]`

## owners-



`owners-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-owners-.md "image_config.base.schema.json#/properties/owners-")

### owners- Type

unknown

## payload\_name



`payload_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-payload_name.md "image_config.base.schema.json#/properties/payload_name")

### payload\_name Type

`string`

### payload\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## payload\_name!



`payload_name!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-payload_name.md "image_config.base.schema.json#/properties/payload_name!")

### payload\_name! Type

`string`

### payload\_name! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## payload\_name?



`payload_name?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-payload_name.md "image_config.base.schema.json#/properties/payload_name?")

### payload\_name? Type

`string`

### payload\_name? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## payload\_name-



`payload_name-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-payload_name-.md "image_config.base.schema.json#/properties/payload_name-")

### payload\_name- Type

unknown

## push



`push`

*   is optional

*   Type: `object` ([Details](image_config-properties-push.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-push.md "image_config.base.schema.json#/properties/push")

### push Type

`object` ([Details](image_config-properties-push.md))

## push!



`push!`

*   is optional

*   Type: `object` ([Details](image_config-properties-push.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-push.md "image_config.base.schema.json#/properties/push!")

### push! Type

`object` ([Details](image_config-properties-push.md))

## push?



`push?`

*   is optional

*   Type: `object` ([Details](image_config-properties-push.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-push.md "image_config.base.schema.json#/properties/push?")

### push? Type

`object` ([Details](image_config-properties-push.md))

## push-



`push-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-push-.md "image_config.base.schema.json#/properties/push-")

### push- Type

unknown

## required



`required`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-required.md "image_config.base.schema.json#/properties/required")

### required Type

`boolean`

## required!



`required!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-required.md "image_config.base.schema.json#/properties/required!")

### required! Type

`boolean`

## required?



`required?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-required.md "image_config.base.schema.json#/properties/required?")

### required? Type

`boolean`

## required-



`required-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-required-.md "image_config.base.schema.json#/properties/required-")

### required- Type

unknown

## scan\_sources



`scan_sources`

*   is optional

*   Type: `object` ([Details](image_config-properties-scan_sources.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-scan_sources.md "image_config.base.schema.json#/properties/scan_sources")

### scan\_sources Type

`object` ([Details](image_config-properties-scan_sources.md))

## scan\_sources!



`scan_sources!`

*   is optional

*   Type: `object` ([Details](image_config-properties-scan_sources.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-scan_sources.md "image_config.base.schema.json#/properties/scan_sources!")

### scan\_sources! Type

`object` ([Details](image_config-properties-scan_sources.md))

## scan\_sources?



`scan_sources?`

*   is optional

*   Type: `object` ([Details](image_config-properties-scan_sources.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-scan_sources.md "image_config.base.schema.json#/properties/scan_sources?")

### scan\_sources? Type

`object` ([Details](image_config-properties-scan_sources.md))

## scan\_sources-



`scan_sources-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-scan_sources-.md "image_config.base.schema.json#/properties/scan_sources-")

### scan\_sources- Type

unknown

## update-csv



`update-csv`

*   is optional

*   Type: `object` ([Details](image_config-properties-update-csv.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-update-csv.md "image_config.base.schema.json#/properties/update-csv")

### update-csv Type

`object` ([Details](image_config-properties-update-csv.md))

## update-csv!



`update-csv!`

*   is optional

*   Type: `object` ([Details](image_config-properties-update-csv.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-update-csv.md "image_config.base.schema.json#/properties/update-csv!")

### update-csv! Type

`object` ([Details](image_config-properties-update-csv.md))

## update-csv?



`update-csv?`

*   is optional

*   Type: `object` ([Details](image_config-properties-update-csv.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-update-csv.md "image_config.base.schema.json#/properties/update-csv?")

### update-csv? Type

`object` ([Details](image_config-properties-update-csv.md))

## update-csv-



`update-csv-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-update-csv-.md "image_config.base.schema.json#/properties/update-csv-")

### update-csv- Type

unknown

## wait\_for



`wait_for`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-wait_for.md "image_config.base.schema.json#/properties/wait_for")

### wait\_for Type

`string`

### wait\_for Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## wait\_for!



`wait_for!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-wait_for.md "image_config.base.schema.json#/properties/wait_for!")

### wait\_for! Type

`string`

### wait\_for! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## wait\_for?



`wait_for?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-wait_for.md "image_config.base.schema.json#/properties/wait_for?")

### wait\_for? Type

`string`

### wait\_for? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## wait\_for-



`wait_for-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-wait_for-.md "image_config.base.schema.json#/properties/wait_for-")

### wait\_for- Type

unknown

## maintainer



`maintainer`

*   is optional

*   Type: `object` ([Details](image_config-properties-maintainer.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-maintainer.md "image_config.base.schema.json#/properties/maintainer")

### maintainer Type

`object` ([Details](image_config-properties-maintainer.md))

## maintainer!



`maintainer!`

*   is optional

*   Type: `object` ([Details](image_config-properties-maintainer.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-maintainer.md "image_config.base.schema.json#/properties/maintainer!")

### maintainer! Type

`object` ([Details](image_config-properties-maintainer.md))

## maintainer?



`maintainer?`

*   is optional

*   Type: `object` ([Details](image_config-properties-maintainer.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-maintainer.md "image_config.base.schema.json#/properties/maintainer?")

### maintainer? Type

`object` ([Details](image_config-properties-maintainer.md))

## maintainer-



`maintainer-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-maintainer-.md "image_config.base.schema.json#/properties/maintainer-")

### maintainer- Type

unknown

## for\_payload



`for_payload`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_payload.md "image_config.base.schema.json#/properties/for_payload")

### for\_payload Type

`boolean`

## for\_payload!



`for_payload!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_payload.md "image_config.base.schema.json#/properties/for_payload!")

### for\_payload! Type

`boolean`

## for\_payload?



`for_payload?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_payload.md "image_config.base.schema.json#/properties/for_payload?")

### for\_payload? Type

`boolean`

## for\_payload-



`for_payload-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_payload-.md "image_config.base.schema.json#/properties/for_payload-")

### for\_payload- Type

unknown

## for\_release



`for_release`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_release.md "image_config.base.schema.json#/properties/for_release")

### for\_release Type

`boolean`

## for\_release!



`for_release!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_release.md "image_config.base.schema.json#/properties/for_release!")

### for\_release! Type

`boolean`

## for\_release?



`for_release?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_release.md "image_config.base.schema.json#/properties/for_release?")

### for\_release? Type

`boolean`

## for\_release-



`for_release-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-for_release-.md "image_config.base.schema.json#/properties/for_release-")

### for\_release- Type

unknown

## name\_in\_bundle



`name_in_bundle`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name_in_bundle.md "image_config.base.schema.json#/properties/name_in_bundle")

### name\_in\_bundle Type

`string`

### name\_in\_bundle Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## name\_in\_bundle!



`name_in_bundle!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name_in_bundle.md "image_config.base.schema.json#/properties/name_in_bundle!")

### name\_in\_bundle! Type

`string`

### name\_in\_bundle! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## name\_in\_bundle?



`name_in_bundle?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name_in_bundle.md "image_config.base.schema.json#/properties/name_in_bundle?")

### name\_in\_bundle? Type

`string`

### name\_in\_bundle? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## name\_in\_bundle-



`name_in_bundle-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-name_in_bundle-.md "image_config.base.schema.json#/properties/name_in_bundle-")

### name\_in\_bundle- Type

unknown

## is



`is`

*   is optional

*   Type: `object` ([Details](image_config-properties-is.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-is.md "image_config.base.schema.json#/properties/is")

### is Type

`object` ([Details](image_config-properties-is.md))

## is!



`is!`

*   is optional

*   Type: `object` ([Details](image_config-properties-is.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-is.md "image_config.base.schema.json#/properties/is!")

### is! Type

`object` ([Details](image_config-properties-is.md))

## is?



`is?`

*   is optional

*   Type: `object` ([Details](image_config-properties-is.md))

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-is.md "image_config.base.schema.json#/properties/is?")

### is? Type

`object` ([Details](image_config-properties-is.md))

## is-



`is-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Configuration](image_config-properties-is-.md "image_config.base.schema.json#/properties/is-")

### is- Type

unknown
