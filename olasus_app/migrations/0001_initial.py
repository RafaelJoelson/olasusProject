# Generated by Django 5.0.1 on 2024-01-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgentedeSaude",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "cns",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=255)),
                ("login", models.CharField(max_length=255, unique=True)),
                ("psf", models.CharField(max_length=10)),
                ("area", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
