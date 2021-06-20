from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    #data_atual = date.today()
    #return HttpResponse(data_atual)
    return render(request, "index.html")

def page2(request):

    return render(request, "page2.html")

def page3(request):
    return render(request, "page3.html")

def page4(request):
    return render(request, "page4.html")

def page5(request):
    horario = str(datetime.now().strftime("%x %X"))
    return render(request, "page5.html", {"horario": horario})