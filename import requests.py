import requests
import time
import json
import pprint
link = 'https://api.coindesk.com/v1/bpi/currentprice.json'
address = 'coin.txt'
while True:
    mydata = requests.get(link)
    time1 = time.localtime()
    time2 = time.strftime('%I/%M/%S %p',time1)
    Bit_price = mydata.json()['bpi']['USD']['rate_float']
    Bit_price = float(Bit_price)
    Bit_price = Bit_price * 32100
    with open(address,'a') as s:
        s.write(f'{time2}.....................{Bit_price} toman\n')
    time.sleep(5)