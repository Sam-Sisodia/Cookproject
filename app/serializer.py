from importlib.metadata import files
from pyexpat import model
from rest_framework import  serializers

from .models import *


class  UserRegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model=UserRegister
        fields = "__all__"




class  CustomerRegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CustomerRegister
        fields = "__all__"


class  CookRegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CookRegister
        fields = "__all__"