from django.db import models
from emi_shedules import EMISchedule


class EMIPayment(models.Model):
    emi = models.ForeignKey(EMISchedule, on_delete=models.CASCADE, related_name="payments")

    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    mode = models.CharField(
        max_length=20,
        choices=[
            ("cash", "Cash"),
            ("upi", "UPI"),
            ("bank", "Bank"),
        ],
        default="cash"
    )

    def __str__(self):
        return f"{self.emi}"