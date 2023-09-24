import pymongo

mongo_url = "mongodb://localhost:27017/"  
database_name = "mydatabase"  

client = pymongo.MongoClient(mongo_url)

db = client[database_name]

db.inventory.insert_many(
    [
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "A",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
    ]
)

print('find {"status": "D"}')
input()
cursor = db.inventory.find({"status": "D"})
for document in cursor:
    print(document)

print('find {"status": {"$in": ["A", "D"]}}')
input()
cursor = db.inventory.find({"status": {"$in": ["A", "D"]}})
for document in cursor:
    print(document)

print('find {"status": "A", "qty": {"$lt": 30}}')
input()
cursor = db.inventory.find({"status": "A", "qty": {"$lt": 30}})
for document in cursor:
    print(document)

print('find {"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]}')
input()
cursor = db.inventory.find({"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]})
for document in cursor:
    print(document)

print('find {"status": "A", "$or": [{"qty": {"$lt": 30}}, {"item": {"$regex": "^p"}}]}')
input()
cursor = db.inventory.find(
    {"status": "A", "$or": [{"qty": {"$lt": 30}}, {"item": {"$regex": "^p"}}]}
)
for document in cursor:
    print(document)
