# Generated by Django 3.0.6 on 2020-05-08 20:38

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200507_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-id'], 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'ordering': ['-id'], 'verbose_name': 'Carpeta', 'verbose_name_plural': 'Carpetas'},
        ),
        migrations.AddField(
            model_name='history',
            name='name_documento',
            field=models.CharField(default='a', max_length=250, verbose_name='nombre documento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='serie',
            field=models.CharField(default='a', max_length=250, verbose_name='documento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='comments',
            field=models.TextField(blank=True, verbose_name='comentarios'),
        ),
        migrations.AlterField(
            model_name='history',
            name='document',
            field=models.CharField(max_length=250, verbose_name='documento'),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.CharField(max_length=250, verbose_name='usuario'),
        ),
        migrations.CreateModel(
            name='HistoricalProfile',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Empleado'), (2, 'Abogado'), (3, 'Administrador')], default=3)),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de creación')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de modificación')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Usuario',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalHistory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('user', models.CharField(max_length=250, verbose_name='usuario')),
                ('document', models.CharField(max_length=250, verbose_name='documento')),
                ('name_documento', models.CharField(max_length=250, verbose_name='nombre documento')),
                ('serie', models.CharField(max_length=250, verbose_name='documento')),
                ('date', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de la acción')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Historial',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFolder',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('is_public', models.BooleanField(default=True, verbose_name='carpeta publica')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de creación')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de modificación')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.Folder', verbose_name='carpeta padre')),
            ],
            options={
                'verbose_name': 'historical Carpeta',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDocument',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('file', models.TextField(max_length=100)),
                ('name', models.CharField(max_length=250, verbose_name='nombre')),
                ('serie', models.CharField(max_length=250)),
                ('is_public', models.BooleanField(default=True, verbose_name='documento publico')),
                ('comments', models.TextField(blank=True, verbose_name='comentarios')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de creación')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='fecha de modificación')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.Folder', verbose_name='ruta del documento')),
            ],
            options={
                'verbose_name': 'historical Documento',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
