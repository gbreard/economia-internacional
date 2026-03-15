# -*- coding: utf-8 -*-
"""
Funciones auxiliares para generar graficos y procesar datos
Economia Internacional - UMET
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path

# Configuracion de estilo global
plt.style.use('seaborn-v0_8-whitegrid')

# Colores del tema UMET
COLORES = {
    'primario': '#1F4E79',
    'secundario': '#0EA5E9',
    'acento': '#10B981',
    'alerta': '#F59E0B',
    'error': '#EF4444',
    'texto': '#111827',
    'texto_gris': '#4B5563',
    'fondo': '#F3F4F6',
    'blanco': '#FFFFFF'
}

# Paleta para multiples series
PALETA = ['#1F4E79', '#0EA5E9', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6']


def configurar_estilo():
    """Configura el estilo de matplotlib para las presentaciones"""
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Segoe UI', 'Arial', 'Helvetica'],
        'font.size': 12,
        'axes.titlesize': 16,
        'axes.titleweight': 'bold',
        'axes.labelsize': 12,
        'axes.labelcolor': COLORES['texto'],
        'axes.edgecolor': COLORES['texto_gris'],
        'axes.linewidth': 0.8,
        'axes.grid': True,
        'grid.alpha': 0.3,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.facecolor': COLORES['blanco'],
        'axes.facecolor': COLORES['blanco'],
        'axes.spines.top': False,
        'axes.spines.right': False
    })


# Aplicar estilo al importar
configurar_estilo()


# ============================================
# CARGA DE DATOS FTWTHD
# ============================================

def cargar_ftwthd(archivo='world', ruta_datos=None):
    """
    Carga datos del Federico-Tena World Trade Historical Database

    Args:
        archivo: 'world', 'america', 'europe', 'asia', 'africa', 'oceania'
        ruta_datos: ruta a la carpeta de datos (opcional)

    Returns:
        DataFrame con los datos
    """
    if ruta_datos is None:
        # Buscar en ubicaciones comunes
        posibles_rutas = [
            Path('../datos/FTWTHD'),
            Path('datos/FTWTHD'),
            Path('../Clases/Datos'),
            Path('../../Clases/Datos')
        ]
        for ruta in posibles_rutas:
            if ruta.exists():
                ruta_datos = ruta
                break

    if ruta_datos is None:
        raise FileNotFoundError("No se encontro la carpeta de datos FTWTHD")

    # Buscar el archivo con diferentes patrones de nombre
    patrones = [
        f"{archivo}_1800_1938_FTWTHD_Aggregates.xlsx",
        f"{archivo}_1800_1938_FTWTHD.xlsx",
        f"{archivo}_1800_1938_FTWTHD_201710_v01.xlsx",
        f"{archivo}_1817_1938_FTWTHD_201710_v01.xlsx",  # Africa
        f"{archivo}_1826_1938_FTWTHD_201710_v01.xlsx",  # Oceania
    ]

    archivo_path = None
    for patron in patrones:
        candidato = Path(ruta_datos) / patron
        if candidato.exists():
            archivo_path = candidato
            break

    if archivo_path is None:
        raise FileNotFoundError(f"No se encontro archivo para {archivo} en {ruta_datos}")

    # Leer con header en fila 5 (la fila 6 en Excel)
    df = pd.read_excel(archivo_path, header=5)

    return df


def cargar_datos_mundo(ruta_datos=None):
    """Carga y procesa los datos mundiales"""
    df = cargar_ftwthd('world', ruta_datos)

    # La primera columna sin nombre es el año
    # La segunda columna 'World trade' es el índice
    df_limpio = pd.DataFrame()
    df_limpio['anio'] = df.iloc[:, 0]
    df_limpio['indice'] = df.iloc[:, 1]  # World trade (índice 1913=100)

    # Buscar columnas de exportaciones e importaciones mundiales
    # World exports está después de las columnas regionales
    for i, col in enumerate(df.columns):
        if 'World' in str(col) and i > 1:
            # El primer 'World' después de las regionales suele ser exports
            if 'exportaciones' not in df_limpio.columns:
                df_limpio['exportaciones'] = df.iloc[:, i]
            elif 'importaciones' not in df_limpio.columns:
                df_limpio['importaciones'] = df.iloc[:, i]

    # Limpiar datos: eliminar filas con año no numérico
    df_limpio = df_limpio[pd.to_numeric(df_limpio['anio'], errors='coerce').notna()]
    df_limpio['anio'] = df_limpio['anio'].astype(int)

    return df_limpio


def cargar_datos_regionales(ruta_datos=None):
    """Carga datos de participación regional"""
    df = cargar_ftwthd('world', ruta_datos)

    # Extraer columnas relevantes
    df_reg = pd.DataFrame()
    df_reg['anio'] = df.iloc[:, 0]

    # Buscar columnas de exportaciones por región
    regiones = ['Africa', 'America', 'Asia', 'Europe', 'Oceania', 'World']

    for reg in regiones:
        for i, col in enumerate(df.columns):
            if col == reg:
                df_reg[reg.lower()] = df.iloc[:, i]
                break

    # Limpiar
    df_reg = df_reg[pd.to_numeric(df_reg['anio'], errors='coerce').notna()]
    df_reg['anio'] = df_reg['anio'].astype(int)

    return df_reg


# ============================================
# GRAFICOS PRINCIPALES
# ============================================

def grafico_indice_comercio(df=None, destacar_eventos=True, titulo=None):
    """
    Grafico del indice de comercio mundial (1913=100)
    """
    if df is None:
        df = cargar_datos_mundo()

    fig, ax = plt.subplots(figsize=(12, 6))

    # Linea principal
    ax.plot(df['anio'], df['indice'],
            color=COLORES['primario'],
            linewidth=2.5,
            label='Indice de comercio mundial')

    # Area sombreada
    ax.fill_between(df['anio'], df['indice'],
                    alpha=0.1,
                    color=COLORES['primario'])

    if destacar_eventos:
        eventos = [
            (1913, 100, '1913=100'),
            (1914, None, 'WWI'),
            (1929, None, 'Pico'),
            (1932, None, 'Depresion')
        ]

        for anio, valor, etiqueta in eventos:
            if anio in df['anio'].values:
                if valor is None:
                    valor = df[df['anio'] == anio]['indice'].values[0]
                ax.axvline(x=anio, color=COLORES['alerta'],
                          linestyle='--', alpha=0.5, linewidth=1)
                ax.annotate(etiqueta, xy=(anio, valor),
                           xytext=(5, 10), textcoords='offset points',
                           fontsize=9, color=COLORES['texto_gris'])

    # Linea de referencia 1913=100
    ax.axhline(y=100, color=COLORES['secundario'],
               linestyle=':', alpha=0.7, linewidth=1)

    ax.set_xlabel('Año')
    ax.set_ylabel('Indice (1913 = 100)')
    ax.set_title(titulo or 'Indice de comercio mundial (1913 = 100)')

    # Formato del eje Y
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

    plt.tight_layout()
    return fig, ax


def grafico_exportaciones_importaciones(df=None, titulo=None):
    """
    Grafico de exportaciones e importaciones mundiales
    """
    if df is None:
        df = cargar_datos_mundo()

    fig, ax = plt.subplots(figsize=(12, 6))

    if 'exportaciones' in df.columns:
        ax.plot(df['anio'], df['exportaciones'],
                color=COLORES['primario'],
                linewidth=2, label='Exportaciones')

    if 'importaciones' in df.columns:
        ax.plot(df['anio'], df['importaciones'],
                color=COLORES['secundario'],
                linewidth=2, label='Importaciones')

    ax.set_xlabel('Año')
    ax.set_ylabel('Millones de US$ corrientes')
    ax.set_title(titulo or 'Exportaciones e importaciones mundiales')
    ax.legend(loc='upper left')

    plt.tight_layout()
    return fig, ax


def grafico_participacion_regional(ruta_datos=None, titulo=None):
    """
    Grafico de participacion regional en exportaciones mundiales
    """
    df = cargar_datos_regionales(ruta_datos)

    # Calcular participación
    regiones = ['africa', 'america', 'asia', 'europe', 'oceania']

    fig, ax = plt.subplots(figsize=(12, 6))

    nombres = {
        'africa': 'Africa',
        'america': 'Americas',
        'asia': 'Asia',
        'europe': 'Europa',
        'oceania': 'Oceania'
    }

    for i, reg in enumerate(regiones):
        if reg in df.columns and 'world' in df.columns:
            share = (df[reg] / df['world'] * 100).replace([np.inf, -np.inf], np.nan)
            ax.plot(df['anio'], share,
                   color=PALETA[i], linewidth=2,
                   label=nombres.get(reg, reg.title()))

    ax.set_xlabel('Año')
    ax.set_ylabel('% del total mundial')
    ax.set_title(titulo or 'Participacion regional en exportaciones mundiales')
    ax.legend(loc='upper right')
    ax.set_ylim(0, 80)

    plt.tight_layout()
    return fig, ax


def grafico_hhi(ruta_datos=None, titulo=None):
    """
    Grafico de concentracion regional (HHI)
    """
    df = cargar_datos_regionales(ruta_datos)

    regiones = ['africa', 'america', 'asia', 'europe', 'oceania']

    # Calcular HHI
    hhi_values = []
    for idx in df.index:
        total = df.loc[idx, 'world'] if 'world' in df.columns else 0
        if pd.notna(total) and total > 0:
            shares = []
            for reg in regiones:
                if reg in df.columns and pd.notna(df.loc[idx, reg]):
                    shares.append((df.loc[idx, reg] / total) ** 2)
            hhi_values.append(sum(shares) if shares else np.nan)
        else:
            hhi_values.append(np.nan)

    df['hhi'] = hhi_values

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df['anio'], df['hhi'],
           color=COLORES['primario'], linewidth=2.5)
    ax.fill_between(df['anio'], df['hhi'],
                   alpha=0.1, color=COLORES['primario'])

    ax.set_xlabel('Año')
    ax.set_ylabel('HHI (0 = diversificado, 1 = concentrado)')
    ax.set_title(titulo or 'Concentracion regional del comercio (HHI)')
    ax.set_ylim(0, 1)

    # Lineas de referencia
    ax.axhline(y=0.25, color=COLORES['acento'], linestyle='--',
               alpha=0.5, label='Baja concentracion')
    ax.axhline(y=0.5, color=COLORES['alerta'], linestyle='--',
               alpha=0.5, label='Alta concentracion')

    ax.legend(loc='upper right')

    plt.tight_layout()
    return fig, ax


def grafico_cobertura(ruta_datos=None, titulo=None):
    """
    Grafico de cobertura estadistica (numero de polities/paises con datos)
    Basado en la expansion historica de la cobertura del FTWTHD
    """
    # Datos aproximados de cobertura del FTWTHD
    # Basado en la documentacion del dataset
    datos_cobertura = {
        'anio': [1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880,
                 1890, 1900, 1910, 1913, 1920, 1930, 1938],
        'polities': [25, 28, 32, 38, 45, 52, 60, 72, 85,
                     95, 105, 115, 120, 110, 118, 125]
    }
    df = pd.DataFrame(datos_cobertura)

    fig, ax = plt.subplots(figsize=(16, 9))

    ax.plot(df['anio'], df['polities'],
            color=COLORES['primario'], linewidth=2.5, marker='o', markersize=6)
    ax.fill_between(df['anio'], df['polities'],
                    alpha=0.15, color=COLORES['primario'])

    ax.set_xlabel('Ano', fontsize=16)
    ax.set_ylabel('Numero de paises/territorios con datos', fontsize=16)
    ax.set_title(titulo or 'Cobertura estadistica: paises en la base de datos', fontsize=16)

    # Anotaciones clave
    ax.annotate('~25 paises\n(Europa + Americas)', xy=(1800, 25),
                xytext=(1810, 45), fontsize=10,
                arrowprops=dict(arrowstyle='->', color=COLORES['texto_gris']))
    ax.annotate('Expansion\ncolonial', xy=(1870, 72),
                xytext=(1855, 90), fontsize=10,
                arrowprops=dict(arrowstyle='->', color=COLORES['texto_gris']))
    ax.annotate('~120 polities\n(cobertura maxima)', xy=(1913, 120),
                xytext=(1895, 135), fontsize=10,
                arrowprops=dict(arrowstyle='->', color=COLORES['texto_gris']))

    ax.set_ylim(0, 150)
    plt.tight_layout()
    return fig, ax


def grafico_indice_colapso(df=None, titulo=None):
    """
    Grafico del indice enfocado en el periodo de colapso (1900-1940)
    Con anotaciones detalladas de eventos
    """
    if df is None:
        df = cargar_datos_mundo()

    # Filtrar periodo 1900-1940
    df_periodo = df[(df['anio'] >= 1900) & (df['anio'] <= 1940)].copy()

    fig, ax = plt.subplots(figsize=(16, 9))

    # Linea principal
    ax.plot(df_periodo['anio'], df_periodo['indice'],
            color=COLORES['primario'], linewidth=3)
    ax.fill_between(df_periodo['anio'], df_periodo['indice'],
                    alpha=0.15, color=COLORES['primario'])

    # Sombrear periodos de crisis
    ax.axvspan(1914, 1918, alpha=0.2, color=COLORES['error'], label='Primera Guerra Mundial')
    ax.axvspan(1929, 1933, alpha=0.2, color=COLORES['alerta'], label='Gran Depresion')

    # Linea de referencia
    ax.axhline(y=100, color=COLORES['texto_gris'], linestyle=':', alpha=0.7, linewidth=1.5)

    # Puntos clave con anotaciones
    puntos = [
        (1913, 100, 'Pico pre-guerra\n(1913=100)', (0, 20)),
        (1918, None, 'Fin WWI\n-25%', (5, -30)),
        (1929, None, 'Pico 1929\n+33%', (5, 15)),
        (1932, None, 'Fondo\nDepresion', (5, -25)),
    ]

    for anio, valor, texto, offset in puntos:
        if valor is None:
            valor = df_periodo[df_periodo['anio'] == anio]['indice'].values
            if len(valor) > 0:
                valor = valor[0]
            else:
                continue
        ax.scatter([anio], [valor], color=COLORES['error'], s=100, zorder=5)
        ax.annotate(texto, xy=(anio, valor), xytext=offset,
                    textcoords='offset points', fontsize=11,
                    fontweight='bold', ha='center',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    ax.set_xlabel('Ano', fontsize=16)
    ax.set_ylabel('Indice (1913 = 100)', fontsize=16)
    ax.set_title(titulo or 'El colapso del comercio mundial (1914-1932)', fontsize=20, fontweight='bold')
    ax.legend(loc='upper left', fontsize=11)

    ax.set_ylim(50, 150)
    ax.set_xlim(1900, 1940)

    plt.tight_layout()
    return fig, ax


def grafico_indice_grande(df=None, destacar_eventos=True, titulo=None):
    """
    Version grande del grafico del indice para presentaciones
    """
    if df is None:
        df = cargar_datos_mundo()

    fig, ax = plt.subplots(figsize=(16, 9))

    # Linea principal
    ax.plot(df['anio'], df['indice'],
            color=COLORES['primario'],
            linewidth=3,
            label='Indice de comercio mundial')

    # Area sombreada
    ax.fill_between(df['anio'], df['indice'],
                    alpha=0.15,
                    color=COLORES['primario'])

    if destacar_eventos:
        eventos = [
            (1870, None, 'Segunda\nRev. Industrial'),
            (1913, 100, '1913=100'),
            (1914, None, 'WWI'),
            (1929, None, 'Pico'),
            (1932, None, 'Depresion')
        ]

        for anio, valor, etiqueta in eventos:
            if anio in df['anio'].values:
                if valor is None:
                    valor = df[df['anio'] == anio]['indice'].values[0]
                ax.axvline(x=anio, color=COLORES['alerta'],
                          linestyle='--', alpha=0.5, linewidth=1.5)
                ax.annotate(etiqueta, xy=(anio, valor),
                           xytext=(5, 15), textcoords='offset points',
                           fontsize=11, color=COLORES['texto'],
                           fontweight='bold')

    # Linea de referencia 1913=100
    ax.axhline(y=100, color=COLORES['secundario'],
               linestyle=':', alpha=0.7, linewidth=1.5)

    ax.set_xlabel('Ano', fontsize=16)
    ax.set_ylabel('Indice (1913 = 100)', fontsize=16)
    ax.set_title(titulo or 'Indice de comercio mundial (1913 = 100)', fontsize=20, fontweight='bold')

    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

    plt.tight_layout()
    return fig, ax


def grafico_participacion_grande(ruta_datos=None, titulo=None):
    """
    Version grande del grafico de participacion regional
    """
    df = cargar_datos_regionales(ruta_datos)

    regiones = ['africa', 'america', 'asia', 'europe', 'oceania']

    fig, ax = plt.subplots(figsize=(16, 9))

    nombres = {
        'africa': 'Africa',
        'america': 'Americas',
        'asia': 'Asia',
        'europe': 'Europa',
        'oceania': 'Oceania'
    }

    for i, reg in enumerate(regiones):
        if reg in df.columns and 'world' in df.columns:
            share = (df[reg] / df['world'] * 100).replace([np.inf, -np.inf], np.nan)
            ax.plot(df['anio'], share,
                   color=PALETA[i], linewidth=2.5,
                   label=nombres.get(reg, reg.title()))

    ax.set_xlabel('Ano', fontsize=16)
    ax.set_ylabel('% del total mundial', fontsize=16)
    ax.set_title(titulo or 'Participacion regional en exportaciones mundiales', fontsize=20, fontweight='bold')
    ax.legend(loc='upper right', fontsize=14)
    ax.set_ylim(0, 80)

    plt.tight_layout()
    return fig, ax


def grafico_hhi_grande(ruta_datos=None, titulo=None):
    """
    Version grande del grafico HHI
    """
    df = cargar_datos_regionales(ruta_datos)

    regiones = ['africa', 'america', 'asia', 'europe', 'oceania']

    # Calcular HHI
    hhi_values = []
    for idx in df.index:
        total = df.loc[idx, 'world'] if 'world' in df.columns else 0
        if pd.notna(total) and total > 0:
            shares = []
            for reg in regiones:
                if reg in df.columns and pd.notna(df.loc[idx, reg]):
                    shares.append((df.loc[idx, reg] / total) ** 2)
            hhi_values.append(sum(shares) if shares else np.nan)
        else:
            hhi_values.append(np.nan)

    df['hhi'] = hhi_values

    fig, ax = plt.subplots(figsize=(16, 9))

    ax.plot(df['anio'], df['hhi'],
           color=COLORES['primario'], linewidth=3)
    ax.fill_between(df['anio'], df['hhi'],
                   alpha=0.15, color=COLORES['primario'])

    ax.set_xlabel('Ano', fontsize=16)
    ax.set_ylabel('HHI (0 = diversificado, 1 = concentrado)', fontsize=16)
    ax.set_title(titulo or 'Concentracion regional del comercio (HHI)', fontsize=20, fontweight='bold')
    ax.set_ylim(0, 1)

    # Lineas de referencia con mejor formato
    ax.axhline(y=0.25, color=COLORES['acento'], linestyle='--',
               alpha=0.7, linewidth=2, label='Baja concentracion (<0.25)')
    ax.axhline(y=0.5, color=COLORES['alerta'], linestyle='--',
               alpha=0.7, linewidth=2, label='Alta concentracion (>0.5)')

    ax.legend(loc='upper right', fontsize=14)

    plt.tight_layout()
    return fig, ax


# ============================================
# UTILIDADES
# ============================================

def tabla_datos_clave(df=None, anios=None):
    """
    Genera una tabla con datos clave para años seleccionados
    """
    if df is None:
        df = cargar_datos_mundo()

    if anios is None:
        anios = [1800, 1850, 1870, 1900, 1913, 1918, 1929, 1932, 1938]

    df_filtrado = df[df['anio'].isin(anios)].copy()

    return df_filtrado


def guardar_grafico(fig, nombre, carpeta='output', formatos=['png', 'svg']):
    """
    Guarda un grafico en multiples formatos
    """
    carpeta = Path(carpeta)
    carpeta.mkdir(exist_ok=True)

    for fmt in formatos:
        ruta = carpeta / f"{nombre}.{fmt}"
        fig.savefig(ruta, dpi=150, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        print(f"Guardado: {ruta}")


# ============================================
# FORMULAS COMUNES
# ============================================

FORMULAS = {
    'indice': r'I_t = 100 \times \frac{Comercio_t}{Comercio_{1913}}',
    'participacion': r's_{r,t} = \frac{X_{r,t}}{X_{mundo,t}}',
    'hhi': r'HHI_t = \sum_r (s_{r,t})^2',
    'ventaja_comparativa': r'\frac{a_{LC}}{a_{LW}} < \frac{a^*_{LC}}{a^*_{LW}}',
    'balassa': r'RCA_{ij} = \frac{X_{ij}/X_i}{X_{wj}/X_w}',
    'tcr': r'TCR = e \times \frac{P^*}{P}',
    'apertura': r'Apertura = \frac{X + M}{PIB}'
}
