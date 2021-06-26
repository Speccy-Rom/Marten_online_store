from django.urls import path
from eStore import views

urlpatterns = [
    path('', views.all_cats, name='all_cats'),

]
