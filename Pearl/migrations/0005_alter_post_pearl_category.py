# Generated by Django 3.2 on 2022-02-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pearl', '0004_auto_20220219_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pearl_category',
            field=models.CharField(choices=[('FOR FAITH', 'faith'), ('FOR WISDOM', 'wisdom'), ('FOR LOVE', 'love'), ('FOR POWER', 'power')], max_length=200),
        ),
    ]