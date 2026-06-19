from django.db import models


class Role(models.Model):
    ROLE_CHOICES = (
        ("SUPER_ADMIN", "Super Admin"),
        ("MANAGEMENT", "Management"),
        ("REGIONAL_MANAGER", "Regional Manager"),
        ("AREA_MANAGER", "Area Manager"),
        ("BRANCH_MANAGER", "Branch Manager"),
        ("STAFF", "Staff"),
        ("LOAN_OFFICER", "Loan Officer"),
        ("FIELD_OFFICER", "Field Officer"),
        ("FINANCE", "Finance"),
        ("ACCOUNTANT", "Accountant"),
    )

    name = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.name