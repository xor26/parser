from fastapi import FastAPI
from sqlalchemy.orm import Session

from data.db import SessionLocal
from data.models import Table1

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    with SessionLocal() as db:
        rows = db.query(Table1).all()

        return {
            "count": len(rows),
            "items": [
                {"id": r.id, "name": r.name}
                for r in rows
            ],
        }