import pymongo


mongo_url = "mongodb://localhost:27017/" 
database_name = "mydatabase" 

client = pymongo.MongoClient(mongo_url)

db = client[database_name]

db.inventory.insert_one(
    {
        "item": "canvas",
        "qty": 100,
        "tags": ["cotton"],
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
    }
)

cursor = db.inventory.find({"item": "canvas"})
print (type(cursor))
for document in cursor:
    print(document)


db.inventory.insert_many(
    [
        {
            "item": "journal",
            "qty": 25,
            "tags": ["blank", "red"],
            "size": {"h": 14, "w": 21, "uom": "cm"},
        },
        {
            "item": "mat",
            "qty": 85,
            "tags": ["gray"],
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        },
        {
            "item": "mousepad",
            "qty": 25,
            "tags": ["gel", "blue"],
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
        },
    ]
)

cursor = db.inventory.find({})
for document in cursor:
    print(document)
