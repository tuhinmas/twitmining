# Generated by Django 2.0.3 on 2018-04-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitmining', '0004_auto_20180405_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='TweetHtml',
        ),
    ]
