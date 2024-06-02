from typing import List
from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    'sentence-transformers/all-mpnet-base-v2',
    cache_folder="assets"
)



def get_embeddings(sentences: List[str]):
    return model.encode(sentences)