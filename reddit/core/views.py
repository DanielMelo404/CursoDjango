from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Discusion
from .forms import FormularioDiscusion


def home(request):
    discusiones = Discusion.objects.all()
    context = {"conversaciones":discusiones}
    return render(request,'home.html',context)


def discusion(request,pk):

    discusion = Discusion.objects.get(id=pk)

    context ={'discusion_frontend': discusion}

    return render(request,'core/discusion.html',context)

def crear_discusion(request):
    context = {'form':FormularioDiscusion()}
    
    if request.method == "POST":
        form = FormularioDiscusion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'core/form_discusion.html',context)

def update_discusion(request,pk):
    discusion = Discusion.objects.get(id = pk)
    context = {"form": FormularioDiscusion(instance = discusion)}

    if request.method =="POST":
        form = FormularioDiscusion(request.POST, instance = discusion)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'core/form_discusion.html', context)

