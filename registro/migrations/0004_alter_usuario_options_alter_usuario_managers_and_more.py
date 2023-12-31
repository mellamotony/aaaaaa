# Generated by Django 4.2.7 on 2023-12-27 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_producto_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuario',
        ),
    ]
