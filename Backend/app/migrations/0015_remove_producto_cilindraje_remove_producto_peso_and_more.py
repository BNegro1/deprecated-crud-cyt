# Generated by Django 5.0.6 on 2024-06-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_producto_cilindraje_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cilindraje',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='potencia_maxima',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipo_motor',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='torque_maximo',
        ),
        migrations.AddField(
            model_name='producto',
            name='especificaciones',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=100),
        ),
    ]
