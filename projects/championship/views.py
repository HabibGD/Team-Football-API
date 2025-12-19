from django.shortcuts import render, get_object_or_404
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ChampionSerializer
from .models import Championship

# Create your views here.


# Adding  and Listing Championships endpoint

@api_view(['GET', 'POST'])
def championships(request):

    if request.method == 'GET':

        championship = Championship.objects.all()
        serialize = ChampionSerializer(championship, many=True)

        return Response({ "Championships": serialize.data})
    
    if request.method == 'POST':

        serialize = ChampionSerializer(data=request.data)

        if serialize.is_valid():
            serialize.save()

            return Response(serialize.data, status=201)
        
        return Response(serialize.errors, status='400')


# Finding one championship endpoint

@api_view(['GET'])
def championship_detail(request, pk):

    championship = get_object_or_404(Championship, pk=pk)
    serializer = ChampionSerializer(championship)

    return Response({ "Championship": serializer.data})

# Updating a championship endpoint

@api_view(['PUT', 'PATCH'])
def champion_update(request, pk):

    championship = get_object_or_404(Championship, pk=pk)
    
    serializer = ChampionSerializer(championship, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)


# Deleting a championship endpoint

@api_view(['DELETE'])
def champion_delete(request, pk):

    championship = get_object_or_404(Championship, pk=pk)
    championship.delete()

    return Response({ "message": 'Championship delete successfully' }, status=204)