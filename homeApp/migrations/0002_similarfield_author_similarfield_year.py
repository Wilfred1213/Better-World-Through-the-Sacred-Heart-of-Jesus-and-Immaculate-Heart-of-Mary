# Generated by Django 5.0 on 2024-07-08 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homeApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="similarfield",
            name="author",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="similarfield",
            name="year",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
