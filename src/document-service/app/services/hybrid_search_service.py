from app.services.search_service import SearchService
from app.repositories.document_repository import DocumentRepository


class HybridSearchService:

    RRF_K = 60

    @staticmethod
    def reciprocal_rank(rank: int) -> float:

        return 1 / (
            HybridSearchService.RRF_K + rank
        )

    @staticmethod
    def hybrid_search(
        db,
        query: str,
        top_k: int = 5
    ):

        # --------------------------------
        # 1. Semantic Search
        # --------------------------------

        semantic_results = SearchService.semantic_search(
            query,
            top_k=10
        )

        # --------------------------------
        # 2. Keyword Search
        # --------------------------------

        keyword_documents = (
            DocumentRepository.keyword_search(
                db,
                query,
                limit=10
            )
        )

        # --------------------------------
        # 3. Calculate RRF Scores
        # --------------------------------

        scores = {}

        documents = {}

        # Semantic ranking

        for rank, result in enumerate(
            semantic_results,
            start=1
        ):

            document_id = result["document_id"]

            scores[document_id] = (
                scores.get(document_id, 0)
                +
                HybridSearchService.reciprocal_rank(rank)
            )

            documents[document_id] = result

        # Keyword ranking

        for rank, document in enumerate(
            keyword_documents,
            start=1
        ):

            document_id = document.id

            scores[document_id] = (
                scores.get(document_id, 0)
                +
                HybridSearchService.reciprocal_rank(rank)
            )

            if document_id not in documents:

                documents[document_id] = {
                    "document_id": document.id,
                    "title": document.title,
                    "author": document.author,
                    "tags": document.tags
                }

        # --------------------------------
        # 4. Sort by RRF Score
        # --------------------------------

        ranked_documents = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # --------------------------------
        # 5. Build Response
        # --------------------------------

        response = []

        for document_id, score in ranked_documents[:top_k]:

            result = documents[document_id].copy()

            result["hybrid_score"] = score

            response.append(result)

        return response