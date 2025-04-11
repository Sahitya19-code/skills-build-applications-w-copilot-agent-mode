# Test data for the OctoFit Tracker application

test_users = [
    {"email": "john.doe@example.com", "name": "John Doe", "age": 25},
    {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30},
]

test_teams = [
    {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]},
]

test_activities = [
    {"user": "john.doe@example.com", "activity_type": "Running", "duration": 30},
    {"user": "jane.smith@example.com", "activity_type": "Cycling", "duration": 45},
]

test_leaderboard = [
    {"user": "john.doe@example.com", "score": 100},
    {"user": "jane.smith@example.com", "score": 150},
]

test_workouts = [
    {"name": "Push-ups", "description": "Do 20 push-ups"},
    {"name": "Sit-ups", "description": "Do 30 sit-ups"},
]