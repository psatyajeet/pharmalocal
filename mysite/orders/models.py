from django.db import models
from django.forms import ModelForm

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    medication = models.CharField(max_length=200)
    prescriber_name= models.CharField(max_length=200)
    prescriber_phone_number= models.CharField(max_length=12)
    paper=models.BooleanField('Paper prescription')

class OrderForm(ModelForm):
    class Meta:
        model = Order
