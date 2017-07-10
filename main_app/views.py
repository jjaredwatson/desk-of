from django.shortcuts import render
from .models import Drink
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DrinkForm

def index(request):
    drinks = Drink.objects.all()
    form = DrinkForm()
    return render(request, 'drink-index.html', {'drinks':drinks, 'form':form})

def show(request, drink_id):
	drink = Drink.objects.get(id=drink_id)
	return render(request, 'drink-show.html', {'drink': drink})

def post_drink(request):
    form = DrinkForm(request.POST)
    if form.is_valid():
        drink = form.save(commit = True)
        drink.save()
    return HttpResponseRedirect('/')
