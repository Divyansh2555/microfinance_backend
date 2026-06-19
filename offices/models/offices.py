from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(unique=True, max_length=10)
    address = models.TextField()
    def __str__(self):
        return self.name

