from django import forms

class ActivityForm(forms.Form):
    activityType = forms.CharField(widget=forms.Select)
    duration = forms.IntegerField()
    date = forms.DateField()