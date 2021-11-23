from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from hijack.contrib.admin import HijackUserAdminMixin

from .models import Action, Appointment, Contact, Document, User


@admin.register(User)
class _UserAdmin(UserAdmin):
    hijack_success_url = reverse_lazy("root")
    fieldsets = (
        (None, {"fields": ("email", "password", "login_type")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "bsn",
                    "rsin",
                    "birthday",
                    "street",
                    "housenumber",
                    "postcode",
                    "city",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "deactivated_on",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ("name", "created_on", "created_by")
    list_filter = ("created_by",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_by", "created_on")
    list_filter = ("created_by",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "file", "created_on", "owner")
    list_filter = ("owner",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "datetime", "created_on", "created_by")
    list_filter = ("created_by",)
