# Generated by Django 4.0 on 2023-06-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_alter_stationsprayers_we_ador'),
    ]

    operations = [
        migrations.AddField(
            model_name='station_open_closing_prayer',
            name='sation_intro',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
