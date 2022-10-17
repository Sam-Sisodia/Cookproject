from importlib.metadata import files
from pyexpat import model
from rest_framework import  serializers

from .models import *


class  UserRegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model=UserRegister
        fields = ['id','name','address','phone_no','role']





class  CustomerRegisterSerilizer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model=CustomerRegister
        fields =['id','job','pincode','user']
        
    @staticmethod
    def get_user(obj):
        return UserRegisterSerilizer(obj.user).data

  
class  CookRegisterSerilizer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model=CookRegister
        fields ='__all__'

    @staticmethod
    def get_user(obj):
        return UserRegisterSerilizer(obj.user).data















'''
    user = serializers.SerializerMethodField()
    @staticmethod
    def get_user(obj):
        return UserRegisterSerilizer(obj.user).data

   # @staticmethod
    # def get_user(obj):
    #     return UserRegisterSerilizer(obj.user).data
'''