from django.utils.translation import activate
from .models import Activity, User
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import uuid


from .models import Activity
# Create your views here.
def companionpage(request):
    if request.method == "POST":
        return HttpResponse("no")
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


    template = loader.get_template('WellnessApplication/companion.html')
    context = {
        'output': output,
    }
    return HttpResponse(template.render(context, request))
def submitpage(request):
    context = {'userid': '7a16c3cf-a5d5-462b-96b5-210cc694a881'}
    return render(request, 'WellnessApplication/submit_activity.html', context)

def submitdata(request, userid):
    if request.method == "POST":
        if (not userid
            or not request.POST.get('activity_duration')
            or not request.POST.get('activity_category')
            or not request.POST.get('activity_completed')):
            return render(request, 'WellnessApplication/submit_activity.html', {
            'userid': userid,
            'error_message': "Please fill in all items!",
        })
        activity = Activity()
        activity.personID_id = uuid.UUID(userid)
        activity.time_spent = activity.time_spent = int(request.POST.get('activity_duration'))
        activity.activity_catergory = request.POST.get('activity_category')
        activity.activity_type = request.POST.get('activity_completed')
        activity.date = datetime.datetime.now()
        activity.save()
        return render(request, 'WellnessApplication/successful_submission.html', {})
    else:
        return submitpage(request)

def logpage(request):
    # user = User.objects.get(name = "Brian")
    # activities = Activity.objects.filter(personID = user.UUID)
    activities = Activity.objects.order_by("-date")
    template = loader.get_template('WellnessApplication/logs.html')
    context = {
        'activities': activities,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("This is the log page")