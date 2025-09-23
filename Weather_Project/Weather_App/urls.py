from django.urls import path
from . import views

app_name = 'Weather_App'

urlpatterns = [
    path('', views.home, name='home'),
]
