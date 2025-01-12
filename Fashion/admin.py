from django.contrib import admin
from Fashion.models import FashionModel
# Register your models here.


class fashionAdmin(admin.ModelAdmin):
    list_filter=['category']


admin.site.register(FashionModel,fashionAdmin)