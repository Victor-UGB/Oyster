# Generated by Django 3.2 on 2022-04-19 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pearl', '0007_alter_post_todays_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='todays_date',
        ),
    ]
