import requests
from bs4 import BeautifulSoup

def read( word ):
    url = f'http://dict.cn/big5/{word}#searchL'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find_all('ul')[0]
    try:
        row = data.find_all('li')[0]
        phones = row.find_all('strong').text
        phone = for e in phones
        s = " ".join( phone )
        return( s )
    except:
        return( '查無此字' )
