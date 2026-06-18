from django.db import models
from groups.models import Groups
from customers.models import Customer


class GroupMember(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'customer')


    def __str__(self):
        return f"{self.group} - {self.customer}"
