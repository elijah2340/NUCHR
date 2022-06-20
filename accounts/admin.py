from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Director, StaffProfile


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'surname')
    filter_horizontal = ()
    list_filter = ('staff_category',)
    fieldsets = ()
    list_display_links = ('email', 'first_name', 'surname')
    ordering = ()


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('staff', 'director_department')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display_links = ('staff', 'director_department')
    ordering = ()


class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'profile_picture')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display_links = ()
    ordering = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(StaffProfile, StaffProfileAdmin)