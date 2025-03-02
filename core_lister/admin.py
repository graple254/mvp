from django.contrib import admin
from .models import *

    
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "role")
    list_filter = ('role',)

admin.site.register(User, UserAdmin)    



@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'city', 'phone_number', 'is_verified', 'status')
    list_filter = ('is_verified', 'status', 'city')
    search_fields = ('business_name', 'user__username', 'phone_number')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'category', 'business_profile', 'daily_rate', 'is_available')
    list_filter = ('category', 'transmission', 'fuel_type', 'is_available')
    search_fields = ('make', 'model', 'license_plate', 'business_profile__business_name')

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    pass  # Add customization when model is implemented

@admin.register(Analytic)
class AnalyticAdmin(admin.ModelAdmin):
    pass  # Add customization when model is implemented

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass  # Add customization when model is implemented



