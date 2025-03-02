from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.contrib import messages

# Get the correct User model
User = get_user_model()



def home(request):
      return render(request, "files/home.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password")
        role = request.POST.get("role")  # Capturing role from the form

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Choose another one.")
            return render(request, "files/sign-up.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use. Use another email.")
            return render(request, "files/sign-up.html")

        # Create user and assign role
        user = User.objects.create_user(username=username, email=email, password=password)
        user.role = role  # Assign role manually
        user.save()

        # Log in the user
        login(request, user)

        # Redirect based on role
        if role == "Partner":
            return redirect("business_dashboard")

    return render(request, "files/sign-up.html")



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == "Partner":
                return redirect("business_dashboard")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, "files/sign-in.html")


@login_required
@role_required("Partner")
def business_dashboard(request):
    return render(request, "files/dashboard.html")