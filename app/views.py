from django.shortcuts import render
from .forms import studentRegister
from .models import USer
# Create your views here.

def home(request):
    form=studentRegister()
    stud=USer.objects.all()
    return render(request,'templates/home.html',{'form':form,'stud':stud})