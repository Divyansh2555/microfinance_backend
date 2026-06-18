from django.db import models
from .meetings import Meeting


class Collection(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="collections")


    amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.meeting} "