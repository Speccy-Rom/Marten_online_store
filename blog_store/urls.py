from django.urls import path
from blog_store import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),

]

