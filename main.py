import schedule
import time
import logging
from utils.functions.generate_initial_file_tickers import generate_initial_file_tickers
from utils.functions.tickers import get_ticker_to_consult, get_total_ticker_to_consult, add_price_to_ticker, create_data_file
from utils.functions.scraper import get_share_price
from utils.functions.supabase import listar, crear


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def job():
    generate_initial_file_tickers()
    res = get_ticker_to_consult()
    logging.info('Obteniendo el precio de: {}'.format(res))
    res_data = get_share_price(res)
    create_data_file()
    add_price_to_ticker(res_data)
    crear(res_data['ticker'], 
          res_data['precio'], 
          res_data['precioAnterior'], 
          res_data['precioApertura'], 
          res_data['precioMaximo'], 
          res_data['precioMinimo'], 
          res_data['VolNominal'], 
          res_data['VolEfectivo'], 
          res_data['VolPromedio'], 
          res_data['VolumenPorc'])



schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
