from django.urls import path

from .views import login

app_name = 'home'

urlpatterns = [
    path('', login, name='login'),
]