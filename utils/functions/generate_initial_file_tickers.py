import os
from os.path import join
import pandas as pd
from utils.constants.tickers import TICKERTS
from utils.constants.paths import FILE_PATH_DATA, NAME_FILE_TICKERS_A_CONSULTAR


def generate_initial_file_tickers():
    file_path = join(FILE_PATH_DATA, NAME_FILE_TICKERS_A_CONSULTAR)
    # Crea las carpetas que faltan en la ruta
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if os.path.exists(file_path):
        return 0
    else:
        # df = pd.read_json('tickers.json', orient='index')
        df = pd.DataFrame.from_dict(TICKERTS, orient='index')

        # Invierte filas por columnas
        df = df.transpose()

        # Saca los None
        df.dropna(inplace=True)

        df_bonos = pd.DataFrame()
        df_bonos['Ticker'] = df['Bonos']
        df_bonos['Type'] = 'Bonos'
        df_bonos['Consulted'] = False

        df_cedear = pd.DataFrame()
        df_cedear['Ticker'] = df['Cedear']
        df_cedear['Type'] = 'Cedear'
        df_cedear['Consulted'] = False

        df_panel_general = pd.DataFrame()
        df_panel_general['Ticker'] = df['PanelGeneral']
        df_panel_general['Type'] = 'PanelGeneral'
        df_panel_general['Consulted'] = False

        df_panel_lider = pd.DataFrame()
        df_panel_lider['Ticker'] = df['PanelLider']
        df_panel_lider['Type'] = 'PanelLider'
        df_panel_lider['Consulted'] = False

        df_tickers = pd.concat([df_bonos, df_cedear, df_panel_general, df_panel_lider], ignore_index=True)

        

        df_tickers.to_json(file_path, orient='records', indent=4)
