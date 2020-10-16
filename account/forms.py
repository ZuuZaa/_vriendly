from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate

from account.models import Account
from account.choices import STATUS_CHOICES


class RegistrationForm(forms.ModelForm):
    
    status          = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'regDropDown'}))
    password1       = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2       = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())    
    
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'status')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

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
            'email',
            'status',
            'date_of_birth'
        ]
        

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'status','date_of_birth', 'is_staff', 'is_superuser')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'status', 'date_of_birth', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
