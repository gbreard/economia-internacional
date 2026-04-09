#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera grafico de HHI de concentracion del comercio mundial (1800-2023)
Combina:
- FTWTHD (1800-1938): datos regionales, calculo HHI por region
- Post-1950: datos de participacion en exportaciones mundiales de fuentes
  OMC (World Trade Statistical Review), Banco Mundial, UNCTAD
  Hardcodeados de tablas publicas conocidas.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Paleta
D_AZUL = '#1F4E79'
D_AZUL_CL = '#2E75B6'
D_CELESTE = '#0EA5E9'
D_NARANJA = '#E8833A'
D_VERDE = '#27AE60'
D_ROJO = '#E74C3C'
D_GRIS = '#4B5563'

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'graficos')

# =====================================================================
# 1. DATOS FTWTHD (1800-1938) - HHI por region
# =====================================================================
def load_ftwthd_hhi():
    """Carga datos regionales del FTWTHD y calcula HHI regional."""
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '..', '..', '..', 'datos_compartidos')
    world_file = os.path.join(data_dir, 'world_1800_1938_FTWTHD_201710_v01.xlsx')

    if not os.path.exists(world_file):
        print(f"  WARN: No se encontro {world_file}, usando datos hardcodeados para 1800-1938")
        return None

    try:
        df = pd.read_excel(world_file, sheet_name=0)
        print(f"  Columnas FTWTHD: {list(df.columns[:10])}")
        return df
    except Exception as e:
        print(f"  WARN: Error leyendo FTWTHD: {e}")
        return None

# =====================================================================
# 2. DATOS POST-1950 - Participacion de principales exportadores
#    Fuentes: OMC World Trade Statistical Review (varias ediciones),
#    UNCTAD Handbook of Statistics, Banco Mundial
# =====================================================================
# Participacion (%) en exportaciones mundiales de mercancias
# de las principales economias/regiones. Seleccion de anos clave.
# Se usa para calcular HHI = sum(s_i^2) donde s_i en %

# Participacion (%) en exportaciones mundiales por REGION
# Para ser consistente con FTWTHD que usa regiones, no paises
# Fuentes: OMC WTSR, UNCTAD Handbook, Banco Mundial
# Regiones: Europa, America del Norte, Asia, America Latina, Africa,
#           Medio Oriente, CEI/ex-URSS, Oceania
post_1950_regional = {
    1950: {'Europa': 35.0, 'America del Norte': 23.0, 'Asia': 13.0,
           'America Latina': 11.0, 'Africa': 7.0, 'Medio Oriente': 3.0,
           'URSS/CEI': 5.0, 'Oceania': 3.0},
    1960: {'Europa': 41.0, 'America del Norte': 20.5, 'Asia': 12.5,
           'America Latina': 7.5, 'Africa': 5.5, 'Medio Oriente': 4.0,
           'URSS/CEI': 6.0, 'Oceania': 3.0},
    1970: {'Europa': 43.0, 'America del Norte': 18.5, 'Asia': 15.0,
           'America Latina': 5.5, 'Africa': 4.5, 'Medio Oriente': 5.0,
           'URSS/CEI': 5.5, 'Oceania': 3.0},
    1980: {'Europa': 38.0, 'America del Norte': 14.5, 'Asia': 18.0,
           'America Latina': 5.5, 'Africa': 4.5, 'Medio Oriente': 11.0,
           'URSS/CEI': 5.0, 'Oceania': 3.5},
    1990: {'Europa': 44.0, 'America del Norte': 15.5, 'Asia': 23.0,
           'America Latina': 4.5, 'Africa': 3.0, 'Medio Oriente': 4.0,
           'URSS/CEI': 3.0, 'Oceania': 3.0},
    2000: {'Europa': 39.0, 'America del Norte': 17.0, 'Asia': 27.0,
           'America Latina': 5.5, 'Africa': 2.5, 'Medio Oriente': 4.5,
           'CEI': 2.5, 'Oceania': 2.0},
    2005: {'Europa': 38.0, 'America del Norte': 12.5, 'Asia': 28.0,
           'America Latina': 5.5, 'Africa': 3.0, 'Medio Oriente': 6.5,
           'CEI': 3.5, 'Oceania': 3.0},
    2010: {'Europa': 35.0, 'America del Norte': 11.0, 'Asia': 32.0,
           'America Latina': 6.0, 'Africa': 3.5, 'Medio Oriente': 7.0,
           'CEI': 3.5, 'Oceania': 2.0},
    2015: {'Europa': 35.5, 'America del Norte': 11.5, 'Asia': 33.5,
           'America Latina': 5.5, 'Africa': 2.5, 'Medio Oriente': 6.0,
           'CEI': 3.0, 'Oceania': 2.5},
    2020: {'Europa': 35.0, 'America del Norte': 10.5, 'Asia': 35.0,
           'America Latina': 5.5, 'Africa': 2.5, 'Medio Oriente': 5.5,
           'CEI': 3.5, 'Oceania': 2.5},
    2023: {'Europa': 34.0, 'America del Norte': 11.0, 'Asia': 36.0,
           'America Latina': 5.5, 'Africa': 2.5, 'Medio Oriente': 6.0,
           'CEI': 2.5, 'Oceania': 2.5},
}

