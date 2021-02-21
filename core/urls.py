from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('Account/',include('authentication.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('adverts/',include('advert.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)