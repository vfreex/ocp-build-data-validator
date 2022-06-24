# Streams Schema

```txt
streams.schema.json
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [streams.schema.json](../out/streams.schema.json "open original schema") |

## Streams Type

`object` ([Streams](streams.md))

# Streams Properties

| Property | Type     | Required | Nullable       | Defined by                                                                      |
| :------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------ |
| `^.+$`   | `object` | Optional | cannot be null | [Streams](streams-defs-stream.md "streams.schema.json#/patternProperties/^.+$") |

## Pattern: `^.+$`



`^.+$`

*   is optional

*   Type: `object` ([Details](streams-defs-stream.md))

*   cannot be null

*   defined in: [Streams](streams-defs-stream.md "streams.schema.json#/patternProperties/^.+$")

### ^.+$ Type

`object` ([Details](streams-defs-stream.md))

# Streams Definitions

## Definitions group stream

Reference this group by using

```json
{"$ref":"streams.schema.json#/$defs/stream"}
```

| Property                                      | Type      | Required | Nullable       | Defined by                                                                                                                          |
| :-------------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| [image](#image)                               | `string`  | Required | cannot be null | [Streams](streams-defs-stream-properties-image.md "streams.schema.json#/$defs/stream/properties/image")                             |
| [upstream\_image\_base](#upstream_image_base) | `string`  | Optional | cannot be null | [Streams](streams-defs-stream-properties-upstream_image_base.md "streams.schema.json#/$defs/stream/properties/upstream_image_base") |
| [upstream\_image](#upstream_image)            | `string`  | Required | cannot be null | [Streams](streams-defs-stream-properties-upstream_image.md "streams.schema.json#/$defs/stream/properties/upstream_image")           |
| [mirror](#mirror)                             | `boolean` | Optional | cannot be null | [Streams](streams-defs-stream-properties-mirror.md "streams.schema.json#/$defs/stream/properties/mirror")                           |
| [transform](#transform)                       | `string`  | Optional | cannot be null | [Streams](streams-defs-stream-properties-transform.md "streams.schema.json#/$defs/stream/properties/transform")                     |

### image



`image`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Streams](streams-defs-stream-properties-image.md "streams.schema.json#/$defs/stream/properties/image")

#### image Type

`string`

#### image Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### upstream\_image\_base



`upstream_image_base`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Streams](streams-defs-stream-properties-upstream_image_base.md "streams.schema.json#/$defs/stream/properties/upstream_image_base")

#### upstream\_image\_base Type

`string`

#### upstream\_image\_base Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### upstream\_image



`upstream_image`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Streams](streams-defs-stream-properties-upstream_image.md "streams.schema.json#/$defs/stream/properties/upstream_image")

#### upstream\_image Type

`string`

#### upstream\_image Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### mirror



`mirror`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Streams](streams-defs-stream-properties-mirror.md "streams.schema.json#/$defs/stream/properties/mirror")

#### mirror Type

`boolean`

### transform



`transform`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Streams](streams-defs-stream-properties-transform.md "streams.schema.json#/$defs/stream/properties/transform")

#### transform Type

`string`

#### transform Constraints

**minimum length**: the minimum number of characters for this string is: `1`
