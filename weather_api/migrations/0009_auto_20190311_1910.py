# Generated by Django 2.1 on 2019-03-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0008_auto_20190311_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rainfalldata',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
