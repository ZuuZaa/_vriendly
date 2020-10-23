from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.utils.safestring import mark_safe

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text, force_bytes
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string


from account.models import Account
from account.forms import (
				RegistrationForm, 
				AccountAuthenticationForm,
				AccountUpdate
)
#from .models import Verification


# Create your views here.
def register_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active =False
			user.save()
			current_site = get_current_site(request)
			domain = current_site.domain
			token = account_activation_token.make_token(user)
			link = f"https://vriendly.herokuapp.com/user/activate/{user.id}/{token}"
			messages.info(request, mark_safe(f"<p>Hi, {user.first_name}.</p><p>Activate your account from link, please.</p><p><a href={link}>{link}</a></p>"))
			return redirect('home')
		else:
			context['register_form'] = form
	else:
		form = RegistrationForm()
		context['register_form'] = form
	return render(request,'account/register.html', context)


def activate_view(request, uid, token):
    try:
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        user.save()
        login(request, user)
		# messages.info(request, f"{user.fist_name}, welcome.")
        return redirect('home')
    else:
        return render(request, 'activation_sent.html')


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

