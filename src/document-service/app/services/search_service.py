from app.services.embedding_service import EmbeddingService
from app.services.qdrant_service import qdrant_service
from app.utils.logger import logger

embedding_service = EmbeddingService()


class SearchService:

    @staticmethod
    def semantic_search(query, top_k=5):

        logger.info("Generating query embedding")

        embedding = embedding_service.generate_embedding(query)

        results = qdrant_service.search(
            embedding,
            limit=top_k
        )
        logger.info("Generating query embedding")
        response = []

        for result in results:

            response.append(
                {
                    "document_id": result.payload["document_id"],
                    "title": result.payload["title"],
                    "author": result.payload["author"],
                    "tags": result.payload["tags"],
                    "score": result.score
                }
            )

        return response