from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, EmailField, IntField, StringField

from datetime import datetime


connect(db='car_parts_shop')


class User(Document):
	meta={'collection':'users'}

	role=StringField(regex=r"(?i)admin|user")
	first_name = StringField(min_length=2, max_length=20)
	last_name = StringField(min_length=2, max_length=20)
	email = EmailField(domain_whitelist=['gmail.com', 'abv.bg'])
	phone_number = IntField()
	password = StringField()
	created = DateTimeField()

ada = User(
	role="admin",
	first_name = "Ada",
	last_name = "Byron",
	email = "ada@gmail.com",
	phone_number = "0884156033",
	password  = "1233",
	created = datetime.now
)

ada.save();