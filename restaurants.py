import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.test
collection = db.restaurants

def borough(x):
    return db.restaurants.find({"borough": x})

def zipcode(x):
    return db.restaurants.find({"address.zipcode": str(x)})

def belowRating(zipcode, threshold):
    return db.restaurants.find({$and: [{"address.zipcode": zipcode}, {"grades.score": {$lt: threshold}} ] })

def notClever(grade, score):
    db.restaurants.find({$and: [{"grades.grade": {$gt: grade} }, {"grades.score": {$gt: score} } ] })