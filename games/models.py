from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=150)
    platform = models.CharField(max_length=20)
    year = models.IntegerField()
    genre = models.CharField(max_length=20)
    publisher = models.CharField(max_length=50)
    NA_Sales = models.FloatField(max_length=5)
    EU_Sales = models.FloatField(max_length=5)
    JP_Sales = models.FloatField(max_length=5)
    Other_Sales = models.FloatField(max_length=5)
    Global_Sales = models.FloatField(max_length=5)
    img = models.CharField(max_length=50, default='None')
    info = models.CharField(max_length=50, default='None')

    def __str__(self):
        return self.name
