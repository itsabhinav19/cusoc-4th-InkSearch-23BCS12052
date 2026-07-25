from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)

from app.core.config import settings


class QdrantService:

    def __init__(self):

        self.collection_name = settings.QDRANT_COLLECTION

        self.client = QdrantClient(
            path=settings.QDRANT_PATH
        )

        self.create_collection()

    def create_collection(self):

        if not self.client.collection_exists(
            self.collection_name
        ):

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def store_document(
        self,
        document_id: int,
        embedding: list[float],
        title: str,
        author: str,
        tags: str
    ):

        point = PointStruct(
            id=document_id,
            vector=embedding,
            payload={
                "document_id": document_id,
                "title": title,
                "author": author,
                "tags": tags
            }
        )

        self.client.upsert(
            collection_name=self.collection_name,
            points=[point],
            wait=True
        )


qdrant_service = QdrantService()