# Generated by Django 2.1 on 2019-03-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0011_remove_rainfalldata_date1'),
    ]

    operations = [
        migrations.AddField(
            model_name='rainfalldata',
            name='date_val',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tmaxdata',
            name='date_val',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tmindata',
            name='date_val',
            field=models.DateField(null=True),
        ),
    ]