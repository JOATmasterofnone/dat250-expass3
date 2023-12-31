import pymongo

mongo_url = "mongodb://localhost:27017/"  
database_name = "mydatabase"  

client = pymongo.MongoClient(mongo_url)

db = client[database_name]

db.inventory.insert_many(
    [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
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
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
)

cursor = db.inventory.find({})
for document in cursor:
    print(document)

print("Update_one")
input()

db.inventory.update_one(
    {"item": "paper"},
    {"$set": {"size.uom": "cm", "status": "P"}, "$currentDate": {"lastModified": True}},
)
cursor = db.inventory.find({})
for document in cursor:
    print(document)


print("Update_many")
input()

db.inventory.update_many(
    {"qty": {"$lt": 50}},
    {"$set": {"size.uom": "in", "status": "P"}, "$currentDate": {"lastModified": True}},
)
cursor = db.inventory.find({})
for document in cursor:
    print(document)
    
print("replace_one")
input()

db.inventory.replace_one(
    {"item": "paper"},
    {
        "item": "paper",
        "instock": [{"warehouse": "A", "qty": 60}, {"warehouse": "B", "qty": 40}],
    },
)
cursor = db.inventory.find({})
for document in cursor:
    print(document)

