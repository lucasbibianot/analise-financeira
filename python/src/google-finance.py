from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

param = {
    'q': ".DJI",
    'x': "INDEXDJX",
}

df = get_price_data(param)
print(df)

"""
https://www.google.com/search?tbm=fin&
q=BVMF:+FLRY3&
stick=H4sIAAAAAAAAAONgecRoyi3w8sc9YSmdSWtOXmNU4-IKzsgvd80rySypFJLgYoOy-KR4uLj0c_UNkrNzUyzSeBaxcjuF-bpZKbj5BEUaAwDu2uI3SAAAAA&
sa=X&
ved=0ahUKEwiotYDZkfjiAhWHEbkGHTLUBQYQlq4CCDswAA&
biw=1366&
bih=625&
dpr=1#scso=_AIcLXYywGd6f5OUP4rS1qA02:0

"""