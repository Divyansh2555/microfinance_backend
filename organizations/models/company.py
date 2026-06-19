from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=100)
    register_number = models.IntegerField()
    def __str__(self):
        return self.name