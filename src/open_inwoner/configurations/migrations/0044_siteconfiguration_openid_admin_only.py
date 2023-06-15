# Generated by Django 3.2.15 on 2023-06-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0043_siteconfiguration_allow_messages_file_sharing"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteconfiguration",
            name="openid_admin_only",
            field=models.BooleanField(
                default=False,
                help_text="If checked, only admin users will be able to login via OpenId.",
                verbose_name="Restrict OpenId Connect to admin users",
            ),
        ),
    ]
