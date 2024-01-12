from django.shortcuts import render
from . import views
from django.views.generic import TemplateView

#def memberlogin(request):
    # Logic for staff dashboard
#    return render(request, 'staff_portal/auth.html', {})


class MemberLogin(TemplateView):
    template_name = 'staff_portal/auth.html'






