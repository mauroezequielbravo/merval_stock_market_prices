from playwright.sync_api import sync_playwright
from datetime import datetime


def get_share_price(ticker):
    with sync_playwright() as p:
        # Abre un navegador (en este caso, Chrome)
        browser = p.chromium.launch(headless=True)

        # Crea un contexto
        context = browser.new_context()

        # Abre una nueva página
        page = context.new_page()

        # Navega a una URL
        page.goto(f'https://www.rava.com/perfil/{ticker}')

        # Utiliza XPath para seleccionar un elemento
        precio = page.main_frame.locator('//*[@id="izqCotiza"]/p[1]').inner_text()
        precioAnterior = page.main_frame.locator('//*[@id="centroCotiza"]/ul/li[1]/span[2]').inner_text()
        precioApertura = page.main_frame.locator('//*[@id="centroCotiza"]/ul/li[2]/span[2]').inner_text()
        precioMaximo = page.main_frame.locator('//*[@id="centroCotiza"]/ul/li[3]/span[2]').inner_text()
        precioMinimo = page.main_frame.locator('//*[@id="centroCotiza"]/ul/li[4]/span[2]').inner_text()
        VolNominal = page.main_frame.locator('//*[@id="derCotiza"]/ul/li[1]/span[2]').inner_text()
        VolEfectivo = page.main_frame.locator('//*[@id="derCotiza"]/ul/li[2]/span[2]').inner_text()
        VolPromedio = page.main_frame.locator('//*[@id="derCotiza"]/ul/li[3]/span[2]').inner_text()
        VolumenPorc = page.main_frame.locator('//*[@id="derCotiza"]/ul/li[4]/span[2]').inner_text()

        # Cierra el navegador
        browser.close()
        activo = {
            'ticker': ticker,
            'date': datetime.now(),
            'price': precio.replace('.', '').replace(',', '.'),
            'previous_price': precioAnterior.replace('.', '').replace(',', '.'),
            'opening_price': precioApertura.replace('.', '').replace(',', '.'),
            'max_price': precioMaximo.replace('.', '').replace(',', '.'),
            'min_price': precioMinimo.replace('.', '').replace(',', '.'),
            'nominal_volume': VolNominal,
            'effective_volume': VolEfectivo,
            'average_volume': VolPromedio,
            'percentage_volume': VolumenPorc
        }
        return activo


if __name__ == '__main__':
    res = get_share_price('ALUA')
    print(res)