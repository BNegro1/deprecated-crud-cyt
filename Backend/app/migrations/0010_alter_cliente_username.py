# Generated by Django 5.0.6 on 2024-06-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cliente_groups_cliente_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
