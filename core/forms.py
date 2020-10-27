from django import forms

class SearchUserForm(forms.Form):
    search_user = forms.CharField(max_length=150)