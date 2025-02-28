# Generated by Django 4.2.15 on 2024-08-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0071_correct_siteconfiguration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="siteconfiguration",
            name="notifications_actions_enabled",
            field=models.BooleanField(
                default=True,
                help_text="Enable notifications for expring actions concerning plans (if enabled, individual users can still opt out by disabling notifications for plans)",
                verbose_name="User notifications for expiring actions",
            ),
        ),
        migrations.AlterField(
            model_name="siteconfiguration",
            name="notifications_cases_enabled",
            field=models.BooleanField(
                default=True,
                help_text="Enable notifications for cases (if enabled, individual users can still opt out of notifications about case updates, though not of notifications that indicate that an action concerning some case is required)",
                verbose_name="User notifications for cases",
            ),
        ),
        migrations.AlterField(
            model_name="siteconfiguration",
            name="notifications_messages_enabled",
            field=models.BooleanField(
                default=True,
                help_text="Enable notifications for messages (if enabled, individual users can still opt out; messages will only be sent if the user also opts in)",
                verbose_name="User notifications for messages",
            ),
        ),
        migrations.AlterField(
            model_name="siteconfiguration",
            name="notifications_plans_enabled",
            field=models.BooleanField(
                default=True,
                help_text="Enable notifications for plans (if enabled, individual users can still opt out)",
                verbose_name="User notifications for expiring plans",
            ),
        ),
    ]
