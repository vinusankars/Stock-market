try:
    # For Python 3.0 and later
    from urllib.request import urlopen
    from urllib import error
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    from urllib2 import error
     
import sys
import re
import html.parser

class Data():

    def __init__(self):
        self.world_market = ''
        self.currencies = ''

    def collect(self):

        url = urlopen('https://www.google.com/finance')
        check = url.getcode()
        data = url.read()

        if check == 404 :
            sys.exit()

        world_market_raw = str(re.findall(r'<div id=markets(.*?)<div id=currencies',str(data))[0])
        market_raw = re.findall(r'<td class=symbol><(.*?)\\n',world_market_raw)
        raw_rate = re.findall(r'<td class=price>(.*?)</span>',world_market_raw)
        market = []
        rate = []

        for raw in market_raw :
            raw += str(-1)
            market += re.findall(r'>(.*?)-1',raw)

        for raw in raw_rate :
            raw = raw[:-1] + str(-1)
            rate += re.findall(r'">(.*?)-1',raw)

        world_market= dict()
                                      
        for n in range(len(market)):
            key = html.parser.HTMLParser().unescape(market[n])
            world_market[key] = rate[n]
                                     
        currencies_raw = str(re.findall(r'<div id=currencies>(.*?)<div id=bonds',str(data))[0])
        name_raw = re.findall(r'<a href=(.*?)</a>',currencies_raw)
        value = re.findall(r'<td class=price>(.*?)\\n',currencies_raw)
        name = []

        for raw in name_raw :
            raw += str(-1)
            name += re.findall(r'>(.*?)-1',raw)

        currencies = dict()

        for n in range(len(name)) :
            currencies[name[n]] = value[n]

        self.world_market = world_market
        self.currencies = currencies       


