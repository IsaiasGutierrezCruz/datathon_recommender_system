from typing import List
from sentence_transformers import SentenceTransformer
from http import HTTPStatus

import requests


model = SentenceTransformer(
    'sentence-transformers/all-mpnet-base-v2',
    cache_folder="assets"
)



def get_embeddings(sentences: List[str]):
    return model.encode(sentences)


def download_embeddings(remote_url: str, dest_path: str) -> None:
    response = requests.get(url=remote_url)

    if response.status_code == HTTPStatus.OK:
        with open(dest_path, "wb") as f:
            f.write(response.content)
            print(f"Successfully downloaded embeddings database at: {dest_path}")
    else:
        raise Exception("Error trying to download embeddings database file")