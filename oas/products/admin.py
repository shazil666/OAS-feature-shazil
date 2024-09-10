from django.contrib import admin
from .models import products

class productAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

admin.site.register(products, productAdmin)

# Register your models here.
