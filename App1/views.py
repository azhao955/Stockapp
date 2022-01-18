import datetime
import pytz #library to offset date time

from django.shortcuts import render


def home(request):
    data = dict()
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    data["time_now"] = now
    return render(request, "Home.html", context = data)