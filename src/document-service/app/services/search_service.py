import json
import numpy as np

from app.services.embedding_service import EmbeddingService

embedding_service = EmbeddingService()


class SearchService:

    @staticmethod
    def cosine_similarity(v1, v2):

        v1 = np.array(v1)
        v2 = np.array(v2)

        return float(
            np.dot(v1, v2)
            /
            (
                np.linalg.norm(v1)
                *
                np.linalg.norm(v2)
            )
        )

    @staticmethod
    def search(query, documents):

        query_embedding = embedding_service.generate_embedding(query)

        results = []

        for doc in documents:

            embedding = json.loads(doc.embedding)

            score = SearchService.cosine_similarity(
                query_embedding,
                embedding
            )

            results.append(
                {
                    "document": doc,
                    "score": score
                }
            )

        return sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )