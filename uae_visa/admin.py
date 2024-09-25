from django.contrib import admin
from .models import *


class VisaInfoAdmin(admin.ModelAdmin):
    list_display = ('serial_id',)

# class VisaApplicationAdmin(admin.ModelAdmin):
#     list_display = ('id_number', 'visa_no')

# admin.site.register(Broker)
# admin.site.register(VisaInfo)
admin.site.register(VisaInfo, VisaInfoAdmin)
# admin.site.register( VisaApplication, VisaAppAdmin)
# admin.site.register(VisaApplication, VisaApplicationAdmin)
admin.site.register(VisaApplication)

