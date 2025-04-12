from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Discusion, Topico
from .forms import FormularioDiscusion
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def home(request):
    discusiones = Discusion.objects.all()
    topicos = Topico.objects.all()

    context = {"conversaciones":discusiones, "topics":topicos}
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

def registrar(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"Error al registrar")

    context = {"form":form}
    return render(request, 'core/login_registro.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "El usuario no existe")

        user = authenticate(request,username=username,password=password)

        try:
            login(request,user)
            return redirect('home')
        except:
            messages.error(request, "El usuario o la contraseña estan mal")
    return render(request,'core/login_registro.html',{"page":"login"})




































