import mysql.connector
from mysql.connector import connection

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
cnx = make_connection (user="root", password="1234", db='customers')

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# fetch Multiple results
with cnx.cursor() as cursor:
	cursor.execute(f'SHOW TABLES')

	results = cursor.fetchall()
	# print(results)
	for r in results:
		print(r)

# Close connection
cnx.close()