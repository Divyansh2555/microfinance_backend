from django.db import models
from customers.models import Customer

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()  # yearly
    tenure_months = models.IntegerField()

    start_date = models.DateField()
    status = models.CharField(max_length=20, default="active")

    def __str__(self):
        return self.customer