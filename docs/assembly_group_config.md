# Assembly Group Configuration Schema

```txt
assembly_group_config.schema.json
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [assembly\_group\_config.schema.json](../out/assembly_group_config.schema.json "open original schema") |

## Assembly Group Configuration Type

`object` ([Assembly Group Configuration](assembly_group_config.md))

# Assembly Group Configuration Properties

| Property                                             | Type          | Required | Nullable       | Defined by                                                                                                                                                        |
| :--------------------------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [arches](#arches)                                    | `array`       | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches")                                       |
| [arches!](#arches-1)                                 | `array`       | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches!")                                      |
| [arches?](#arches-2)                                 | `array`       | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches?")                                      |
| [arches-](#arches-)                                  | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-arches-.md "assembly_group_config.schema.json#/properties/arches-")                               |
| [repos](#repos)                                      | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-repositories-2.md "repos.schema.json#/properties/repos")                                          |
| [repos!](#repos-1)                                   | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-repositories-2.md "repos.schema.json#/properties/repos!")                                         |
| [repos?](#repos-2)                                   | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-repositories-2.md "repos.schema.json#/properties/repos?")                                         |
| [repos-](#repos-)                                    | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-repos-.md "assembly_group_config.schema.json#/properties/repos-")                                 |
| [advisories](#advisories)                            | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-advisories.md "assembly_group_config.schema.json#/properties/advisories")                         |
| [advisories!](#advisories-1)                         | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-advisories.md "assembly_group_config.schema.json#/properties/advisories!")                        |
| [advisories?](#advisories-2)                         | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-advisories.md "assembly_group_config.schema.json#/properties/advisories?")                        |
| [advisories-](#advisories-)                          | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-advisories-.md "assembly_group_config.schema.json#/properties/advisories-")                       |
| [dependencies](#dependencies)                        | Merged        | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies")          |
| [dependencies!](#dependencies-1)                     | Merged        | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies!")         |
| [dependencies?](#dependencies-2)                     | Merged        | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies?")         |
| [dependencies-](#dependencies-)                      | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-dependencies-.md "assembly_group_config.schema.json#/properties/dependencies-")                   |
| [release\_jira](#release_jira)                       | `string`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-release_jira.md "assembly_group_config.schema.json#/properties/release_jira")                     |
| [release\_jira!](#release_jira-1)                    | `string`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-release_jira.md "assembly_group_config.schema.json#/properties/release_jira!")                    |
| [release\_jira?](#release_jira-2)                    | `string`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-release_jira.md "assembly_group_config.schema.json#/properties/release_jira?")                    |
| [release\_jira-](#release_jira-)                     | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-release_jira-.md "assembly_group_config.schema.json#/properties/release_jira-")                   |
| [upgrades](#upgrades)                                | `string`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-upgrades.md "assembly_group_config.schema.json#/properties/upgrades")                             |
| [upgrades!](#upgrades-1)                             | `string`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-upgrades.md "assembly_group_config.schema.json#/properties/upgrades!")                            |
| [upgrades?](#upgrades-2)                             | `string`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-upgrades.md "assembly_group_config.schema.json#/properties/upgrades?")                            |
| [upgrades-](#upgrades-)                              | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-upgrades-.md "assembly_group_config.schema.json#/properties/upgrades-")                           |
| [check\_golang\_versions](#check_golang_versions)    | `boolean`     | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions.md "assembly_group_config.schema.json#/properties/check_golang_versions")   |
| [check\_golang\_versions!](#check_golang_versions-1) | `boolean`     | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions.md "assembly_group_config.schema.json#/properties/check_golang_versions!")  |
| [check\_golang\_versions?](#check_golang_versions-2) | `boolean`     | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions.md "assembly_group_config.schema.json#/properties/check_golang_versions?")  |
| [check\_golang\_versions-](#check_golang_versions-)  | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions-.md "assembly_group_config.schema.json#/properties/check_golang_versions-") |
| [cachito](#cachito)                                  | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito")                                           |
| [cachito!](#cachito-1)                               | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito!")                                          |
| [cachito?](#cachito-2)                               | `object`      | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito?")                                          |
| [cachito-](#cachito-)                                | Not specified | Optional | cannot be null | [Assembly Group Configuration](assembly_group_config-properties-cachito-.md "assembly_group_config.schema.json#/properties/cachito-")                             |

## arches



`arches`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches")

### arches Type

`string[]`

## arches!



`arches!`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches!")

### arches! Type

`string[]`

## arches?



`arches?`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-architectures-2.md "arches.schema.json#/properties/arches?")

### arches? Type

`string[]`

## arches-



`arches-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-arches-.md "assembly_group_config.schema.json#/properties/arches-")

### arches- Type

unknown

## repos



`repos`

*   is optional

