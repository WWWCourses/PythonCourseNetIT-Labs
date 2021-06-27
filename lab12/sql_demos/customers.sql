use customers;

CREATE TABLE `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8

CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `order_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8


SELECT first_name, order_date
FROM customers.customers as customers, orders
WHERE customers.id=orders.customer_id


/* -------------------------------------------------------------------------- */
/*                                    JOINS                                   */
/* -------------------------------------------------------------------------- */
-- Inner Join - same as WHERE....
SELECT first_name, order_date
FROM customers.customers as customers
INNER JOIN orders
ON customers.id=orders.customer_id

/* -------------------------------- LEFT JOIN ------------------------------- */
SELECT first_name, order_date
FROM customers.customers as customers
LEFT JOIN orders
ON customers.id=orders.customer_id

-- LEFT JOIN with WHERE
-- select all orders of Ana
SELECT first_name, order_date
FROM customers.customers as customers
LEFT JOIN orders
ON customers.id=orders.customer_id
WHERE customers.first_name='Ana'

-- select all customers, which do not have ordres
SELECT first_name, order_date
FROM customers.customers as customers
LEFT JOIN orders
ON customers.id=orders.customer_id
WHERE orders.customer_id IS NULL

/* ------------------------------- RIGHT JOIN ------------------------------- */
SELECT first_name, order_date
FROM customers.customers as customers
RIGHT JOIN orders
ON customers.id=orders.customer_id

/* ------------------------------- OUTER JOIN ------------------------------- */
SELECT first_name, order_date
FROM customers.customers as customers
FULL OUTER JOIN orders
ON customers.id=orders.customer_id



/* -------------------------------------------------------------------------- */
/*                                    VIEWS                                   */
/* -------------------------------------------------------------------------- */
CREATE VIEW cust_order
AS (
SELECT first_name, order_date
FROM customers.customers as customers, orders
WHERE customers.id=orders.customer_id
);