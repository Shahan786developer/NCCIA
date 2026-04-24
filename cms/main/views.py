from django.shortcuts import render

# Create your views here.
def dashboard(request):
    x = 5
    return render(request, 'dashboard.html', {'x': x})

def verifications(request):
    return render(request, 'Verifications.html')

def login(request):
    return render(request, 'Login.html')