from django.urls import path
from . import views

urlpatterns = [
    path('', views.homerun),
    path('about/', views.about),
]