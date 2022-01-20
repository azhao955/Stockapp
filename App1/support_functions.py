from App1.models import Currency, Country, Rates


def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "https://thefactfile.org/countries-currencies-symbols/"
    response = requests.get(url)
    if not response.status_code == 200:
        return currency_list
    soup = BeautifulSoup(response.content)
    data_lines = soup.find_all('tr')
    for line in data_lines:
        try:
            detail = line.find_all('td')
            country = detail[1].get_text().strip()
            currency = detail[2].get_text().strip()
            iso = detail[3].get_text().strip()
            # print(country, currency, iso)
            currency_list.append((country, currency, iso))
        except:
            continue
    return currency_list


def get_currency_rates(iso_code):
    url = "http://www.xe.com/currencytables/?from=" + iso_code
    import requests
    from bs4 import BeautifulSoup
    x_rate_list = list()
    try:
        page_source = BeautifulSoup(requests.get(url).content)
    except:
        return x_rate_list
    data = page_source.find('tbody')
    data_lines = data.find_all('tr')
    for line in data_lines:
        symbol = line.find('th').get_text()
        data=line.find_all('td')
        try:
            x_rate = float(data[2].get_text().strip())
            x_rate_list.append((symbol,x_rate))
        except:
            continue
    return x_rate_list


def add_countries_and_currencies(currency_list):
    for currency in currency_list:
        country_name = currency[0]
        currency_name = currency[1]
        currency_symbol = currency[2]
        wiki_link = "https://en.wikipedia.org/wiki/"+country_name
        capital_city = ""
        try:
            c = Currency.objects.get(symbol=currency_symbol)
        except:
            c = Currency(name=currency_name, symbol=currency_symbol)
        c.name = currency_name
        c.save()
    try:
        print("Trying country stuff")
        cy = Country.objects.get(name=country_name)
        cy.name = country_name
        cy.wiki_link = wiki_link
        cy.capital = capital_city
        cy.currency = c
        print("Updating existing country object", cy)
    except:
        cy = Country(name=country_name, capital=capital_city, wiki_link=wiki_link, currency=c)
        print("Creating new country object", cy)
    cy.save()


def get_capitals():
    import pandas as pd
    print("start")
    df = pd.read_html("https://en.wikipedia.org/wiki/List_of_national_capitals")[1]
    df.set_index('Country/Territory', inplace=True)
    return df

def update_xrates(currency):
    try:
        new_rates = get_currency_rates(currency.symbol)
        for new_rate in new_rates:
            from datetime import datetime, timezone
            time_now = datetime.now(timezone.utc)
            try:
                rate_object = Rates.objects.get(currency=currency, x_currency=new_rate[0])
                rate_object.rate = new_rate[1]
                rate_object.last_update_time = time_now
            except:
                rate_object = Rates(currency=currency, x_currency=new_rate[0], rate=new_rate[1],
                                    last_update_time=time_now)
            rate_object.save()
    except:
        pass
