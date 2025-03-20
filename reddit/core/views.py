from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

discusiones = [
    {"id":1,"titulo":"mañana sera dia civico?"},
    {"id":2,"titulo":"que es mejor marvel o dragon ball"}
]

def home(request):
    context = {"conversaciones":discusiones}
    return render(request,'home.html',context)


def discusion(request,pk):
    for discusion_i in discusiones:
        if discusion_i['id'] == int(pk):
            context ={'discusion_frontend': discusion_i}

    return render(request,'core/discusion.html',context)