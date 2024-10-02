from os.path import join
from dotenv import dotenv_values
from datetime import datetime
from supabase import create_client, Client
from supabase.client import ClientOptions


dotenv_path = join('.env')
var_secret = dotenv_values(dotenv_path)

url: str = var_secret["NEXT_PUBLIC_SUPABASE_URL"]
key: str = var_secret["NEXT_PUBLIC_SUPABASE_ANON_KEY"]

supabase: Client = create_client(url, key,
  options=ClientOptions(
    postgrest_client_timeout=100,
    storage_client_timeout=100,
    schema="public",
  ))


def listar(ticker: str):
    response = supabase.table("tickers").select("*").eq("nombre", ticker).execute()
    return response

def crear(ticker: str, 
          precio: float, 
          precioAnterior: float, 
          precioApertura: float, 
          precioMaximo: float, 
          precioMinimo: float, 
          VolNominal: float, 
          VolEfectivo: float, 
          VolPromedio: float, 
          VolumenPorc: float):
    response = supabase.table("tickers").insert({
        "nombre": ticker,
        "precio": precio,
        "precio_anterior": precioAnterior,
        "precio_apertura": precioApertura,
        "precio_maximo": precioMaximo,
        "precio_minimo": precioMinimo,
        "volumen_nominal": VolNominal,
        "volumen_efectivo": VolEfectivo,
        "volumen_promedio": VolPromedio,
        "volumen_porcentual": VolumenPorc,
        "fecha": datetime.now().isoformat()
    }).execute()
    return response


