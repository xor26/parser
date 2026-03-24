import asyncio
import json
from datetime import datetime

import websockets

from data import db
from data.models import PublicTrade, Base


async def stream():
    url = "wss://stream.bybit.com/v5/public/spot"

    async with websockets.connect(url) as ws:

        sub = {
            "op": "subscribe",
            "args": [
                "publicTrade.BTCUSDT",
                "publicTrade.ETHUSDT",
                "publicTrade.SOLUSDT",
                "publicTrade.XRPUSDT",
                "publicTrade.DOGEUSDT",
                "publicTrade.ADAUSDT",
                "publicTrade.AVAXUSDT",
                "publicTrade.DOTUSDT",
                "publicTrade.LINKUSDT",
                "publicTrade.MATICUSDT",
            ]
        }

        await ws.send(json.dumps(sub))

        while True:
            msg = await ws.recv()
            async with db.async_session() as session:
                async with session.begin():
                    msg = json.loads(msg)
                    if 'topic' not in msg:
                        continue

                    data = json.dumps(msg['data'])
                    ts = datetime.fromtimestamp(int(msg['ts'])/ 1e3)
                    trade = PublicTrade(topic=msg['topic'], ts=ts, type=msg['type'],data=data)
                    session.add(trade)
                    print('added')



async def init_db():
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("PURGED")
        print(Base.metadata is Base.metadata)

asyncio.run(stream())