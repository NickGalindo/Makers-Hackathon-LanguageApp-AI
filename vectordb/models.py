from pymilvus import DataType, FieldSchema, CollectionSchema

# English schemas for cards and words
en_cardid = FieldSchema(
    name="cardid",
    dtype=DataType.VARCHAR,
    max_length=200,
    is_primary=True,
)

en_card = FieldSchema(
    name="card",
    dtype=DataType.FLOAT_VECTOR,
    dim=1024,
)

en_card_schema = CollectionSchema(
    fields=[en_cardid, en_card],
    description="english card schema"
)


en_wordid = FieldSchema(
    name="wordid",
    dtype=DataType.VARCHAR,
    max_length=200,
    is_primary=True,
)

en_word = FieldSchema(
    name="word",
    dtype=DataType.FLOAT_VECTOR,
    dim=1024,
)

en_word_schema = CollectionSchema(
    fields=[en_wordid, en_word],
    description="english word schema"
)

# french schemas for cards and words
fr_cardid = FieldSchema(
    name="cardid",
    dtype=DataType.VARCHAR,
    max_length=200,
    is_primary=True,
)

fr_card = FieldSchema(
    name="card",
    dtype=DataType.FLOAT_VECTOR,
    dim=1024,
)

fr_card_schema = CollectionSchema(
    fields=[fr_cardid, fr_card],
    description="french card schema"
)


fr_wordid = FieldSchema(
    name="wordid",
    dtype=DataType.VARCHAR,
    max_length=200,
    is_primary=True,
)

fr_word = FieldSchema(
    name="word",
    dtype=DataType.FLOAT_VECTOR,
    dim=1024,
)

fr_word_schema = CollectionSchema(
    fields=[fr_wordid, fr_word],
    description="french word schema"
)
