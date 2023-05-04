from django.shortcuts import render
from . models import Place
from . models import Person

# Create your views here.
def home(request):
    obj = Place.objects.all()
    obje = Person.objects.all()
    return render(request,'index.html',{'res':obj,'result':obje})


