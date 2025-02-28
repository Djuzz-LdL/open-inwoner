# Generated by Django 4.2.16 on 2024-10-23 08:26

from django.db import migrations


def delete_old_celery_tasks(apps, _):
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")

    legacy_tasks = PeriodicTask.objects.filter(
        name__in=[
            "Send emails about messages",
            "Send emails about expiring plans",
            "Send emails about expiring actions",
            "Delete old emails",
            "Retry emails",
            "Rebuild search index",
            "Import ZGW data",
        ]
    )
    legacy_tasks.delete()


class Migration(migrations.Migration):

    dependencies = [("django_celery_beat", "0018_improve_crontab_helptext")]

    operations = [
        migrations.RunPython(
            code=delete_old_celery_tasks,
            reverse_code=migrations.RunPython.noop,
        )
    ]
