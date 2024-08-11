from utils.functions.generate_initial_file_tickers import generate_initial_file_tickers
from utils.functions.tickers import get_ticker_to_consult, get_total_ticker_to_consult, add_price_to_ticker
from utils.functions.scraper import get_share_price

# generate_initial_file_tickers()
res = get_ticker_to_consult()
print(get_share_price(res))

# print(get_total_ticker_to_consult())

print(add_price_to_ticker(res))

