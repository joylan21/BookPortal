from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='books')

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_top = models.ImageField(upload_to='about_us')
    image_bottom = models.ImageField(upload_to='about_us')

class ContactUs(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class BookOrder(models.Model):
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    address=models.TextField()
    message = models.TextField()

class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()