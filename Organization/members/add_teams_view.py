from django.shortcuts import redirect,render
from .models import Team

def add_team_view(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        # Perform any validation or processing as needed
        Team.objects.create(name=team_name)
        return redirect('teams')
    return render(request, 'add_teams.html')