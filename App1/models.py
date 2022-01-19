from django.db import models

# Create your models here.

# Database structure goes here, create python classes that correspond to tables in the database
# each database represented as a python class

class Currency(models.Model):
    name = models.CharField(max_length=40) #string type with max length of 40
    symbol = models.CharField(max_length=3) #string type with max length of 3

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

class Stock (models.Model):
   name = models.CharField(max_length = 40)
   ticker = models.CharField(max_length =5)
   price = models.CharField(max_length = 10)

