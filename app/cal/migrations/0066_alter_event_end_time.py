# Generated by Django 4.2.16 on 2024-12-06 01:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0065_alter_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 6, 2, 41, 26, 295836, tzinfo=datetime.timezone.utc)),
        ),
    ]