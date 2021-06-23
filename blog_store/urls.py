from django.urls import path
from blog_store import views

urlpatterns = [
    path('', views.index, name='all_blogs'),
    path('blog/', views.all_blogs, name='all_blogs'),
    path('category/<int:category_id>/', views.get_category, name='get_category'),

]

