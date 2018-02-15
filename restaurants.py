
# All restaurants in a specified borough.
# All restaurants in a specified zip code.
# All restaurants in a specified zip code and with a specified grade.
# All restaurants in a specified zip code with a score below a specified threshold.
# Something more clever.



	

import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.test
collection = db.restaurants

def borough(x):
    return collection.find({"borough": x})

def zipcode(x):
    return collection.find({"address.zipcode": str(x)})

def belowRating(zipcode, threshold):
    return collection.find({"$and": [{"address.zipcode": zipcode}, {"grades.score": {"$lt": threshold}} ] })
    

def notClever(grade, score):
    return collection.find({"$and": [{"grades.grade": {"$gt": grade} }, {"grades.score": {"$gt": score} } ] })

