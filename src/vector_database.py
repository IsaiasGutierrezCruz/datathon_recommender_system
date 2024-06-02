from functools import lru_cache

import numpy as np
from annoy import AnnoyIndex

from src.constants import DEFAULT_EMBEDDINGS_PATH, EMBEDDINGS_SIZE

database = None


def load_vector_database(embeddings_path: str = DEFAULT_EMBEDDINGS_PATH):
    global database

    if database:
        return

    database = AnnoyIndex(EMBEDDINGS_SIZE, "angular")
    database.load(embeddings_path)


def get_top_similar(query_embedding: np.ndarray, n: int):
    return database.get_nns_by_vector(query_embedding, n)

def get_embedding_from_id(product_id: int):
    return database.get_item_vector(product_id)