import sys
sys.path.append('/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend')

import os
from django.conf import settings

# Ensure settings are configured
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
import django
django.setup()

from pymongo import MongoClient

def populate_database():
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB_NAME]

    # Clear existing data
    db.users.delete_many({})
    db.teams.delete_many({})
    db.activity.delete_many({})
    db.leaderboard.delete_many({})
    db.workouts.delete_many({})

    # Add test users
    user1 = {"email": "john.doe@example.com", "name": "John Doe", "age": 25}
    user2 = {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30}
    db.users.insert_many([user1, user2])

    # Add test teams
    team1 = {"name": "Team Alpha", "members": [user1["email"], user2["email"]]}
    db.teams.insert_one(team1)

    # Add test activities
    activity1 = {"user": user1["email"], "activity_type": "Running", "duration": 30}
    activity2 = {"user": user2["email"], "activity_type": "Cycling", "duration": 45}
    db.activity.insert_many([activity1, activity2])

    # Add test leaderboard entries
    leaderboard1 = {"user": user1["email"], "score": 100}
    leaderboard2 = {"user": user2["email"], "score": 150}
    db.leaderboard.insert_many([leaderboard1, leaderboard2])

    # Add test workouts
    workout1 = {"name": "Push-ups", "description": "Do 20 push-ups"}
    workout2 = {"name": "Sit-ups", "description": "Do 30 sit-ups"}
    db.workouts.insert_many([workout1, workout2])

    print("Database populated with test data")

if __name__ == "__main__":
    populate_database()
