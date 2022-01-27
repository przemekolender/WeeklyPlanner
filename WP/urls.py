from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('tasks/', views.backlog, name='backlog'),
    path('report/', views.report, name='report'),
    path('log-in/', views.logIn, name='login'),
    path('log-out/', views.logOut, name='logout'),
    path('register/', views.register, name='register'),
    path('new-task/', views.newTask, name='newtask'),
    path('update-task/<str:pk>', views.updateTask, name='update'),
    path('team/<str:pk>/', views.team, name='team'),

]
