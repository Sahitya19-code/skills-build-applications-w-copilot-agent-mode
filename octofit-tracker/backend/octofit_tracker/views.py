from octofit_tracker.models import users_collection, teams_collection, activity_collection, leaderboard_collection, workouts_collection
from rest_framework.response import Response
from rest_framework.views import APIView

class UserView(APIView):
    def get(self, request):
        users = list(users_collection.find({}, {"_id": 0}))
        return Response(users)

class TeamView(APIView):
    def get(self, request):
        teams = list(teams_collection.find({}, {"_id": 0}))
        return Response(teams)

class ActivityView(APIView):
    def get(self, request):
        activities = list(activity_collection.find({}, {"_id": 0}))
        return Response(activities)

class LeaderboardView(APIView):
    def get(self, request):
        leaderboard = list(leaderboard_collection.find({}, {"_id": 0}))
        return Response(leaderboard)

class WorkoutView(APIView):
    def get(self, request):
        workouts = list(workouts_collection.find({}, {"_id": 0}))
        return Response(workouts)
