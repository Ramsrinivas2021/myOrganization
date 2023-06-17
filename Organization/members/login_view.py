from django.shortcuts import render
from .models import Team


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == 'srinivas' and password == '0000':
            # Successful login
            teams = Team.objects.all()  # Fetch the teams from the database
            return render(request, 'success.html',{'username': username, 'teams':teams})
        else:
            #Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')