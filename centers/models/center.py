from django.db import models
from organizations.models.branch import Branch

class Center(models.Model):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    center_number = models.IntegerField()
    address = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.branch_name} - {self.center_number} - {self.address}"

