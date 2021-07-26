from django.contrib import admin
from .models import UrlShortner

# Register your models here.
@admin.register(UrlShortner)
class UrlShortnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'long_url', 'short_url']