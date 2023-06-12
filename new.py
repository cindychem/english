import requests
from bs4 import BeautifulSoup

url = f'http://dict.cn/big5/{word}#searchL'

html = requests.get( url )
bs = BeautifulSoup(html.text,'lxml')
data = bs.find('h1').text
row = bs.find('strong').text
try:
    chinese = data
    phones = row
    s = " ".join( phones )
    # s = row.find('sub')
    return( chinese + s )
except:
    return( '查無此字' )
