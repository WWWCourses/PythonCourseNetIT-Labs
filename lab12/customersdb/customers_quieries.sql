
-- Show the name and order date of all customers who have ordered something. Sort by first_name, ascending:
SELECT first_name, order_date
	FROM customers, orders
	WHERE customers.id=orders.customer_id
	ORDER BY first_name;


/* -------------------------------------------------------------------------- */
/*                                    JOINS                                   */
/* -------------------------------------------------------------------------- */
/* ------------------------------- INNER JOIN ------------------------------- */
-- Same as SELECT ... WHERE above
-- Show the name and order date of all customers who have ordered something. Sort by first_name, ascending
SELECT first_name, order_date
	FROM customers
	INNER JOIN orders
	ON customers.id=orders.customer_id
	ORDER BY first_name;

/* -------------------------------- LEFT JOIN ------------------------------- */
-- Show the name and order date of all customers, no matter if they have orders or not:
SELECT first_name, order_date
	FROM customers
	LEFT JOIN orders
	ON customers.id=orders.customer_id;

-- LEFT JOIN with WHERE
-- select all orders of Ivan:
SELECT first_name, order_date
	FROM customers
	LEFT JOIN orders
	ON customers.id=orders.customer_id
	WHERE customers.first_name='Ivan';

-- select all customers, which do not have any orders:
SELECT first_name, order_date
	FROM customers
	LEFT JOIN orders
	ON customers.id=orders.customer_id
	WHERE orders.customer_id IS NULL;

/* ------------------------------- RIGHT JOIN ------------------------------- */
-- select all orders rows
SELECT first_name, order_date
	FROM customers.customers as customers
	RIGHT JOIN orders
	ON customers.id=orders.customer_id;

/* ------------------------------- OUTER JOIN ------------------------------- */
-- LEFT OUTER JOIN
SELECT first_name, order_date
	FROM customers.customers as customers
	LEFT OUTER JOIN orders
	ON customers.id=orders.customer_id;

-- RIGHT OUTER JOIN
SELECT first_name, order_date
	FROM customers.customers as customers
	RIGHT OUTER JOIN orders
	ON customers.id=orders.customer_id;



/* -------------------------------------------------------------------------- */
/*                                    VIEWS                                   */
/* -------------------------------------------------------------------------- */
CREATE VIEW cust_order AS (
	SELECT first_name, order_date
	FROM customers.customers as customers, orders
	WHERE customers.id=orders.customer_id
);

SELECT * FROM cust_order;