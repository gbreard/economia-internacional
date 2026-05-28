"""
M4 — Mapa global del ECI 2022 (Atlas of Economic Complexity, Harvard Growth Lab).
Verde = alta complejidad, Rojo = baja complejidad.
"""

import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent / 'datos'))

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap, Normalize
from pathlib import Path

from eci_values import ECI_2022

DATOS = Path(__file__).parent.parent / 'datos'
OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
GRIS = '#9CA3AF'
GRIS_TXT = '#4B5563'

world = gpd.read_file(DATOS / 'ne_110m_admin_0_countries.geojson')

# Mapear ECI
world['eci'] = world['ADM0_A3'].map(lambda c: ECI_2022.get(c, [None, None])[1])

# Colormap: rojo (-2) → blanco (0) → verde (+2)
cmap = LinearSegmentedColormap.from_list(
    'eci_cmap',
    ['#9B1C1C', '#E74C3C', '#FCE4A8', '#27AE60', '#1B6E3A'],
    N=256
)
norm = Normalize(vmin=-2.0, vmax=2.5)

fig, ax = plt.subplots(figsize=(14, 8.5), facecolor='white')

# Países sin dato (gris)
world[world['eci'].isna()].plot(ax=ax, color='#E5E7EB',
                                 edgecolor='white', linewidth=0.3)
# Países con dato
world[world['eci'].notna()].plot(ax=ax, column='eci', cmap=cmap, norm=norm,
                                  edgecolor='white', linewidth=0.3)

# Anotaciones de países clave (con flechita)
labels = [
    ('JPN', 'Japón #1', 138, 36, 162, 48),
    ('KOR', 'Corea #4', 127.5, 36.5, 152, 28),
    ('DEU', 'Alemania #5', 10, 51, -5, 70),
    ('CHN', 'China #14', 105, 35, 88, 60),
    ('USA', 'EE.UU. #18', -98, 40, -135, 60),
    ('MEX', 'México #19', -102, 24, -148, 32),
    ('BRA', 'Brasil', -55, -10, -28, 0),
    ('ARG', 'Argentina', -65, -38, -38, -52),
    ('CHL', 'Chile', -71, -35, -100, -55),
]

for iso, nombre, x, y, tx, ty in labels:
    eci = ECI_2022.get(iso, [None, None])[1]
    if eci is None:
        continue
    color = cmap(norm(eci))
    ax.annotate(nombre, xy=(x, y), xytext=(tx, ty),
                fontsize=8.5, fontweight='bold', color=AZUL_OSC,
                ha='center', va='center',
                arrowprops=dict(arrowstyle='->', color=GRIS_TXT, lw=0.9),
                bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                          edgecolor=GRIS_TXT, linewidth=0.7, alpha=0.92))

# Colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, orientation='horizontal',
                    fraction=0.035, pad=0.04, aspect=45, shrink=0.6)
cbar.set_label('ECI 2022 — Índice de Complejidad Económica',
               fontsize=10, color=GRIS_TXT)
cbar.ax.tick_params(labelsize=9)

ax.set_title('Atlas de Complejidad Económica — qué tan sofisticada es la canasta exportadora',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=14)
fig.text(0.5, 0.005,
         'Fuente: Atlas of Economic Complexity, Harvard Growth Lab (atlas.hks.harvard.edu) — rankings 2022. '
         'ECI mide diversidad y ubicuidad de los productos exportados.',
         ha='center', fontsize=9, style='italic', color=GRIS_TXT)

ax.set_axis_off()
ax.set_xlim(-180, 180)
ax.set_ylim(-60, 85)

plt.tight_layout(rect=[0, 0.05, 1, 0.97])
out_path = OUT / 'mapa_eci_mundo.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
