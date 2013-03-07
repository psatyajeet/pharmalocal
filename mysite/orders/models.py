from django.db import models
from django.forms import ModelForm
from django import forms

class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    order_date = models.CharField(max_length=200)
    birth_date = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    medication = models.CharField(max_length=200)
    prescriber_name= models.CharField(max_length=200)
    prescriber_phone_number= models.CharField(max_length=12)
    paper=models.BooleanField('Paper prescription')
    zipcode=models.CharField(max_length=200)

class OrderForm(ModelForm):
    fullname = forms.CharField(label = "Full name")
    
    class Meta:
        model = Order
        fields = ("fullname", "email", "order_date", "birth_date", "phone_number", "medication", "prescriber_name", "prescriber_phone_number", "zipcode", "paper")
        
    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)
        first_name, last_name = (self.cleaned_data["fullname"].split()[0], self.cleaned_data["fullname"].split()[-1])
        order.first_name = first_name
        order.last_name = last_name
        order.email = self.cleaned_data["email"]
        if commit:
            order.save()
        return order     
