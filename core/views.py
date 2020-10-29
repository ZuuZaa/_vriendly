from django.shortcuts import render
from django.contrib import messages
from django_ip_geolocation.decorators import with_ip_geolocation

from account.models import Account
from core.forms import SearchUserForm


@with_ip_geolocation
def home(request):
    context = {}


# proceed with city
    #user_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
    if request.POST:
        form = SearchUserForm(request.POST)
        if form.is_valid():
            search_term = request.POST.get('search_user')
            users_query = Account.objects.all().filter(email__icontains=search_term)
            if users_query:
                context['users'] = users_query
            else:
                messages.info(request, 'user is not found')
    else:
        form = SearchUserForm()  
    context['search_user_form'] = form
    context['count'] = Account.objects.count()
    context['location'] = request.geolocation
    
    return render(request, 'core/index.html', context)
