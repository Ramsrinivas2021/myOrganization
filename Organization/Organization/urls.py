"""
URL configuration for Organization project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from members.login_view import login_view
from members.home_view import home
from members.teams_view import teams_view
from members.add_teams_view import add_team_view
from members.delete_team_view import delete_team_view
from members.add_instance_view import add_instance_view
from members.team_instances_view import team_instances_view
from members.start_instance_view import start_instance_view
from members.stop_instance_view import stop_instance_view
from members.delete_instance_view import delete_instance

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('teams/', teams_view, name='teams'),
    path('teams/add/', add_team_view, name='add_team'),
    path('teams/delete/<int:team_id>/', delete_team_view, name='delete_team'),
    path('teams/<int:team_id>/', team_instances_view, name='team_instances_view'),
    path('add_instance/<int:team_id>/add_instance/', add_instance_view, name='add_instance_view'),
    path('delete_instance/<int:instance_id>/', delete_instance, name='delete_instance'),
    path('start_instance/<int:team_id>/', start_instance_view, name='start_instance'),
    path('stop_instance/<int:team_id>/', stop_instance_view, name='stop_instance'),
]

