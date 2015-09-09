from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello in polls")


# Create your views here.
