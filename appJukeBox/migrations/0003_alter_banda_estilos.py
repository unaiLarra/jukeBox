# Generated by Django 4.2.6 on 2023-10-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appJukeBox', '0002_remove_estilo_bandas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='estilos',
            field=models.ManyToManyField(to='appJukeBox.estilo'),
        ),
    ]
