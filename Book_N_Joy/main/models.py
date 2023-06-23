from django.db import models
from django.utils.text import slugify

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=200,unique=True)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='books')

    # SEO metadata
    slug = models.SlugField(unique=True, editable=False,null=True,blank=True)
    meta_title = models.CharField(max_length=200,null=True,blank=True)
    meta_description = models.TextField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        self.meta_title = self.book_name
        self.meta_description = self.description
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_name

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_top = models.ImageField(upload_to='about_us')
    image_bottom = models.ImageField(upload_to='about_us')

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.email

class BookOrder(models.Model):
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    address=models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.book.book_name

class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name