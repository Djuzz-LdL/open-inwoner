from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ordered_model.admin import OrderedInlineModelAdminMixin, OrderedTabularInline
from solo.admin import SingletonModelAdmin

from .models import (
    ContactFormSubject,
    ESuiteKlantConfig,
    KlantContactMomentAnswer,
    KlantenSysteemConfig,
    OpenKlant2Config,
)


class ContactFormSubjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subject_code"].widget.attrs["placeholder"] = _(
            "Must be configured if E-suite is used"
        )

    class Meta:
        model = ContactFormSubject
        fields = (
            "subject",
            "subject_code",
        )


class ContactFormSubjectInlineAdmin(OrderedTabularInline):
    model = ContactFormSubject
    form = ContactFormSubjectForm
    fields = ("subject", "subject_code", "order", "move_up_down_links")
    readonly_fields = ("order", "move_up_down_links")
    ordering = ("order",)
    extra = 0


class ESuiteKlantConfigAdminForm(forms.ModelForm):
    class Meta:
        model = ESuiteKlantConfig
        fields = "__all__"


@admin.register(ESuiteKlantConfig)
class ESuiteKlantConfigAdmin(OrderedInlineModelAdminMixin, SingletonModelAdmin):
    form = ESuiteKlantConfigAdminForm
    inlines = [
        ContactFormSubjectInlineAdmin,
    ]
    fieldsets = [
        (
            _("Klanten en Contacten API registratie"),
            {
                "fields": [
                    "register_bronorganisatie_rsin",
                    "register_type",
                    "register_channel",
                    "register_employee_id",
                    "use_rsin_for_innNnpId_query_parameter",
                ],
            },
        ),
        (
            _("Filter Contactmomenten"),
            {
                "fields": [
                    "exclude_contactmoment_kanalen",
                ]
            },
        ),
        (
            _("Services"),
            {
                "fields": [
                    "klanten_service",
                    "contactmomenten_service",
                ],
            },
        ),
    ]


@admin.register(KlantContactMomentAnswer)
class KlantContactMomentAnswerAdmin(admin.ModelAdmin):
    search_fields = [
        "user__first_name",
        "user__last_name",
        "user__email",
        "contactmoment_url",
    ]
    list_filter = ["is_seen"]
    list_display = ["user", "contactmoment_url", "is_seen"]


#
# OpenKlant2
#


class OpenKlant2ConfigAdminForm(forms.ModelForm):
    class Meta:
        model = OpenKlant2Config
        fields = "__all__"


@admin.register(OpenKlant2Config)
class OpenKlant2ConfigAdmin(SingletonModelAdmin):
    model = OpenKlant2Config
    form = OpenKlant2ConfigAdminForm
    fieldsets = [
        (
            _("API configuration"),
            {
                "fields": [
                    "service",
                ]
            },
        ),
        (
            _("Vragen"),
            {
                "fields": [
                    "mijn_vragen_kanaal",
                    "mijn_vragen_organisatie_naam",
                    "mijn_vragen_actor",
                    "interne_taak_gevraagde_handeling",
                    "interne_taak_toelichting",
                ]
            },
        ),
    ]


@admin.register(KlantenSysteemConfig)
class KlantenSysteemConfigAdmin(SingletonModelAdmin):
    model = KlantenSysteemConfig
    change_form_template = "admin/openklant/klantensysteemconfig/change_form.html"
    fieldsets = [
        (
            _("API configuration globals"),
            {"fields": ["primary_backend"]},
        ),
        (
            _("Vragen/contactmomenten"),
            {
                "fields": [
                    "register_contact_via_api",
                    "register_contact_email",
                    "send_email_confirmation",
                ]
            },
        ),
    ]
