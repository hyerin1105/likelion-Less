from django.contrib import admin
from .models import Product, Client, Event
# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Event)