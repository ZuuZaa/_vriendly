from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


from account.models import Account
from account.choices import STATUS_CHOICES


class RegistrationForm(UserCreationForm):
    
    status          = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'regDropDown'}))
    password1       = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2       = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())    
    
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'status','password1','password2')


class AccountAuthenticationForm(forms.ModelForm):
    password    = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = Account
        fields = ('email', 'password')
        
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class DateInput(forms.DateInput):
    input_type = 'date'

class AccountUpdate(forms.ModelForm):
    class Meta:
        model = Account
        widgets = {'date_of_birth' : DateInput()}
        fields = [
            'first_name',
            'last_name',
            'status',
            'date_of_birth'
        ]

