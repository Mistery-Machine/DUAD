SET search_path TO lyfter_car_rental;

SELECT
    c.id,
    c.brand,
    c.model,
    c.year,
    u.full_name AS rented_by,
    r.rental_date
FROM cars c
JOIN rentals r ON r.car_id = c.id
JOIN users  u ON r.user_id = u.id
WHERE c.status = 'rented'
  AND r.status = 'active';

SELECT
    id,
    brand,
    model,
    year
FROM cars
WHERE status = 'available';