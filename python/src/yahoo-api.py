import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
import json
from bs4 import BeautifulSoup


my_share = share.Share('GGRC11.SA')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          10,
                                          share.FREQUENCY_TYPE_MINUTE,
                                          5)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

soup = BeautifulSoup(str(symbol_data), 'html.parser')

print(soup.prettify)
#print(dicionario)
