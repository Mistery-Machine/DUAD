SET search_path TO lyfter_car_rental;

UPDATE users
SET status = 'inactive'
WHERE id = 1;

SELECT id, full_name, status FROM users WHERE id = 1;