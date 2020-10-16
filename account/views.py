from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from account.forms import (
				RegistrationForm, 
				AccountAuthenticationForm,
				AccountUpdate
)

# Create your views here.
def register_view(request):

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['register_form'] = form
    else:
        form = RegistrationForm()
        context['register_form'] = form
    return render(request,'account/register.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')

def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "account/login.html", context)
    
def profile_view(request):

	if not request.user.is_authenticated:
		return redirect("login")

	else:
		user = request.user
		context = {'user':user}
		return render(request, 'account/profile.html', context)


def profile_edit_view(request):

	if not request.user.is_authenticated:
		return redirect("login")
	context = {}
	if request.POST:
		form = AccountUpdate(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.info(request, f'{request.user.first_name} {request.user.last_name}, your info sucsessfully edited.')
			return redirect('profile')
	else:
		form = AccountUpdate(instance=request.user)
	context['profile_edit_form'] = form
	context['user'] = request.user
	return render(request, 'account/profile_edit.html', context)

