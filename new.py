import requests
from bs4 import BeautifulSoup

def read( word ):
    url = f'http://dict.cn/big5/{word}#searchL'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    row = bs.find('strong').text
    try:
        phones = row
        phone = [e.text for e in phones]
        s = " ".join( phone )
        # s = row.find('sub')
        print( s )
    except:
        return( '查無此字' )
