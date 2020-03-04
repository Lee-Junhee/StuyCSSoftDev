import pymongo
from pymongo import MongoClient
import json

client = MongoClient()
db = client.test

def loadFromFile():
    file = open("role.json", "r")
    lines = file.read()
    dictionary = json.loads(lines)
    for object in dictionary['objects']:
        db.government.insert_one(object)

def party(party):
    for official in db.government.find({"party":party}):
        print(official)

def district(district):
    for official in db.government.find({"district":district}):
        print(official)

def gender(gender):
    for official in db.government.find({"person.gender":gender}):
        print(official)
    
def currentGender(gender):
    for official in db.government.find({"$and": [{"current" : {"$ne": False}}, {"person.gender":  gender}]}):
        print(official)

#loadFromFile() 
#party("Republican")
#district(4)

#gender("female")
#currentGender("male")
