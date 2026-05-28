"""
M2 — Mapa de Asia Oriental con los 4 tigres asiáticos destacados.
Para ubicar el "milagro asiático" geográficamente.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
import geopandas as gpd
from pathlib import Path

DATOS = Path(__file__).parent.parent / 'datos'
OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
GRIS = '#9CA3AF'
GRIS_TXT = '#4B5563'

world = gpd.read_file(DATOS / 'ne_110m_admin_0_countries.geojson')

TIGRES = {'KOR', 'TWN', 'HKG', 'SGP'}
JAPON = {'JPN'}
CHINA = {'CHN'}

def clasificar(iso):
    if iso in TIGRES:
        return 'tigre'
    elif iso in JAPON:
        return 'japon'
    elif iso in CHINA:
        return 'china'
    else:
        return 'otro'

world['grupo'] = world['ADM0_A3'].apply(clasificar)

fig, ax = plt.subplots(figsize=(11, 8), facecolor='white')

colors = {
    'tigre': NARANJA,
    'japon': '#6B7280',
    'china': AZUL_MED,
    'otro': '#E5E7EB',
}
for g, c in colors.items():
    subset = world[world['grupo'] == g]
    subset.plot(ax=ax, color=c, edgecolor='white', linewidth=0.4)

# Recortar a Asia oriental (bajamos ylim para que entre Singapur)
ax.set_xlim(95, 150)
ax.set_ylim(-7, 52)

# Anotaciones de tigres (con flechitas)
labels = [
    ('KOR', 'Corea del Sur', 127.5, 36.5, 132, 44, NARANJA),
    ('TWN', 'Taiwán', 121, 23.5, 128, 19, NARANJA),
    ('HKG', 'Hong Kong', 114.2, 22.3, 100, 16, NARANJA),
    ('SGP', 'Singapur', 103.8, 1.3, 118, 2, NARANJA),
    ('JPN', 'Japón\n(modelo)', 138, 36, 144, 48, '#6B7280'),
    ('CHN', 'China\n(siguiente ola)', 105, 35, 99, 47, AZUL_MED),
]

for iso, nombre, x, y, tx, ty, color in labels:
    ax.annotate(nombre, xy=(x, y), xytext=(tx, ty),
                fontsize=10.5, fontweight='bold', color=color,
                ha='center',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.4),
                bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                          edgecolor=color, linewidth=1.2, alpha=0.95))

# Leyenda
from matplotlib.patches import Patch
leg = [
    Patch(facecolor=NARANJA, label='Los 4 tigres asiáticos'),
    Patch(facecolor='#6B7280', label='Japón (modelo inspirador)'),
    Patch(facecolor=AZUL_MED, label='China (siguiente ola)'),
]
ax.legend(handles=leg, loc='upper right', fontsize=10, framealpha=0.95,
          edgecolor=GRIS)

ax.set_title('Los 4 tigres asiáticos — Corea, Taiwán, Hong Kong, Singapur',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=14)
ax.text(0.5, -0.04,
        'De 1960 a 2000 multiplicaron su PIB per cápita por 10-15x. '
        'Caso paradigmático de "ventajas comparativas construidas".',
        transform=ax.transAxes, ha='center', fontsize=10,
        style='italic', color=GRIS_TXT)

ax.set_axis_off()
plt.tight_layout()
out_path = OUT / 'mapa_asia_tigres.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
