import os
from os.path import join
import pandas as pd
from utils.constants.paths import FILE_PATH_DATA, NAME_FILE_TICKERS_A_CONSULTAR, NAME_FILE_DATA
import pyarrow as pa

_FILE_PATH = join(FILE_PATH_DATA, NAME_FILE_TICKERS_A_CONSULTAR)
# Crea las carpetas que faltan en la ruta
os.makedirs(os.path.dirname(_FILE_PATH), exist_ok=True)


def get_ticker_to_consult() -> str:
    df = pd.read_json(_FILE_PATH)
    ticker = df[df['Consulted'] == False]['Ticker'].head(
        1).to_string(index=False)
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
    df.to_json(_FILE_PATH, orient='records', indent=4)


def get_total_ticker_to_consult() -> int:
    df = pd.read_json(_FILE_PATH)
    return df[df['Consulted'] == False].shape[0]


def create_data_file():
    if os.path.exists(join(FILE_PATH_DATA, NAME_FILE_DATA)):
        return 0
    else:
        columnas = {
            'fecha': 'datetime64[ns]',   # Fecha y hora
            'precio': 'float64',          # Precio actual
            'precioAnterior': 'float64',  # Precio anterior
            'precioApertura': 'float64',  # Precio de apertura
            'precioMaximo': 'float64',    # Precio máximo
            'precioMinimo': 'float64',    # Precio mínimo
            'VolNominal': 'int64',        # Volumen nominal
            'VolEfectivo': 'float64',     # Volumen efectivo
            'VolPromedio': 'float64',     # Volumen promedio
            'VolumenPorc': 'float64'      # Volumen porcentual
        }
        # Crear el DataFrame vacío con las columnas y tipos de datos especificados
        df = pd.DataFrame({col: pd.Series(dtype=tipo) for col, tipo in columnas.items()})
        df.to_parquet(join(FILE_PATH_DATA, NAME_FILE_DATA))


def add_price_to_ticker(data: dict):
    df = pd.read_parquet(join(FILE_PATH_DATA, NAME_FILE_DATA), engine='pyarrow')

    df_data = pd.DataFrame([data])

    df_total = pd.concat([df, df_data], ignore_index=True)
    df_total.to_parquet(join(FILE_PATH_DATA, NAME_FILE_DATA), engine='pyarrow')
    _put_ticker_in_true(data['ticker'])
    return 1


if __name__ == '__main__':
    print(get_total_ticker_to_consult())
