import okx.MarketData as MarketData


flag = "0"  # Production trading:0 , demo trading:1
marketDataAPI = MarketData.MarketAPI(flag=flag)


def okx_market(coin):

    # Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours
    result = marketDataAPI.get_index_tickers(
        instId=f"{coin}"
    )
    return result


def okx_market_index(coin):
    result = marketDataAPI.get_index_candlesticks(
        instId=f"{coin}"
    )
    return result


# print(okx_market("DOGS-USD"))
