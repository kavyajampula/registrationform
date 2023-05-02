from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            NSUO.set_Password['password']
            NSUO.save()
            NSPO=pfd.save()
            NSPO.username=NSUO
            NSPO.save()
            return HttpResponse('Registration is successfull')
        else:
            return HttpResponse('Not valid')
    return render(request,'registration.html',d)



