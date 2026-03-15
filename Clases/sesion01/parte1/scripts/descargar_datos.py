"""
Script para descargar datos de cuenta corriente, tipo de cambio real y reservas
Fuentes: FMI WEO, BCRA
"""

import requests
import pandas as pd
import json
from pathlib import Path

# Directorios
BASE_DIR = Path(__file__).parent.parent
DATOS_DIR = BASE_DIR / "datos"
DATOS_DIR.mkdir(exist_ok=True)

def descargar_fmi_cuenta_corriente():
    """Descarga cuenta corriente (% PIB) del FMI DataMapper API"""

    url = "https://www.imf.org/external/datamapper/api/v1/BCA_NGDPD"

    print("Descargando datos del FMI...")
    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        data = response.json()

        # Países de interés
        paises = {
            'USA': 'Estados Unidos',
            'CHN': 'China',
            'DEU': 'Alemania',
            'ARG': 'Argentina'
        }

        # Extraer datos
        valores = data.get('values', {}).get('BCA_NGDPD', {})

        registros = []
        for codigo, nombre in paises.items():
            if codigo in valores:
                for anio, valor in valores[codigo].items():
                    registros.append({
                        'pais': nombre,
                        'codigo': codigo,
                        'anio': int(anio),
                        'cuenta_corriente_pib': round(valor, 2)
                    })

        df = pd.DataFrame(registros)
        df = df.sort_values(['pais', 'anio'])

        # Guardar
        archivo = DATOS_DIR / "cuenta_corriente_fmi.csv"
        df.to_csv(archivo, index=False)
        print(f"Guardado: {archivo}")
        print(f"  Países: {df['pais'].unique().tolist()}")
        print(f"  Años: {df['anio'].min()} - {df['anio'].max()}")

        return df
    else:
        print(f"Error descargando FMI: {response.status_code}")
        return None


def crear_datos_bcra_manual():
    """
    Crea datos del BCRA manualmente (la API del BCRA requiere scraping complejo)
    Fuente: BCRA Series Estadísticas
    https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp
    """

    # ITCRM - Tipo de Cambio Real Multilateral (base dic 2015 = 100)
    # Datos anuales promedio aproximados de series BCRA
    itcrm_data = {
        'anio': [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
                 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
                 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        'itcrm': [68, 67, 66, 65, 62, 178, 152, 147, 144,
                  148, 145, 143, 133, 117, 104, 93, 90, 88,
                  100, 88, 83, 97, 115, 107, 103, 93, 105, 140]
    }

    df_itcrm = pd.DataFrame(itcrm_data)
    archivo = DATOS_DIR / "itcrm_bcra.csv"
    df_itcrm.to_csv(archivo, index=False)
    print(f"Guardado: {archivo}")

    # Reservas internacionales (miles de millones USD, fin de período)
    reservas_data = {
        'anio': [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
                 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
                 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
                 2020, 2021, 2022, 2023, 2024],
        'reservas_usd_bn': [6.2, 8.4, 12.3, 14.8, 15.7, 16.1, 19.7, 22.4, 24.8, 26.3,
                           25.1, 14.6, 10.5, 14.1, 19.6, 28.1, 32.0, 46.2, 46.4, 48.0,
                           52.2, 46.4, 43.3, 30.6, 31.4, 25.6, 38.8, 55.1, 66.0, 44.8,
                           39.4, 39.7, 44.6, 23.1, 32.0]
    }

    df_reservas = pd.DataFrame(reservas_data)
    archivo = DATOS_DIR / "reservas_bcra.csv"
    df_reservas.to_csv(archivo, index=False)
    print(f"Guardado: {archivo}")

    # Cuenta corriente Argentina (% PIB) - datos más detallados
    cc_arg_data = {
        'anio': list(range(1990, 2025)),
        'cuenta_corriente_pib': [
            3.7, -0.3, -2.4, -3.4, -4.3, -2.0, -2.5, -4.2, -4.8, -4.2,  # 1990-1999
            -3.2, -1.4, 8.6, 6.3, 2.1, 2.9, 3.6, 2.8, 2.1, 2.5,        # 2000-2009
            -0.4, -0.8, -0.2, -2.1, -1.6, -2.7, -2.7, -4.8, -5.2, -0.8, # 2010-2019
            0.9, 1.4, -0.6, -3.5, 0.9                                   # 2020-2024
        ]
    }

    df_cc_arg = pd.DataFrame(cc_arg_data)
    archivo = DATOS_DIR / "cuenta_corriente_argentina.csv"
    df_cc_arg.to_csv(archivo, index=False)
    print(f"Guardado: {archivo}")

    return df_itcrm, df_reservas, df_cc_arg


if __name__ == "__main__":
    print("=" * 50)
    print("Descargando datos para gráficos de clase 1+2")
    print("=" * 50)

    # FMI
    df_fmi = descargar_fmi_cuenta_corriente()

    print()

    # BCRA (datos manuales)
    print("Creando datos BCRA (series manuales)...")
    crear_datos_bcra_manual()

    print()
    print("=" * 50)
    print("Datos descargados en:", DATOS_DIR)
    print("=" * 50)
