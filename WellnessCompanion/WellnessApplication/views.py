from django.shortcuts import render
from django.http import HttpResponse

from .models import Activity
# Create your views here.
def companionpage(request):
    latest_activity_category = Activity.objects.order_by('-date')[:5]
    #output = latest_activity_category#.activity_catergory
    output = ', '.join([q.activity_catergory for q in latest_activity_category])
    return HttpResponse(output)
def submitpage(request):
    return HttpResponse("This is the submit page")
def logpage(request):
    return HttpResponse("This is the log page")