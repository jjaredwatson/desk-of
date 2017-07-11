from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Drink, Journal, Ipod
from .forms import DrinkForm, JournalForm, IpodForm



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
        drink = form.save(commit = True)
        drink.save()
    return HttpResponseRedirect('/drinks')

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
        journal = form.save(commit = True)
        journal.save()
    return HttpResponseRedirect('/journal')

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
        ipod = form.save(commit = True)
        ipod.save()
    return HttpResponseRedirect('/ipod')
