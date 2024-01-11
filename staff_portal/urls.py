from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns for your app
    # Example:
    path('', views.memberlogin, name='memberlogin'),
]