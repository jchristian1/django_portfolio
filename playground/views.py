from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def site_info(request):
    return render(request,'site_info.html')
def cyclist_project(request):
    return render(request, 'cyclistic.html')
def cyclist_project_intro(request):
    return render(request, 'cyclistic_intro.html')    
def sentimenter(request):
    return render(request, 'sentimenter.html')
def sentimenter_plain(request):
    return render(request, 'sentimenter_plain.html')
def spammer(request):
    return render(request, 'spammer.html')
def spammer_plain(request):
    return render(request, 'spammer_plain.html')
