from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'Login.html', {'error': 'Invalid email or password'})
    return render(request, 'Login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def verifications(request):
    return render(request, 'Verifications.html')

@login_required
def newcomplaint(request):
    return render(request, 'newcomplain.html')

@login_required
def newenquiry(request):
    return render(request, 'newenquiry.html')
