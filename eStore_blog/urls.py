from django.urls import path

from .views import *


urlpatterns = [
    # path('', index, name='index'),
    path('', IndexBlog.as_view(), name='index'),
    # path('blog/', all_blogs, name='all_blogs'),
    path('blog/', ListBlog.as_view(), name='all_blogs'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', BlogByCategory.as_view(), name='category'),
    # path('<int:blog_id>/', view_post, name='view_post'),
    path('blog/<int:pk>/', ViewPost.as_view(), name='view_post'),
    path('tag/<slug:slug>/', TagView.as_view(), name='Tag'),
]

