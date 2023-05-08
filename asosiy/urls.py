from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/haker/', admin.site.urls),   
    path('', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
    path('arm/', include('arm.urls')),    
    path('talaba/', include('talaba.urls')),
    path('dekanat/', include('dekanat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
