"""
M1 — Mapa Norte Global vs. Sur Global (Hickel et al. 2022).
Muestra qué países integran el "Norte" (centro) y el "Sur" (periferia)
para visualizar la dirección de la transferencia de valor.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
import geopandas as gpd
from pathlib import Path

DATOS = Path(__file__).parent.parent / 'datos'
OUT = Path(__file__).parent.parent / 'graficos'
OUT.mkdir(exist_ok=True)

# Paleta
AZUL_OSC = '#1F4E79'
NARANJA = '#E8833A'
GRIS = '#9CA3AF'
GRIS_TXT = '#4B5563'

world = gpd.read_file(DATOS / 'ne_110m_admin_0_countries.geojson')

# Definición del Norte Global según Hickel et al. 2022
# (basado en clasificación de Naciones Unidas + OCDE)
NORTE_GLOBAL = {
    'USA', 'CAN', 'GBR', 'IRL', 'FRA', 'DEU', 'ITA', 'ESP', 'PRT', 'NLD',
    'BEL', 'LUX', 'CHE', 'AUT', 'DNK', 'NOR', 'SWE', 'FIN', 'ISL', 'GRC',
    'CZE', 'SVK', 'POL', 'HUN', 'SVN', 'EST', 'LVA', 'LTU', 'JPN', 'KOR',
    'AUS', 'NZL', 'ISR', 'SGP', 'TWN', 'HKG', 'MLT', 'CYP'
}

def clasificar(iso):
    if iso in NORTE_GLOBAL:
        return 'norte'
    elif iso == 'ATA':  # Antártida
        return 'no'
    else:
        return 'sur'

world['grupo'] = world['ADM0_A3'].apply(clasificar)

fig, ax = plt.subplots(figsize=(14, 7.5), facecolor='white')

# Colores
colors = {'norte': AZUL_OSC, 'sur': NARANJA, 'no': '#E5E7EB'}
for grupo, color in colors.items():
    subset = world[world['grupo'] == grupo]
    subset.plot(ax=ax, color=color, edgecolor='white', linewidth=0.3)

# Flecha del Sur al Norte: del Atlántico Sur al Atlántico Norte (zona oceánica)
ax.annotate('', xy=(-30, 55), xytext=(-15, -25),
            arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=3.5,
                            connectionstyle='arc3,rad=-0.35'))
# Cuadro de texto en Pacífico Sur (zona azul oceánica, sin tapar continentes)
ax.text(-130, -40, 'TRANSFERENCIA\nDE VALOR\nSur → Norte\n~USD 2 billones/año',
        fontsize=11, fontweight='bold', color='#E74C3C',
        ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.55', facecolor='white',
                  edgecolor='#E74C3C', linewidth=1.6, alpha=0.97))

# Leyenda en el Pacífico Norte (zona vacía)
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=AZUL_OSC, edgecolor='white', label='Norte Global (centro)'),
    Patch(facecolor=NARANJA, edgecolor='white', label='Sur Global (periferia)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=11,
          framealpha=0.95, edgecolor=GRIS,
          bbox_to_anchor=(0.02, 0.92))

ax.set_title('Norte Global y Sur Global — la geografía del intercambio desigual',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=14)
ax.text(0.5, -0.04,
        'Fuente: elaboración propia a partir de Hickel et al. (2022) "Imperialist Appropriation in the World Economy" — Global Environmental Change.',
        transform=ax.transAxes, ha='center', fontsize=8.5,
        style='italic', color=GRIS_TXT)

ax.set_axis_off()
ax.set_xlim(-180, 180)
ax.set_ylim(-60, 85)
ax.set_aspect('equal')  # IMPORTANTE: para que el mapa no se estire

plt.tight_layout()
out_path = OUT / 'mapa_norte_sur.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
