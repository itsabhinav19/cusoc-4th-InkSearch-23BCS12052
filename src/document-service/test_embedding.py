from app.services.embedding_service import EmbeddingService

service = EmbeddingService()

embedding = service.generate_embedding(
    "Semantic Search is amazing"
)

print(len(embedding))

print(embedding[:10])