CREATE DATABASE stock_market;
use stock_market;
CREATE TABLE stock_prices (
    date DATE,
    symbol VARCHAR(10),
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume BIGINT
);
select * from stock_prices;
SELECT COUNT(*) FROM stock_prices;
/*top 10 most traded stocks*/
SELECT symbol, SUM(volume) AS total_volume
FROM stock_prices
GROUP BY symbol
ORDER BY total_volume DESC
LIMIT 10;
/*Highest Average Price Stocks*/
SELECT symbol, AVG(close) AS avg_price
FROM stock_prices
GROUP BY symbol
ORDER BY avg_price DESC
LIMIT 10;
/*Monthly Market Trend*/
SELECT MONTH(date) AS month, AVG(close) AS avg_price
FROM stock_prices
GROUP BY month
ORDER BY month;
/*Highest volatility Stocks*/
SELECT symbol,
MAX(high) - MIN(low) AS price_volatility
FROM stock_prices
GROUP BY symbol
ORDER BY price_volatility DESC
LIMIT 10;