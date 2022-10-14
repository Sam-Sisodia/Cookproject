from tokenize import Name
from unicodedata import name
from urllib import response
from django.shortcuts import render

# Create your views here.


from . serializer import *
from  . models import *
from  rest_framework.viewsets import  ModelViewSet

from rest_framework import status
from rest_framework.response  import Response




class UserRegisterDetails(ModelViewSet):
    queryset = ""
    serializer_class = UserRegisterSerilizer

    def list(self, request):
        queryset = UserRegister.objects.all()
        serializer = UserRegisterSerilizer(queryset, many=True)
        return Response(serializer.data)



    def create(self, request, *args, **kwargs):
        serializer= UserRegisterSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "msb blablabla"} )

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class CustomerRegisterDetails(ModelViewSet):
    queryset = ""
    serializer_class = CustomerRegisterSerilizer
    def list(self, request):
        queryset = CustomerRegister.objects.all()
        serializer = CustomerRegisterSerilizer(queryset, many=True)
        return Response(serializer.data)



class CookRegisterDetails(ModelViewSet):
    queryset = ""
    serializer_class = CookRegisterSerilizer













#static method 











































































































































#,data=serializer.data, status=status.HTTP_201_CREATED,


''' name = serializer.validated_data['name']
            # address = serializer.validated_data['address']
            # address = serializer.validated_data['address']
            
            # role = serializer.validated_data['role']

            # if role == "Customer":
            #     CustomerRegister.objects.create(name=name,address=address)
            # elif  role == "Cook":
            #      CookRegister.objects.create(name=name,address=address)'''


















'''
class UserRegisterDetails(ModelViewSet):
    queryset = ""
    serializer_class = UserRegisterSerilizer
    http_method_names = ['post', ]
    def create(self, request, *args, **kwargs):
        serializer= UserRegisterSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "msb blablabla"} )

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class CustomerRegisterDetails(ModelViewSet):
    queryset = ""
    serializer_class = CustomerRegisterSerilizer



class CookRegisterDetails(ModelViewSet):
    queryset = ""
    serializer_class = CookRegisterSerilizer




'''