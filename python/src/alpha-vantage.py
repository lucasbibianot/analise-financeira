import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

KEY = 'KJ37REN2F7J1JP3V'
STOCK = 'CIEL3.SA'
FUNCAO = 'TIME_SERIES_MONTHLY'
endpoint = """https://www.alphavantage.co/query?function={0}&symbol={1}&apikey={2}""".format(
    FUNCAO, STOCK, KEY)

print(endpoint)
response = requests.get(url=endpoint)

soup = BeautifulSoup(response.text, 'html.parser')

dicionario = json.loads(str(response.text))
df = pd.DataFrame.from_dict(dicionario)
print(df.head)
