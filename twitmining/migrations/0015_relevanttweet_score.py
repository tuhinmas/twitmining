# Generated by Django 2.0.3 on 2018-05-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitmining', '0014_auto_20180527_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='relevanttweet',
            name='score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]