from django.http import HttpResponse

def index(request):
    return HttpResponse("Sampson says Hello!")