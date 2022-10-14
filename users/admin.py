from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class TodoUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('profile_pic', 'biography')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_pic', 'biography')}),
    )


admin.site.unregister(User)
admin.site.register(User, TodoUserAdmin)
# admin.site.register(User)
