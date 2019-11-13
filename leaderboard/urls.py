from django.urls import path

from . import views

app_name = 'leaderboard'
urlpatterns = [
    path('', views.leaderboard, name='index'),
    path('added/', views.added, name='added'),
    path('add/', views.add, name='add'),
    path('scoreform/', views.scoreform, name='scoreform'),
]