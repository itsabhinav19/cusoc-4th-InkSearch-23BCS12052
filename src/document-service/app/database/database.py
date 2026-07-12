from sqlalchemy import create_engine  # type: ignore[import]
from sqlalchemy.orm import sessionmaker  # type: ignore[import]
from app.config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()