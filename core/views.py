from django.shortcuts import render
from account.models import Account
from core.forms import SearchUserForm

# Create your views here.
def home(request):
    context = {}
    if request.POST:
        form = SearchUserForm(request.POST)
        if form.is_valid():
            search_term = request.POST.get('search_user')
            users_query = Account.objects.all().filter(email__icontains=search_term)
            context['users'] = users_query
    else:
        form = SearchUserForm()  
    context['search_user_form'] = form
    context['count'] = Account.objects.count()
    return render(request, 'core/index.html', context)
