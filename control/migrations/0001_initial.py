# Generated by Django 3.0.6 on 2020-09-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_out', models.DateField(blank=True, null=True, verbose_name='Fecha Salida')),
                ('reparado', models.CharField(blank=True, choices=[('0', 'Si'), ('1', 'No')], max_length=1, verbose_name='Reparado')),
                ('diagnostico', models.TextField(blank=True, null=True, verbose_name='Diagnostico')),
                ('reparacion', models.TextField(blank=True, null=True, verbose_name='Reparacion')),
                ('gasto', models.DecimalField(decimal_places=0, default='0', max_digits=10)),
                ('cobro', models.DecimalField(decimal_places=0, default='0', max_digits=10)),
                ('total', models.DecimalField(decimal_places=0, default='0', max_digits=10, null=True)),
                ('medio_pago', models.CharField(choices=[('0', 'Efectivo'), ('1', 'Transferencia'), ('2', 'Debe')], default='Efectivo', max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Control',
                'verbose_name_plural': 'Controls',
                'ordering': ['-id'],
            },
        ),
    ]