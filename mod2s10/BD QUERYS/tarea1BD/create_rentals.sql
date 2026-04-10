SET search_path TO lyfter_car_rental;

CREATE TABLE IF NOT EXISTS rentals (
    id              SERIAL PRIMARY KEY,
    user_id         INT NOT NULL REFERENCES users(id),
    car_id          INT NOT NULL REFERENCES cars(id),
    rental_date     TIMESTAMP NOT NULL DEFAULT NOW(),
    status          VARCHAR(20) NOT NULL
);

INSERT INTO rentals (user_id, car_id, status) VALUES
(1,  3,  'completed'),
(2,  8,  'active'),
(3,  11, 'active'),
(4,  17, 'completed'),
(5,  21, 'active'),
(6,  27, 'cancelled'),
(7,  1,  'completed'),
(8,  4,  'active'),
(9,  7,  'completed'),
(10, 13, 'active');