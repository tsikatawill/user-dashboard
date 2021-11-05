from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('sign-up/', views.signUp, name='sign-up'),
    path('sign-out/', views.signOut, name='sign-out'),
]
