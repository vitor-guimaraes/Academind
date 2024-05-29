from django.db import models

class Book(models.model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
