from django.contrib import admin
from .models import CarTires
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AdminCarTires(ImportExportModelAdmin,admin.ModelAdmin ):
    list_display = ('name','sureName', 'carNo', 'phoneNumber', 'note')
    list_filter = ('name','sureName', 'carNo', 'phoneNumber', 'note')
    search_fields = ('name','sureName', 'carNo', 'phoneNumber', 'note')
    


admin.site.register(CarTires , AdminCarTires)






admin.site.site_header = "Luxury autospa"
admin.site.site_title = "Luxury autospa rengas hotelli"

