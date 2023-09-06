import logging
from django.shortcuts import redirect,render
from .models import Team

# Creating a logger instance
logger = logging.getLogger(__name__)

def add_team_view(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        # Perform any validation or processing as needed
        logger.info(f"Adding team: {team_name}")
        Team.objects.create(name=team_name)
        return redirect('teams')
    return render(request, 'add_teams.html')    