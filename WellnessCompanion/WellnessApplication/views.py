from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Activity
from django.template import loader


# Create your views here.
def companionpage(request):
    return HttpResponse("This is the companion page")
def submitpage(request):
    return HttpResponse("This is the submit page")
def logpage(request):
    activities = Activity.objects.order_by('-date')
    template = loader.get_template('WellnessApplication/logs.html')
    context = {
        'activities': activities,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("This is the log page")