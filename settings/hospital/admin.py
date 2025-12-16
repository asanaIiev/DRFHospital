from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password', 'email', 'role', 'data_registered', 'token'
            ),
        }),
    ]
    readonly_fields = ['token', 'data_registered']

admin.site.register(Appointment)
admin.site.register(AppointmentHistory)
admin.site.register(Bill)
admin.site.register(Doctor)