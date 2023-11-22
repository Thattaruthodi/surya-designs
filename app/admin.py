
from django.contrib import admin
from app.models import *
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display=['full_name','email','subject']
    
admin.site.register(Main_banner)


admin.site.register(Main)
admin.site.register(Contact,ContactUsAdmin)


