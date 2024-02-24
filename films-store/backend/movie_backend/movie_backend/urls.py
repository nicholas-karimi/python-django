
from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    # URI structure http://[host]:[port]/api/{service name}]/v{version number}/{resource}
    path('api/moviestore/v1/', include('core.movies.urls')),
    # path('accounts/', include('core.accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
