from django.contrib import admin
from .models import Cart, Cart_item
# Register your models here.
admin.site.register(Cart_item)
admin.site.register(Cart)