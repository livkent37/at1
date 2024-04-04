# Import necessary modules
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# View for rendering index page
def index(request):
    # Check if user is authenticated, if not, redirect to login page
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    # Render user.html template
    return render(request, "users/user.html")

# View for handling user login
def login_view(request):
    # If request method is POST, process login form data
    if request.method == "POST":
        # Get username and password from POST data
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        # If user is authenticated, log them in and redirect to index page
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        # If authentication fails, display error message
        else:
            messages.success(request, "Invalid Credentials.")
            return render(request, "users/login.html")
    # Render login.html template for GET requests
    return render(request, "users/login.html")

# View for handling user logout
def logout_view(request):
    # Log out the user
    logout(request)
    # Display success message
    messages.success(request, "Successfully logged out.")
    # Redirect to login page
    return redirect(reverse('users:login'))
