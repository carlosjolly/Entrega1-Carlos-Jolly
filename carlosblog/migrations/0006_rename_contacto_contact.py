# Generated by Django 4.0.4 on 2022-06-03 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlosblog', '0005_remove_contacto_mensaje'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacto',
            new_name='Contact',
        ),
    ]
