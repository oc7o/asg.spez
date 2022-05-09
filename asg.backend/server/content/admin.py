from django.contrib import admin

from .models import Category, Document, Image, Page

admin.site.register(Image)
admin.site.register(Document)
admin.site.register(Category)
admin.site.register(Page)
