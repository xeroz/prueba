from django.urls import path, reverse_lazy
from .views import home
from django.contrib.auth.decorators import login_required


app_name = 'web'


urlpatterns = [
    path('home/', login_required(home), name='home'),
]
