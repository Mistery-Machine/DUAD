SET search_path TO lyfter_car_rental;

INSERT INTO users (full_name, email, username, password, birthdate, status)
VALUES (
    'Daniel Fonseca',
    'd.fonseca@gmail.com',
    'dfonseca',
    'Pass123!',
    '1995-05-20',
    'active'
);

SELECT * FROM users WHERE username = 'dfonseca';