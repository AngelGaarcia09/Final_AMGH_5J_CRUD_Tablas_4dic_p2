# Generated by Django 5.1 on 2024-12-03 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trocas_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='troca',
            old_name='date',
            new_name='date_color',
        ),
    ]