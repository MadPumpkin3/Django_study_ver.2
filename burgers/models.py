from django.db import models


# Create your models here.
class Burger(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Drink(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.name
