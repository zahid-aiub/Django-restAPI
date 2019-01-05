from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True,)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name


