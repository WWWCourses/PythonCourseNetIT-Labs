import mysql.connector
from mysql.connector import connection


# TODO: check where the data is loaded
def make_connection(user, password, db, host="localhost", port=3306):
	try:
		cnx = mysql.connector.connect(
			user=user,
			password=password,
			db=db,
			host=host,
			port=port
		)

	except mysql.connector.Error as e:
		print(e)

	print('Connection Established')
	return cnx


# Connect to server
# mysql -u root -p 1234 customers
cnx = make_connection (user="root", password="1234", db='customers')

# Get a cursor
cur = cnx.cursor()

# Execute a query
first_name = 'hristo'
last_name = 'hristov'
email = 'hristo@gmail.com'


sql = f"""
	INSERT into customers (first_name, last_name, email)
	VALUES ('{first_name}', '{last_name}', '{email}')
"""
print(sql)

cur.execute(sql)
print(cur.lastrowid)


sql = 'SELECT * FROM customers.customers;'
cur.execute(sql)

# Fetch one result
# row = cur.fetchone()
# print(row)

rows = cur.fetchall()
for r in rows:
	print(r[1])

# Close connection
cnx.close()