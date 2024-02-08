from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create DB
SQLALCHEMY_DATABASE_URI = 'sqlite:///social_network.db'

# Connecting to DB
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Generate of session
SessionLocal = sessionmaker(bind=engine)

# Main Class for modules
Base = declarative_base()


# Function for generator for connecting DB

def get_db():
    db = SessionLocal()
    try:
        yield db

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
