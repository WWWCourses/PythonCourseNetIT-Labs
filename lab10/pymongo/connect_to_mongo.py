from pymongo import MongoClient


local_client = MongoClient('mongodb://localhost:27017/python_course')

# this cluster is set to allow access from any IP, so you should be connected:
atlas_client = MongoClient('mongodb+srv://power_user:q1a2z3@cluster0.xm0yw.mongodb.net/')


print(local_client.database_names())
print(atlas_client.database_names())


# db = local_client.get_database('python_course')
# print(list(db.list_collections()))
