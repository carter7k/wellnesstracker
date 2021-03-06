from django.utils.translation import activate
from .models import Activity
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
import datetime
import random

from .models import Activity
# Create your views here.
def companionpage(request):
    activity_suggestions = {'Mindfulness and Stress Management': ["Popping bubble wrap", "To meditate", "Breathing deeply", "Listening to music" ],
    'Physical Health': ["Running", "Pushups", "Squats", "Biking", "Stretching", "Yoga", "Swimming", "Walking"],
    'Nutrition': ["To eat an apple", "To eat a banana", "To eat some carrots", "planning a meal", "Preparing a healthy lunch instead of eating out"],
    }

    if request.method == "POST":
        with open("WellnessApplication/quotes.txt") as fp:
            line_chosen = random.randint(0,sum(1 for line in open('WellnessApplication/quotes.txt'))-1) # 0 to 27
            for i, line in enumerate(fp): #0 all the way to 27 ,28 times
                if i == line_chosen:
                    inspirational_response = line
                    break
        return HttpResponse(inspirational_response)
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
        elif count[i] == lowest_count:
            if random.randint(0,1) == 0:
                least_done = i

    

    output = least_done

    random_list = []
    for i in list(activity_suggestions.keys()):
        if i not in count:
            random_list.append(i)
    if len(random_list) > 0:
        output = random.choice(random_list)


    random_activity = random.choice(activity_suggestions[output])
    




    template = loader.get_template('WellnessApplication/companion.html')
    context = {
        'output': output,
        'random_activity':random_activity,
    }
    return HttpResponse(template.render(context, request))
def submitpage(request):
    return render(request, 'WellnessApplication/submit_activity.html')

def submitdata(request):
    if request.method == "POST":
        if (request.POST.get('activity_category') == 'Nutrition' # do not requre duration for Nutrition category
            and request.POST.get('activity_completed')):
            pass
        elif (not request.POST.get('activity_duration')
            or int(request.POST.get('activity_duration')) < 0
            or not request.POST.get('activity_category')
            or not request.POST.get('activity_completed')):
            return render(request, 'WellnessApplication/submit_activity.html', {
            'error_message': "Please fill in all items!",
        })
        activity = Activity()
        activity.activity_catergory = request.POST.get('activity_category')
        activity.activity_type = request.POST.get('activity_completed')
        activity.date = datetime.datetime.now()

        if (request.POST.get('activity_duration')):
            activity.time_spent = activity.time_spent = int(request.POST.get('activity_duration'))
        else:
            activity.time_spent = 0 # for Nutrition category

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
    #print(activities[0].date.minute)
    return HttpResponse(template.render(context, request))
    # return HttpResponse("This is the log page")