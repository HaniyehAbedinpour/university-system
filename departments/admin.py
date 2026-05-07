from django.contrib import admin
from .models import Department


@admin.register(Department)
class DEpartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','code')

