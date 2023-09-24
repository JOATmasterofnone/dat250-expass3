import pymongo
from datetime import datetime
import math


mongo_url = "mongodb://localhost:27017/"  
database_name = "orders"  

client = pymongo.MongoClient(mongo_url)

db = client[database_name]
collection = db[database_name]


'''db.orders.insert_many([
    {
        "_id": 1,
        "cust_id": "Ant O. Knee",
        "ord_date": datetime(2020, 3, 1),
        "price": 25,
        "items": [
            {"sku": "oranges", "qty": 5, "price": 2.5},
            {"sku": "apples", "qty": 5, "price": 2.5}
        ],
        "status": "A"
    },
    {
        "_id": 2,
        "cust_id": "Ant O. Knee",
        "ord_date": datetime(2020, 3, 8),
        "price": 70,
        "items": [
            {"sku": "oranges", "qty": 8, "price": 2.5},
            {"sku": "chocolates", "qty": 5, "price": 10}
        ],
        "status": "A"
    },
    {
        "_id": 3,
        "cust_id": "Busby Bee",
        "ord_date": datetime(2020, 3, 8),
        "price": 50,
        "items": [
            {"sku": "oranges", "qty": 10, "price": 2.5},
            {"sku": "pears", "qty": 10, "price": 2.5}
        ],
        "status": "A"
    },
    {
        "_id": 4,
        "cust_id": "Busby Bee",
        "ord_date": datetime(2020, 3, 18),
        "price": 25,
        "items": [
            {"sku": "oranges", "qty": 10, "price": 2.5}
        ],
        "status": "A"
    },
    {
        "_id": 5,
        "cust_id": "Busby Bee",
        "ord_date": datetime(2020, 3, 19),
        "price": 50,
        "items": [
            {"sku": "chocolates", "qty": 5, "price": 10}
        ],
        "status": "A"
    },
    {
        "_id": 6,
        "cust_id": "Cam Elot",
        "ord_date": datetime(2020, 3, 19),
        "price": 35,
        "items": [
            {"sku": "carrots", "qty": 10, "price": 1.0},
            {"sku": "apples", "qty": 10, "price": 2.5}
        ],
        "status": "A"
    },
    {
        "_id": 7,
        "cust_id": "Cam Elot",
        "ord_date": datetime(2020, 3, 20),
        "price": 25,
        "items": [
            {"sku": "oranges", "qty": 10, "price": 2.5}
        ],
        "status": "A"
    },
    {
        "_id": 8,
        "cust_id": "Don Quis",
        "ord_date": datetime(2020, 3, 20),
        "price": 75,
        "items": [
            {"sku": "chocolates", "qty": 5, "price": 10},
            {"sku": "apples", "qty": 10, "price": 2.5}
        ],
        "status": "A"
    },
    {
        "_id": 9,
        "cust_id": "Don Quis",
        "ord_date": datetime(2020, 3, 20),
        "price": 55,
        "items": [
            {"sku": "carrots", "qty": 5, "price": 1.0},
            {"sku": "apples", "qty": 10, "price": 2.5},
            {"sku": "oranges", "qty": 10, "price": 2.5}
        ],
        "status": "A"
    },
    {
        "_id": 10,
        "cust_id": "Don Quis",
        "ord_date": datetime(2020, 3, 23),
        "price": 25,
        "items": [
            {"sku": "oranges", "qty": 10, "price": 2.5}
        ],
        "status": "A"
    }
])

cursor = db.orders.find({})
for document in cursor:
    print(document)
'''    
    
def map_process_each_doc():
    emit(this["cust_id"], this["price"])
    
def reduce_process_each_doc(customer_id, valuesPrices):
    the_sum = 0
    for num in valuesPrices:
    	the_sum += num
    return the_sum
    
#names = [name for name in dir(db.orders) if callable(getattr(db.orders, name))]
#print(names)

#db.orders.map_reduce(map_process_each_doc, reduce_process_each_doc,
#    {"out": "map_reduce_example"})

'''aggregation = db.orders.aggregate([
    {
        '$group': {
            '_id': '$cust_id', 
            'value': {
                '$sum': '$price'  
            }
        }
    },
    {
        '$out': 'agg_alternative1' 
    }
])
   
    
agg = db.agg_alternative1.find().sort('_id', pymongo.ASCENDING) 
for doc in agg:
    print(doc)'''
     
quantity = db.orders.aggregate([
    {'$unwind': '$items'},
    {'$match': {'items.sku': 'chocolates'}},
    {'$group': {'_id': '$items.sku', 'value': { '$sum': '$items.qty'}}},
    {'$out': 'irw_quantity'}])


#how many chocolates
agg = db.irw_quantity.find().sort('_id', pymongo.ASCENDING) 
for doc in agg:
    print(doc)
	
    
