# Generated by Django 3.0.6 on 2020-05-07 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200507_0247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LogDoc',
            new_name='History',
        ),
    ]
