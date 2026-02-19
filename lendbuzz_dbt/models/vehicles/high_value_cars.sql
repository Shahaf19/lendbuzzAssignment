SELECT * FROM (
    SELECT *,
        NTILE(100) OVER (PARTITION BY year ORDER BY price DESC) AS year_price_percentile
    FROM {{ ref('all_cars') }}
)
WHERE year_price_percentile <= 10
ORDER BY year DESC, price DESC