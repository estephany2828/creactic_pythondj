# Generated by Django 2.0.6 on 2018-08-24 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Categoria',
        ),
    ]
