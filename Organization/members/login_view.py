import logging
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Team

# Create a logger instance
logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logger.info(f"Login attempt for user: {username}")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            teams = Team.objects.all()  # Fetch the teams from the database
            return render(request, 'teams.html', {'username': username, 'teams': teams})
        else:
            logger.warning(f"Failed login attempt for user: {username}")
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
