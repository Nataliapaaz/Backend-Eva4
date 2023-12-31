# Generated by Django 4.2.7 on 2023-12-04 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularioProfesor', '0001_initial'),
        ('formularioRamos', '0002_alter_ramos_creditos_alter_ramos_horas'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoRamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularioProfesor.profesor')),
                ('ramo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Info', to='formularioRamos.ramos')),
            ],
            options={
                'db_table': 'inforamo',
            },
        ),
    ]
