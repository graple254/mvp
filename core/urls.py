from django.urls import path
from .views import *

urlpatterns = [
      path('signup/', signup_view, name='signup'),
      path('login/', login_user, name='login_user'),
      path('', Select_Vehicle, name='Select_Vehicle'),
      path('select_vehicle/', Get_Booking_Details, name='Get_Booking_Details'),
      path('vehicle_booking/', Researve_Vehicle, name='Researve_Vehicle'),
      path('b&profile/', Bookings_Profile, name='profile'),
]
