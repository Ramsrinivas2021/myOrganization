# teams_view.py
from django.shortcuts import render
from .models import Team



def teams_view(request):
    teams = Team.objects.all()
    print(teams)
    return render(request, 'teams.html', {'teams': teams})


