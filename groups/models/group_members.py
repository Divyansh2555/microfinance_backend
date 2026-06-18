from django.db import models
from customers.models.customer import Customer
from .groups import Groups
from centers.models.center import Center
class Group_Members(models.Model):
    group_member_name = models.CharField(max_length=10)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.group_member_name - self.group}"

