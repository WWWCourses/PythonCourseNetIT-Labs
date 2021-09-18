import sys, random
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from configparser import ConfigParser

class ManageUserDB:
	def __init__(self):
		self.db_config = self.read_db_config()
		self.openDBConnection()
		self.query = QSqlQuery()


	def read_db_config(self, filename='./config.ini', section='mysql'):
		""" Read database configuration file and return a dictionary object
				:param filename: name of the configuration file
				:param section: section of database configuration
				:return: a dictionary of database parameters
		"""
		# create parser and read the configuration file
		parser = ConfigParser()
		parser.read(filename)

		db_config = {}
		if parser.has_section(section):
			items = parser.items(section)
			for item in items:
				db_config[item[0]] = item[1]
		else:
			raise Exception(f'{section} not found in the {filename} file')

		return db_config


	def openDBConnection(self):
		# Create connection to database. If db file does not exist,
		# a new db file will be created.
		# database = QSqlDatabase.addDatabase("QSQLITE")
		# database.setDatabaseName("./users.db")
		# if not database.open():
		# 	print("Unable to open data source file.")
		# 	sys.exit(1) # Error code 1 - signifies error

		db = QSqlDatabase.addDatabase("QMYSQL")
		db.setHostName(self.db_config['HOST'])
		db.setDatabaseName(self.db_config['DATABASE'])
		db.setUserName(self.db_config['USER'])
		db.setPassword(self.db_config['PASSWORD'])

		try:
			ok = db.open()
			print(ok)
		except:
			print(f"Unable to open database.")
			print(db.lastError().text())




db = ManageUserDB()
