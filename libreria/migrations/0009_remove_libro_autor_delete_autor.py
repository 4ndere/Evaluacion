# Generated by Django 5.0 on 2023-12-15 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0008_alter_libro_portada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
    ]
