from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('random_word', views.random_word)
    ]