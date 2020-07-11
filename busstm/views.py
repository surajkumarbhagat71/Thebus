from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

def home(r):

    return render(r,'main/home.html')

############################################ For User   ######################################


def user_signup(r):
    form = UserSingupForm(r.POST or None , r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(home)

    data = {"userform":form}
    return render(r,'main/usersignup.html',data)

def user_login(r):
    if r.method == "POST":
        username = r.POST.get('email')
        password = r.POST.get('password')
        cond = Q(user_email = username) & Q(password = password)

        cheak = UserSingup.objects.filter(cond).count()

        if (cheak > 0 ):
            r.session["user_login"] = username
            return redirect(user_profile)
        else:
            return redirect(user_login)

    return render(r,'main/userlogin.html')


def user_booking(r):
    if not r.session.has_key("user_login"):
        return redirect(user_login)

    data = {"bus":Bus.objects.all()}
    return render(r,'user/my_booking.html',data)

def user_profile(r):
    if not r.session.has_key('user_login'):
        return redirect(user_login)

    log = r.session["user_login"]
    data = {"user":UserSingup.objects.get(user_email=log)}
    return render(r,'user/profile.html',data)

def tikat_book(r):

    return render(r,'user/titak_book.html')


def logout(r):
    if r.session.has_key("user_login"):
        del r.session["user_login"]
        return redirect(home)

    return render(r,'main/home.html')



###################################  Oner ##############################################

def oner_signup(r):
    form = OnerSignUpForm(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(home)

    data = {"onerform": form}
    return render(r, 'main/onersignup.html',data)


def oner_login(r):
    if r.method == "POST":
        email = r.POST.get('email')
        password = r.POST.get('password')

        cond = Q(email = email) & Q(password = password)

        cheak = OnerSignup.objects.filter(cond).count()

        if (cheak > 0 ):
            r.session['oner_login'] = email
            return redirect(dashaboard)
        else:
            return redirect(oner_login)
    return render(r,'main/onerlogin.html')


def dashaboard(r):

    return render(r,'bus_oner/dashaboard.html')


def all_booking(r):

    return render(r,'bus_oner/booking.html')

def oner_profile(r):
    if not r.session.has_key('oner_login'):
        return redirect(oner_login)

    log = r.session['oner_login']
    data = {"oner":OnerSignup.objects.get(email = log)}

    return render(r,'bus_oner/profile.html',data)

def add_bus(r):
    if not r.session.has_key('oner_login'):
        return redirect(oner_login)

    form = Busform(r.POST or None )
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(dashaboard)
    return render(r,'bus_oner/add_bus.html',{"busform":form})


def oner_logout(r):
    if r.session.has_key('oner_login'):
        del r.session['oner_login']
        return redirect(home)


