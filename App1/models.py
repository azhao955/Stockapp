from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

# Create your models here.

# Database structure goes here, create python classes that correspond to tables in the database
# each database represented as a python class

class Currency(models.Model):
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=3)
    def __repr__(self):
        return self.name + " " + self.symbol
    def __str__(self):
        return self.name + " " + self.symbol


class Country (models.Model):
    name = models.CharField(max_length = 100)
    capital = models.CharField(max_length =50)
    wiki_link = models.URLField()
    currency = models.ForeignKey(Currency,null = True, on_delete=models.SET_NULL) #ForeignKey to pull in other objects
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __repr__(self):
        return self.name + ' ' + self.capital + ' ' + self.currency.name

    def __str__(self):
        return self.name + ' ' + self.capital + ' ' + self.currency.name

class Rates(models.Model):
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    x_currency = models.CharField(max_length=3)
    rate = models.FloatField(default=1.0)
    last_update_time = models.DateTimeField()
    def __repr__(self):
        return self.currency.symbol + " " + self.x_currency + " " + str(self.rate)
    def __str__(self):
        return self.currency.symbol + " " + self.x_currency + " " + str(self.rate)



class Stocks(models.Model):
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=5)
    price = models.FloatField(max_length=3)
    def __repr__(self):
        return self.name + " " + self.ticker + " " + str(self.price)

    def __str__(self):
        return self.name + " " + self.ticker+ " " + str(self.price)

class AccountHolder (models.Model):
    userid = models.OneToOneField(User,on_delete=models.CASCADE)
    available_cash = models.FloatField(default=1000000)
    # countries_visited = models.ManyToManyField(Country)
    def __str__(self):
        return self.userid.username + " " + str(self.available_cash)
    def __repr__(self):
        return self.userid.username + " " + str(self.available_cash)

class Holdings (models.Model):
    userid = models.ForeignKey(AccountHolder,on_delete=models.CASCADE)
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    units = models.FloatField(default=0.0)

    def __repr__(self):
        return self.userid.userid.username + " " + self.stock.ticker + " " + str(self.units)

    def __str__(self):
        return self.userid.userid.username + " " + self.stock.ticker + " " + str(self.units)
    #
    #     to display portfolio, holdings.objects.all(user = )


