# Generated by Django 3.2.17 on 2023-04-06 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cslapps', '0006_auto_20220903_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='available_to_all',
        ),
    ]
