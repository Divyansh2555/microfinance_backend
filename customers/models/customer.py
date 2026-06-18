from django.db import models

class Customer(models.Model):

    borrower_first_name = models.CharField(max_length=15)
    borrower_last_name = models.CharField(max_length=15)
    borrower_gender = models.CharField(max_length=15)
    borrower_dob = models.DateField()
    no_of_dependents = models.IntegerField()

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    # Co-Borrower Details
    co_borrower_first_name = models.CharField(max_length=15)
    co_borrower_last_name = models.CharField(max_length=15)
    co_borrower_gender = models.CharField(max_length=15)
    co_borrower_dob = models.DateField()

    son_of = models.CharField(max_length=15)
    relationship = models.CharField(max_length=15)
    caste = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.borrower_first_name} {self.borrower_last_name}"