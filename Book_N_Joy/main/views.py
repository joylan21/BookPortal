from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        try:
            data = request.POST
            book = Books.objects.get(book_name=data['book'])
            BookOrder.objects.create(email = data['email'],book=book,message=data['message'],contact_number=data['phone'],address=data['address'])
            messages.success(request,'Book order submitted successfully.')
            return redirect(reverse('home'))
        except :
            return redirect(reverse('home'))
    query = request.GET.get('search')
    if query:
        book_objects = Books.objects.filter(book_name__icontains=query)
    else:
        book_objects = Books.objects.all()
    context = {'book_objects':book_objects}
    return render(request, 'index.html',context=context)

def AboutUs(request):
    return render(request, 'aboutUs.html')

def ContactUs(request,message=None):
    context={'message':''}
    if request.method == 'POST':
        try:
            data = request.POST
            UserMessage.objects.create(email = data['email'],name=data['name'],message=data['message'])
            messages.success(request,'Message sent successfully.')
        except Exception as e:
            print(e)

    return render(request, 'contactUs.html',context=context)