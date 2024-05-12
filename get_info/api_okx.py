import okx.MarketData as MarketData

TON_USDT = "TON-USDT"
TON_USD = "TON-USD"

flag = "0"  # Production trading:0 , demo trading:1
marketDataAPI = MarketData.MarketAPI(flag=flag)


def okx_market(ton):

    # Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours
    result = marketDataAPI.get_index_tickers(
        instId=f"{ton}"
    )

    return result


def okx_market_index(ton):
    result = marketDataAPI.get_index_candlesticks(
        instId=f"{ton}"
    )

    return result


print(okx_market(TON_USD))
