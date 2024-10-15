# Generated by Django 4.2.16 on 2024-10-17 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "digid_eherkenning_oidc_generics",
            "0009_remove_digidconfig_oidc_exempt_urls_and_more",
        ),
        ("accounts", "0077_no_roepnaam"),
    ]

    operations = [
        migrations.CreateModel(
            name="OpenIDDigiDConfig",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("digid_eherkenning_oidc_generics.digidconfig",),
        ),
        migrations.CreateModel(
            name="OpenIDEHerkenningConfig",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("digid_eherkenning_oidc_generics.eherkenningconfig",),
        ),
    ]
