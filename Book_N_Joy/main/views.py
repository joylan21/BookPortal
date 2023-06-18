from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method == 'POST':
        try:
            data = request.POST
            book = Books.objects.get(book_name=data['book'])
            BookOrder.objects.create(email = data['email'],book=book,message=data['message'],contact_number=data['phone'],address=data['address'])
            return redirect(reverse('home'))
        except :
            return redirect(reverse('home'))
    book_objects = Books.objects.all()
    print(book_objects.count())
    context = {'book_objects':book_objects}
    return render(request, 'index.html',context=context)

def AboutUs(request):
    return render(request, 'aboutUs.html')

def ContactUs(request,message=None):
    context={'message':''}
    if request.method == 'POST':
        try:
            data = request.POST
            print(data)
            UserMessage.objects.create(email = data['email'],name=data['name'],message=data['message'])
            context={'message':'Form submitted successfully'}
        except Exception as e:
            print(e)

    return render(request, 'contactUs.html',context=context)