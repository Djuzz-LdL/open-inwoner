# Generated by Django 4.2.15 on 2024-08-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0069_merge_20240724_0945"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteconfiguration",
            name="enable_notification_channel_choice",
            field=models.BooleanField(
                default=False,
                help_text="Give users the option to choose how they want to receive notifications (digital and post or digital only)",
                verbose_name="Enable choice of notification channel",
            ),
        ),
    ]
