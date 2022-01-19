import datetime
import pytz #library to offset date time

from django.shortcuts import render

from App1 import support_functions


def home(request):
    data = dict()
    now = datetime.datetime.now()
    data["time_now"] = now
    return render(request, "Home.html", context = data)

def maintenance(request):
    data = dict()
    try:
        request.GET['form_submitted']
        currency_list = support_functions.get_currency_list()
        support_functions.add_countries_and_currencies(currency_list)

    except:
        pass
    return render(request, "Maintenance.html", context=data)

def maintenance(request):
    data = dict()
    try:
        request.GET['form_submitted']


    except:
        pass
    return render(request, "stockinput.html", context=data)