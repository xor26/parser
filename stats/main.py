from fastapi import FastAPI
from sqlalchemy import select

from data.db import async_session
from data.models import PublicTrade

app = FastAPI()

@app.get("/")
async def root():
    async with async_session() as session:
        stmt = select(PublicTrade)
        rows = await session.execute(stmt)
        return {
            "count": len(list(rows.scalars())),
        }