# Generated by Django 3.1.8 on 2021-05-20 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210520_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_tasks',
            name='date',
            field=models.DateField(default=datetime.date),
        ),
    ]
