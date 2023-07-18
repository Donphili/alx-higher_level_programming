-- Using temperature details set from ex.18
-- Shows top 3 cities by temperature during July and August
-- Ordered by temperature descending
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month = 8 OR month = 7
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
