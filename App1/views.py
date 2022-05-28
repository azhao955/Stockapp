import datetime
import pytz #library to offset date time
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django import forms
from App1 import support_functions
from App1.models import AccountHolder, Holdings, Stocks


def home(request):
    data = dict()

    return render(request, "Home.html", context = data)



def stockinput(request):
    data = dict()
    try:
        request.GET['form_submitted']
        data = support_functions.add_stocks(support_functions.get_stocks())
        return render(request, "Update_success.html", context=data)

    except:
        pass
    return render(request, "Maintenance.html", context=data)


def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        acct_holder = AccountHolder(userid=new_user, available_cash=1000000)
        acct_holder.save()
        print("test2")
        return render(request,"registration/register.html",context=dict())
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context)

def entry(request):
    data = dict()
    return render(request, "entry.html", context=data)

# def portfolio():
#     try:
#         user = request.user
#         if user.is_authenticated:
#             Account_Holder.portfolio.add(stock, units)
#
#     return test

@login_required
def view_portfolio(request):
    data = dict()
    user = request.user
    print(user)
    if user.is_authenticated:
        account = AccountHolder.objects.get(userid=user)
        print(account)
        holdings = list()
        port = Holdings.objects.filter(userid=account)
        cash = round(account.available_cash, 2)
        print(port)
        portfolio_value = 0
        for p in port:
            price = p.stock.price
            holdings.append([p.stock.ticker,p.units,f"{round(p.units*price):,.2f}"])
            portfolio_value = portfolio_value + p.units*price

        holdings.append(["Cash","Cash",f"{cash:,.2f}"])
        portfolio_value = portfolio_value + cash
        portfolio_value = f"{portfolio_value:,.2f}"
        data['holdings'] = holdings
        print(data['holdings'])

        # fetch cash balance
        balance = list()

        data['balance'] = portfolio_value
        print(data['balance'])
    return render(request, "Portfolio.html", context = data)

# Buy sell function that updates holdings
def buy_sell(request):
    data = dict()
    # Takes form values
    buysell_ticker = request.GET['input_ticker']
    buysell_unit = request.GET['input_unit']
    buysell_buy = request.GET['buysell']

    try:
        stock = Stocks.objects.get (ticker = buysell_ticker)

        #checks user login and initiates ForeignKeys from AccountHolder/Stocks
        user = request.user
        Accountholder = AccountHolder.objects.get(userid=user)
        stock = Stocks.objects.get (ticker = buysell_ticker)
        if buysell_buy == 'buy':

        # check if user owns stock already in Holding table
            transaction_price = float(buysell_unit) * float(stock.price)
            if transaction_price < Accountholder.available_cash: #check if user has enough funds
                try: #does user already own stock? If yes, add to units
                    current_ownership = Holdings.objects.get(userid = Accountholder, stock = stock)
                    current_ownership.units = current_ownership.units + float(buysell_unit)
                    current_ownership.save()

                    Accountholder.available_cash = Accountholder.available_cash - transaction_price
                    Accountholder.save()
                    return render(request, "orderconfirmation.html", context=data)

                except: #if user does not own, add new object in Holdings
                    new_holding = Holdings(userid=Accountholder, stock=stock, units=float(buysell_unit))
                    new_holding.save()
                    Accountholder.available_cash = Accountholder.available_cash - transaction_price
                    Accountholder.save()
                    return render(request, "orderconfirmation.html", context=data)
            else:
                return render(request,"Notenoughcash.html", context = data)

        #sell functionality

        else:
            print(buysell_buy)
            transaction_price = float(buysell_unit) * float(stock.price)
            current_ownership = Holdings.objects.get(userid=Accountholder, stock=stock)
            if current_ownership.units >= 0:
                # check if user has units available to sell
                if float(buysell_unit) < current_ownership.units:
                    Accountholder.available_cash = Accountholder.available_cash + transaction_price
                    Accountholder.save()
                    print(user, buysell_ticker, buysell_unit)
                    current_ownership.units = current_ownership.units - float(buysell_unit)
                    current_ownership.save()
                    return render(request, "orderconfirmation.html", context=data)
                else:
                    return render(request, "Notecantshort.html", context=data)

            else:
                return render(request, "Notecantshort.html", context=data)

    except:
        return render(request, "invalid_ticker.html", context = data)

# def view_currentSP(request):
#     data = dict()
# #    user = request.user
# #    print(user)
# #    if user.is_authenticated:
# #        stocks = Stocks.objects.get()
# #        stocklist = list()
# #        for stock in stocklist:
# #            stocklist.append([stock.ticker,stock.price])
# #        data['stocks'] = stocklist
# #        print(data['stocks'])
#     return render(request, "Displaystockprices.html", context = data)

# def view_balance(request):
#     data = dict()
#     user = request.user
#     if user.is_authenticated:
#         account = AccountHolder.objects.get(userid=user)
#         balance = list()
#         ah = AccountHolder.objects.filter(userid=account)
#         print(port)
#         for a in ah:
#             balance.append([ah.stock.ticker,ah.units])
#         data['balance'] = balance
#         print(data['balance'])
#     return render(request, "Portfolio.html", context = data)