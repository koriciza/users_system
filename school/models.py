from django.db import models

# Create your models here.


class School(models.Model):   

    name=models.CharField(max_length=50) 
    logo = models.ImageField(upload_to='school_imgs/',null=True)
    addresse = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
       
       return self.name
  
