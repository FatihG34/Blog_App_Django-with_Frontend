from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin



# @admin.register(User)
# class TodoUserAdmin(UserAdmin):
#     list_display = UserAdmin.list_display + ('profile_pic', 'biography')
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('profile_pic', 'biography')}),
#     )

# admin.site.unregister(User)

admin.site.register(User)