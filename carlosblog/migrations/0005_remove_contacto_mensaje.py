# Generated by Django 4.0.4 on 2022-06-03 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlosblog', '0004_trabajos_delete_examenes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='mensaje',
        ),
    ]
