import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),  # Incluye las URLs de tu app
    re_path(r'^ads.txt$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'static'), 'path': 'ads.txt'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
