SET search_path TO lyfter_car_rental;

UPDATE rentals
SET status = 'completed'
WHERE id = 2;

UPDATE cars
SET status = 'available'
WHERE id = 2;

SELECT
    r.id,
    u.full_name,
    c.brand,
    c.model,
    r.rental_date,
    r.status AS rental_status,
    c.status AS car_status
FROM rentals r
JOIN users u ON r.user_id = u.id
JOIN cars  c ON r.car_id  = c.id
WHERE r.id = 2;