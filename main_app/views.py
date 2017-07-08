from django.shortcuts import render
from .models import Treasure

def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})

def show(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request, 'show.html', {'treasure': treasure}) 
