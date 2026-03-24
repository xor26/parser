import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, JSON, DateTime

from data.db import engine


class Base(AsyncAttrs, DeclarativeBase):
    async def reinit_base(self):
        async with engine.begin() as conn:
            await conn.run_sync(self.metadata.drop_all)
            await conn.run_sync(self.metadata.create_all)


class PublicTrade(Base):
    __tablename__ = "public_trade"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    topic: Mapped[str] = mapped_column(String)
    ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    type: Mapped[str] = mapped_column(String)
    data: Mapped[str] = mapped_column(JSON)
