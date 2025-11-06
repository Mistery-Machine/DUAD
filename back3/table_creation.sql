CREATE TABLE products (
  code INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(50) NOT NULL, 
  price DOUBLE NOT NULL, 
  date_in DATETIME, 
  brand VARCHAR(50)
);

CREATE TABLE invoices (
  invoice_number INTEGER PRIMARY KEY AUTOINCREMENT, 
  buy_date DATETIME NOT NULL, 
  buyer_mail VARCHAR(50) NOT NULL, 
  total_amount DOUBLE
);

CREATE TABLE invoice_details (
  id_detail INTEGER PRIMARY KEY AUTOINCREMENT, 
  invoice_number INTEGER NOT NULL REFERENCES invoices(invoice_number),
  product_code INTEGER NOT NULL REFERENCES products(code),
  amount INTEGER NOT NULL, 
  total_amount DOUBLE
);

CREATE TABLE shopping_carts (
  id_cart INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_mail VARCHAR(50) NOT NULL
);

CREATE TABLE cart_products (
  id_cart INTEGER NOT NULL REFERENCES shopping_carts(id_cart),
  product_code INTEGER NOT NULL REFERENCES products(code),
  amount INTEGER NOT NULL, 
  PRIMARY KEY (id_cart, product_code)
);