from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Discusion


def home(request):
    discusiones = Discusion.objects.all()
    context = {"conversaciones":discusiones}
    return render(request,'home.html',context)


def discusion(request,pk):

    discusion = Discusion.objects.get(id=pk)

    context ={'discusion_frontend': discusion}

    return render(request,'core/discusion.html',context)