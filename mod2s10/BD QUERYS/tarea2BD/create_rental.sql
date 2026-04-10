SET search_path TO lyfter_car_rental;

INSERT INTO rentals (user_id, car_id, status)
VALUES (2, 2, 'active');

UPDATE cars
SET status = 'rented'
WHERE id = 2;

SELECT
    r.id,
    u.full_name,
    c.brand,
    c.model,
    r.rental_date,
    r.status
FROM rentals r
JOIN users u ON r.user_id = u.id
JOIN cars  c ON r.car_id  = c.id
WHERE r.user_id = 2 AND r.car_id = 2;