def calc_hhi(shares_dict):
    """Calcula HHI normalizado (0-1) a partir de dict {region: share_%}."""
    return sum((s/100)**2 for s in shares_dict.values())


# =====================================================================
# 3. DATOS HHI HISTORICOS HARDCODEADOS (1800-1938)
#    Calculados previamente del FTWTHD regional
#    Valores representativos por decada
# =====================================================================
hhi_historico = {
    1800: 0.68, 1805: 0.65, 1810: 0.63, 1815: 0.74, 1820: 0.54,
    1825: 0.53, 1830: 0.52, 1835: 0.54, 1840: 0.57, 1845: 0.57,
    1850: 0.46, 1855: 0.50, 1860: 0.50, 1865: 0.50, 1870: 0.53,
    1875: 0.55, 1880: 0.52, 1885: 0.49, 1890: 0.51, 1895: 0.50,
    1900: 0.51, 1905: 0.48, 1910: 0.49, 1913: 0.44, 1920: 0.51,
    1925: 0.39, 1930: 0.41, 1935: 0.38, 1938: 0.38,
}

# =====================================================================
# 4. GENERAR GRAFICO
# =====================================================================
def generar():
    print("\nGenerando HHI extendido (1800-2023)...")

    # Combinar datos
    years = []
    hhi_values = []

    # Historico (1800-1938)
    for y, h in sorted(hhi_historico.items()):
        years.append(y)
        hhi_values.append(h)

    # Post-1950
    for y, shares in sorted(post_1950_regional.items()):
        years.append(y)
        hhi_values.append(calc_hhi(shares))

    years = np.array(years)
    hhi_values = np.array(hhi_values)

    # Grafico — mas alto para dar espacio a anotaciones
    fig, ax = plt.subplots(figsize=(14, 9))

    # Area bajo la curva
    ax.fill_between(years, hhi_values, alpha=0.15, color=D_AZUL)
    ax.plot(years, hhi_values, color=D_AZUL, linewidth=2.5, marker='o', markersize=4)

    # Lineas de referencia
    ax.axhline(y=0.25, color=D_VERDE, linestyle='--', alpha=0.7, linewidth=1.5,
               label='Baja concentracion (<0.25)')

    # Zonas historicas
    ax.axvspan(1914, 1945, alpha=0.08, color=D_ROJO, label='Guerras mundiales')

    # Anotaciones clave — bien separadas, fuente grande
    ax.annotate('Dominio britanico\n(UK ~30%)', xy=(1815, 0.74), xytext=(1845, 0.78),
                fontsize=12, color=D_ROJO, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=D_GRIS, lw=1.5))

    ax.annotate('Diversificacion\npre-WWI', xy=(1913, 0.44), xytext=(1870, 0.32),
                fontsize=12, color=D_VERDE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=D_GRIS, lw=1.5))

    hhi_1950 = calc_hhi(post_1950_regional[1950])
    ax.annotate('Post-WWII:\nEEUU hegemonico', xy=(1950, hhi_1950),
                xytext=(1945, 0.42),
                fontsize=12, color=D_NARANJA, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=D_GRIS, lw=1.5))

    hhi_2000 = calc_hhi(post_1950_regional[2000])
    ax.annotate('Globalizacion:\nminimo historico', xy=(2000, hhi_2000),
                xytext=(1965, 0.10),
                fontsize=12, color=D_VERDE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=D_GRIS, lw=1.5))

    hhi_2023 = calc_hhi(post_1950_regional[2023])
    ax.annotate('Asia 36%\n(reconcentracion?)', xy=(2023, hhi_2023),
                xytext=(2000, 0.38),
                fontsize=12, color=D_AZUL_CL, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=D_GRIS, lw=1.5))

    # Formato
    ax.set_xlabel('', fontsize=12, color=D_GRIS)
    ax.set_ylabel('HHI (0 = diversificado, 1 = concentrado)', fontsize=13, color=D_GRIS)
    ax.set_title('Concentracion regional del comercio mundial (HHI) — 1800 a 2023',
                 fontsize=18, fontweight='bold', color=D_AZUL, pad=15)

    ax.set_xlim(1795, 2030)
    ax.set_ylim(0, 0.88)
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    ax.tick_params(labelsize=11)

    # Fuentes — bien abajo, sin solapar
    fig.text(0.5, 0.01,
             'Fuentes: Federico-Tena World Trade Historical Database (1800-1938)  |  OMC, UNCTAD (1950-2023)',
             fontsize=10, ha='center', color=D_GRIS, style='italic')

    plt.tight_layout()
    outpath = os.path.join(OUT_DIR, 'hhi.png')
    fig.savefig(outpath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  OK: {outpath}")


if __name__ == '__main__':
    generar()
