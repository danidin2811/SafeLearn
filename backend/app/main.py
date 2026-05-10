from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database, security

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"status": "SafeLearn is Online"}


@app.post("/test-save/")
def test_save(title: str, content: str, db: Session = Depends(get_db)):
    # 1. Encrypt the content using security.py
    encrypted = security.encrypt_content(content)

    # 2. Create the Database object
    new_memory = models.SecureMemory(title=title, encrypted_content=encrypted)

    # 3. Save to safelearn.db
    db.add(new_memory)
    db.commit()
    db.refresh(new_memory)

    return {"message": "Saved!", "database_record": new_memory}


# This endpoint lets you see what is in the database
@app.get("/test-view/")
def test_view(db: Session = Depends(get_db)):
    all_memories = db.query(models.SecureMemory).all()
    return all_memories