# Generated by Django 2.0.5 on 2019-07-11 19:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190711_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 19, 10, 50, 646547, tzinfo=utc)),
        ),
    ]
