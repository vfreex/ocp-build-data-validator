# Untitled object in Image Content Schema

```txt
image_content.base.schema.json#/properties/source/properties/git!
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [image\_content.base.schema.json\*](../out/image_content.base.schema.json "open original schema") |

## git! Type

`object` ([Details](image_content-properties-source-properties-git.md))

# git! Properties

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                  |
| :------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [branch](#branch)    | `object`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-branch.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch")   |
| [branch?](#branch-1) | `object`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-branch.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch?")  |
| [branch!](#branch-2) | `object`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-branch.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch!")  |
| [branch-](#branch-)  | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-branch-.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch-") |
| [url](#url)          | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-url.md "image_content.base.schema.json#/properties/source/properties/git/properties/url")         |
| [url?](#url-1)       | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-url.md "image_content.base.schema.json#/properties/source/properties/git/properties/url?")        |
| [url!](#url-2)       | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-url.md "image_content.base.schema.json#/properties/source/properties/git/properties/url!")        |
| [url-](#url-)        | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-url-.md "image_content.base.schema.json#/properties/source/properties/git/properties/url-")       |
| [web](#web)          | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-web.md "image_content.base.schema.json#/properties/source/properties/git/properties/web")         |
| [web?](#web-1)       | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-web.md "image_content.base.schema.json#/properties/source/properties/git/properties/web?")        |
| [web!](#web-2)       | `string`      | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-web.md "image_content.base.schema.json#/properties/source/properties/git/properties/web!")        |
| [web-](#web-)        | Not specified | Optional | cannot be null | [Image Content](image_content-properties-source-properties-git-properties-web-.md "image_content.base.schema.json#/properties/source/properties/git/properties/web-")       |

## branch



`branch`

*   is optional

*   Type: `object` ([Details](image_content-properties-source-properties-git-properties-branch.md))

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-branch.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch")

### branch Type

`object` ([Details](image_content-properties-source-properties-git-properties-branch.md))

## branch?



`branch?`

*   is optional

*   Type: `object` ([Details](image_content-properties-source-properties-git-properties-branch.md))

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-branch.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch?")

### branch? Type

`object` ([Details](image_content-properties-source-properties-git-properties-branch.md))

## branch!



`branch!`

*   is optional

*   Type: `object` ([Details](image_content-properties-source-properties-git-properties-branch.md))

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-branch.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch!")

### branch! Type

`object` ([Details](image_content-properties-source-properties-git-properties-branch.md))

## branch-



`branch-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-branch-.md "image_content.base.schema.json#/properties/source/properties/git/properties/branch-")

### branch- Type

unknown

## url



`url`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-url.md "image_content.base.schema.json#/properties/source/properties/git/properties/url")

### url Type

`string`

### url Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^((git@[\w\.]+))([\w\.@\:/\-~]+)(\.git)(/)?$
```

[try pattern](https://regexr.com/?expression=%5E\(\(git%40%5B%5Cw%5C.%5D%2B\)\)\(%5B%5Cw%5C.%40%5C%3A%2F%5C-\~%5D%2B\)\(%5C.git\)\(%2F\)%3F%24 "try regular expression with regexr.com")

## url?



`url?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-url.md "image_content.base.schema.json#/properties/source/properties/git/properties/url?")

### url? Type

`string`

### url? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^((git@[\w\.]+))([\w\.@\:/\-~]+)(\.git)(/)?$
```

[try pattern](https://regexr.com/?expression=%5E\(\(git%40%5B%5Cw%5C.%5D%2B\)\)\(%5B%5Cw%5C.%40%5C%3A%2F%5C-\~%5D%2B\)\(%5C.git\)\(%2F\)%3F%24 "try regular expression with regexr.com")

## url!



`url!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-url.md "image_content.base.schema.json#/properties/source/properties/git/properties/url!")

### url! Type

`string`

### url! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^((git@[\w\.]+))([\w\.@\:/\-~]+)(\.git)(/)?$
```

[try pattern](https://regexr.com/?expression=%5E\(\(git%40%5B%5Cw%5C.%5D%2B\)\)\(%5B%5Cw%5C.%40%5C%3A%2F%5C-\~%5D%2B\)\(%5C.git\)\(%2F\)%3F%24 "try regular expression with regexr.com")

## url-



`url-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-url-.md "image_content.base.schema.json#/properties/source/properties/git/properties/url-")

### url- Type

unknown

## web



`web`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-web.md "image_content.base.schema.json#/properties/source/properties/git/properties/web")

### web Type

`string`

### web Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## web?



`web?`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-web.md "image_content.base.schema.json#/properties/source/properties/git/properties/web?")

### web? Type

`string`

### web? Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## web!



`web!`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-web.md "image_content.base.schema.json#/properties/source/properties/git/properties/web!")

### web! Type

`string`

### web! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## web-



`web-`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Image Content](image_content-properties-source-properties-git-properties-web-.md "image_content.base.schema.json#/properties/source/properties/git/properties/web-")

### web- Type

unknown
