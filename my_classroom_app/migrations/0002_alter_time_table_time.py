# Generated by Django 4.0.1 on 2022-01-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_classroom_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_table',
            name='time',
            field=models.CharField(choices=[('8:30 - 9:30', '8:30 - 9:30'), ('9:30 - 10:30', '9:30 - 10:30'), ('11:00 - 11:50', '11:00 - 11:50'), ('11:50 - 12:40', '11:50 - 12:40'), ('12:40 - 1:30', '12:40 - 1:30'), ('2:30 - 3:30', '2:30 - 3:30'), ('3:30 - 4:30', '3:30 - 4:30'), ('4:30 - 5:30', '4:30 - 5:30')], max_length=100),
        ),
    ]
