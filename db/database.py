from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Create database engine (this will create the file)
DATABASE_URL = "sqlite:///./gym_trainer.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()