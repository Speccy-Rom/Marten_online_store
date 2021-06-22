from django.urls import path
from fishs_food import views

urlpatterns = [
    path('', views.all_fishs, name='all_fishs'),

]