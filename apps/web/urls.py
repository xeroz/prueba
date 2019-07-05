from django.urls import path, reverse_lazy
from .views import home

app_name = 'web'


urlpatterns = [
    path('home/', home, name='home'),
]
