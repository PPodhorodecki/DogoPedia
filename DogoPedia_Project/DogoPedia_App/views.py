from django.shortcuts import render
from DogoPedia.models import Users, Dogs, Races
from django.http import HttpResponse
from DogoPedia_App import races

def insert_races():
    for race in races:
        Races.objects.create(race=race)

def basesite(request):
    return render(request, 'basesite.html')