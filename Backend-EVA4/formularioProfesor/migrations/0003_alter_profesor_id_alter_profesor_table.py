# Generated by Django 4.2.7 on 2023-12-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioProfesor', '0002_alter_profesor_id_alter_profesor_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='profesor',
            table='profesores',
        ),
    ]
