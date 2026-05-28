"""
G8 — Ranking ECI 2022: top 20 mundial + países latinoamericanos.
Para visualizar dónde está cada uno en la jerarquía de complejidad.

Fuente: Atlas of Economic Complexity, Harvard Growth Lab (rankings 2022).
"""
import sys, io, os, sys as _sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent / 'datos'))

import matplotlib.pyplot as plt
from pathlib import Path
from eci_values import ECI_2022

OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'
GRIS_CLARO = '#9CA3AF'

# Top 20 + países latinoamericanos relevantes
top_isos = sorted([iso for iso in ECI_2022 if ECI_2022[iso][1] > 1.05], key=lambda i: -ECI_2022[i][1])
latam_isos = ['MEX', 'BRA', 'ARG', 'CHL', 'PER', 'COL', 'URY', 'VEN']
top_20 = top_isos[:20]

# Países a mostrar
todos = top_20 + [iso for iso in latam_isos if iso not in top_20]
datos = [(ECI_2022[iso][0], ECI_2022[iso][1], iso) for iso in todos]
datos.sort(key=lambda x: -x[1])

nombres = [d[0] for d in datos]
valores = [d[1] for d in datos]
isos = [d[2] for d in datos]

LATAM = {'MEX', 'BRA', 'ARG', 'CHL', 'PER', 'COL', 'URY', 'VEN'}
colores = []
for iso, v in zip(isos, valores):
    if iso in LATAM:
        if v > 0:
            colores.append(AZUL_MED)
        else:
            colores.append(ROJO)
    elif v > 1.5:
        colores.append(AZUL_OSC)
    else:
        colores.append(NARANJA)

fig, ax = plt.subplots(figsize=(11, 9), facecolor='white')

bars = ax.barh(nombres, valores, color=colores, edgecolor='white',
               linewidth=0.6)
ax.invert_yaxis()

# Valor al lado de cada barra
for i, (nombre, valor, iso) in enumerate(datos):
    rank = i + 1 if iso not in LATAM or valor > 0 else None
    label = f'{valor:+.2f}'
    x_pos = valor + 0.05 if valor >= 0 else valor - 0.05
    ha = 'left' if valor >= 0 else 'right'
    ax.text(x_pos, i, label, va='center', ha=ha,
            fontsize=9, color=GRIS, fontweight='bold')

# Línea en 0
ax.axvline(0, color='black', linewidth=0.8, alpha=0.7)

ax.set_xlabel('ECI 2022 — Índice de Complejidad Económica',
              fontsize=11, color=GRIS)
ax.set_xlim(-1.0, 2.7)
ax.tick_params(axis='y', labelsize=9.5)
ax.tick_params(axis='x', labelsize=9, colors=GRIS)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRIS_CLARO)
ax.spines['bottom'].set_color(GRIS_CLARO)
ax.grid(True, axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Leyenda
from matplotlib.patches import Patch
leg = [
    Patch(facecolor=AZUL_OSC, label='Top mundial (ECI > 1.5)'),
    Patch(facecolor=NARANJA, label='Alto (1.0 - 1.5)'),
    Patch(facecolor=AZUL_MED, label='América Latina (positivo)'),
    Patch(facecolor=ROJO, label='América Latina (negativo)'),
]
ax.legend(handles=leg, loc='lower right', fontsize=9.5, framealpha=0.95,
          edgecolor=GRIS_CLARO)

ax.set_title('Ranking ECI 2022 — top mundial y América Latina',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: Atlas of Economic Complexity, Harvard Growth Lab (atlas.hks.harvard.edu/rankings) — 2022.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

plt.tight_layout(rect=[0, 0.03, 1, 1])
out_path = OUT / 'ranking_eci_2022.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
