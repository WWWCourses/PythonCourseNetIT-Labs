from pymongo import MongoClient


local_client = MongoClient('mongodb://localhost:27017/python_course')

db = local_client.get_database('python_course')

db.todos.insert_one({
	"title": "NEW TODO",
	"completed": False
})
