from django.shortcuts import render
from django.http import request
from .models import Person
from rest_framework.decorators import api_view
from .serializer import PersonSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def person_lists(request):
    
    if request.method == 'GET':
        
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True) 

        return Response({ "Persons": serializer.data})
    
    if request.method == 'POST':

        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)