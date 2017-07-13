from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Drink, Journal, Ipod
from .forms import DrinkForm, JournalForm, IpodForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'desk.html', {'username': username})

def desk(request):
    return render(request, 'desk.html')

def index_drink(request):
    drinks = Drink.objects.all()
    form = DrinkForm()
    return render(request, 'drink-index.html', {'drinks':drinks, 'form':form})

def show_drink(request, drink_id):
	drink = Drink.objects.get(id=drink_id)
	return render(request, 'drink-show.html', {'drink': drink})

def post_drink(request):
    form = DrinkForm(request.POST)
    if form.is_valid():
        drink = form.save(commit = False)
        drink.user = request.user
        drink.save()
    return HttpResponseRedirect('/drinks')

def delete_drink(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    drink.delete()
    return redirect('/drinks')

def index_journal(request):
    journals = Journal.objects.all()
    form = JournalForm()
    return render(request, 'journal-index.html', {'journals':journals, 'form':form})

def show_journal(request, journal_id):
	journal = Journal.objects.get(id=journal_id)
	return render(request, 'journal-show.html', {'journal': journal})

def post_journal(request):
    form = JournalForm(request.POST)
    if form.is_valid():
        journal = form.save(commit = False)
        journal.user = request.user
        journal.save()
    return HttpResponseRedirect('/journal')

def delete_journal(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    journal.delete()
    return redirect('/journal')

def index_ipod(request):
    ipods = Ipod.objects.all()
    form = IpodForm()
    return render(request, 'ipod-index.html', {'ipods':ipods, 'form':form})

def show_ipod(request, ipod_id):
	ipod = Ipod.objects.get(id=ipod_id)
	return render(request, 'ipod-show.html', {'ipod': ipod})

def post_ipod(request):
    form = IpodForm(request.POST)
    if form.is_valid():
        ipod = form.save(commit = False)
        ipod.user = request.user
        ipod.save()
    return HttpResponseRedirect('/ipod')

def delete_ipod(request, pk):
    ipod = get_object_or_404(Ipod, pk=pk)
    ipod.delete()
    return redirect('/ipod')

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/login')
    else:
        form = LoginForm()
        return render(request, 'landing.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
