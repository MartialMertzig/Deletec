from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue dans le système de gestion d'inventaire !")
