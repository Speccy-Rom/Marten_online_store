from django.urls import path
from eStore_blog import views
from .views import TagView


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('tag/<slug:slug>/', TagView.as_view(), name='Tag'),
]

