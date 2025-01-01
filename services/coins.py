from services.api_okx import okx_market_index, okx_market
from services.api_coinmarketcap import get_info


def coins():
    ton_info = get_info('toncoin')['data']['11419']
    ton_index = okx_market("TON-USD")['data'][0]['idxPx']

    not_info = get_info('notcoin')['data']['28850']
    not_index = okx_market("NOT-USD")['data'][0]['idxPx']

    punk_info = get_info('punk')['data']['8490']

    hmstr_info = get_info('hamster')['data']['10336']
    hmstr_index = okx_market("HMSTR-USD")['data'][0]['idxPx']

    major_info = get_info('major')['data']['33188']
    major_index = okx_market("MAJOR-USD")['data'][0]['idxPx']

    dogs_info = get_info('dogs')['data']['32698']
    dogs_index = okx_market("DOGS-USD")['data'][0]['idxPx']

    return [
        {"logo": ton_info["logo"], "name": ton_info["name"], "symbol": ton_info["symbol"], "index": ton_index, "category": ton_info["category"], "website": ton_info["urls"]["website"][0], "source_code": ton_info["urls"]["source_code"][0]},
        {"logo": not_info["logo"], "name": not_info["name"], "symbol": not_info["symbol"], "index": not_index, "category": not_info["category"], "website": not_info["urls"]["website"][0]},
        {"logo": punk_info["logo"], "name": punk_info["name"], "symbol": punk_info["symbol"], "category": punk_info["category"], "website": punk_info["urls"]["website"][0]},
        {"logo": hmstr_info["logo"], "name": hmstr_info["name"], "symbol": hmstr_info["symbol"], "index": hmstr_index, "category": hmstr_info["category"], "website": hmstr_info["urls"]["website"][0]},
        {"logo": major_info["logo"], "name": major_info["name"], "symbol": major_info["symbol"], "index": major_index, "category": major_info["category"], "website": major_info["urls"]["website"][0]},
        {"logo": dogs_info["logo"], "name": dogs_info["name"], "symbol": dogs_info["symbol"], "index": dogs_index, "category": dogs_info["category"], "website": dogs_info["urls"]["website"][0]},
    ]
