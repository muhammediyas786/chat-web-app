# Generated by Django 4.0.5 on 2022-08-02 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0005_group_maker_alter_message_crt_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='maker',
        ),
        migrations.AlterField(
            model_name='message',
            name='crt_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 15, 34, 30, 308646)),
        ),
    ]
