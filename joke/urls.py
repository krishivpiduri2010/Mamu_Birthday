from .views import *
from django.urls import path

urlpatterns = [
    path('<int:joke_num>', home),
]