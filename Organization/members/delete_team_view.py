from django.shortcuts import redirect
from members.models import Team


def delete_team_view(request, team_id):
    team = Team.objects.get(pk=team_id)
    team.delete()
    return redirect('teams')
