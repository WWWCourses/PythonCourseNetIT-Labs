
DROP DATABASE IF EXISTS customers_db;
CREATE DATABASE customers_db;
use customers_db;

CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `order_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) DEFAULT CHARSET=utf8;

INSERT into customers (first_name, last_name, email)
  VALUES
    ('Ivan', 'Ivanov', 'ivan@gmail.com'),
    ('Asen', 'Asenov',''),
    ('Stoyan', 'Stoyanov', 'stoyan@abv.bg'),
    ('Petar', 'Petrov', 'petar@abv.bg'),
    ('Maria', 'Petrova','');

INSERT INTO orders (customer_id,order_date)
  VALUES
    (1, "2020-01-20 21:00:00"),
    (3, "2020-01-20 21:30:00"),
    (4, "2020-01-20 21:40:00"),
    (1, "2020-01-20 22:00:00"),
    (1, "2020-01-20 22:10:00"),
    (3, "2020-01-20 22:10:00");

