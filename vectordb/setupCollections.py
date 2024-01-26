from typing import Dict, Tuple
from manager.load_config import CONFIG

from pymilvus import Collection, utility

from vectordb.models import fr_card_schema, fr_word_schema, en_word_schema, en_card_schema

def setupCols() -> Tuple[Collection, Collection, Collection, Collection]:
    """
    Load the collections from the vector database

    :return: returns a tuple of the collections in order fr_card_col, fr_word_col, en_card_col, en_word_col
    """
    index_params: Dict = {
        "metric_type": "L2",
        "index_type": "IVF_SQ8",
        "params":{"nlist": 1024}
    }

    # French collections
    if not utility.has_collection("fr_card"):
        fr_card_col = Collection(
            name="fr_card",
            schema=fr_card_schema,
            using=CONFIG["VDB_ALIAS"]
        )
        fr_card_col.create_index(field_name="card", index_params=index_params)
    else:
        fr_card_col = Collection("fr_card")

    fr_card_col.load()


    if not utility.has_collection("fr_word"):
        fr_word_col = Collection(
            name="fr_word",
            schema=fr_word_schema,
            using=CONFIG["VDB_ALIAS"]
        )
        fr_word_col.create_index(field_name="word", index_params=index_params)
    else:
        fr_word_col = Collection("fr_word")

    fr_word_col.load()


    #Englsh collections
    if not utility.has_collection("en_card"):
        en_card_col = Collection(
            name="en_card",
            schema=en_card_schema,
            using=CONFIG["VDB_ALIAS"]
        )
        en_card_col.create_index(field_name="card", index_params=index_params)
    else:
        en_card_col = Collection("en_card")

    en_card_col.load()


    if not utility.has_collection("en_word"):
        en_word_col = Collection(
            name="en_word",
            schema=en_word_schema,
            using=CONFIG["VDB_ALIAS"]
        )
        en_word_col.create_index(field_name="word", index_params=index_params)
    else:
        en_word_col = Collection("en_word")

    en_word_col.load()

    return fr_card_col, fr_word_col, en_card_col, en_word_col
