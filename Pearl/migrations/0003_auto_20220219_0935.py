# Generated by Django 3.2 on 2022-02-19 08:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pearl', '0002_auto_20220211_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pearl',
            new_name='pearl_image',
        ),
        migrations.AddField(
            model_name='post',
            name='pearl_audio',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media/audio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pearl_video',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media/video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('FAITH', 'faith'), ('WISDOM', 'wisdom'), ('LOVE', 'love'), ('POWER', 'power')], max_length=200),
        ),
    ]