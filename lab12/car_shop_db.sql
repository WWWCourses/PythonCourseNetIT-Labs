-- CREATE  DATABASE car_shop_db

use car_shop_db;

/* -------------------------------------------------------------------------- */
/*                                  car_parts                                 */
/* -------------------------------------------------------------------------- */
-- code,product_name,category,buying_price,client_price,application,manufacturer

DROP TABLE IF EXISTS  car_parts;
CREATE TABLE car_parts(
	code INT,
	product_name VARCHAR(200),
	buying_price DECIMAL(7,2),
	created_at TIMESTAMP,
	PRIMARY KEY(code)
);

ALTER TABLE car_parts
	ADD INDEX(product_name(200));


/* -------------------------------------------------------------------------- */
/*                                   orders                                   */
/* -------------------------------------------------------------------------- */
-- date,user,ordered_parts,total_costs,profit
DROP TABLE IF EXISTS  orders;
CREATE TABLE orders(
    id int NOT NULL AUTO_INCREMENT,
    order_date DATETIME NOT NULL,
	user_id int,
	primary key(id),
	FOREIGN KEY(user_id) REFERENCES users (id)
) default charset utf8;

/* -------------------------------------------------------------------------- */
/*                                    users                                   */
/* -------------------------------------------------------------------------- */
-- role,first_name,last_name,email,phone_number,password,created
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id int NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(id)
) default charset utf8;

INSERT INTO users (first_name)
	VALUES
		('Maria'),
		('Pesho'),
		('Ivan');

INSERT INTO orders (order_date, user_id)
	VALUES
		('2021-01-31 12:30:23', 1),
		('2021-01-31 13:30:23', 1),
		('2021-01-31 13:35:23', 2),
		('2021-01-31 14:35:23', 1);

DELETE from orders
	WHERE orders.id=2;