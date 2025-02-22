# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')  # Create an index.html template for the landing page

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optional: Log the user in right after signup
            return redirect('login')  # Redirect to login page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')  # Render the home page template

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout

def men_view(request):
    print("Men view has been called")
    return render(request, 'men.html')

def women_view(request):
    return render(request, 'women.html')

def kids_view(request):
    return render(request, 'kids.html')

def personalize_view(request):
    return render(request, 'personalize.html')

def sales_view(request):
    return render(request, 'sales.html')

def trending_view(request):
    return render(request, 'trending.html')

def brands_view(request):
    return render(request, 'brands.html')

def product_view(request):
    return render(request, 'product1.html','product2.html','product3.html','product4.html','product5.html','product5.html')

def product1(request):
    return render(request, 'product1.html')

def product2(request):
    return render(request, 'product2.html')

def product3(request):
    return render(request, 'product3.html')

def product4(request):
    return render(request, 'product4.html')

def product5(request):
    return render(request, 'product5.html')

def product6(request):
    return render(request, 'product6.html')
