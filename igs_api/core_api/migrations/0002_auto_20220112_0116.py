# Generated by Django 2.2.26 on 2022-01-12 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['id'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='created',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated',
        ),
    ]
