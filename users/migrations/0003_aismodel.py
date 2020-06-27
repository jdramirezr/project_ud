# Generated by Django 2.2.3 on 2020-06-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_resultpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='AisModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_confined_walls', models.IntegerField()),
                ('option_detail', models.IntegerField()),
                ('option_mooring', models.IntegerField()),
                ('option_characteristics', models.IntegerField()),
                ('option_mezzanine', models.IntegerField()),
                ('option_cover', models.IntegerField()),
                ('option_floor', models.IntegerField()),
                ('option_wall', models.IntegerField()),
                ('option_height', models.IntegerField()),
                ('option_quality', models.IntegerField()),
                ('option_location', models.IntegerField()),
                ('option_materials', models.IntegerField()),
                ('option_base', models.IntegerField()),
                ('option_soil', models.IntegerField()),
                ('option_environment', models.IntegerField()),
            ],
        ),
    ]
