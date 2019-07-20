from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email



class cust_reg_form(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter username:'}
    ), required=True, max_length=50)
    
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Enter your email:'}
    ), required=True, max_length=50)
    
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter your first name:'}
    ), required=True, max_length=50)
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter your last name:'}
    ), required=True, max_length=50)
    
    # dob = forms.DateField(widget=forms.DateInput(
    #     attrs={'class':'form-control','placeholder':'Enter your birthday:'}
    # ), required=True,)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter your password:'}
    ), required=True, max_length=50)
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Confirm your password:'}
    ), required=True, max_length=50)

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    
    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = User.objects.get(username = user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already exists.")


    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = validate_email(email)
        except:
            return forms.ValidationError("Please enter a valid email.")
        return email

    
    def clean_confirm_password(self):
        psk = self.cleaned_data['password']
        cpsk = self.cleaned_data['confirm_password']
        if psk and cpsk:
            if psk!=cpsk:
                raise forms.ValidationError("Passwords don't match.")
            else:
                if len(psk) < 8:
                    raise forms.ValidationError("Passwords should contain at least 8 characters.")
                if psk.isdigit():
                    raise forms.ValidationError("Passwords should not be all numeric.")
