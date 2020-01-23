from django import forms
from .models import Visitor
from django.core import validators


class NewUserForm(forms.ModelForm):
    class Meta():
        model = Visitor
        fields = (
            'first_name', 'last_name', 'email', 'phone_number', 
            'address', 'city', 'referral', 'gender', 'household_number', 
            'household_income', 'dob', 'marital_status', 'veteran', 'disabled', 'race', 
            'purpose1', 'purpose2', 'purpose3', 'purpose4', 'purpose5', 'purpose6', 'purpose7', 'purpose8', 'purpose9'
        )

'''
class FirstTimeUserForm(forms.ModelForm):
    class Meta():
        model = Visitor
        fields = ('address', 'referral', 'gender')
'''