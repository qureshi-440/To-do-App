# Generated by Django 3.1.8 on 2021-05-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_tasks',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='to_do_tasks',
            name='satisfaction_level',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]