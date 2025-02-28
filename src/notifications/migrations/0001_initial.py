# Generated by Django 4.2.15 on 2024-09-04 10:18

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("zgw_consumers", "0022_set_default_service_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationsAPIConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notification_delivery_max_retries",
                    models.PositiveIntegerField(
                        default=5,
                        help_text="The maximum number of automatic retries. After this amount of retries, guaranteed delivery stops trying to deliver the message.",
                    ),
                ),
                (
                    "notification_delivery_retry_backoff",
                    models.PositiveIntegerField(
                        default=3,
                        help_text="If specified, a factor applied to the exponential backoff. This allows you to tune how quickly automatic retries are performed.",
                    ),
                ),
                (
                    "notification_delivery_retry_backoff_max",
                    models.PositiveIntegerField(
                        default=48,
                        help_text="An upper limit in seconds to the exponential backoff time.",
                    ),
                ),
                (
                    "notifications_api_service",
                    models.ForeignKey(
                        limit_choices_to={"api_type": "nrc"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="notifications_api_configs",
                        to="zgw_consumers.service",
                        verbose_name="notifications api service",
                    ),
                ),
            ],
            options={
                "verbose_name": "Notificatiescomponentenconfiguratie",
            },
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "callback_url",
                    models.URLField(
                        help_text="Where to send the notifications (webhook url)",
                        verbose_name="callback url",
                    ),
                ),
                (
                    "client_id",
                    models.CharField(
                        help_text="Client ID to construct the auth token",
                        max_length=50,
                        verbose_name="client ID",
                    ),
                ),
                (
                    "secret",
                    models.CharField(
                        help_text="Secret to construct the auth token",
                        max_length=50,
                        verbose_name="client secret",
                    ),
                ),
                (
                    "channels",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        help_text="Comma-separated list of channels to subscribe to",
                        size=None,
                        verbose_name="channels",
                    ),
                ),
                (
                    "_subscription",
                    models.URLField(
                        blank=True,
                        editable=False,
                        help_text="Subscription as it is known in the NC",
                        verbose_name="NC subscription",
                    ),
                ),
                (
                    "notifications_api_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="notifications.notificationsapiconfig",
                    ),
                ),
            ],
            options={
                "verbose_name": "Webhook subscription",
                "verbose_name_plural": "Webhook subscriptions",
            },
        ),
    ]
