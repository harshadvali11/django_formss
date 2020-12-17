from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def StudentForm(request):
    form=Student()
    if request.method=="POST":
        form_data=Student(request.POST)
        if form_data.is_valid():
            #print(form_data.cleaned_data)
            #return HttpResponse(str(form_data.cleaned_data))
            name=form_data.cleaned_data['name']
            age=form_data.cleaned_data['age']
            address=form_data.cleaned_data['address']
            gender=form_data.cleaned_data['gender']
            course=form_data.cleaned_data['course']
            d={'name':name,'age':age,'address':address,'gender':gender,'course':course}
            return render(request,'student_formdata.html',context=d)
    return render(request,'student.html',context={'form':form})