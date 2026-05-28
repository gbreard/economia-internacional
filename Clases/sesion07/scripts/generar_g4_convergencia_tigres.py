"""
G4 — Convergencia de tigres asiáticos vs. estancamiento latinoamericano.
PIB per cápita 1960-2023 (USD constantes 2017 PPA).

Fuente: Maddison Project Database 2023 (Bolt & van Zanden) +
World Bank WDI para actualización post-2018.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'
GRIS_CLARO = '#9CA3AF'
VIOLETA = '#7C3AED'
CYAN = '#0EA5E9'

# PIB per cápita en USD 2017 PPA (Maddison + WB WDI)
# Valores cada 5 años entre 1960 y 2020 + 2023
anios = [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2023]

series = {
    'Corea del Sur': ([1300, 2700, 5800, 13000, 22000, 33000, 43000, 46000], NARANJA, 3),
    'Taiwán':       ([1500, 3400, 7500, 13500, 24000, 38000, 50000, 53000], VERDE, 3),
    'Singapur':     ([3500, 7000, 14000, 32000, 52000, 75000, 90000, 95000], VIOLETA, 3),
    'Hong Kong':    ([3500, 6500, 14000, 28000, 41000, 55000, 60000, 62000], CYAN, 3),
    'Argentina':    ([10500, 13500, 14000, 11000, 14500, 19500, 21000, 22500], AZUL_OSC, 2.5),
    'Brasil':       ([3500, 5500, 9500, 10500, 12500, 16500, 17000, 17500], AZUL_MED, 2.5),
    'México':       ([6000, 9500, 14500, 14500, 18500, 19500, 20000, 21500], GRIS, 2.5),
}

fig, ax = plt.subplots(figsize=(12, 6.5), facecolor='white')

# Estilo: tigres con línea continua, LatAm con línea punteada
for nombre, (valores, color, lw) in series.items():
    es_tigre = nombre in ('Corea del Sur', 'Taiwán', 'Singapur', 'Hong Kong')
    estilo = '-' if es_tigre else '--'
    ax.plot(anios, valores, color=color, linewidth=lw, linestyle=estilo,
            marker='o', markersize=5.5, markerfacecolor='white',
            markeredgecolor=color, markeredgewidth=1.5,
            label=nombre, zorder=5)

ax.set_xlabel('Año', fontsize=11, color=GRIS)
ax.set_ylabel('PIB per cápita (USD 2017 PPA)', fontsize=11, color=GRIS)
ax.set_xlim(1958, 2025)
ax.set_ylim(0, 100000)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRIS_CLARO)
ax.spines['bottom'].set_color(GRIS_CLARO)

# Formato eje Y con miles
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000)}k'))

# Anotaciones clave
ax.annotate('1960: Argentina\n8x más rica que\nCorea del Sur',
            xy=(1960, 10500), xytext=(1968, 60000),
            fontsize=10, color=AZUL_OSC, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=AZUL_OSC, lw=1.3),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=AZUL_OSC, linewidth=1.2, alpha=0.95))

ax.annotate('2023: Corea es\n2x más rica que\nArgentina',
            xy=(2023, 46000), xytext=(2010, 86000),
            fontsize=10, color=NARANJA, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.3),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=NARANJA, linewidth=1.2, alpha=0.95))

ax.legend(loc='center left', bbox_to_anchor=(1.01, 0.5),
          fontsize=10, framealpha=0.95, edgecolor=GRIS_CLARO)

ax.set_title('La Gran Divergencia (1960-2023): tigres asiáticos vs. América Latina',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: Maddison Project Database 2023 (Bolt & van Zanden) + Banco Mundial WDI. PIB pc en USD 2017 PPA.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

plt.tight_layout(rect=[0, 0.04, 1, 1])
out_path = OUT / 'convergencia_tigres.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
