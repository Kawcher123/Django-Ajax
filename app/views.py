from django.shortcuts import render
from .forms import studentRegister
from .models import USer
from django.http import JsonResponse
# Create your views here.

def home(request):
    form=studentRegister()
    stud=USer.objects.all()
    return render(request,'templates/home.html',{'form':form,'stud':stud})

def save_data(request):
    if request.method=="POST":
        form=studentRegister(request.POST)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            usr=USer(name=name, email=email, password=password)
            usr.save()
            stud=USer.objects.values()
            student_data=list(stud)
            return JsonResponse({'status':'save','student_data':student_data})
        else:
            return JsonResponse({'status':0})


def delete_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        pi=USer.objects.get(pk=id)
        pi.delete()

        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})