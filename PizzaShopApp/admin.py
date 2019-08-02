from django.contrib import admin
from .models import PizzaShop, Pizza, Client

admin.site.register(PizzaShop)
admin.site.register(Pizza)
admin.site.register(Client)