from django import forms
from .models import Order,CustomUser
from django.contrib.auth.forms import UserCreationForm
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'phone', 'food', 'item', 'price']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control right'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control right'}),
            'food': forms.Select(attrs={'class': 'form-control right'}),
            'item': forms.TextInput(attrs={'class': 'form-control right'}),
            'price': forms.NumberInput(attrs={'class': 'form-control right'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'mobile','address')