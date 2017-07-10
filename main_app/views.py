from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Drink
from .forms import DrinkForm
from .models import Journal
from .forms import JournalForm

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
	return render(request, 'journal-show.html', {'drink': drink})

def post_journal(request):
    form = JournalForm(request.POST)
    if form.is_valid():
        journal = form.save(commit = True)
        journal.save()
    return HttpResponseRedirect('/journal')
