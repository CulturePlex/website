from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Esta es la web del lab.")
