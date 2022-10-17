from django.contrib import admin

# Register your models here.
from . models import *


admin.site.register(UserRegister)

admin.site.register(CustomerRegister)

admin.site.register(CookRegister)