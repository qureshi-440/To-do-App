# Generated by Django 3.1.8 on 2021-05-23 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20210522_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='category',
        ),
    ]
