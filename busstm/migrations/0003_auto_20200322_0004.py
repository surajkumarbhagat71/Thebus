# Generated by Django 2.2.7 on 2020-03-22 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busstm', '0002_auto_20200320_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='bus_start_time',
            new_name='bus_arival_time',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='bus_all_seet',
            new_name='bus_distance',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='bus_end_stop',
            new_name='bus_form_city',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='bus_start',
            new_name='bus_to_city',
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_rant',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_trival_time',
            field=models.IntegerField(default=' '),
            preserve_default=False,
        ),
    ]
