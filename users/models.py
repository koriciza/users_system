from django.db import models

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.urls import reverse
from school.models import School
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from django.contrib.auth.models import AbstractUser
from django.db import models

import random
import string


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('superadmin', 'Superadmin'),
        ('supermanager', 'Supermanager'),
        ('employee', 'Employee'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only hash the password for new user instances
            self.set_password(self.password)
        super().save(*args, **kwargs)
   
    
class SuperAdminUser(User):

    
    userIdentity = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=20, unique=True)


    def __init__(self, *args, **kwargs):
        if not args:
             kwargs.update({"is_staff": True})
             kwargs.update({"is_superuser": True})
             kwargs.update({"user_type": "superadmin"})
        super(SuperAdminUser, self).__init__(*args, **kwargs)

    
class SuperManagerUser(User):

    userIdentity = models.CharField(max_length=12)
    profile_photo = models.ImageField(upload_to='supermanager_imgs/',null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    school = models.OneToOneField(School, on_delete=models.CASCADE, unique=False) 
    is_otp_verified = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)


    def __init__(self, *args, **kwargs):
        if not args:
             kwargs.update({"is_staff": True})
             kwargs.update({"user_type": "supermanager"})
        super(SuperManagerUser, self).__init__(*args, **kwargs)


class StudentUser(User):
    # Additional fields for student user
    userIdentity = models.CharField(max_length=12)
    profile_photo = models.ImageField(upload_to='student_imgs/',null=True)

    father_name =  models.CharField(max_length=50, null=True, default="-")
    mother_name =  models.CharField(max_length=50, null = True, default="-")
    addresse =  models.CharField(max_length=50, null = True, default="-")

    student_phone =   models.CharField(max_length=12, null = True,default="-")
    mother_phone =   models.CharField(max_length=12, null = True,default="-")
    father_phone =   models.CharField(max_length=12, null = True,default="-")

    school = models.ForeignKey(School, on_delete=models.CASCADE) 
    matricule = models.CharField(max_length=10)
    grade_level = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    
    def __init__(self, *args, **kwargs):
        if not args:
             kwargs.update({"user_type": "student"})
        super(StudentUser, self).__init__(*args, **kwargs)


class ParentUser(User):
    # Additional fields for student user
    userIdentity = models.CharField(max_length=12)
    profile_photo = models.ImageField(upload_to='parent_imgs/',null=True)
    profession =  models.CharField(max_length=50, null = True, default="-")
    addresse =  models.CharField(max_length=50, null = True, default="-")
    parent_phone_number1 =   models.CharField(max_length=50, null = True, default="-")
    parent_phone_number2 =   models.CharField(max_length=50, null = True, default="-")


    def __init__(self, *args, **kwargs):
        if not args:
             kwargs.update({"user_type": "parent"})
        super(ParentUser, self).__init__(*args, **kwargs)     


class EmployeeUser(User):
    # Additional fields for student user
    SERVICE_TYPE_CHOICES = (
        ('LIBRARY', 'Library'),
        ('FINANCE', 'Finance'),
        ('DISCIPLINE', 'Discipline'),
        ('TEACHER', 'Teacher'),
        ('SECRETAIRE', 'Secretaire'),
    )

    employee_service = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    userIdentity = models.CharField(max_length=12)
    matricule = models.CharField(max_length=10)
    profile_photo = models.ImageField(upload_to='employee_imgs/',null=True)
    addresse =  models.CharField(max_length=50, null = True, default="-")
    phone_number1 =   models.CharField(max_length=50, null = True, default="-")
    phone_number2 =   models.CharField(max_length=50, null = True, default="-")
    school = models.ForeignKey(School, on_delete=models.CASCADE) 
    course = models.TextField(null = True, default="-")
    years_of_exeprience = models.CharField(max_length=2, default="-")
   

    
    def __init__(self, *args, **kwargs):
        if not args:
             kwargs.update({"user_type": "employee"})
        super(EmployeeUser, self).__init__(*args, **kwargs)


# ######################## SIGNALS TO ASSIGN RANDOM USER_IDENTITY ##################################

def generate_random_id(length=12):
    characters = string.ascii_letters + string.digits  # All letters (lowercase and uppercase) and digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id

# supermanageruser  

def set_user_identity_to_supermanager(sender, instance,created,**kwargs):
   
    if created:
        instance.userIdentity =generate_random_id()
        instance.save()
        post_save.disconnect(set_user_identity_to_supermanager,sender=SuperManagerUser)   

post_save.connect(set_user_identity_to_supermanager,sender=SuperManagerUser)


# superadminuser  

def set_user_identity_to_superadmin(sender, instance,created,**kwargs):

 
    if created:
        instance.userIdentity =generate_random_id()
        instance.save()
        post_save.disconnect(set_user_identity_to_superadmin,sender=SuperAdminUser)   

post_save.connect(set_user_identity_to_superadmin,sender=SuperAdminUser)


# student 

def set_user_identity_to_student(sender, instance,created,**kwargs):
   
    if created:
        instance.userIdentity =generate_random_id()
        instance.save()
        post_save.disconnect(set_user_identity_to_student,sender=StudentUser)   

post_save.connect(set_user_identity_to_student,sender=StudentUser)


# parent

def set_user_identity_to_parent(sender, instance,created,**kwargs):
   
    if created:
        instance.userIdentity =generate_random_id()
        instance.save()
        post_save.disconnect(set_user_identity_to_parent,sender=ParentUser)   

post_save.connect(set_user_identity_to_parent,sender=ParentUser)


# employee

def set_user_identity_to_employee(sender, instance,created,**kwargs):
   
    if created:
        instance.userIdentity =generate_random_id()
        instance.save()
        post_save.disconnect(set_user_identity_to_employee,sender=EmployeeUser)   

post_save.connect(set_user_identity_to_employee,sender=EmployeeUser)


