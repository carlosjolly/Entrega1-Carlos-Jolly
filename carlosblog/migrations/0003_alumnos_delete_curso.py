# Generated by Django 4.0.4 on 2022-06-02 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlosblog', '0002_alter_contacto_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('cursos', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]