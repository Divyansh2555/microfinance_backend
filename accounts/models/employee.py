from django.db import models
from .user import User
from .role import Role
from organizations.models.headoffice import HeadOffice
from organizations.models.areaoffice import AreaOffice
from organizations.models.regional import RegionalOffice
from organizations.models.branchoffice import Branch




class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_code = models.CharField(max_length=20, unique=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    head_office = models.ForeignKey(HeadOffice, null=True, blank=True, on_delete=models.PROTECT)
    regional_office = models.ForeignKey(RegionalOffice, null=True, blank=True, on_delete=models.PROTECT)
    area_office = models.ForeignKey(AreaOffice, null=True, blank=True, on_delete=models.PROTECT)
    branch_office = models.ForeignKey(Branch, null=True, blank=True, on_delete=models.PROTECT)
    manager = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.user - self.role}"