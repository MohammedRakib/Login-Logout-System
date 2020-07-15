from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Student


def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        print(fname)
        print(email)
        s = Student(first_name=fname, email=email)
        s.save()
    return render(request, 'lol.html')


@login_required()
def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request,'base.html')

