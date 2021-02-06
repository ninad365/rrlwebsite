from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return(render(request,'home.html'))

def bio(request):
    return(render(request,'biography.html'))

def mypage(request):
    return(render(request,'biography.html'))

def courses(request):
    return(render(request,'courses.html'))

def publications(request):
    return(render(request,'publications.html'))

def research(request):
    return(render(request,'research.html'))

def students(request):
    return(render(request,'students.html'))