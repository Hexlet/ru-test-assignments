CREATE TABLE products (
    product_key INT,
    category_key INT,
    name VARCHAR(512),
    price INT
);

INSERT INTO products (product_key, category_key, name, price) VALUES
	(1, 1, 'Laptop', 1200),
	(2, 2, 'Smartphone', 800),
	(3, 3, 'Tablet', 600),
	(4, 1, 'Desktop', 1000),
	(5, 4, 'Monitor', 300),
	(6, 2, 'Smartwatch', 250),
	(7, 3, 'E-Reader', 180),
	(8, 4, 'Keyboard', 100),
	(9, 1, 'Mouse', 50),
	(10, 2, 'Charger', 25);