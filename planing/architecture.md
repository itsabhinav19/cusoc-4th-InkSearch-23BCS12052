# High Level Architecture

User

↓

React Frontend

↓

API Gateway

↓

Search Service

↓

Embedding Service

↓

PostgreSQL

↓

Vector Database

↓

Redis Cache

↓

Search Results

## Document Service

Responsible for:
- Uploading documents
- Updating documents
- Deleting documents
- Storing metadata in PostgreSQL

---

## Embedding Service

Responsible for:
- Generating embeddings
- Updating embeddings
- Sending vectors to the vector database

---

## Search Service

Responsible for:
- Receiving user queries
- Generating query embeddings
- Performing vector similarity search
- Returning ranked results