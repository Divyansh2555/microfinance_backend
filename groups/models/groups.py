from django.db import models
from centers.models.center import Center

class Groups(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    group_name=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.center} {self.group_name}"
