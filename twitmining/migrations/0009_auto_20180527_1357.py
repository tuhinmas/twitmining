# Generated by Django 2.0.3 on 2018-05-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitmining', '0008_auto_20180408_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelevantTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='link',
            field=models.CharField(default='DEFAULT VALUE', max_length=60),
        ),
        migrations.AddField(
            model_name='tweet',
            name='location',
            field=models.CharField(default='DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='tweet',
            name='score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='text',
            field=models.CharField(default='DEFAULT VALUE', max_length=140),
        ),
        migrations.AddField(
            model_name='tweet',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id_number',
            field=models.CharField(max_length=30),
        ),
    ]
