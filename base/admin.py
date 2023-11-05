from django.contrib import admin
from .models import Food,Pay,CustomUser,Order
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Order)


