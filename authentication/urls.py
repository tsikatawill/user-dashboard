from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('red/', admin.site.urls),
    path('', include('main.urls')),
]
