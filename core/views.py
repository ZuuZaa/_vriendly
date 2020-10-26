from django.shortcuts import render
from account.models import Account

# Create your views here.
def home(request):
    context = {}
    context['count'] = Account.objects.count()
    return render(request, 'core/index.html', context)