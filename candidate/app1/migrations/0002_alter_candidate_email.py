# Generated by Django 3.2 on 2023-06-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]
