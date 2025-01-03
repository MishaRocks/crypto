from services.api_okx import okx_market_index, okx_market
from services.api_coinmarketcap import get_info


def coins():
    ton_info = get_info('toncoin')['data']['11419']
    ton_index = okx_market("TON-USD")['data'][0]

    not_info = get_info('notcoin')['data']['28850']
    not_index = okx_market("NOT-USD")['data'][0]

    punk_info = get_info('punk')['data']['8490']

    hmstr_info = get_info('hamster')['data']['10336']
    hmstr_index = okx_market("HMSTR-USD")['data'][0]

    major_info = get_info('major')['data']['33188']
    major_index = okx_market("MAJOR-USD")['data'][0]

    dogs_info = get_info('dogs')['data']['32698']
    dogs_index = okx_market("DOGS-USD")['data'][0]

    return [
        {"logo": ton_info["logo"], "name": ton_info["name"], "symbol": ton_info["symbol"], "category": ton_info["category"], "website": ton_info["urls"]["website"][0],
         "index": ton_index['idxPx'], "index_max24": ton_index['high24h'],  "index_min24": ton_index['low24h']},
        {"logo": not_info["logo"], "name": not_info["name"], "symbol": not_info["symbol"], "category": not_info["category"], "website": not_info["urls"]["website"][0],
         "index": not_index['idxPx'], "index_max24": not_index['high24h'],  "index_min24": not_index['low24h']},
        # {"logo": punk_info["logo"], "name": punk_info["name"], "symbol": punk_info["symbol"], "category": punk_info["category"], "website": punk_info["urls"]["website"][0],
        #  },
        {"logo": hmstr_info["logo"], "name": hmstr_info["name"], "symbol": hmstr_info["symbol"], "category": hmstr_info["category"], "website": hmstr_info["urls"]["website"][0],
         "index": hmstr_index['idxPx'], "index_max24": hmstr_index['high24h'],  "index_min24": hmstr_index['low24h']},
        {"logo": major_info["logo"], "name": major_info["name"], "symbol": major_info["symbol"], "category": major_info["category"], "website": major_info["urls"]["website"][0],
         "index": major_index['idxPx'], "index_max24": major_index['high24h'],  "index_min24": major_index['low24h']},
        {"logo": dogs_info["logo"], "name": dogs_info["name"], "symbol": dogs_info["symbol"], "category": dogs_info["category"], "website": dogs_info["urls"]["website"][0],
         "index": dogs_index['idxPx'], "index_max24": dogs_index['high24h'],  "index_min24": dogs_index['low24h']},
    ]
