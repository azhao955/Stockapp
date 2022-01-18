import datetime

from django.shortcuts import render


def home(request):
    data = dict()
    now = datetime.datetime.now()
    data["time_now"] = now
    print(now)
    return render(request, "home.html", context = data)