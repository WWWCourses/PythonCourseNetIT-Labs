from pymongo import MongoClient
from pymongo.message import delete


local_client = MongoClient('mongodb://localhost:27017/car_parts_shop')

db = local_client.get_database('car_parts_shop')

car_parts_data = [
  {
    "code": 1,
    "product_name": "BRAKE DISC",
    "category": "BRAKING SYSTEM",
    "buying_price": 45.88,
    "client_price": 65.5,
    "application": "MITSUBISHI SPACE STAR 1.6, 2002",
    "manufacturer": "ABE"
  },
  {
    "code": 2,
    "product_name": "FRONT BRAKE PADS SET",
    "category": "BRAKING SYSTEM",
    "buying_price": 24,
    "client_price": 35.86,
    "application": "AUDI A6 3.0D, 2015",
    "manufacturer": "STARLINE"
  },
  {
    "code": 3,
    "product_name": "CRANKSHAFT POSITION SENSOR",
    "category": "IGNITION SYSTEM",
    "buying_price": 125.47,
    "client_price": 184,
    "application": "MERCEDES-BENZ CLK 220, 2007",
    "manufacturer": "OE MERCEDES"
  },
  {
    "code": 4,
    "product_name": "FUEL PRESSURE REGULATOR",
    "category": "FUEL SYSTEM",
    "buying_price": 98.22,
    "client_price": 132.22,
    "application": "RENAULT MAGANE 1.9 DCI, 2008",
    "manufacturer": "SENSATA"
  },
  {
    "code": 5,
    "product_name": "EXHAUST GAS RECIRCULATION(EGR) VALVE",
    "category": "EXHAUST SYSTEM",
    "buying_price": 217,
    "client_price": 302.56,
    "application": "VOLKSWAGEN BORA 1.9TDI, 2008",
    "manufacturer": "NRF"
  },
  {
    "code": 6,
    "product_name": "END-SPRINDLE ROD",
    "category": "STEERING SYSTEM",
    "buying_price": 28.66,
    "client_price": 37.11,
    "application": "CITROEN C3 1.4HDI, 2009",
    "manufacturer": "TRW"
  },
  {
    "code": 7,
    "product_name": "STABILIZER ROD CONNECTOR",
    "category": "STABILITY SYSTEM",
    "buying_price": 11.26,
    "client_price": 18,
    "application": "OPEL CORSA D 1.0 ECOTEC, 2012",
    "manufacturer": "MOOG"
  },
  {
    "code": 8,
    "product_name": "FRONT BEARING",
    "category": "DRIVE SHAFT",
    "buying_price": 66.55,
    "client_price": 81.35,
    "application": "PEUGEOT 307 1.6HDI, 2009",
    "manufacturer": "FAG"
  },
  {
    "code": 9,
    "product_name": "OIL PAN",
    "category": "OIL SYSTEM",
    "buying_price": "124,10",
    "client_price": "171,25",
    "application": "HONDA ACCORD 2.4 VTEC, 2010",
    "manufacturer": "STAL"
  },
  {
    "code": 10,
    "product_name": "WATER PUMP",
    "category": "COOLING SYSTEM",
    "buying_price": 88.98,
    "client_price": 135.68,
    "application": "TOYOTA RAV4 2.2 D-CAT. 2002",
    "manufacturer": "AISIN"
  },
  {
    "code": 11,
    "product_name": "SHORT BLOCK ASSEMBLY",
    "category": "ENGINE",
    "buying_price": "2,259.65",
    "client_price": "3,098.58",
    "application": "VOLKSWAGEN GOLF VII 1.8TFSI, 2017",
    "manufacturer": "OE VW"
  },
  {
    "code": 12,
    "product_name": "AIR FILTER",
    "category": "INTAKE SYSTEM",
    "buying_price": 22.36,
    "client_price": 32.75,
    "application": "SUZUKI BALENO 1.3, 2000",
    "manufacturer": "FILTRON"
  },
  {
    "code": 13,
    "product_name": "SPARK PLUG",
    "category": "IGNITION SYSTEM",
    "buying_price": 13.56,
    "client_price": 27.2,
    "application": "SEAT IBIZA 1.6SR, 2005",
    "manufacturer": "NGK"
  },
  {
    "code": 14,
    "product_name": "IGNITION COIL",
    "category": "IGNITION SYSTEM",
    "buying_price": 100.05,
    "client_price": 142,
    "application": "OPEL ASTRA H 1.2, 2007",
    "manufacturer": "BOSCH"
  },
  {
    "code": 15,
    "product_name": "FUEL INJECTOR",
    "category": "FUEL SYSTEM",
    "buying_price": 255.2,
    "client_price": 326,
    "application": "TOYOTA AVENSIS 2.0 D4D, 2006",
    "manufacturer": "SIEMENS"
  },
  {
    "code": 16,
    "product_name": "TIMING BELT SET",
    "category": "VALVE TIMING",
    "buying_price": 332.25,
    "client_price": 469.23,
    "application": "PEUGEOT 206CC 1.4I, 2004",
    "manufacturer": "CONTINENTAL"
  },
  {
    "code": 17,
    "product_name": "STEERING SERVO PUMP",
    "category": "STEERING SYSTEM",
    "buying_price": "1,200.00",
    "client_price": "1,566.54",
    "application": "DAIHATSU SIRION 1.3, 2009",
    "manufacturer": "TRW"
  },
  {
    "code": 18,
    "product_name": "INTAKE MANIFOLD",
    "category": "INTAKE SYSTEM",
    "buying_price": 202.44,
    "client_price": 293.16,
    "application": "FORD FOCUS 1.8 DURATEC, 2001",
    "manufacturer": "FoMoCo"
  },
  {
    "code": 19,
    "product_name": "CLUTCH SET",
    "category": "CLUTCH SYSTEM",
    "buying_price": "2,155.25",
    "client_price": "3,000.00",
    "application": "PORSCHE CAYENNE 3.0D, 2010",
    "manufacturer": "VALEO"
  },
  {
    "code": 20,
    "product_name": "SHOCK ABBSORBER",
    "category": "SUSPENSION",
    "buying_price": 65.21,
    "client_price": 92.88,
    "application": "SKODA FABIA 1.9D, 2001",
    "manufacturer": "MONROE"
  }
]

def insert_list_of_documents(data):
	db.car_parts.insert_many(data)


def read_all():
	return db.car_parts.find({},)


# query single document
# for p in pr1:
# 	print(p['manufacturer'])

# print(db.car_parts.find_one({}, {"manufacturer":1}))


# return all documents, which "buying_price" < 45:
# products = db.car_parts.find({"buying_price": {"$lt": 45}})
# for pr in products:
# 	print(pr)


# find all "category": "BRAKING SYSTEM", which "buying_price" > 50:
# products = db.car_parts.find(
# 	{
# 		"category": "BRAKING SYSTEM",
# 		"buying_price" : {"$gt": 5}
# 	},
# 	{"_id":0}
# )
# for pr in products:
# 	print(pr)


# update name of 'product_name': 'BRAKE DISC' =>"brake disc"
# res = db.car_parts.update_many(
# 	{'product_name': 'BRAKE DISC'},
# 	{
# 		"$set": {'product_name': 'brake disc'}
# 	}
# )

# print(dir(res))


# delete {'product_name': 'brake disc'}
db.car_parts.delete_one({'product_name': 'brake disc'})



