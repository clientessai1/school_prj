from django.shortcuts import render

from django.shortcuts import HttpResponse;
# Create your views here.

def homeOld(request):
    return HttpResponse('<h2> Soyez les bienvenus  Soyez les bienvenus !!</h2>');
    pass

def home(request):
    return render(request, 'home.html');
    pass
