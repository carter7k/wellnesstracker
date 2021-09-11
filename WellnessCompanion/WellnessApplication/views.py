from django.shortcuts import render
from django.http import HttpResponse

from .models import Activity
# Create your views here.
def companionpage(request):
    latest_activity_category = Activity.objects.order_by('-date')[:50]
    count = {}
    for i in latest_activity_category:
        if i.activity_catergory not in count:
            count[i.activity_catergory] = 1
        else:
            count[i.activity_catergory] += 1


    output = sorted(count)[0]
    return HttpResponse(output)
def submitpage(request):
    return HttpResponse("This is the submit page")
def logpage(request):
    return HttpResponse("This is the log page")