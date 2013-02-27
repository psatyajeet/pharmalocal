from django import forms
from orders.models import Order

class OrderCreateForm(forms.Form):
    fullname = forms.CharField(label = "Full name")
    email = forms.EmailField(label = "Email")
    
    class Meta:
        model = Order
        fields = ("fullname", "email", "order date", "date of birth", "phone number", "medication", "prescriber name", "prescriber phone number", "paper")

    def save(self, commit=True):
        order = super(OrderCreateForm, self).save(commit=False)
        first_name, last_name = self.cleaned_data["fullname"].split()
        order.first_name = first_name
        order.last_name = last_name
        order.email = self.cleaned_data["email"]
        if commit:
            order.save()
        return order
        
        
