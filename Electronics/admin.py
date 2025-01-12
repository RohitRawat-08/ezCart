from django.contrib import admin
from Electronics.models import ElectronicsModel

# Register your models here.



class ElectronicAdmin(admin.ModelAdmin):
    list_filter = ['category']


admin.site.register(ElectronicsModel,ElectronicAdmin)