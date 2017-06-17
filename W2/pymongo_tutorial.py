query = {'type': 'exam'}
projection = {'student_id': 1, 'id': 0}

find(query, projection)

query = {'type': 'exam', 'score': {'$gt': 50, '$lt': 70}}

#Importing from reddit:

curl https://www.reddit.com/r/technology/.json > reddit.json

cat reddit.json | python -m json.tool | more

#!/usr/bin/env python

import json
import urllib2
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
stories = db.stories

# drop existing collection
stories.drop()

# get the reddit home page
reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

# parse the json into python objects
parsed = json.loads(reddit_page.read())

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert_one(item['data'])



#skip, limit and sort:
#1) sort
#2) skip
#3) limit

cursor = scores.find(query).sort("student_id", pymongo.ASCENDING).skip(4).limit(1)

#this is the same as

cursor = scores.find(query).skip(4)
cursor = cursor.limit(1)
cursor = cursor.sort('student_id', pymongo.ASCENDING)

#because the query is not run in the db until we start iterating with the cursor


#Difference between PyMongo and Mongo Shell for multiple sorting
db.scores.find().sort({student_id: 1, score: -1})
cursor.sort([('student_id': pymongo.ASCENDING, 'score': pymongo.DESCENDING)])

#why? Because dictionaries in python are not ordered
