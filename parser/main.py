import asyncio
import json
from datetime import datetime

import websockets

from data import db
from data.models import PublicTrade, Base
from parser.const import PUBLIC_SPOTS_URL, SUBSCRIPTIONS, PUB_MSG_CRITERIA

class Parser:
    def __init__(self):
        pass

    async def stream(self):
        async with websockets.connect(PUBLIC_SPOTS_URL) as ws:
            await ws.send(json.dumps(SUBSCRIPTIONS))
            while True:
                msg = await ws.recv()
                msg = json.loads(msg)
                if PUB_MSG_CRITERIA in msg:
                    await self.process_pub_trade_msg(msg)


    async def process_pub_trade_msg(self, msg):
        async with db.async_session() as session:
            async with session.begin():
                data = json.dumps(msg["data"])
                ts = datetime.fromtimestamp(int(msg["ts"])/ 1e3)
                trade = PublicTrade(topic=msg["topic"], ts=ts, type=msg["type"],data=data)
                session.add(trade)

    async def init_db(self,):
        # todo move it to db dir
        async with db.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

async def parser():
    p = Parser()
    await p.stream()


asyncio.run(parser())