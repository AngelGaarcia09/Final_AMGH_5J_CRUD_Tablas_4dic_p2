# Generated by Django 5.1 on 2024-12-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trocas_app', '0005_alter_troca_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='troca',
            name='id_sucursal',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='troca',
            name='tipo_llantas',
            field=models.CharField(max_length=100),
        ),
    ]
