from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# User model
class User(AbstractUser):
    USER_CHOICES_TYPE=((0,'OWNER'),(1,'BILLING'))
    STATUS_CHOICES_TYPE=((1,'ACTIVE'),(2,'INACTIVE'))
    username=models.CharField(max_length=150,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    user_type=models.IntegerField(choices=USER_CHOICES_TYPE,default=0)
    phone_number=models.IntegerField()
    address=models.TextField(max_length=200)
    status_id=models.IntegerField(choices=STATUS_CHOICES_TYPE,default=1)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username','phone_number']

    def __str__(self):
        return self.email