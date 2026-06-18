from django.db import models
from loans.models.loans import Loans


class EMISchedule(models.Model):
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE, related_name="emis")

    installment_number = models.IntegerField()
    due_date = models.DateField()

    principal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_amount = models.DecimalField(max_digits=10, decimal_places=2)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("paid", "Paid"),
            ("overdue", "Overdue"),
        ],
        default="pending"
    )