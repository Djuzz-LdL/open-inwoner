# Generated by Django 3.2.15 on 2023-03-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plans", "0015_plancontact_notify_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plancontact",
            name="notify_new",
            field=models.BooleanField(default=True, verbose_name="Notify contact"),
        ),
    ]
