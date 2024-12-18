
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('lawlist/', include('laws.urls')),
    path('register/',include('login.urls')),
    path('login/',include('login.urls')),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
