# Generated by Django 4.0.2 on 2022-09-21 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_comment_novena_novenacomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='novenacomment',
            old_name='novena',
            new_name='novenas',
        ),
    ]
