from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AboutUs)
admin.site.register(ContactUs)
admin.site.register(UserMessage)

class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'email', 'contact_number', 'address')
admin.site.register(BookOrder, BookOrderAdmin)

class BooksAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'meta_title', 'meta_description')

admin.site.register(Books, BooksAdmin)