from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from eStore_blog import views
from eStore_blog.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index_view),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('eStore_blog.urls'), name='blog'),
    path('store/', include('eStore.urls'), name='store'),
    path('api/v1/', include('eStore_api.urls'), name='api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
