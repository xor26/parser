CREATE TABLE public_trade (
    id BIGSERIAL PRIMARY KEY,
    topic VARCHAR(255) NOT NULL,
    ts INTEGER NOT NULL,
    type VARCHAR(255) NOT NULL,
    data JSONB NOT NULL
);

-- test data
-- INSERT INTO public_trade (topic, ts, type, data)
-- SELECT
--     (ARRAY['market_data', 'order_book', 'trade_execution'])[floor(random() * 3 + 1)],
--     floor(extract(epoch from now()) - random() * 86400)::int,
--     (ARRAY['BUY', 'SELL', 'LIMIT', 'MARKET'])[floor(random() * 4 + 1)],
--     jsonb_build_object(
--         'symbol', (ARRAY['AAPL', 'TSLA', 'BTC', 'ETH', 'GOOGL'])[floor(random() * 5 + 1)],
--         'price', round((random() * 1000)::numeric, 2),
--         'volume', floor(random() * 1000)
--     )
-- FROM generate_series(1, 1000);