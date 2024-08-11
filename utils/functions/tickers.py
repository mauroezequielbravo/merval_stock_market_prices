import os
from os.path import join
import pandas as pd
from utils.constants.paths import FILE_PATH_DATA, NAME_FILE_TICKERS_A_CONSULTAR, NAME_FILE_DATA


_FILE_PATH = join(FILE_PATH_DATA, NAME_FILE_TICKERS_A_CONSULTAR)
# Crea las carpetas que faltan en la ruta
os.makedirs(os.path.dirname(_FILE_PATH), exist_ok=True)

def get_ticker_to_consult() -> str:
    df = pd.read_json(_FILE_PATH)
    ticker = df[df['Consulted'] == False]['Ticker'].head(1).to_string(index=False)
    if ticker:
        return ticker
    else:
        _put_tickers_in_false()
        return get_ticker_to_consult()

def _put_tickers_in_false():
    df = pd.read_json(_FILE_PATH)
    df['Consulted'] = False
    df.to_json(_FILE_PATH)

def _put_ticker_in_true(ticker: str):
    df = pd.read_json(_FILE_PATH)
    df.loc[df['Ticker'] == ticker, 'Consulted'] = True
    df.to_json(_FILE_PATH)

def get_total_ticker_to_consult() -> int:
    df = pd.read_json(_FILE_PATH)
    return df[df['Consulted'] == False].shape[0]

def add_price_to_ticker(data: dict):
    df_data = pd.DataFrame.to_dict(data)
    return df_data

if __name__ == '__main__':
    print(get_total_ticker_to_consult())

