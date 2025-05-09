from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerceweb/', include('ecommerceweb.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes login, logout, etc.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
