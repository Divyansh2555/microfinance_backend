from django.db import models
from .customer import Customer


class Kyc(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pan=models.CharField(max_length=8)
    aadhar=models.IntegerField(unique=True)
    bank_name=models.CharField(max_length=50)
    account_no=models.IntegerField(unique=True)
    conform_account_number=models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.customer} {self.pan} {self.aadhar}"