# Untitled boolean in Image Content Schema

```txt
image_content.base.schema.json#/properties/source/properties/ci_alignment/properties/streams_prs/properties/merge_first!
```

`merge_first` means that child images will not get PRs opened until this image is aligned. This helps prevent images like OpenShift's base image from having 100s of PRs referencing its PR.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [image\_content.base.schema.json\*](../out/image_content.base.schema.json "open original schema") |

## merge\_first! Type

`boolean`
