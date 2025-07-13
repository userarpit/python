CREATE TABLE pediatrics.products (
    product_id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    price DECIMAL(10, 2),
    stock INTEGER,
    status TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO pediatrics.products (name, price, stock, status) VALUES
('Laptop', 999.99, 50, 'active'),
('Keyboard', 79.99, 100, 'active'),
('Mouse', 29.99, 200, 'active');


CREATE TABLE pediatrics.product_updates (
    name TEXT,
    price DECIMAL(10, 2),
    stock INTEGER,
    status TEXT
);

INSERT INTO pediatrics.product_updates VALUES
('Laptop', 1199.99, 999, 'active'),      -- Update: price and stock change
('Monitor', 299.99, 130, 'active'),      -- Insert: new product
('Keyboard', 100.99, 10, 'active'),  -- Delete: mark as discontinued
('Headphones', 89.99, 70, 'active');    -- Insert: another new product

truncate table pediatrics.product_updates;
SELECT * FROM pediatrics.products order by last_updated;
SELECT * FROM pediatrics.product_updates;

MERGE INTO pediatrics.products AS p
USING pediatrics.product_updates AS u
    ON p.name = u.name
WHEN MATCHED AND u.STATUS = 'discontinued' THEN
    DELETE
WHEN MATCHED AND u.STATUS = 'active' THEN
	UPDATE SET
        price = COALESCE(u.price, p.price),
        stock = u.stock,
        status = u.status,
        last_updated = CURRENT_TIMESTAMP
WHEN NOT MATCHED AND u.STATUS = 'active' THEN
	INSERT (name, price, stock, status)
    VALUES (u.name, u.price, u.stock, u.status)
RETURNING 
	merge_action() as action,
	p.product_id,
	p.name,
    p.price,
	u.stock,
    p.stock,
    p.status,
    p.last_updated;
