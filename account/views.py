from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.utils.safestring import mark_safe

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text, force_bytes
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from account.models import Account
from account.forms import (
				RegistrationForm, 
				AccountAuthenticationForm,
				AccountUpdate
)

# --------------- REGISTER ------------
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
			# if settings.DEBUG:
			# 	link = f"localhost:8000/user/activate/{user.id}/{token}"
			# else:
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


# --------------- LOG IN, LOG OUT ------------
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


# --------------- PASSWORD CHANGE ------------
def password_reset_view(request):
	if request.method == "POST":
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			try:
				user = Account.objects.filter(email=email).last()
			except (TypeError, ValueError, OverflowError, user.DoesNotExist):
				user = None
			if user is not None:
				token = account_activation_token.make_token(user)
				# if settings.DEBUG:
				# 	link = f"localhost:8000/user/password/{user.id}/{token}"
				# else:
				link = f"https://vriendly.herokuapp.com/user/password/{user.id}/{token}"
				messages.info(request, mark_safe(f"<p>Hi, {user.first_name}.</p><p>Reset your password from link below, please.</p><p><a href={link}>{link}</a></p>"))
					# subject = "Password Reset Requested"
					# email_template_name = "main/password/password_reset_email.txt"
					# c = {
					# "email":user.email,
					# 'domain':'127.0.0.1:8000',
					# 'site_name': 'Website',
					# "uid": urlsafe_base64_encode(force_bytes(user.pk)),
					# "user": user,
					# 'token': default_token_generator.make_token(user),
					# 'protocol': 'http',
					# }
					# email = render_to_string(email_template_name, c)
					# try:
					# 	send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					# except BadHeaderError:
					# 	return HttpResponse('Invalid header found.')
				return redirect ("password_reset_done")
	else:
		form = PasswordResetForm()
	return render(request, 'account/password_reset.html', {'password_reset_form': form})

def password_reset_done_view(request):
	return render(request, 'account/password_reset_done.html')

def password_confirm_view(request, uid, token):
	try:
		user = Account.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, user.DoesNotExist):
		user = None
	context = {}
    # checking if the user exists, if the token is valid.
	if user is not None and account_activation_token.check_token(user, token):
		if request.method == 'POST':
			form = SetPasswordForm(request.user, request.POST)
			if form.is_valid():
				new_password = form.cleaned_data['new_password1']
				user.set_password(new_password)
				user.save()
				login(request, user) 
				messages.success(request, f'{user.first_name}, your password was successfully updated!')
				return redirect('home')
			else:
				messages.error(request, 'Please correct the error below.')
		else:
			form = SetPasswordForm(request.user)
		context['password_confirm_form'] = form
	return render(request, 'account/password_reset_confirm.html', context)

def password_reset_complete_view(request):
	return render(request, 'account/password_reset_complete.html')


# --------------- PROFILE ------------
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

