from django.shortcuts import render, get_object_or_404
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team
from .serializer import TeamSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def teams_list(request):

    if request.method == 'GET':
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)

        return Response({ "Teams": serializer.data})


    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def team_detail(request, pk):

    team = get_object_or_404(Team, pk=pk)

    if request.method == 'GET':

        serializer = TeamSerializer(team)
        return Response({ "Team": serializer.data})
    
    if request.method in ['PUT', 'PATCH']:

        serializer = TeamSerializer(team, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        team.delete()
        return Response({ "message": "Team deleted successfully" }, status=204)

