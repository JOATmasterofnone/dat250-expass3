import pymongo

mongo_url = "mongodb://localhost:27017/"  
database_name = "pizzas"  

client = pymongo.MongoClient(mongo_url)

db = client[database_name]
collection = db[database_name]

db.pizzas.delete_many({})

db.pizzas.insert_many( [
    {"_id": 0, "type": "pepperoni", "size": "small", "price": 4},
    {"_id": 1, "type": "cheese", "size": "medium", "price": 7},
    {"_id": 2, "type": "vegan", "size": "large", "price": 8}
] )

cursor = db.pizzas.find({})
for document in cursor:
    print(document)
input()
    
 
db.pizzas.insert_one({"_id": 3, "type": "beef", "size": "medium", "price": 6})
db.pizzas.insert_one({"_id": 4, "type": "sausage", "size": "large", "price": 10})
db.pizzas.update_one({"type": "cheese"}, {"$set": {"price": 8}})
db.pizzas.delete_one({"type": "pepperoni"})
db.pizzas.replace_one({"type": "vegan"}, {"type": "tofu", "size": "small", "price": 4})

cursor = db.pizzas.find({})
for document in cursor:
    print(document)
