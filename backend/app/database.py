from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates a local SQLite database file named 'safelearn.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./safelearn.db"

# engine: The actual connection to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal: The factory we'll use to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: The class our models (User, Secret) will inherit from
Base = declarative_base()