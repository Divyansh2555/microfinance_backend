from django.db import models
from customers.models.customer import Customer
from .meetings import Meeting

class MeetingAttendance(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="attendances")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10,
        choices=[
            ("present", "Present"),
            ("absent", "Absent"),
        ]
    )

    def __str__(self):
        return f"{self.meeting} - {self.customer}"