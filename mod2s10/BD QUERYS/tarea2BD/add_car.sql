SET search_path TO lyfter_car_rental;

INSERT INTO cars (brand, model, year, status)
VALUES (
    'Toyota',
    'Yaris',
    2023,
    'available'
);

SELECT * FROM cars WHERE model = 'Yaris';