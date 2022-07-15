from django.contrib import admin
from .models import Department, Leave, Query


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}


class LeaveAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'status' )


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Leave, LeaveAdmin)
admin.site.register(Query)
