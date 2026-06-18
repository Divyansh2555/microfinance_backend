from django.db import models
from .customer import Customer


class Document(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    pan_card_image = models.ImageField(
        upload_to="documents/pan/",
        null=True,
        blank=True
    )

    aadhaar_front_image = models.ImageField(
        upload_to="documents/aadhaar/front/",
        null=True,
        blank=True
    )

    aadhaar_back_image = models.ImageField(
        upload_to="documents/aadhaar/back/",
        null=True,
        blank=True
    )

    accounts_number = models.ImageField(
        upload_to="documents/accounts/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}"