from django.shortcuts import render , get_object_or_404 , redirect
 
# Create your views here.

from .models import Chaussure
from .forms import ShoeForm

def all_shoes(request):
    all_shoes = Chaussure.objects.filter(active=True)
    context = {
        'all_shoes' : all_shoes, 
    }
    return render(request,'all_shoes.html',context)
 

def shoe(request, id):
    #shoe =  Chaussure.objects.get(id=id)
    shoe =  get_object_or_404(Chaussure,id=id)
    context ={
        'shoe' : shoe,
    }
    return render(request,'shoeDetail.html',context)

def shoe_on_demand(request):
    if(request.method == 'POST'):
        form = ShoeForm(request.POST,request.FILES)
        form.save()
    else:
        form = ShoeForm()
    context = {
        'form' : form ,
    }

    return render(request , 'shoe_on_demand.html', context)

def edit_shoe(request, id):
    shoe = get_object_or_404(Chaussure,id=id)
    if(request.method == 'POST'):
        form = ShoeForm(request.POST,request.FILES, instance=shoe)
        form.save()
        return redirect('/')
    else:
        form = ShoeForm(instance=shoe)
    context = {
        'form' : form ,
    }
    return render(request , 'edit.html', context)
    
