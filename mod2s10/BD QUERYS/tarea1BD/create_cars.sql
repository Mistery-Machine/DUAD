SET search_path TO lyfter_car_rental;

CREATE TABLE IF NOT EXISTS cars (
    id            SERIAL PRIMARY KEY,
    brand         VARCHAR(50)  NOT NULL,
    model         VARCHAR(50)  NOT NULL,
    year          INT          NOT NULL,
    status        VARCHAR(20)  NOT NULL
);

INSERT INTO cars (brand, model, year, status) VALUES
('Toyota',      'Corolla',   2020, 'available'),
('Toyota',      'Hilux',     2021, 'available'),
('Toyota',      'RAV4',      2019, 'rented'),
('Honda',       'Civic',     2022, 'available'),
('Honda',       'CR-V',      2020, 'available'),
('Honda',       'Pilot',     2018, 'disabled'),
('Hyundai',     'Tucson',    2021, 'available'),
('Hyundai',     'Elantra',   2022, 'rented'),
('Hyundai',     'Santa Fe',  2019, 'available'),
('Kia',         'Sportage',  2021, 'available'),
('Kia',         'Sorento',   2020, 'rented'),
('Kia',         'Picanto',   2022, 'available'),
('Nissan',      'Sentra',    2021, 'available'),
('Nissan',      'X-Trail',   2019, 'disabled'),
('Nissan',      'Frontier',  2022, 'available'),
('Mazda',       'CX-5',      2020, 'available'),
('Mazda',       'Mazda3',    2021, 'rented'),
('Mazda',       'CX-30',     2022, 'available'),
('Suzuki',      'Vitara',    2020, 'available'),
('Suzuki',      'Swift',     2021, 'available'),
('Ford',        'Explorer',  2019, 'rented'),
('Ford',        'Escape',    2022, 'available'),
('Ford',        'Ranger',    2020, 'available'),
('Chevrolet',   'Tracker',   2021, 'available'),
('Chevrolet',   'Captiva',   2019, 'disabled'),
('Mitsubishi',  'Outlander', 2021, 'available'),
('Mitsubishi',  'L200',      2020, 'rented'),
('Volkswagen',  'Golf',      2022, 'available'),
('Volkswagen',  'Tiguan',    2021, 'available'),
('Subaru',      'Forester',  2020, 'available');