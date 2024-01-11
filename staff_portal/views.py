from django.shortcuts import render
from . import views

def memberlogin(request):
    # Logic for staff dashboard
    return render(request, 'staff_portal/auth.html', {})