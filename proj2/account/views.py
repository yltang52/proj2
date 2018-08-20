from django.shortcuts import render

from account.models import User
from userProfile2.models import UserProfile2


def account(request):
    try:
        admin = User.objects.get(username='admin')
        UserProfile2.objects.create(user=admin, age=30)
        user = User.objects.get(username='user')
        UserProfile2.objects.create(user=user, age=20)
    except:
        admin = None

    return render(request,
                  'account/account.html',
                  {'users':User.objects.all()})
