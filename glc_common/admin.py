from django.contrib import admin
from .models import NavbarItem


class NavbarItemAdmin(admin.ModelAdmin):
    fieldsets = [
       (
           'Name of the Menu', {
               'fields':[
                   'name'
               ]
           }
           
       ),
       (
           'URL Link', {
               'fields':[
                   'url'
               ]
           }
           
       )
    ]
    

admin.site.register(NavbarItem,NavbarItemAdmin)
