# Generated by Django 3.2.12 on 2022-02-14 13:40

from django.db import migrations, models
import privates.storages


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0026_message_sent"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="action",
            options={
                "ordering": ("end_date", "-created_on"),
                "verbose_name": "action",
                "verbose_name_plural": "actions",
            },
        ),
        migrations.AlterModelOptions(
            name="appointment",
            options={
                "verbose_name": "appointment",
                "verbose_name_plural": "appointments",
            },
        ),
        migrations.AlterModelOptions(
            name="invite",
            options={
                "verbose_name": "invitation",
                "verbose_name_plural": "invitations",
            },
        ),
        migrations.AlterModelOptions(
            name="message",
            options={"verbose_name": "message", "verbose_name_plural": "messages"},
        ),
        migrations.AlterField(
            model_name="contact",
            name="function",
            field=models.CharField(
                blank=True,
                default="",
                help_text="The function of the contact within an organization.",
                max_length=200,
                verbose_name="Function",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="file",
            field=models.FileField(
                storage=privates.storages.PrivateMediaFileSystemStorage(),
                upload_to="",
                verbose_name="File",
            ),
        ),
    ]