*   Type: `object` ([Repositories](assembly_group_config-properties-repositories-2.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-repositories-2.md "repos.schema.json#/properties/repos")

### repos Type

`object` ([Repositories](assembly_group_config-properties-repositories-2.md))

## repos!



`repos!`

*   is optional

*   Type: `object` ([Repositories](assembly_group_config-properties-repositories-2.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-repositories-2.md "repos.schema.json#/properties/repos!")

### repos! Type

`object` ([Repositories](assembly_group_config-properties-repositories-2.md))

## repos?



`repos?`

*   is optional

*   Type: `object` ([Repositories](assembly_group_config-properties-repositories-2.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-repositories-2.md "repos.schema.json#/properties/repos?")

### repos? Type

`object` ([Repositories](assembly_group_config-properties-repositories-2.md))

## repos-



`repos-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-repos-.md "assembly_group_config.schema.json#/properties/repos-")

### repos- Type

unknown

## advisories



`advisories`

*   is optional

*   Type: `object` ([Details](assembly_group_config-properties-advisories.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-advisories.md "assembly_group_config.schema.json#/properties/advisories")

### advisories Type

`object` ([Details](assembly_group_config-properties-advisories.md))

## advisories!



`advisories!`

*   is optional

*   Type: `object` ([Details](assembly_group_config-properties-advisories.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-advisories.md "assembly_group_config.schema.json#/properties/advisories!")

### advisories! Type

`object` ([Details](assembly_group_config-properties-advisories.md))

## advisories?



`advisories?`

*   is optional

*   Type: `object` ([Details](assembly_group_config-properties-advisories.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-advisories.md "assembly_group_config.schema.json#/properties/advisories?")

### advisories? Type

`object` ([Details](assembly_group_config-properties-advisories.md))

## advisories-



`advisories-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-advisories-.md "assembly_group_config.schema.json#/properties/advisories-")

### advisories- Type

unknown

## dependencies



`dependencies`

*   is optional

*   Type: `object` ([Assembly Dependencies](assembly_group_config-properties-assembly-dependencies-2.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies")

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

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies!")

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

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-assembly-dependencies-2.md "assembly_dependencies.schema.json#/properties/dependencies?")

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

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-dependencies-.md "assembly_group_config.schema.json#/properties/dependencies-")

### dependencies- Type

unknown

## release\_jira



`release_jira`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-release_jira.md "assembly_group_config.schema.json#/properties/release_jira")

### release\_jira Type

`string`

### release\_jira Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## release\_jira!



`release_jira!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-release_jira.md "assembly_group_config.schema.json#/properties/release_jira!")

### release\_jira! Type

`string`

### release\_jira! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## release\_jira?



`release_jira?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-release_jira.md "assembly_group_config.schema.json#/properties/release_jira?")

### release\_jira? Type

`string`

### release\_jira? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## release\_jira-



`release_jira-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-release_jira-.md "assembly_group_config.schema.json#/properties/release_jira-")

### release\_jira- Type

unknown

## upgrades



`upgrades`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-upgrades.md "assembly_group_config.schema.json#/properties/upgrades")

### upgrades Type

`string`

## upgrades!



`upgrades!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-upgrades.md "assembly_group_config.schema.json#/properties/upgrades!")

### upgrades! Type

`string`

## upgrades?



`upgrades?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-upgrades.md "assembly_group_config.schema.json#/properties/upgrades?")

### upgrades? Type

`string`

## upgrades-



`upgrades-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-upgrades-.md "assembly_group_config.schema.json#/properties/upgrades-")

### upgrades- Type

unknown

## check\_golang\_versions



`check_golang_versions`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions.md "assembly_group_config.schema.json#/properties/check_golang_versions")

### check\_golang\_versions Type

`boolean`

## check\_golang\_versions!



`check_golang_versions!`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions.md "assembly_group_config.schema.json#/properties/check_golang_versions!")

### check\_golang\_versions! Type

`boolean`

## check\_golang\_versions?



`check_golang_versions?`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions.md "assembly_group_config.schema.json#/properties/check_golang_versions?")

### check\_golang\_versions? Type

`boolean`

## check\_golang\_versions-



`check_golang_versions-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-check_golang_versions-.md "assembly_group_config.schema.json#/properties/check_golang_versions-")

### check\_golang\_versions- Type

unknown

## cachito

Cachito integration configuration

`cachito`

*   is optional

*   Type: `object` ([Cachito](assembly_group_config-properties-cachito-2.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito")

### cachito Type

`object` ([Cachito](assembly_group_config-properties-cachito-2.md))

## cachito!

Cachito integration configuration

`cachito!`

*   is optional

*   Type: `object` ([Cachito](assembly_group_config-properties-cachito-2.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito!")

### cachito! Type

`object` ([Cachito](assembly_group_config-properties-cachito-2.md))

## cachito?

Cachito integration configuration

`cachito?`

*   is optional

*   Type: `object` ([Cachito](assembly_group_config-properties-cachito-2.md))

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-cachito-2.md "cachito.schema.json#/properties/cachito?")

### cachito? Type

`object` ([Cachito](assembly_group_config-properties-cachito-2.md))

## cachito-



`cachito-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Assembly Group Configuration](assembly_group_config-properties-cachito-.md "assembly_group_config.schema.json#/properties/cachito-")

### cachito- Type

unknown
