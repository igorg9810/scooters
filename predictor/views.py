from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import loader
from .forms import ConditionsForm
import pickle
import os
import numpy as np
from time import strptime

# Create your views here.

cur_dir = os.path.dirname(__file__)
forest = pickle.load(open(os.path.join(cur_dir,
                 'pkl_objects',
                 'predictor.pkl'), 'rb'))
label = {'on': True, False: False}
				 
def forecast(conditions):
    X = conditions
    y = forest.predict(X)
    return y

def index(request):
    title = "I can predict anything"
    template = loader.get_template('predictor/index.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))
	
def post_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConditionsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
		    # process the data in form.cleaned_data as required
		    # ...
		    # redirect to a new URL:
	        timestamp = strptime(request.POST.get('время', '2011-11-11 00:00:00'), "%Y-%m-%d %H:%M:%S").tm_hour
	        humidity = request.POST['humidity']
	        weather = request.POST['weather']
	        holiday = label[request.POST.get('holiday', False)]
	        workday = label[request.POST.get('workday', False)]
	        temp = request.POST['temp']
	        felt_temp = request.POST['felt_temp']
	        wind = request.POST['wind']
	        season = request.POST['season']
	        arr = np.array([timestamp, season, holiday*1, workday*1, weather, temp, felt_temp, humidity, wind])
	        quantity = forecast(arr.reshape(1, -1))
	        return render(request, 'predictor/prediction.html', {'form': form, 'quantity': quantity})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ConditionsForm()

    return render(request, 'predictor/post_edit.html', {'form': form})
	
def train(request):
    return render(request, 'predictor/finish.html')