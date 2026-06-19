from django.db import models
from .regional import RegionalOffice



class AreaOffice(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    regional_office = models.ForeignKey(RegionalOffice, on_delete=models.CASCADE)


    def __str__(self):
        return self.name