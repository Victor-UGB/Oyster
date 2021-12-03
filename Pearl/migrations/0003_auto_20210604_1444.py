# Generated by Django 3.2 on 2021-06-04 13:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pearl', '0002_post_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Pearl.post')),
            ],
            bases=('Pearl.post',),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 6, 4, 14, 44, 23, 52274)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pearl',
            field=models.ImageField(upload_to='media/img'),
        ),
    ]
