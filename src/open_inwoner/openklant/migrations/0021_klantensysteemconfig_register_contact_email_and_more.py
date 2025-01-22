# Generated by Django 4.2.16 on 2025-01-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("openklant", "0020_add_more_help_texts_to_openklant2_config"),
    ]

    operations = [
        migrations.AddField(
            model_name="klantensysteemconfig",
            name="register_contact_email",
            field=models.EmailField(
                blank=True,
                help_text="Contacts initiated or questions submitted by a client (e.g. via a contact form) will be registered via email.",
                max_length=254,
                verbose_name="Registreer vragen/contactmomenten op email adres",
            ),
        ),
        migrations.AddField(
            model_name="klantensysteemconfig",
            name="register_contact_via_api",
            field=models.BooleanField(
                default=False,
                help_text="Contacts initiated or questions submitted by a client (e.g. via a contact form) will be registered in the appropriate API (eSuite or OpenKlant2).",
                verbose_name="Registreer vragen/contactmomenten op API",
            ),
        ),
        migrations.AddField(
            model_name="klantensysteemconfig",
            name="send_email_confirmation",
            field=models.BooleanField(
                help_text="If enabled the 'contactform_confirmation' email template will be sent. If disabled the external API will send a confirmation email.",
                verbose_name="Stuur contactformulier e-mailbevestiging",
                default=False,
            ),
        ),
    ]
