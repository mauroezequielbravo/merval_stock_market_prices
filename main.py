import schedule
import time
from utils.functions.generate_initial_file_tickers import generate_initial_file_tickers
from utils.functions.tickers import get_ticker_to_consult, get_total_ticker_to_consult, add_price_to_ticker, create_data_file
from utils.functions.scraper import get_share_price


def job():
    generate_initial_file_tickers()
    res = get_ticker_to_consult()
    res_data = get_share_price(res)
    create_data_file()
    add_price_to_ticker(res_data)


schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
