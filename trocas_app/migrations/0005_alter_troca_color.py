# Generated by Django 5.1 on 2024-12-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trocas_app', '0004_alter_troca_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='troca',
            name='color',
            field=models.CharField(max_length=100),
        ),
    ]