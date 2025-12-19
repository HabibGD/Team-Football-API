from django.urls import path
from . import views



urlpatterns = [

    path('', views.championships, name='championship'),
    path('<int:pk>', views.championship_detail, name='champ_detail'),
    path('<int:pk>/update', views.champion_update, name='champ_update'),
    path('<int:pk>/delete', views.champion_delete, name='champ_delete'),

]