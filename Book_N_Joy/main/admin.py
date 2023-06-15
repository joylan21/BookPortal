from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Books)
admin.site.register(AboutUs)
admin.site.register(ContactUs)
admin.site.register(BookOrder)
admin.site.register(UserMessage)