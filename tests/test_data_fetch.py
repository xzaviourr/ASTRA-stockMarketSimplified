from lib.modules.fetch_historical_data import fetch_historical_data
import settings
import pytest

@pytest.mark.parametrize("ticker_list", [['ADBE'], ['AMZN', 'AAPL']])
def test_fetch_historical_data(ticker_list):
    fetch_historical_data(ticker_list)
    try:
        for ticker in ticker_list:
            file = open(f"{settings.HISTORICAL_DATA_DIRECTORY}/{ticker}.csv", 'r')
            file.close()
        assert True
    except Exception as e:
        assert False