from django.shortcuts import render, redirect

from .form import MovieForm
from . models import Load

# Create your views here.
def movief(request):
    task1 = Load.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        description=request.POST['description']
        year=request.POST['year']
        img=request.FILES['img']
        a=Load(name=name,description=description,year=year,img=img)
        a.save()
    return render(request, 'task.html', {'task1': task1})

def delete(request,task_id):
    task1= Load.objects.get(id=task_id)
    if request.method =="POST":
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Load.objects.get(id=id)
    f=MovieForm(request.POST or None,request.FILES, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})


