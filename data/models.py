import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, JSON, DateTime


class Base(AsyncAttrs, DeclarativeBase):
    pass

class PublicTrade(Base):
    __tablename__ = "public_trade"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    topic: Mapped[str] = mapped_column(String)
    ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    type: Mapped[str] = mapped_column(String)
    data: Mapped[str] = mapped_column(JSON)
