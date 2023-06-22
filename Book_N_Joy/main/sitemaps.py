from django.contrib.sitemaps import Sitemap
from .models import Books, AboutUs, ContactUs, BookOrder, UserMessage

class BooksSitemap(Sitemap):
    def items(self):
        return Books.objects.all()

class AboutUsSitemap(Sitemap):
    def items(self):
        return AboutUs.objects.all()

class ContactUsSitemap(Sitemap):
    def items(self):
        return ContactUs.objects.all()

class BookOrderSitemap(Sitemap):
    def items(self):
        return BookOrder.objects.all()

class UserMessageSitemap(Sitemap):
    def items(self):
        return UserMessage.objects.all()
