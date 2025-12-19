from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/champions/', include('championship.urls')),
    path('api/teams/', include('team.urls')),
    path('api/persons/', include('person.urls'))
]
