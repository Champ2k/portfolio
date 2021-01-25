from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ('name', 'email', 'message')