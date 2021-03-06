# Generated by Django 2.0.4 on 2018-04-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_auto_20180430_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='division',
            field=models.CharField(blank=True, default='A', max_length=255),
        ),
        migrations.AddField(
            model_name='attendee',
            name='year_of_study',
            field=models.CharField(blank=True, choices=[('TY', 'Third Year'), ('SY', 'Second Year'), ('FY', 'First Year'), ('B.Tech', 'Final/Fourth Year')], default='FY', max_length=255),
        ),
    ]
