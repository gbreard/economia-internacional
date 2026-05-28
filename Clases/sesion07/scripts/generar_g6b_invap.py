"""
G6b — INVAP: timeline de hitos tecnológicos (reactores nucleares y satélites).
Caso argentino de capacidades en nichos de alto valor tecnológico.

Versión simplificada: solo los hitos más representativos para evitar densidad.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
NARANJA = '#E8833A'
VERDE = '#27AE60'
GRIS = '#4B5563'
GRIS_CLARO = '#9CA3AF'

# Solo 8 hitos clave — 4 reactores y 4 satélites
hitos = [
    (1976, 'reactor', 'INVAP\ncreado', 'arriba'),
    (1987, 'reactor', 'Reactor\nNUR a Argelia', 'abajo'),
    (1999, 'reactor', 'Reactor ETRR-2\na Egipto', 'arriba'),
    (2007, 'reactor', 'Reactor OPAL\na Australia\n(USD 180 M)', 'abajo'),
    (1996, 'satelite', 'SAC-B\n(primer satélite\ncientífico)', 'abajo'),
    (2014, 'satelite', 'ARSAT-1\n(geoestacionario\nde comunicaciones)', 'arriba'),
    (2018, 'satelite', 'SAOCOM-1A\n(radar banda L)', 'abajo'),
    (2024, 'reactor', 'RA-10\n(reactor multipropósito\nen Ezeiza)', 'arriba'),
]

fig, ax = plt.subplots(figsize=(14, 7), facecolor='white')

# Línea de tiempo
ax.axhline(0, color=GRIS_CLARO, linewidth=2.5, zorder=1)

# Ticks de años cada 5
for año in range(1975, 2026, 5):
    ax.plot([año, año], [-0.08, 0.08], color=GRIS_CLARO, linewidth=1.2, zorder=1)
    ax.text(año, -0.22, str(año), ha='center', fontsize=10, color=GRIS, fontweight='bold')

# Hitos
for año, sector, texto, posicion in hitos:
    color = VERDE if sector == 'satelite' else NARANJA
    if posicion == 'arriba':
        y = 1.3
        va_caja = 'bottom'
    else:
        y = -1.3
        va_caja = 'top'

    # Punto en la línea
    ax.scatter([año], [0], s=180, color=color,
               edgecolor='white', linewidth=2, zorder=4)

    # Línea conectora
    ax.plot([año, año], [0, y * 0.85], color=color, linewidth=1.8,
            linestyle='--', alpha=0.65, zorder=2)

    # Caja con texto
    ax.text(año, y, texto, ha='center', va=va_caja,
            fontsize=9.5, color='white', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=color,
                      edgecolor=color, linewidth=1, alpha=0.95))

ax.set_xlim(1972, 2028)
ax.set_ylim(-2.3, 2.3)
ax.set_axis_off()

fig.suptitle('INVAP: 50 años de capacidades nucleares y satelitales argentinas',
             fontsize=14, fontweight='bold', color=AZUL_OSC, y=0.97)

from matplotlib.patches import Patch
leg = [
    Patch(facecolor=NARANJA, label='Reactores nucleares'),
    Patch(facecolor=VERDE, label='Satélites'),
]
ax.legend(handles=leg, loc='upper right', fontsize=10.5, framealpha=0.95,
          edgecolor=GRIS_CLARO, bbox_to_anchor=(0.99, 0.99))

ax.text(2000, -2.05,
        'Caso de capacidades de nicho de alto valor: no exporta volumen, exporta tecnología.\n'
        'Reactores a Argelia, Egipto, Australia, Holanda. Única empresa latinoamericana habilitada por la OIEA Categoría A.',
        ha='center', fontsize=10, style='italic', color=GRIS)

fig.text(0.5, 0.01,
         'Fuente: INVAP S.E. annual reports, CONAE, CNEA.',
         ha='center', fontsize=8.5, style='italic', color=GRIS_CLARO)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
out_path = OUT / 'invap_timeline.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
