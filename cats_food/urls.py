from django.urls import path
from cats_food import views

urlpatterns = [
    path('', views.all_cats, name='all_cats'),

]
