from django.contrib import admin
from django.urls import path, include
from login.views import to_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/',include('login.urls')),
    path('manage/',include('management.urls')),
    path('',to_redirect),
]
