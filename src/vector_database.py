import os

import numpy as np
from annoy import AnnoyIndex

from src.constants import DEFAULT_EMBEDDINGS_PATH, EMBEDDINGS_S3_URI, EMBEDDINGS_SIZE
from src.model import download_embeddings

database = None


def load_vector_database(embeddings_path: str = DEFAULT_EMBEDDINGS_PATH):
    global database

    if database:
        return

    if not os.path.isfile(embeddings_path):
        print("Downloading embeddings from internet")
        download_embeddings(
            remote_url=EMBEDDINGS_S3_URI,
            dest_path=embeddings_path
        )

    database = AnnoyIndex(EMBEDDINGS_SIZE, "angular")
    database.load(embeddings_path)


def get_top_similar(query_embedding: np.ndarray, n: int):
    return database.get_nns_by_vector(query_embedding, n)

def get_embedding_from_id(product_id: int):
    return database.get_item_vector(product_id)