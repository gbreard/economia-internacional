"""
Script para generar gráficos de Balanza de Pagos y Tipo de Cambio
Para clases 1+2 combinadas
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Configuración
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

# Colores del tema UMET
AZUL_OSCURO = '#1F4E79'
AZUL_CLARO = '#0EA5E9'
GRIS = '#4B5563'
ROJO = '#DC2626'
VERDE = '#059669'
AMARILLO = '#F59E0B'

# Directorios
BASE_DIR = Path(__file__).parent.parent
DATOS_DIR = BASE_DIR / "datos"
GRAFICOS_DIR = BASE_DIR / "graficos"
GRAFICOS_DIR.mkdir(exist_ok=True)


def grafico_desequilibrios_globales():
    """Gráfico de cuenta corriente: EEUU, China, Alemania"""

    df = pd.read_csv(DATOS_DIR / "cuenta_corriente_fmi.csv")

    # Filtrar solo datos históricos (no proyecciones) y período relevante
    df = df[(df['anio'] >= 1980) & (df['anio'] <= 2024)]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Colores por país
    colores = {
        'Estados Unidos': ROJO,
        'China': AMARILLO,
        'Alemania': AZUL_CLARO
    }

    # Graficar cada país (excepto Argentina que va aparte)
    for pais in ['Estados Unidos', 'China', 'Alemania']:
        datos = df[df['pais'] == pais].sort_values('anio')
        ax.plot(datos['anio'], datos['cuenta_corriente_pib'],
                label=pais, color=colores[pais], linewidth=2.5)

    # Línea de cero
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)

    # Sombrear déficit vs superávit
    ax.axhspan(-15, 0, alpha=0.05, color=ROJO, label='_nolegend_')
    ax.axhspan(0, 15, alpha=0.05, color=VERDE, label='_nolegend_')

    # Anotaciones de eventos
    ax.annotate('Crisis\n2008', xy=(2008, -4.5), fontsize=9, ha='center', color=GRIS)
    ax.annotate('Pico China\n10% PIB', xy=(2007, 10), fontsize=9, ha='center', color=GRIS)

    # Formato
    ax.set_xlabel('Año', fontsize=12, color=GRIS)
    ax.set_ylabel('Cuenta Corriente (% PIB)', fontsize=12, color=GRIS)
    ax.set_title('Desequilibrios globales: Cuenta Corriente', fontsize=14,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    ax.legend(loc='lower left', frameon=True, fontsize=10)
    ax.set_xlim(1980, 2024)
    ax.set_ylim(-8, 12)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Texto interpretativo
    ax.text(1982, 10.5, 'SUPERÁVIT (presta al mundo)', fontsize=9, color=VERDE, alpha=0.7)
    ax.text(1982, -7, 'DÉFICIT (se endeuda)', fontsize=9, color=ROJO, alpha=0.7)

    plt.tight_layout()

    archivo = GRAFICOS_DIR / "desequilibrios_globales.png"
    plt.savefig(archivo, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Guardado: {archivo}")


def grafico_tcr_argentina():
    """Gráfico del tipo de cambio real multilateral Argentina"""

    df = pd.read_csv(DATOS_DIR / "itcrm_bcra.csv")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(df['anio'], df['itcrm'], color=AZUL_OSCURO, linewidth=2.5, marker='o', markersize=4)

    # Línea de referencia (100 = dic 2015)
    ax.axhline(y=100, color=GRIS, linestyle='--', linewidth=1, alpha=0.7)
    ax.text(2024.5, 102, 'Base=100\n(dic 2015)', fontsize=9, color=GRIS, va='bottom')

    # Sombrear zonas
    ax.axhspan(0, 100, alpha=0.05, color=ROJO)  # apreciado
    ax.axhspan(100, 200, alpha=0.05, color=VERDE)  # depreciado/competitivo

    # Anotaciones de eventos clave
    eventos = [
        (2002, 178, 'Crisis 2001\n+200%', 'above'),
        (1999, 66, 'Convertibilidad\n(apreciado)', 'below'),
        (2018, 97, 'Crisis\n2018', 'above'),
        (2024, 140, '2024', 'right')
    ]

    for anio, valor, texto, pos in eventos:
        if pos == 'above':
            ax.annotate(texto, xy=(anio, valor), xytext=(anio, valor+15),
                       fontsize=9, ha='center', color=GRIS,
                       arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.5))
        elif pos == 'below':
            ax.annotate(texto, xy=(anio, valor), xytext=(anio, valor-20),
                       fontsize=9, ha='center', color=GRIS,
                       arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.5))
        elif pos == 'right':
            ax.annotate(texto, xy=(anio, valor), xytext=(anio+1, valor),
                       fontsize=9, ha='left', color=GRIS)

    # Formato
    ax.set_xlabel('Año', fontsize=12, color=GRIS)
    ax.set_ylabel('ITCRM (Base dic 2015 = 100)', fontsize=12, color=GRIS)
    ax.set_title('Tipo de Cambio Real Multilateral - Argentina', fontsize=14,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    ax.set_xlim(1996, 2026)
    ax.set_ylim(40, 200)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Leyenda interpretativa
    ax.text(1998, 185, '↑ ITCRM alto = peso barato = más competitivo', fontsize=9, color=VERDE)
    ax.text(1998, 55, '↓ ITCRM bajo = peso caro = menos competitivo', fontsize=9, color=ROJO)

    plt.tight_layout()

    archivo = GRAFICOS_DIR / "tcr_argentina.png"
    plt.savefig(archivo, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Guardado: {archivo}")


def grafico_cc_argentina():
    """Gráfico de cuenta corriente Argentina"""

    df = pd.read_csv(DATOS_DIR / "cuenta_corriente_argentina.csv")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras coloreadas según superávit/déficit
    colores = [VERDE if x >= 0 else ROJO for x in df['cuenta_corriente_pib']]
    ax.bar(df['anio'], df['cuenta_corriente_pib'], color=colores, alpha=0.7, edgecolor='white')

    # Línea de cero
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)

    # Sombrear períodos
    # Convertibilidad (1991-2001)
    ax.axvspan(1991, 2001, alpha=0.1, color=AZUL_CLARO)
    ax.text(1996, 7.5, 'Convertibilidad', fontsize=9, ha='center', color=AZUL_OSCURO, alpha=0.7)

    # Post-crisis (2002-2008)
    ax.axvspan(2002, 2008, alpha=0.1, color=VERDE)
    ax.text(2005, 7.5, 'Post-crisis', fontsize=9, ha='center', color=VERDE, alpha=0.7)

    # Formato
    ax.set_xlabel('Año', fontsize=12, color=GRIS)
    ax.set_ylabel('Cuenta Corriente (% PIB)', fontsize=12, color=GRIS)
    ax.set_title('Cuenta Corriente - Argentina (1990-2024)', fontsize=14,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    ax.set_xlim(1989, 2025)
    ax.set_ylim(-8, 10)
    ax.grid(True, alpha=0.3, linestyle='--', axis='y')

    # Anotaciones
    ax.annotate('Crisis\n2001', xy=(2001, -1.4), xytext=(2001, -5),
               fontsize=9, ha='center', color=GRIS,
               arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.5))

    ax.annotate('Superávit\nrecord', xy=(2002, 8.6), xytext=(2004, 5),
               fontsize=9, ha='center', color=GRIS,
               arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.5))

    plt.tight_layout()

    archivo = GRAFICOS_DIR / "cc_argentina.png"
    plt.savefig(archivo, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Guardado: {archivo}")


def grafico_reservas_argentina():
    """Gráfico de reservas internacionales Argentina"""

    df = pd.read_csv(DATOS_DIR / "reservas_bcra.csv")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.fill_between(df['anio'], df['reservas_usd_bn'], alpha=0.3, color=AZUL_CLARO)
    ax.plot(df['anio'], df['reservas_usd_bn'], color=AZUL_OSCURO, linewidth=2.5)

    # Marcar puntos clave manualmente (más relevante pedagógicamente)
    # Mínimo crisis 2002
    ax.scatter([2002], [10.5], color=ROJO, s=100, zorder=5)
    # Máximo 2018 (préstamo FMI)
    ax.scatter([2018], [66.0], color=VERDE, s=100, zorder=5)
    # Mínimo reciente 2023
    ax.scatter([2023], [23.1], color=ROJO, s=80, zorder=5)

    # Anotaciones de eventos
    eventos = [
        (2002, 10.5, 'Crisis 2002\nMínimo US$ 10.5 bn', 'below'),
        (2007, 46.2, 'Acumulación\npost-crisis', 'above'),
        (2018, 66, 'Máximo\n(préstamo FMI)', 'above'),
        (2023, 23.1, 'Mínimo\n2023', 'below'),
    ]

    for anio, valor, texto, pos in eventos:
        offset = 10 if pos == 'above' else -12
        ax.annotate(texto, xy=(anio, valor), xytext=(anio, valor+offset),
                   fontsize=9, ha='center', color=GRIS,
                   arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.5))

    # Formato
    ax.set_xlabel('Año', fontsize=12, color=GRIS)
    ax.set_ylabel('Reservas (miles de millones USD)', fontsize=12, color=GRIS)
    ax.set_title('Reservas Internacionales - Argentina', fontsize=14,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    ax.set_xlim(1989, 2025)
    ax.set_ylim(0, 75)
    ax.grid(True, alpha=0.3, linestyle='--')

    plt.tight_layout()

    archivo = GRAFICOS_DIR / "reservas_argentina.png"
    plt.savefig(archivo, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Guardado: {archivo}")


if __name__ == "__main__":
    print("=" * 50)
    print("Generando gráficos para clase 1+2")
    print("=" * 50)

    grafico_desequilibrios_globales()
    grafico_tcr_argentina()
    grafico_cc_argentina()
    grafico_reservas_argentina()

    print()
    print("=" * 50)
    print("Gráficos guardados en:", GRAFICOS_DIR)
    print("=" * 50)
