# Generated by Django 4.2.6 on 2023-10-30 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('bandas', models.ManyToManyField(null=True, to='appJukeBox.banda')),
            ],
        ),
        migrations.AddField(
            model_name='banda',
            name='estilos',
            field=models.ManyToManyField(null=True, to='appJukeBox.estilo'),
        ),
        migrations.AddField(
            model_name='banda',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appJukeBox.pais'),
        ),
    ]
