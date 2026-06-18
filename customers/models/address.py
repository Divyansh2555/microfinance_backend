from django.db import models
from .customer import Customer

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street= models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.street

