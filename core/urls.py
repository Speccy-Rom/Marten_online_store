from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dogs_food.urls'), name='dogs'),
    path('cats/', include('cats_food.urls'), name='cats'),
    path('fishs/', include('fishs_food.urls'), name='fishs'),
    path('blog/', include('blog_store.urls'), name='blog')
]
