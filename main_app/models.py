from django.db import models

class Flavour(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    rating = models.IntegerField()

    def __str__(self):
        return self.name