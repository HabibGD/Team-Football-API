from django.urls import path
from . import views



urlpatterns = [
    
    path('champions', views.championships, name='championship'),
    path('champions/<int:pk>', views.championship_detail, name='champ_detail'),
    path('champions/<int:pk>/update', views.champion_update, name='champ_update'),
    path('champions/<int:pk>/delete', views.champion_delete, name='champ_delete'),

]