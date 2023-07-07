from rest_framework import serializers
from .models import (

        User,
        SuperManagerUser, 
        SuperAdminUser,
        StudentUser,
        ParentUser, 
        EmployeeUser
        
        )


class SuperAdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperAdminUser
        fields = ('id', 'first_name','last_name','username', 'email', 'password', 'phone_number', 'is_superuser','userIdentity')
        extra_kwargs = {'password': {'write_only': True},'userIdentity':{'read_only':True},'is_superuser':{'read_only':True}}
        # depth = 1

class SuperManagerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperManagerUser
        fields = ('id', 'first_name','last_name', 'username', 'email', 'password', 'phone_number' , 'userIdentity','profile_photo','school','is_otp_verified','is_activated','is_superuser','is_staff')
        extra_kwargs = {'password': {'write_only': True},'is_superuser':{'read_only':True},'is_staff':{'read_only':True},'userIdentity':{'read_only':True} }
        # depth = 1


class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ('id', 'first_name','last_name','username', 'email', 'password','father_name','mother_name','addresse','mother_phone','father_phone','student_phone', 'userIdentity', 'school', 'grade_level','section')
        extra_kwargs = {'password': {'write_only': True},'userIdentity':{'read_only':True}}



class ParentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentUser
        fields = ('id' ,'profile_photo',  'first_name','last_name','username', 'email', 'password','profession','addresse','parent_phone_number1','parent_phone_number2', 'userIdentity')
        extra_kwargs = {'password': {'write_only': True},'userIdentity':{'read_only':True}}


class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ('id', 'profile_photo', 'first_name','last_name','username', 'email', 'employee_service', 'password','addresse','phone_number1','phone_number2', 'userIdentity', 'school', 'employee_service', 'course', 'years_of_exeprience')
        extra_kwargs = {'password': {'write_only': True},'userIdentity':{'read_only':True}}












