"""
Genera 4 gráficos para la Etapa 5: Globalización financiera (1980-hoy)
1. Apertura comercial mundial con 3 fases (globalización → hiper → slowbalization)
2. Ascenso de China en exportaciones mundiales
3. Caída de costos de transporte y comunicación
4. Flujos de IED global
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import numpy as np
import os, sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Estilo compartido ──────────────────────────────────────────
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#7F8C8D'
AMARILLO    = '#F1C40F'
MORADO      = '#8E44AD'
ROJO_CHINA  = '#DE2910'

def estilo_base(fig, ax, fuente_texto):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.tick_params(colors='#555555', labelsize=10)
    ax.grid(axis='y', alpha=0.3, color='#CCCCCC')
    fig.text(0.5, 0.01, fuente_texto, ha='center', fontsize=8, color='#888888', style='italic')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 1: Apertura comercial con 3 fases
# ═══════════════════════════════════════════════════════════════
def grafico_apertura_fases():
    # Comercio (X+M) como % del PIB mundial
    # Fuente: Banco Mundial (NE.TRD.GNFS.ZS), FMI
    years = list(range(1960, 2024))

    # Datos aproximados del Banco Mundial / FMI
    trade_gdp = [
        24.0, 23.8, 23.5, 24.0, 24.2, 24.0, 24.5, 24.3, 25.0, 25.5,  # 1960-69
        26.0, 26.3, 27.0, 29.5, 33.0, 32.5, 33.0, 33.5, 33.0, 34.5,  # 1970-79
        35.5, 35.0, 33.5, 32.5, 33.5, 33.0, 32.5, 33.5, 33.8, 35.5,  # 1980-89
        36.0, 36.5, 37.0, 37.5, 38.5, 40.0, 41.0, 43.0, 44.0, 45.5,  # 1990-99
        47.5, 46.5, 46.0, 47.0, 50.0, 52.5, 55.0, 56.5, 60.5, 52.0,  # 2000-09
        56.0, 58.5, 57.5, 57.0, 57.5, 56.5, 53.5, 55.5, 57.5, 56.0,  # 2010-19
        51.5, 55.0, 58.0, 56.5                                          # 2020-23
    ]

    fig, ax = plt.subplots(figsize=(12, 6.5))

    # Fases con colores de fondo
    # Fase 1: Globalización lenta (1960-1986)
    ax.axvspan(1960, 1986, alpha=0.08, color=AZUL_CLARO, zorder=0)
    # Fase 2: Hiperglobalización (1986-2008)
    ax.axvspan(1986, 2008, alpha=0.08, color=VERDE, zorder=0)
    # Fase 3: Slowbalization (2008-hoy)
    ax.axvspan(2008, 2024, alpha=0.08, color=NARANJA, zorder=0)

    # Línea principal
    ax.plot(years, trade_gdp, color=AZUL_OSCURO, linewidth=2.5, zorder=5)
    ax.fill_between(years, trade_gdp, alpha=0.1, color=AZUL_MEDIO)

    # Etiquetas de fases
    ax.text(1973, 20, 'Globalización\n(+0.19 pp/año)', ha='center', fontsize=10,
            color=AZUL_MEDIO, fontweight='bold')
    ax.text(1997, 20, 'Hiperglobalización\n(+0.52 pp/año)', ha='center', fontsize=10,
            color=VERDE, fontweight='bold')
    ax.text(2016, 20, 'Slowbalization\n(−0.04 pp/año)', ha='center', fontsize=10,
            color=NARANJA, fontweight='bold')

    # Eventos clave
    eventos = [
        (1986, 'Ronda Uruguay\ncomienza', VERDE),
        (2001, 'China\nen OMC', ROJO_CHINA),
        (2008, 'Crisis\nfinanciera', ROJO),
        (2018, 'Guerra\ncomercial', NARANJA),
    ]
    for yr, txt, color in eventos:
        idx = yr - 1960
        val = trade_gdp[idx] if idx < len(trade_gdp) else trade_gdp[-1]
        ax.axvline(x=yr, color=color, linestyle=':', alpha=0.4, linewidth=1)
        ax.annotate(txt, xy=(yr, val), xytext=(yr, val + 5),
                   fontsize=8, color=color, ha='center', fontweight='bold',
                   arrowprops=dict(arrowstyle='->', color=color, lw=1))

    ax.set_title('Apertura comercial mundial: tres fases de la globalización',
                fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('Comercio (X+M) como % del PIB mundial', fontsize=11)
    ax.set_xlim(1960, 2024)
    ax.set_ylim(15, 68)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}%'))

    estilo_base(fig, ax, 'Fuente: Banco Mundial, FMI — "Charting Globalization\'s Turn to Slowbalization" (2023)')

    path = os.path.join(OUTPUT_DIR, 'apertura_comercial_fases.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 2: Ascenso de China
# ═══════════════════════════════════════════════════════════════
def grafico_china_exportaciones():
    # Participación de China en exportaciones mundiales de mercancías (%)
    # Fuente: OMC, UNCTAD, Banco Mundial (WITS)
    years = list(range(1980, 2024))

    china_share = [
        0.9, 1.0, 1.1, 1.1, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8,  # 1980-89
        1.8, 2.0, 2.2, 2.4, 2.7, 2.9, 2.8, 3.2, 3.3, 3.4,   # 1990-99
        3.9, 4.3, 5.0, 5.8, 6.5, 7.3, 8.0, 8.7, 8.9, 9.6,   # 2000-09
        10.3, 10.4, 11.1, 11.7, 12.3, 13.7, 13.1, 12.8, 12.7, 13.1,  # 2010-19
        14.7, 15.1, 14.4, 14.2                                  # 2020-23
    ]

    # EEUU para comparación
    eeuu_share = [
        11.0, 11.5, 10.8, 10.5, 11.0, 10.5, 10.0, 10.0, 11.0, 11.5,  # 1980-89
        11.3, 11.8, 11.5, 12.0, 11.8, 11.3, 11.5, 12.0, 12.0, 11.5,  # 1990-99
        12.3, 11.8, 10.8, 9.8, 9.0, 8.7, 8.6, 8.3, 8.1, 8.5,         # 2000-09
        8.4, 8.1, 8.4, 8.4, 8.5, 9.1, 9.1, 8.7, 8.5, 8.6,            # 2010-19
        7.9, 7.9, 8.0, 8.3                                              # 2020-23
    ]

    fig, ax = plt.subplots(figsize=(11, 6.5))

    # China
    ax.fill_between(years, china_share, alpha=0.15, color=ROJO_CHINA)
    ax.plot(years, china_share, color=ROJO_CHINA, linewidth=2.5, label='China', zorder=5)

    # EEUU
    ax.plot(years, eeuu_share, color=AZUL_OSCURO, linewidth=2, linestyle='--',
            label='EEUU', zorder=5, alpha=0.8)

    # Marcar entrada a la OMC
    ax.axvline(x=2001, color=ROJO_CHINA, linestyle=':', alpha=0.6, linewidth=2)
    ax.annotate('China entra\na la OMC\n(2001)', xy=(2001, 4.3), xytext=(1993, 8),
               fontsize=10, color=ROJO_CHINA, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=ROJO_CHINA, lw=1.5),
               bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0', edgecolor=ROJO_CHINA, alpha=0.9))

    # Cruce de líneas
    ax.annotate('China supera\na EEUU (~2009)', xy=(2009, 9.6), xytext=(2013, 6),
               fontsize=9, color='#555555', fontweight='bold',
               arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Valores extremos
    ax.text(1982, 1.5, '0.9%\n(1980)', fontsize=8.5, color=ROJO_CHINA, ha='center')
    ax.text(2021, 15.8, '15.1%\n(2021)', fontsize=9, color=ROJO_CHINA, ha='center', fontweight='bold')

    ax.set_title('El ascenso de China: de actor marginal a "fábrica del mundo"',
                fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('Participación en exportaciones mundiales (%)', fontsize=11)
    ax.legend(loc='center left', fontsize=11, framealpha=0.9)
    ax.set_xlim(1979, 2025)
    ax.set_ylim(0, 18)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}%'))

    estilo_base(fig, ax, 'Fuente: OMC, UNCTAD — Participación en exportaciones mundiales de mercancías')

    path = os.path.join(OUTPUT_DIR, 'china_exportaciones.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 3: Costos de transporte y comunicación
# ═══════════════════════════════════════════════════════════════
def grafico_costos_transporte():
    # Índices de costo (1930 = 100)
    # Fuente: Our World in Data, basado en Bureau of Transportation Statistics (EEUU)

    # Flete marítimo (índice real)
    years_sea = [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2005]
    sea_freight = [100, 90, 65, 48, 35, 30, 28, 23, 11]

    # Transporte aéreo (ingreso por pasajero-milla, ajustado)
    years_air = [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2005]
    air_transport = [100, 85, 55, 38, 24, 20, 14, 10, 8]

    # Llamada telefónica internacional (3 min NY-Londres)
    years_phone = [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2005]
    phone_cost = [100, 80, 50, 25, 10, 5, 2.5, 0.5, 0.1]

    # Container (costo por TEU, índice)
    years_container = [1956, 1960, 1970, 1980, 1990, 2000, 2005]
    container_cost = [100, 70, 40, 25, 18, 12, 8]

    fig, ax = plt.subplots(figsize=(11, 6.5))

    ax.plot(years_sea, sea_freight, color=AZUL_OSCURO, linewidth=2.5, marker='o', markersize=5,
            label='Flete marítimo', zorder=5)
    ax.plot(years_air, air_transport, color=NARANJA, linewidth=2.5, marker='s', markersize=5,
            label='Transporte aéreo', zorder=5)
    ax.plot(years_phone, phone_cost, color=VERDE, linewidth=2.5, marker='^', markersize=5,
            label='Llamada telefónica (NY-Londres)', zorder=5)
    ax.plot(years_container, container_cost, color=ROJO, linewidth=2, marker='D', markersize=5,
            label='Container (desde 1956)', linestyle='--', zorder=5)

    # Anotación sobre telecomunicaciones
    ax.annotate('Telecomunicaciones:\ncosto → 0', xy=(2000, 0.5), xytext=(1985, 30),
               fontsize=9, color=VERDE, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=VERDE, lw=1.2))

    # Marcar la era de globalización financiera
    ax.axvspan(1980, 2005, alpha=0.06, color=AZUL_CLARO, zorder=0)
    ax.text(1992, 95, 'Era de la globalización', fontsize=10, ha='center',
            color=AZUL_MEDIO, fontweight='bold', alpha=0.7)

    ax.set_title('Caída de los costos de transporte y comunicación',
                fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('Índice de costo (1930 = 100)', fontsize=11)
    ax.legend(loc='upper right', fontsize=9.5, framealpha=0.9)
    ax.set_xlim(1928, 2008)
    ax.set_ylim(-3, 110)

    # Nota explicativa
    ax.text(0.02, 0.15, 'Sin esta revolución tecnológica,\nlas cadenas globales de valor\nno serían posibles',
            transform=ax.transAxes, fontsize=9, color='#555555',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F9F9F9', edgecolor='#CCCCCC'))

    estilo_base(fig, ax, 'Fuente: Our World in Data, Bureau of Transportation Statistics (EEUU) — Índices reales')

    path = os.path.join(OUTPUT_DIR, 'costos_transporte_comunicacion.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 4: Flujos de IED global
# ═══════════════════════════════════════════════════════════════
def grafico_ied_global():
    # Flujos de IED global (inflows, miles de millones USD corrientes)
    # Fuente: UNCTAD World Investment Report
    years = list(range(1980, 2024))

    # IED total mundial (inflows, bn USD)
    ied_desarrollados = [
        42, 38, 30, 28, 30, 32, 50, 80, 100, 130,     # 1980-89
        150, 100, 95, 120, 130, 200, 220, 260, 470, 800,  # 1990-99
        1100, 550, 460, 360, 380, 560, 830, 1200, 900, 530,  # 2000-09
        600, 700, 500, 560, 490, 920, 1000, 710, 540, 750,   # 2010-19
        280, 720, 370, 500                                     # 2020-23
    ]

    ied_en_desarrollo = [
        12, 15, 18, 14, 17, 15, 20, 25, 30, 35,       # 1980-89
        40, 45, 55, 80, 100, 115, 140, 175, 180, 210,  # 1990-99
        260, 220, 200, 190, 280, 350, 400, 520, 580, 470,  # 2000-09
        590, 650, 660, 640, 680, 740, 620, 680, 670, 720,  # 2010-19
        660, 830, 910, 840                                   # 2020-23
    ]

    ied_total = [d + e for d, e in zip(ied_desarrollados, ied_en_desarrollo)]

    fig, ax = plt.subplots(figsize=(12, 6.5))

    # Áreas apiladas
    ax.fill_between(years, ied_desarrollados, alpha=0.4, color=AZUL_MEDIO, label='Países desarrollados')
    ax.fill_between(years, ied_desarrollados, ied_total, alpha=0.4, color=NARANJA, label='Países en desarrollo')

    ax.plot(years, ied_total, color=AZUL_OSCURO, linewidth=2, zorder=5, label='Total mundial')

    # Eventos clave
    eventos = [
        (1990, 'Caída del\nMuro', GRIS),
        (2001, 'Burbuja\npunto com', ROJO),
        (2008, 'Crisis\nfinanciera', ROJO),
        (2020, 'COVID-19', ROJO),
    ]
    for yr, txt, color in eventos:
        ax.axvline(x=yr, color=color, linestyle=':', alpha=0.4, linewidth=1)
        idx = yr - 1980
        val = ied_total[idx] if idx < len(ied_total) else ied_total[-1]
        ax.text(yr, val + 80, txt, fontsize=8, color=color, ha='center', fontweight='bold')

    # Anotar el pico de 2007
    ax.annotate(f'Pico: ${int(ied_total[27])}B\n(2007)', xy=(2007, ied_total[27]),
               xytext=(2000, 1900), fontsize=9, color=AZUL_OSCURO, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=1.2))

    # Nota sobre países en desarrollo
    ax.text(0.72, 0.55, 'Los países en desarrollo\npasan de 20% (1980)\na >50% (2020s)\nde la IED mundial',
            transform=ax.transAxes, fontsize=9, color=NARANJA, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF5EB', edgecolor=NARANJA, alpha=0.9))

    ax.set_title('Flujos de Inversión Extranjera Directa global',
                fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('IED (inflows, miles de millones USD)', fontsize=11)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.set_xlim(1979, 2025)
    ax.set_ylim(0, 2100)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${int(x)}B'))

    estilo_base(fig, ax, 'Fuente: UNCTAD — World Investment Report (datos anuales de IED inflows)')

    path = os.path.join(OUTPUT_DIR, 'ied_global.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generando gráficos de Etapa 5: Globalización financiera...")
    grafico_apertura_fases()
    grafico_china_exportaciones()
    grafico_costos_transporte()
    grafico_ied_global()
    print("\n¡4 gráficos de Etapa 5 generados!")
