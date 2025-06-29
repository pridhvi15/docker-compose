from django.shortcuts import render,redirect
from django.views.generic import View
from project.models import *
from project.forms import *

# Create your views here.

class Task_view_create(View):

    def get(self,request):

        form = TaskForm

        return render(request,"create.html",{"form":form})
    
    def post(self,request):

        form = TaskForm(request.POST)

        if form.is_valid():

            Task.objects.create(**form.cleaned_data)

            return redirect("list")

        else:

            return render(request,"create.html",{"form":form})
        
class Task_view(View):

    def get(self,request):

        data = Task.objects.all()

        return render(request,"list.html",{"data":data})


