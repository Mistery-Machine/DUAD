SET search_path TO lyfter_car_rental;

UPDATE cars
SET status = 'disabled'
WHERE id = 3;

SELECT id, brand, model, status FROM cars WHERE id = 3;