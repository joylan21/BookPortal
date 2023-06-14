from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def AboutUs(request):
    return render(request, 'aboutUs.html')

def ContactUs(request):
    return render(request, 'contactUs.html')