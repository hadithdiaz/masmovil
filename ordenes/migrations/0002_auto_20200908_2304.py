# Generated by Django 3.0.6 on 2020-09-09 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='fecha_out',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='reparado',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='solucion',
        ),
    ]
