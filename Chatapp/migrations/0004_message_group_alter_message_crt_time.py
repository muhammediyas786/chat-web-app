# Generated by Django 4.0.5 on 2022-08-02 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='group',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='message',
            name='crt_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 10, 50, 38, 835668)),
        ),
    ]
