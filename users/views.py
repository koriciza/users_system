from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from django.core import serializers
from urllib.parse import quote

from .models import (

        SuperManagerUser,
        SuperAdminUser,
        StudentUser, 
        ParentUser,
        EmployeeUser,
        User
        
        )

from .serializers import (
        SuperManagerUserSerializer, 
        SuperAdminUserSerializer,
        StudentUserSerializer,
        ParentUserSerializer,
        EmployeeUserSerializer
        
        )


class SuperAdminUserViewSet(viewsets.ModelViewSet):
    queryset = SuperAdminUser.objects.all()
    serializer_class = SuperAdminUserSerializer

class SuperManagerUserViewSet(viewsets.ModelViewSet):
    queryset = SuperManagerUser.objects.all()
    serializer_class = SuperManagerUserSerializer

   

class StudentUserViewSet(viewsets.ModelViewSet):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserSerializer    


class ParentUserViewSet(viewsets.ModelViewSet):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserSerializer        


class EmployeeUserViewSet(viewsets.ModelViewSet):
    queryset = EmployeeUser.objects.all()
    serializer_class = EmployeeUserSerializer            


class SchoolEmployeesViewSet(viewsets.ViewSet):

    def  school_employee_list(self, request, school):
        queryset = EmployeeUser.objects.filter(school=school)
        serializer = EmployeeUserSerializer(queryset, many=True)
       
        return Response(serializer.data)
        

class UserCheckingViewSet(viewsets.ViewSet):

    def  checkUsername(self, request, username):

        if User.objects.filter(username=username):
              return JsonResponse({'bool':False, 'msg':'Your username  is taken.'}) 
        
    def  checkUserEmail(self, request, email):  

        if User.objects.filter(email=email):
              return JsonResponse({'bool':False, 'msg':'Your email  is taken.'}) 
       
    def  checkSuperManagerUserPhone(self, request, phone_number):  

        if SuperManagerUser.objects.filter(phone_number=quote(phone_number)):
              return JsonResponse({'bool':False, 'msg':'Your phone number  is taken.'})    
        
                