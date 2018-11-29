from django.contrib import admin
from .models import News, SportsNews, RegistrationData
from django.contrib.auth.models import Group 

# Register your models here.

admin.site.unregister(Group)
admin.site.register(News)
admin.site.register(SportsNews)
class RegistrationDataAdmin(admin.ModelAdmin):
    list_display = ('username','password','email','phone')
    list_filter = ('username','email','phone')


admin.site.register(RegistrationData,RegistrationDataAdmin)



admin.site.site_header = 'Django Administrator'