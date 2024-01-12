from django.urls import path
from .views import MemberLogin


app_name = "staff_portal"
urlpatterns = [
    # Define URL patterns for your app
    # Example:
    path('', MemberLogin.as_view(), name='MemberLogin'),
]