from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_list, name='teams'),
    path('<int:pk>', views.team_detail, name='details')
]