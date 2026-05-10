from sqlalchemy.orm import Session
import models, security

def create_memory(db: Session, title: str, content: str):
    # Encrypt content before saving to the database
    encrypted = security.encrypt_content(content)
    db_memory = models.SecureMemory(title=title, encrypted_content=encrypted)
    db.add(db_memory)
    db.commit()
    db.refresh(db_memory)
    return db_memory

def get_memories(db: Session):
    return db.query(models.SecureMemory).all()