# Generated by Django 4.2.6 on 2023-11-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_rename_autores_libro_autor_alter_libro_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.DateField(),
        ),
    ]
