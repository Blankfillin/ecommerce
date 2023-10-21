from django.db import models

# Create your models here.


class Products(models.Model):
    class Meta:
        verbose_name_plural = "Products"

    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=300)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    total = models.FloatField(default=0.0)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    def __str__(self):
        return f"Order {self.id}"
