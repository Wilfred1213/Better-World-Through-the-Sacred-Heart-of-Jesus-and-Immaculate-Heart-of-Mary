# Generated by Django 4.0 on 2023-06-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0052_alter_my_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='station_img',
            field=models.ImageField(null=True, upload_to='new image/'),
        ),
    ]
