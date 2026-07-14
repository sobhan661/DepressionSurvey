from django.urls import path
from django.shortcuts import redirect
from pathlib import Path

from core.views import Home

urlpatterns = [
    path('', lambda x: redirect('/home')),
    path('home', Home.as_view())
]

