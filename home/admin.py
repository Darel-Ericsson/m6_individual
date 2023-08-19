from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2"
                    ),
            },
        ),
    )
    fieldsets = (
    (None, {"fields": ("username", "password")}),
    (
        ("Personal info"),
        {
            "fields": (
                "first_name",
                "last_name",
                "rut",
                "phone",
                "birthday",
                "email"
            )
        }
    ),
    (
        ("Permissions"),
        {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        },
    ),
    (("Important dates"), {"fields": ("last_login", "date_joined")}),
)


admin.site.register(User, CustomUserAdmin)