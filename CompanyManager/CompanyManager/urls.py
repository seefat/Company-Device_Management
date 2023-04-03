from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/',include('login.urls')),
    path('manage/',include('management.urls')),
]
