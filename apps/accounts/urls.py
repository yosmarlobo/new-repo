from rest_framework import routers
from .views import UserView

from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('api/v1/user/<pk>/', UserView.as_view()),
]
