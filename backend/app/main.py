from fastapi import FastAPI
from database import engine, Base
import models

# This line is the magic!
# It tells SQLAlchemy to look at 'Base' and create
# all tables it finds in 'models.py' inside the database 'engine'.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SafeLearn API is running and Database is initialized!"}