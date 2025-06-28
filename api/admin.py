from django.contrib import admin

from django.contrib import admin
from .models import Account
from .models import Product

admin.site.register(Account)
admin.site.register(Product)
