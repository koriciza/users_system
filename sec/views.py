from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import SuperManagerUser,StudentUser,ParentUser,EmployeeUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['user_type'] = user.user_type
        token['email'] = user.email
        # ...

        if user.user_type == "superadmin":
            pass

        else:

            if user.user_type == "supermanager":

                school = SuperManagerUser.objects.get(user_ptr_id=user.id).school_id
                
                token['school'] = school

            if user.user_type == "employee":

                school = EmployeeUser.objects.get(user_ptr_id=user.id).school_id
                service = EmployeeUser.objects.get(user_ptr_id=user.id).employee_service
               
                token['school'] = school
                token['service'] = service


            if user.user_type == "student":
                school = StudentUser.objects.get(user_ptr_id=user.id).school_id
                grade_level = StudentUser.objects.get(user_ptr_id=user.id).grade_level
                section = StudentUser.objects.get(user_ptr_id=user.id).section
                
                token['school'] = school
                token['grade_level'] = grade_level
                token['section'] = section

          
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET','POST'])
def getRoutes (request):

    routes = [

           '/token',
           '/token/refresh',
           '/token/verify'

    ]

    return Response(routes)


