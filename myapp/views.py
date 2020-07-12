from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        print(fname)
        print(email)
        s = Student(first_name=fname,email=email)
        s.save()
    return render(request, 'lol.html')

