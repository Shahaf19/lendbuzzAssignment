SELECT * FROM {{ source('Car_Inventory', 'car_inventory') }}
QUALIFY ROW_NUMBER() OVER (PARTITION BY vin ORDER BY price DESC) = 1
