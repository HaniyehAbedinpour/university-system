from django.contrib import admin
from .models import Department
from students.models import Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0

@admin.register(Department)
class DEpartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','code')
    inlines = [StudentInline]

