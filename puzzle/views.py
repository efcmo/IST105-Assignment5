from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the Interactive Treasure Hunt!</h1><p>Find the clues and unlock the secret!</p>")
