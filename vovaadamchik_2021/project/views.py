from django.shortcuts import render

def project(request):
    return render(request,'project.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')