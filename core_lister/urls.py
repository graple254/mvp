from django.urls import path
from .views import *

urlpatterns = [
      path('', home, name='home'),
      path('signup/', signup_view, name='signup'),
      path('login/', login_user, name='login'),
      path('business_dashboard/', business_dashboard, name='business_dashboard'),
]
