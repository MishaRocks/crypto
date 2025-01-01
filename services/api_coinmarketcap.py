from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from config import coinmarketcap_key

cm_key = coinmarketcap_key


def get_info(your_coin):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    parameters = {
        'slug': f'{your_coin}'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': cm_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e


# print(get_info('dogs'))
