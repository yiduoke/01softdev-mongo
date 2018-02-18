'''
/r/funny json from reddit
it includes data about each post on the front page of the funny subreddit at the time I got it (2/16)

https://www.reddit.com/r/funny.json

I got rid of several top layers so I could have separate documents for each post
I just established a connection in this script
'''

import pymongo
import json
from pprint import pprint

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection['keY-taoI']
collection = db['r/funny']

# with open("reddit.json", 'r') as f:
#     datastore = json.load(f)

# # cleaning it up so the upper layers are gone
# for document in datastore['data']['children']:
#     collection.insert(document)

def below_score(threshold):
    output = collection.find({"data.score" : {'$lt' : threshold}})
    for i in output:
   		pprint(i)

def above_score(threshold):
    output = collection.find({"data.score" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def below_ups(threshold):
    output = collection.find({"data.ups" : {'$lt' : threshold}})
    for i in output:
   		pprint(i)

def above_ups(threshold):
    output = collection.find({"data.ups" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def below_comments(threshold):
    output = collection.find({"data.num_comments" : {'$lt' : num_comments}})
    for i in output:
   		pprint(i)

def above_comments(threshold):
    output = collection.find({"data.num_comments" : {'$gt' : num_comments}})
    for i in output:
   		pprint(i)

def is_video(boolean):
    output = collection.find({"data.is_video" : boolean})
    for i in output:
   		pprint(i)

def good_video(score_threshold, ups_threshold):
    output = collection.find({"data.is_video" : True, "data.score": {'$gt': score_threshold}, "data.ups": {'$gt': ups_threshold}})
    for i in output:
   		pprint(i)