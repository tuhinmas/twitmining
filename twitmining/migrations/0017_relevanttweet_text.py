# Generated by Django 2.1.2 on 2018-10-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitmining', '0016_auto_20181017_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='relevanttweet',
            name='text',
            field=models.CharField(default='DEFAULT VALUE', max_length=140),
        ),
    ]
