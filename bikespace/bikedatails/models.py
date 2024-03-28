from django.db import models

class Bike(models.Model):
    name = models.CharField(max_length=200)
    rating= models.FloatField()
    price = models.FloatField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    isfavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
