# Generated by Django 4.0 on 2023-06-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_stationsprayers_hymn'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationsprayers',
            name='words_of_our_lord',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
