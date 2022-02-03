from django.db import models

# Create your models here.

class Category(models.Model):
    STATUS_CHOICES_TYPE=((1,'ACTIVE'),(2,'INACTIVE'))
    category_name=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)
    status_id=models.IntegerField(choices=STATUS_CHOICES_TYPE,default=1)

class Item(models.Model):
    STATUS_CHOICES_TYPE=((1,'ACTIVE'),(2,'INACTIVE'))
    category=models.ForeignKey(Category,on_delete=models.RESTRICT)
    item_name=models.CharField(max_length=150,null=False)
    price=models.IntegerField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    status_id=models.IntegerField(choices=STATUS_CHOICES_TYPE,default=1)

class Rack(models.Model):
    STATUS_CHOICES_TYPE=((1,'ACTIVE'),(2,'INACTIVE'))
    item=models.ForeignKey(Item,on_delete=models.RESTRICT)
    category=models.ForeignKey(Category,on_delete=models.RESTRICT)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    status_id=models.IntegerField(choices=STATUS_CHOICES_TYPE,default=1)