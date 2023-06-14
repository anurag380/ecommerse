from typing import Any, Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, unique=True)
    email=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=15)
    phno=models.CharField(max_length=10 , unique=True)

    def __str__(self):
        return self.name

    def save(self):
        if self.user is None:
            user = User.objects.create_user(username=self.name, email=self.email, password=self.password)
            self.user = user
        super().save()
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phno=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    image=models.ImageField(upload_to='media/images')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending','Pending'),
        ('Ordered','Ordered')
    )
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.FloatField(blank=True,default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_items(self):
        orderitems = self.orderline_set.all()
        count = orderitems.count()
        return count  

  
class Orderline(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField(default=0)
    total = models.FloatField(default=0)
    is_order = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)


    