import pymongo;

connection = pymongo.MongoClient("homer.stuy.edu");

db = connection.test
collection = db.restaurants

# All restaurants in a specified borough.
# All restaurants in a specified zip code.
# All restaurants in a specified zip code and with a specified grade.
# All restaurants in a specified zip code with a score below a specified threshold.
# Something more clever.


def borough(x):
	print collection.find({"borough" : x})
	return collection.find({"borough" : x})

def zip(x):
	print collection.find("address" : {"zipcode" : x})
	return collection.find("address" : {"zipcode" : x})

zip("11358")


