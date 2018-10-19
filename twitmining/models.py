from django.db import models


class Keyword(models.Model):
    keyword = models.CharField(max_length=100, default='DEFAULT VALUE', verbose_name='Please enter a keyword :')

    def __str__(self):
        return self.keyword


class RelevantTweet(models.Model):
    link = models.CharField(max_length=60, default='DEFAULT VALUE')
    text = models.CharField(max_length=140, default='DEFAULT VALUE')
