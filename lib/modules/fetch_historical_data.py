import yfinance as yf
import settings

def fetch_historical_data(ticker_list):
	data = yf.download(
		tickers=ticker_list,
		threads=True,
		group_by='ticker',
		interval='1d',
	)

	# Saving data
	if len(ticker_list) == 1:
		data[data['Open'].notna()].to_csv(f'{settings.HISTORICAL_DATA_DIRECTORY}/{ticker_list[0]}.csv', sep=',')
	else:
		for ticker in ticker_list:
			data[ticker][data[ticker]['Open'].notna()].to_csv(f'{settings.HISTORICAL_DATA_DIRECTORY}/{ticker}.csv', sep=',')
 