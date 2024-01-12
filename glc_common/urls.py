from django.urls import path
from .views import Navbar, Footer


app_name = "glc_common"
urlpatterns = [
    # Define URL patterns for your app
    # Example:
    path('', Navbar.as_view(), name='Navbar'),
    path('', Footer.as_view(), name='Footer'),
]