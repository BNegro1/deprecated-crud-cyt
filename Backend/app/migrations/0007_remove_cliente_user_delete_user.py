# Generated by Django 5.0.6 on 2024-06-30 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
