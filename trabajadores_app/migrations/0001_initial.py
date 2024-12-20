# Generated by Django 5.1.1 on 2024-12-03 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id_trabajador', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('curp', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('puesto', models.CharField(max_length=20)),
            ],
        ),
    ]
