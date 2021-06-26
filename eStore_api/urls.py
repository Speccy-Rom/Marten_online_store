from django.urls import path
from eStore_api import views

urlpatterns = [
    path('', views.all_fishs, name='all_fishs'),

]