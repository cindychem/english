import re
import requests
from bs4 import BeautifulSoup

def read( word ):
    url = f'http://dict.cn/big5/{word}#searchL'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('h1').text
    row = bs.find('strong').text
    try:
        chinese = data
        phone = row
        s = " ".join( phone )
        text = chinese + s
        regex= re.compile(r'[\u4E00-\u9FFF\uFF00-\uFFFF]|[a-zA-Z0-9]+')
        arr = re.findall(regex, text)
        text = ' '.join(arr)

        regex= re.compile(r'(?<=[^a-zA-Z0-9\u0021-\u002E])(\x20)(?=[^a-zA-Z0-9\u0021-\u002E])')
        text = re.sub(regex, '', text)
        return( text )
    except:
        return( '查無此字' )
