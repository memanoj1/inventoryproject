from itertools import product
from operator import mod
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY=(
    ('Stationary','stationary'),
    ('Electronics','Electronics'),
    ('Food','Food'),
)
class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=20, choices=CATEGORY)
    quantity=models.PositiveIntegerField()
   # Price=models.PositiveIntegerField()
    class Meta:
        verbose_name_plural='Product'
    def __str__(self):
        return f'{self.name}--{self.quantity}'

class order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    staff=models.ForeignKey(User,models.CASCADE, null=True )
    Order_quantity=models.PositiveIntegerField(null=True)
    Datetime=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='Staff Order'
    def __str__(self):
        return f'{self.product} order by{self.staff.username}'
