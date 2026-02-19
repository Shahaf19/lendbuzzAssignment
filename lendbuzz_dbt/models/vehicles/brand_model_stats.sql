SELECT brand,
 model,
 MIN(year) AS min_year,
 MEDIAN(year) AS median_year,
 MAX(year) AS max_year,

 MIN(mileage) AS min_mileage,
 MEDIAN(mileage) AS median_mileage,
 MAX(mileage) AS max_mileage,

 MIN(price) AS min_price,
 MEDIAN(price) AS median_price,
 MAX(price) AS max_price

 FROM {{ref('all_cars')}} GROUP BY brand, model

