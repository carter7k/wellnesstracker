from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Activity
from django.template import loader


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
    least_done = ''
    lowest_count = 51
    for i in count:
        if count[i] < lowest_count:
            least_done = i
            lowest_count = count[i]



    output = least_done
    return HttpResponse(output)
def submitpage(request):
    return HttpResponse("This is the submit page")
def logpage(request):
    # user = User.objects.get(name = "Brian")
    # activities = Activity.objects.filter(personID = user.UUID)
    activities = Activity.objects.all()
    template = loader.get_template('WellnessApplication/logs.html')
    context = {
        'activities': activities,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("This is the log page")