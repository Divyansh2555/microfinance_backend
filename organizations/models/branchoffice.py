from django.db import models
from .areaoffice import AreaOffice



class Branch(models.Model):
    area = models.ForeignKey(AreaOffice, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=20,unique=True)
    branch_code = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=20,unique=True)
    number = models.CharField(max_length=15,unique=True)
    address = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.branch_name} "