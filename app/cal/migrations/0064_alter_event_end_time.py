# Generated by Django 4.2.16 on 2024-12-05 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0063_alter_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 5, 23, 18, 32, 595335, tzinfo=datetime.timezone.utc)),
        ),
    ]