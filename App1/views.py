import datetime
import pytz #library to offset date time
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render

from App1 import support_functions
from App1.models import Country, AccountHolder


def home(request):
    data = dict()

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

def stockinput(request):
    data = dict()
    try:
        request.GET['form_submitted']


    except:
        pass
    return render(request, "StockInput.html", context=data)

def currency_selection(request):
    data = dict()
    countries =Country.objects.all()
    data['countries'] = countries
    print(countries)
    return render(request,"country_selector.html",data)

def exch_rate(request):
    data=dict()
    try:
        country1 = request.GET['country_from']
        country2 = request.GET['country_to']
        try:
            user = request.user
            if user.is_authenticated:
                account_holder = AccountHolder.objects.get(user=user)
                account_holder.countries_visited.add(country2)
                data['countries_visited'] = account_holder.countries.all()
        except:
            pass

        data['country1'] = Country.objects.get(id=country1)
        data['country2'] = Country.objects.get(id=country2)
        currency1 = Country.objects.get(id=country1).currency
        currency2 = Country.objects.get(id=country2).currency
        support_functions.update_xrates(currency1)
        data['currency1'] = currency1
        data['currency2'] = currency2
        try:
            rate = currency1.rates_set.get(x_currency=currency2.symbol).rate
            data['rate'] = rate
        except:
            pass
    except:
        pass
    return render(request,"exchange_detail.html",data)

# register a new user function
def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = AccountHolder(user=new_user, date_of_birth=dob)
        acct_holder.save()
        return render(request, "entry.html", context=dict())

    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context)

def entry(request):
    data = dict()
    return render(request, "entry.html", context=data)

def portfolio(request):
    data = dict()
    return render(request, "portfolio.html", context=data)