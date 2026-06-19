from django.db import models
from .company import Company

class HeadOffice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    hade_office_code = models.IntegerField()
    state = models.TextField()
    pincode = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.TextField()
    state = models.TextField()
    pincode = models.IntegerField()
    address = models.TextField()



    def __str__(self):
        return self.name