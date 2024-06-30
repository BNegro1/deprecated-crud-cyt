# Generated by Django 5.0.6 on 2024-06-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_cliente_contraseña_cliente_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='username',
            field=models.CharField(default='defaultusername', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
