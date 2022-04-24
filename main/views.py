from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group


def index(request):
    return render(request, 'main/index.html', {})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(reverse('main:cabinet_page', args=()))
        else:
            return redirect(reverse('main:login_page', args=()))
    return render(request, 'main/login.html', {})


def cabinet_view(request):
    if request.user.is_authenticated:
        accounts = models.Account.objects.all()
        return render(request, 'main/cabinet.html', {'accounts': accounts})
    else:
        return redirect(reverse('main:login_page', args=()))


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        group_id = request.POST.get('group')
        group = Group.objects.get(id=group_id)
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=firstname,
            last_name=lastname
        )
        user.set_password(password)
        user.groups.add(group)
        user.save()
        return redirect(reverse('main:login_page', args=()))
    groups = Group.objects.all()
    return render(request, 'main/register.html', {'groups': groups})

def logout_view(request):
    logout(request)
    return redirect(reverse('main:login_page', args=()))


def about_view(request):
    return render(request, 'main/about.html')



def account_detail(request, id):
    account = models.Account.objects.get(id=id)
    return render(request, "main/account_detail.html", {"account": account})


def account_create(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        release_date = request.POST.get("release_date")
        summa = request.POST.get("summa")
        currency = models.Currency.objects.get(id=request.POST.get("currency"))
        account = models.Account(
            first_name = first_name,
            last_name = last_name,
            release_date = release_date,
            summa = float(summa),
            currency = currency
        )
        account.save()
        return redirect(reverse('main:cabinet_page'))
    else:
        options = models.Currency.objects.all()
        return render(request, "main/account_create.html", {'options': options})
