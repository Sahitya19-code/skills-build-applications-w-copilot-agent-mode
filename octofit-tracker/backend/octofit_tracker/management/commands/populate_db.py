import sys
sys.path.append('/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend')

import os
import django
from pymongo import MongoClient
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

# Ensure settings are configured
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import users_collection, teams_collection, activity_collection, leaderboard_collection, workouts_collection

def populate_database():
    # Clear existing data
    users_collection.delete_many({})
    teams_collection.delete_many({})
    activity_collection.delete_many({})
    leaderboard_collection.delete_many({})
    workouts_collection.delete_many({})

    # Insert test data
    users_collection.insert_many(test_users)
    teams_collection.insert_many(test_teams)
    activity_collection.insert_many(test_activities)
    leaderboard_collection.insert_many(test_leaderboard)
    workouts_collection.insert_many(test_workouts)

    print("Database populated with test data")

if __name__ == "__main__":
    populate_database()
