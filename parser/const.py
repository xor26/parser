PUBLIC_SPOTS_URL = "wss://stream.bybit.com/v5/public/spot"
SUBSCRIPTIONS = {
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

PUB_MSG_CRITERIA = "topic"