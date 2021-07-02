from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, sql


# connect to Mysql/MariaDB:
engine = create_engine("mysql+pymysql://root:1234@localhost/SimpleCompanyDB")


# Create a MetaData instance
metadata = MetaData()
print(metadata.tables)

# reflect db schema to MetaData
metadata.reflect(bind=engine)
print(metadata.tables)

#
conn = engine.connect()

result = conn.execute(sql.select(company))
for r in result:
	print(r)