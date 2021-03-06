from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path(r'', include('apps.auth.urls', namespace='auth')),
    path(r'', include('apps.web.urls', namespace='web')),
]
