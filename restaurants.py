import pymongo
from pprint import pprint

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.test
collection = db.restaurants

def borough(x):
   output = collection.find({"borough": x})
   for i in output:
   		pprint(i)


def zipcode(x):
   	output = collection.find({"address.zipcode": str(x)})
   	for i in output:
   		pprint(i)


def belowRating(zipcode, threshold):
    output = collection.find({'address.zipcode' : zipcode, "grades.score" : {'$lt' : threshold}})

    for i in output:
    	pprint(i)

def notClever(zipcode, grade, score):
    output = collection.find({"address.zipcode" : zipcode, "grades.grade": grade, "grades.score": {"$gt": score} }  )
    for i in output:
    	pprint(i)

print("----------------Borough Staten Island--------------")
print("===================================================")

borough('Staten Island')

print("----------------Zipcode 10282---------------")
print("===================================================")
zipcode('10282')

print("----------------Zipcode 10282, belowRating 13---------------")
print("===================================================")
belowRating('10282', 13)

print("----------------Zipcode 10282, Grade A, BelowRating 10---------------")
print("===================================================")
notClever('10282', 'B',10)




