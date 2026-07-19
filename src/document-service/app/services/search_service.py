import json
import numpy as np

from app.services.embedding_service import EmbeddingService

embedding_service = EmbeddingService()


class SearchService:

    @staticmethod
    def cosine_similarity(v1, v2):

        v1 = np.array(v1)
        v2 = np.array(v2)

        return np.dot(v1, v2) / (
            np.linalg.norm(v1) * np.linalg.norm(v2)
        )

    @staticmethod
    def semantic_search(query, documents):

        query_embedding = embedding_service.generate_embedding(query)

        results = []

        for document in documents:

            if document.embedding is None:
                continue

            document_embedding = json.loads(document.embedding)

            similarity = SearchService.cosine_similarity(
                query_embedding,
                document_embedding
            )

            results.append(
                {
                    "document": document,
                    "score": float(similarity)
                }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results