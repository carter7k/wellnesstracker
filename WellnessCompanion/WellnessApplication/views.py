from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def companionpage(request):
    return HttpResponse("This is the companion page")
def submitpage(request):
    return HttpResponse("This is the submit page")
def logpage(request):
    return HttpResponse("This is the log page")