# Generated by Django 3.0.6 on 2020-05-08 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200508_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalhistory',
            old_name='name_documento',
            new_name='name_document',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='name_documento',
            new_name='name_document',
        ),
    ]
