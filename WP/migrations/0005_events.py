# Generated by Django 4.0.1 on 2022-01-24 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WP', '0004_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('desc', models.CharField(max_length=120, null=True)),
                ('startTime', models.CharField(max_length=120, null=True)),
                ('endTime', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
