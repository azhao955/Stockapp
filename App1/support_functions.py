from django.http import request
from django.shortcuts import render
from django.db.models import Q

from App1.models import Stocks, Holdings

# Gets stocks and prices by web scraping
def get_stocks():
    from bs4 import BeautifulSoup as soup
    import requests
    url = 'https://www.slickcharts.com/sp500'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62"}
    soup = soup(requests.get(url, headers=headers).content, 'html.parser')
    data_lines = soup.find_all("td")
    lst = []
    i = 1
    while i < len(data_lines):
        company = data_lines[i].text
        try:
            symbol = data_lines[i + 1].text

        except:
            pass

        try:
            price = data_lines[i + 3].text
            price = price[3:]
            price = price.replace(',','')
            try:
                price=float(price)
            except:
                price = 0
        except:
            pass
        lst.append((company, symbol, price))
        i = i + 7
    return lst
# Takes the get stocks and adds it to Django database


def add_stocks(stocks_list):

    for stock in stocks_list:
        stock_name = stock[0]
        stock_ticker = stock[1]
        stock_price = stock[2]
        try:
            s = Stocks.objects.get(ticker=stock_ticker)
            s.name = stock_name
            s.ticker = stock_ticker
            s.price = stock_price
            s.save()
            print("Existing entry updated")
        except:
            s = Stocks(name=stock_name, ticker=stock_ticker, price = stock_price)
            print("New entry added:", s.ticker)
            s.save()


def output_table(request):
    output = My_Model()
    return render_to_response('outputtable.html', {'output': output})