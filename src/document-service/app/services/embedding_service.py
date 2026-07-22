import json
from functools import lru_cache
from sentence_transformers import SentenceTransformer

@lru_cache(maxsize=1)
def get_model():

    return SentenceTransformer("all-MiniLM-L6-v2")
class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate_embedding(self, text: str):

        embedding = self.model.encode(text)

        return embedding.tolist()

    def generate_embedding_json(self, text: str):

        embedding = self.model.encode(text)

        return json.dumps(embedding.tolist())