from typing import Dict, List
from endpoints.models import CardHistory, WordHistory

from manager.load_config import CONFIG

import numpy as np

from pymilvus import Collection 
from sentence_transformers import SentenceTransformer

from vectordb.transform import transform

def __checkCardExistence(card: Dict, col: Collection):
    res = col.query(
        expr = f"cardid == \"{card['cardid']}\"",
        offset=0,
        limit=1,
        output_fields=["cardid", "card"],
        consistency_level="Strong"
    )

    if len(res) > 0:
        return res

    return None

def addCard(card: Dict, col: Collection, model: SentenceTransformer):
    print(col.schema)
    if __checkCardExistence(card, col):
        return 

    card_vector: List = transform(card["card"], model).flatten().tolist()

    new_card: List = [
        [card["cardid"]],
        [card_vector]
    ]

    col.insert(new_card)

    return


def __checkWordExistence(word: Dict, col: Collection):
    res = col.query(
        expr = f"wordid == \"{word['wordid']}\"",
        offset=0,
        limit=1,
        output_fields=["wordid", "word"],
        consistency_level="Strong"
    )

    if len(res) > 0:
        return res

    return None

def addWord(word: Dict, col: Collection, model: SentenceTransformer):
    if __checkWordExistence(word, col):
        return 

    word_vector: List = transform(word["word"], model).flatten().tolist()

    new_word: List = [
        [word["wordid"]],
        [word_vector]
    ]

    col.insert(new_word)

    return


def recommendCards(card_history: CardHistory, card_col: Collection, model: SentenceTransformer):
    search_params: Dict = {"metric_type": "L2", "params": {"nprobe": 10}}

    card_embeddings: List = []

    for i in card_history.history:
        card_embedding = transform(i, model).flatten().tolist()
        card_embeddings.append(card_embedding)

    for _ in range(CONFIG["BOUNCINESS"]):
        card_embeddings.append(np.random.uniform(low=-2.0, high=2.0, size=1024))

    res = card_col.search(
        data=card_embeddings,
        anns_field="card",
        param=search_params,
        limit=4
    )

    recommendations = set()
    for aux in res: #type: ignore
        for entity in aux:
            recommendations.add(entity.id)

    return [i for i in np.random.choice(list(recommendations), size=min(4, len(recommendations)), replace=False).tolist()]
