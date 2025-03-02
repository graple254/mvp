from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password")


        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Choose another one.")
            return render(request, "files/signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use. Use another email.")
            return render(request, "files/signup.html")

        # Create user without role first
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Log in user
        login(request, user)
        return redirect("select_vehicle")


    return render(request, "files/signup.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == "business_admin":
                return redirect("business_dashboard")
            elif user.role == "cpc_admin":
                return redirect("cpc_dashboard")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, "files/login.html")


def Select_Vehicle(request):
    return render(request, "files/select_vehicle.html")


#@login_required
def Get_Booking_Details(request):
    return render(request, "files/vehicle_details.html")


#@login_required
def Researve_Vehicle(request):
    return render(request, "files/vehicle_booking.html")


#@login_required
def Bookings_Profile(request):
    return render(request, "files/profile.html")

