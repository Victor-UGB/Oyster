# Generated by Django 3.2 on 2021-06-16 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pearl', '0006_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.date(2021, 6, 16)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pearl',
            field=models.FileField(upload_to='media/img'),
        ),
        migrations.DeleteModel(
            name='PreviousPost',
        ),
    ]
