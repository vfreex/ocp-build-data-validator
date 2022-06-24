# Untitled string in Image Content Schema

```txt
image_content.base.schema.json#/properties/source/properties/git/properties/url!
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [image\_content.base.schema.json\*](../out/image_content.base.schema.json "open original schema") |

## url! Type

`string`

## url! Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^((git@[\w\.]+))([\w\.@\:/\-~]+)(\.git)(/)?$
```

[try pattern](https://regexr.com/?expression=%5E\(\(git%40%5B%5Cw%5C.%5D%2B\)\)\(%5B%5Cw%5C.%40%5C%3A%2F%5C-\~%5D%2B\)\(%5C.git\)\(%2F\)%3F%24 "try regular expression with regexr.com")
