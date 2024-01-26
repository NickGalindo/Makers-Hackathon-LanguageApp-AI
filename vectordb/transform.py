from typing import List
from sentence_transformers import SentenceTransformer
from torch import Tensor
from numpy import ndarray

def transform(sentence: str, model: SentenceTransformer) -> Tensor:
    """
    Use LLM model to transform the input sentence into vector representation

    :param sentence: the sentence to transform
    :param model: the model to use for transformation
    """
    res: List[Tensor] | ndarray | Tensor = model.encode(sentence, convert_to_tensor=True)
    assert(isinstance(res, Tensor))

    return res
