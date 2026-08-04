# from sqlalchemy.orm import Session

# from app.models.document import Document


# class SearchRepository:

#     @staticmethod
#     def get_documents_with_embeddings(db: Session):

#         return (
#             db.query(Document)
#             .filter(Document.embedding != None)
#             .all()
#         )