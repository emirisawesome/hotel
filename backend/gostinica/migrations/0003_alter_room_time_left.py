# Generated by Django 4.0.2 on 2022-02-23 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gostinica', '0002_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='time_left',
            field=models.CharField(choices=[(datetime.datetime(2022, 2, 24, 9, 5, 10, 240455), '1'), (datetime.datetime(2022, 2, 25, 9, 5, 10, 240473), '2'), (datetime.datetime(2022, 2, 26, 9, 5, 10, 240475), '3'), (datetime.datetime(2022, 2, 27, 9, 5, 10, 240478), '4'), (datetime.datetime(2022, 2, 28, 9, 5, 10, 240480), '5'), (datetime.datetime(2022, 3, 1, 9, 5, 10, 240482), '6'), (datetime.datetime(2022, 3, 2, 9, 5, 10, 240485), '7')], max_length=100),
        ),
    ]
