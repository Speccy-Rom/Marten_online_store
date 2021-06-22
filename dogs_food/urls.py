from django.urls import path
from dogs_food import views

urlpatterns = [
    path('', views.all_dogs, name='all_dogs'),

]