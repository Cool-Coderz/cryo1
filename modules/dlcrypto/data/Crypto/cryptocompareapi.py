import pandas as pd
import requests
import datetime

# Taken from https://medium.com/@galea/cryptocompare-api-quick-start-guide-ca4430a484d4

def daily_price_historical(symbol, comparison_symbol, all_data=True, limit=2000, aggregate=1, exchange=''):
    """ Gets the historical daily prices"""
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    df = df.set_index('timestamp')
    df = df.drop(['time'], axis=1)

    return df

def hourly_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    """Gets the historical hourly prices"""
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    df = df.set_index('timestamp')
    df = df.drop(['time'], axis=1)

    return df

def minute_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    """ Gets the historical prices by minute"""
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    df = df.set_index('timestamp')
    df = df.drop(['time'], axis=1)

    return df

def price(symbol, comparison_symbols=['USD'], exchange=''):
    """
    Gets the live coin price
    price('BTC', ['USD, ETH'], exchange='Coinbase')
    """
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()

    return data
