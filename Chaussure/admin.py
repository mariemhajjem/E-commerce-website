from django.contrib import admin

# Register your models here.
from .models import Chaussure

class ShoeAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    list_display = ['nom', 'created_at','active']
    search_fields = ['nom','description']

admin.site.register(Chaussure, ShoeAdmin)
