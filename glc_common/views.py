from django.shortcuts import render
from . import views
from django.views.generic import TemplateView




class Navbar(TemplateView):
    template_name = 'common/navbar.html'



class Footer(TemplateView):
    template_name = 'common/footer.html'


