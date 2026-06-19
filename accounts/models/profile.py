from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField(null=True, blank=True)

    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    pincode = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    aadhar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)

    aadhar_image = models.ImageField(upload_to='aadhar_images/', blank=True, null=True)

    pan = models.CharField(max_length=10, unique=True, null=True, blank=True)
    pan_image = models.ImageField(upload_to='pan_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} Profile"