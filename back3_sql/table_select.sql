SELECT * FROM products;

SELECT * FROM products WHERE price > 50000;

SELECT * FROM invoice_details WHERE product_code = 1;

SELECT 
  product_code, 
  SUM(amount) AS total_amount_sold FROM invoice_details GROUP BY product_code;

SELECT * from invoices WHERE buyer_mail = 'juan@example.com';

SELECT * from invoices ORDER BY total_amount DESC;

SELECT * from invoices WHERE invoice_number =1