from django.db import models
from .customer import Customer


class Kyc(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pan=models.CharField(max_length=8)
    aadhar=models.IntegerField(max_length=12)

    def __str__(self):
        return f"{self.customer} {self.pan} {self.aadhar}"