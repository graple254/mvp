from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('Partner', 'Partner'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)

    # Fix related_name conflicts
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set", blank=True)



User = get_user_model()


class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile', blank=True, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    business_registration_number = models.CharField(max_length=100, blank=True, null=True)
    
    # Location details
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Contact details
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    # Business details
    description = models.TextField(blank=True, null=True)
    operating_hours = models.JSONField(default=dict, blank=True, null=True)
    establishment_date = models.DateField(blank=True, null=True)
    
    # Verification and status
    is_verified = models.BooleanField(default=False, blank=True, null=True)
    verification_documents = models.FileField(upload_to='business_documents/', blank=True, null=True)
    status = models.CharField(max_length=20, default='pending', blank=True, null=True,
        choices=[('pending', 'Pending'), ('active', 'Active'), ('suspended', 'Suspended')])
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name = 'Business Profile'
        verbose_name_plural = 'Business Profiles'


class CarImage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.name}"

    class Meta:
        verbose_name = 'Car Image'
        verbose_name_plural = 'Car Images'


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]
    
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    CAR_CATEGORY_CHOICES = [
        ('Small Car', 'Small Car'),
        ('suv', 'SUV'),
        ('minivan', 'Minivan'),
        ('Medium Car', 'Medium Car'),
        ('Pickup Truck', 'Pickup Truck'),
        ('safari', 'Safari'),
        ('pickup', 'Pickup Truck'),
        ('Luxury', 'Luxury'),
        ('mid-Size Suv', 'mid-Size Suv'),
    ]

    # Business relationship
    business_profile = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name='cars', blank=True, null=True)
    
    # Basic car information
    make = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CAR_CATEGORY_CHOICES, blank=True, null=True)
    
    # Registration and identification
    license_plate = models.CharField(max_length=20, blank=True, null=True)
    
    # Specifications
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, blank=True, null=True)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, blank=True, null=True)
    seats = models.PositiveIntegerField(blank=True, null=True)
    doors = models.PositiveIntegerField(blank=True, null=True)
    
    # Features
    features = models.JSONField(default=dict, blank=True, null=True)  # Store features as a JSON array
    
    # Rental details
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    minimum_rental_days = models.PositiveIntegerField(default=1, blank=True, null=True)
    is_available = models.BooleanField(default=True, blank=True, null=True)
    
    # Car condition
    mileage = models.PositiveIntegerField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    
    # Car Image Reference
    car_image = models.ForeignKey(CarImage, on_delete=models.SET_NULL, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Revenue(models.Model):
    pass

class Analytic(models.Model):
    pass

class Booking(models.Model):
    pass