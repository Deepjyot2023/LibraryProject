# Generated by Django 3.2 on 2023-04-27 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='bookinfo',
        ),
    ]
