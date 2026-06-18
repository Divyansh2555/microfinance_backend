from django.db import models
from groups.models.groups import Groups
from customers.models.customer import Customer


class Meeting(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="meetings")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="meetings")


    meeting_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("scheduled", "Scheduled"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="scheduled"
    )

    def __str__(self):
        return f"{self.meeting_date} - {self.status}"