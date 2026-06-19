from django.db import models
class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        MANAGEMENT = "MANAGEMENT", "Management"
        REGIONAL_MANAGER = "REGIONAL_MANAGER", "Regional Manager"
        AREA_MANAGER = "AREA_MANAGER", "Area Manager"
        BRANCH_MANAGER = "BRANCH_MANAGER", "Branch Manager"
        STAFF = "STAFF", "Staff"
        LOAN_OFFICER = "LOAN_OFFICER", "Loan Officer"
        FIELD_OFFICER = "FIELD_OFFICER", "Field Officer"
        FINANCE = "FINANCE", "Finance"
        ACCOUNTANT = "ACCOUNTANT", "Accountant"