"""
G9 — Trayectoria ECI 1995-2022 para países seleccionados.
Argentina pierde complejidad mientras Corea, China, Polonia ganan.

Fuente: Atlas of Economic Complexity, Harvard Growth Lab — serie histórica ECI.
"""
import sys, io, sys as _sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent / 'datos'))

import matplotlib.pyplot as plt
from pathlib import Path
from eci_values import ECI_SERIE

OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'
GRIS_CLARO = '#9CA3AF'
VIOLETA = '#7C3AED'

# Países a graficar
config = {
    'KOR': ('Corea del Sur', NARANJA, '-', 3),
    'CHN': ('China', ROJO, '-', 3),
    'POL': ('Polonia', VIOLETA, '-', 3),
    'MEX': ('México', VERDE, '-', 2.5),
    'BRA': ('Brasil', AZUL_MED, '--', 2.5),
    'ARG': ('Argentina', AZUL_OSC, '--', 3),
    'CHL': ('Chile', GRIS, '--', 2.5),
}

fig, ax = plt.subplots(figsize=(11, 6.5), facecolor='white')

for iso, (nombre, color, estilo, lw) in config.items():
    serie = ECI_SERIE[iso]
    anios = sorted(serie.keys())
    valores = [serie[a] for a in anios]
    ax.plot(anios, valores, color=color, linewidth=lw, linestyle=estilo,
            marker='o', markersize=6, markerfacecolor='white',
            markeredgecolor=color, markeredgewidth=1.5,
            label=nombre, zorder=4)

ax.axhline(0, color='black', linewidth=0.7, alpha=0.5)

ax.set_xlabel('Año', fontsize=11, color=GRIS)
ax.set_ylabel('ECI — Índice de Complejidad Económica',
              fontsize=11, color=GRIS)
ax.set_xlim(1993, 2024)
ax.set_ylim(-0.8, 2.3)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRIS_CLARO)
ax.spines['bottom'].set_color(GRIS_CLARO)

# Anotaciones clave
ax.annotate('China sube 4x\nsu complejidad',
            xy=(2022, 1.30), xytext=(2017, 1.85),
            fontsize=10, color=ROJO, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                      edgecolor=ROJO, linewidth=1.2, alpha=0.95))

ax.annotate('Argentina pierde\ncomplejidad\ndesde 1995',
            xy=(2022, -0.39), xytext=(2015, -0.7),
            fontsize=10, color=AZUL_OSC, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=AZUL_OSC, lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                      edgecolor=AZUL_OSC, linewidth=1.2, alpha=0.95))

ax.legend(loc='upper left', fontsize=10, framealpha=0.95,
          edgecolor=GRIS_CLARO, ncol=2)

ax.set_title('La Gran Divergencia en complejidad económica (1995-2022)',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: Atlas of Economic Complexity, Harvard Growth Lab. ECI: índice basado en diversidad y ubicuidad de productos exportados.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

plt.tight_layout(rect=[0, 0.04, 1, 1])
out_path = OUT / 'trayectoria_eci.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
