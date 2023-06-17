from django.shortcuts import render, get_object_or_404
from .models import Team, Instance

def team_instances_view(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    instances = Instance.objects.filter(team=team)
    
    context = {
        'team': team,
        'instances': instances
    }
    
    return render(request, 'instances.html', context)
