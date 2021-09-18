# create_database.py
# Import necessary modules
import sys, random
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class ManageUserDB:
    def __init__(self):
        # Create connection to database. If db file does not exist,
        # a new db file will be created.
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("./users.db")
        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

        self.query = QSqlQuery()

        self.createTables()

    def createTables(self):
        self.query.exec_("DROP TABLE orders")
        self.query.exec_("DROP TABLE users")

        # Create users table
        self.query.exec_("""CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    first_name VARCHAR(30) NOT NULL,
                    last_name VARCHAR(30) NOT NULL,
                    email VARCHAR(40) NOT NULL,
                    order_id VARCHAR(20) REFERENCES orders(id))""")

        # Positional binding to insert records into the database
        self.query.prepare("""INSERT INTO
                        users (first_name, last_name, email, order_id)
                        VALUES (?, ?, ?, ?)
                    """)

        first_names = ["Maria", "Ivan", "Stoyan"]
        last_names = ["Marinova", "Ivanov", "Stoyanov"]

        orders = {
           "1":"TV",
           "2":"mobile phone"
        }
        order_codes = list(orders.keys())
        order_names = list(orders.values())

        # Add the values to the query to be inserted in users
        for f_name in first_names:
            l_name = last_names.pop()
            email = (f"{l_name}_{f_name[0].lower()}@abv.bg")

            order_id = random.choice(order_codes)

            self.query.addBindValue(f_name)
            self.query.addBindValue(l_name)
            self.query.addBindValue(email)
            self.query.addBindValue(order_id)
            self.query.exec_()

        # Create the orders table
        order_query = QSqlQuery()
        order_query.exec_("""CREATE TABLE orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    order VARCHAR(20) NOT NULL)""")

        order_query.prepare("INSERT INTO orders (order) VALUES (?)")
        # Add the values to the query to be inserted in orders
        for name in order_names:
            order_query.addBindValue(name)
            order_query.exec_()
        print("[INFO] Database successfully created.")


if __name__ == "__main__":
    ManageUserDB()