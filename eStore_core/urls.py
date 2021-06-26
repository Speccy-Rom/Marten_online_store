from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eStore_blog.urls'), name='blog'),
    path('cats/', include('eStore.urls'), name='cats'),
    path('fishs/', include('eStore_api.urls'), name='fishs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
