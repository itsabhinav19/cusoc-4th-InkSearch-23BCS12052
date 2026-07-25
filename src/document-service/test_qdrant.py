from app.services.embedding_service import EmbeddingService
from app.services.qdrant_service import qdrant_service


embedding_service = EmbeddingService()

text = "Semantic search uses vector embeddings."

embedding = embedding_service.generate_embedding(text)

qdrant_service.store_document(
    document_id=999,
    embedding=embedding,
    title="Test Document",
    author="Test",
    tags="AI"
)

print("Vector stored successfully!")