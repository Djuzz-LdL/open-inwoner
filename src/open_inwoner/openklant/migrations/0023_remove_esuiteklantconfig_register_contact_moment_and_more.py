# Generated by Django 4.2.16 on 2025-01-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("openklant", "0022_contactmoment_register_config"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="esuiteklantconfig",
            name="register_contact_moment",
        ),
        migrations.RemoveField(
            model_name="esuiteklantconfig",
            name="register_email",
        ),
        migrations.RemoveField(
            model_name="esuiteklantconfig",
            name="send_email_confirmation",
        ),
        migrations.AlterField(
            model_name="klantensysteemconfig",
            name="register_contact_email",
            field=models.EmailField(
                blank=True,
                help_text="Contacts initiated or questions submitted by a client (e.g. via a contact form) will be registered via email.",
                max_length=254,
                verbose_name="Registreer op email adres",
            ),
        ),
        migrations.AlterField(
            model_name="klantensysteemconfig",
            name="register_contact_via_api",
            field=models.BooleanField(
                default=False,
                help_text="Contacts initiated or questions submitted by a client (e.g. via a contact form) will be registered in the appropriate API (eSuite or OpenKlant2).",
                verbose_name="Registreer op API",
            ),
        ),
    ]
