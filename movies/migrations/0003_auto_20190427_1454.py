# Generated by Django 2.2 on 2019-04-27 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190427_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]