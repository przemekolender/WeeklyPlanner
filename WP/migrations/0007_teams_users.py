# Generated by Django 4.0.1 on 2022-01-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WP', '0006_events_team_events_user_task_team_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='users',
            field=models.ManyToManyField(to='WP.User'),
        ),
    ]
