import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                    AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
}
URL = "https://coinmarketcap.com/currencies/"


def getCrypto(name):
    """Get The Price"""
    url = URL + name + '/'
    data = requests.get(url, headers=headers)
    if data.status_code == 200:
        soup = BeautifulSoup(data.content, features='html.parser')

        # get the price of the bitcoin
        price = soup.find('div', {'class': 'priceValue'})
        return price.text
    else:
        return 'Server Error'


if __name__ == '__main__':
    print(getCrypto('bitcoin'))
    print(getCrypto('ethereum'))
    print(getCrypto('dogecoin'))
    print(getCrypto('cronos'))
