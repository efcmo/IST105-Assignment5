from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def clue(request):
    return HttpResponse("<h2>Clue #1:</h2><p>The treasure is hidden where knowledge grows.</p>")
