# Generated by Django 3.2.15 on 2022-11-28 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("plans", "0008_alter_plan_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="plan",
            name="plan_contacts",
            field=models.ManyToManyField(
                blank=True,
                help_text="The contact that will help you with this plan.",
                related_name="plans",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Contacts",
            ),
        ),
    ]
