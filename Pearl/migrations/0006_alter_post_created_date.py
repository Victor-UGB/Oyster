# Generated by Django 3.2 on 2021-06-11 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pearl', '0005_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.date(2021, 6, 11)),
        ),
    ]
