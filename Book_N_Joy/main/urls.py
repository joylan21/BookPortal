from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BooksSitemap, AboutUsSitemap, ContactUsSitemap, BookOrderSitemap, UserMessageSitemap
from django.views.generic import TemplateView

sitemaps = {
    'books': BooksSitemap,
    'about_us': AboutUsSitemap,
    'contact_us': ContactUsSitemap,
    'book_order': BookOrderSitemap,
    'user_message': UserMessageSitemap,
}

urlpatterns = [
    path('',home,name='home'),
    path('aboutUs',AboutUs,name='aboutUs'),
    path('contactUs',ContactUs,name='contactUs'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]