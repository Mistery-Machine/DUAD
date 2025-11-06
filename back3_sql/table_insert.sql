INSERT INTO products (name, price, date_in, brand)
VALUES
('Laptop Lenovo', 550000, '2025-01-10', 'Lenovo'),
('Celular Samsung', 320000, '2025-02-15', 'Samsung'),
('Mouse Logitech', 15000, '2025-03-05', 'Logitech'),
('Monitor LG', 120000, '2025-03-20', 'LG'),
('Teclado Redragon', 25000, '2025-04-02', 'Redragon');


INSERT INTO invoices (buy_date, buyer_mail, total_amount, phone_number, cashier_code)
VALUES
('2025-05-01', 'juan@example.com', 685000, '88881234', 'E001'),
('2025-05-03', 'maria@example.com', 345000, '89994567', 'E002'),
('2025-05-05', 'juan@example.com', 15000, '88881234', 'E001');


INSERT INTO invoice_details (invoice_number, product_code, amount, total_amount)
VALUES
(1, 1, 1, 550000),
(1, 3, 1, 15000),
(1, 4, 1, 120000),
(2, 2, 1, 320000),
(2, 5, 1, 25000),
(3, 3, 1, 15000);


INSERT INTO shopping_carts (user_mail)
VALUES
('juan@example.com'),
('maria@example.com');


INSERT INTO cart_products (id_cart, product_code, amount)
VALUES
(1, 1, 1),
(1, 3, 2),
(2, 2, 1);