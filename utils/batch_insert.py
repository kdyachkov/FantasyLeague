import pymongo
from pymongo import MongoClient
import players

COLLECTION = 'midwoodfc'


client = MongoClient()
db = client[COLLECTION]

players_db = db.player
for p in players_db.find():
    print p

players_db.insert(players.get_players_dict())


