from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class SecureMemory(Base):
    __tablename__ = "memories"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String,index=True)
    encrypted_content = Column(Text)