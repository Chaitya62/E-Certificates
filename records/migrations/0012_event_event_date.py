# Generated by Django 2.0.4 on 2018-04-30 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_auto_20180430_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
