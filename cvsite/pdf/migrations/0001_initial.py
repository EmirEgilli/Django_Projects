# Generated by Django 5.1.5 on 2025-01-23 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PersonalInfo",
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
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField()),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("summary", models.TextField(max_length=2000)),
                ("degree", models.CharField(max_length=200)),
                ("school", models.CharField(max_length=200)),
                ("previous_work", models.TextField(max_length=1000)),
                ("skills", models.TextField(max_length=1000)),
            ],
        ),
    ]
