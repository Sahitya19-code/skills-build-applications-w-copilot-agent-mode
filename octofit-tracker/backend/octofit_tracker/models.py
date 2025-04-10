from pymongo import MongoClient
from django.conf import settings

# Establish MongoDB connection
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

# Define collections
users_collection = db['users']
teams_collection = db['teams']
activity_collection = db['activity']
leaderboard_collection = db['leaderboard']
workouts_collection = db['workouts']
