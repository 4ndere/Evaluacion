# Generated by Django 4.2.6 on 2023-11-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0005_alter_libro_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(upload_to='../media/portadas'),
        ),
    ]
