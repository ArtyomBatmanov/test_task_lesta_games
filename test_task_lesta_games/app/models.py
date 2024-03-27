from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=100)
    tf = models.IntegerField()
    idf = models.FloatField(null=True)

    def __str__(self):
        return self.word
