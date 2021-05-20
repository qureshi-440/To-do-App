from django.contrib import admin
from django.contrib.admin.sites import site
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserForm
    list_display = ("email","is_admin","last_login","date_joined")
    readonly_fields = ("last_login","date_joined")
    list_filter = ('is_admin','is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1',"password2"),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User,CustomUserAdmin)
admin.site.unregister(Group)