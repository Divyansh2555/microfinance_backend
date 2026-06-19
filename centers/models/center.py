from django.db import models
from django.core.exceptions import ValidationError
from organizations.models.branchoffice import Branch

class Center(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="centers")
    center_number = models.PositiveIntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.branch} - Center {self.center_number}"

    def clean(self):
        if not self.branch:
            raise ValidationError("Branch required hai")