"""
M3 — Mapa de Sudamérica con Brasil + Argentina destacados.
Para ubicar los dos casos latinoamericanos: Embraer (Brasil) e INVAP (Argentina).
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

BRASIL = {'BRA'}
ARGENTINA = {'ARG'}

def clasificar(iso):
    if iso in BRASIL: return 'bra'
    elif iso in ARGENTINA: return 'arg'
    else: return 'otro'

world['grupo'] = world['ADM0_A3'].apply(clasificar)

fig, ax = plt.subplots(figsize=(8.5, 9.5), facecolor='white')

colors = {'bra': VERDE, 'arg': AZUL_MED, 'otro': '#E5E7EB'}
for g, c in colors.items():
    subset = world[world['grupo'] == g]
    subset.plot(ax=ax, color=c, edgecolor='white', linewidth=0.5)

# Recortar a Sudamérica
ax.set_xlim(-90, -30)
ax.set_ylim(-58, 15)

# Anotaciones con casos
ax.annotate('BRASIL\nEmbraer\n(aeronáutica)',
            xy=(-50, -10), xytext=(-32, -5),
            fontsize=11, fontweight='bold', color=VERDE,
            ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=VERDE, lw=1.6),
            bbox=dict(boxstyle='round,pad=0.45', facecolor='white',
                      edgecolor=VERDE, linewidth=1.5, alpha=0.95))

ax.annotate('ARGENTINA\nINVAP\n(satélites + reactores)',
            xy=(-65, -38), xytext=(-86, -45),
            fontsize=11, fontweight='bold', color=AZUL_MED,
            ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=AZUL_MED, lw=1.6),
            bbox=dict(boxstyle='round,pad=0.45', facecolor='white',
                      edgecolor=AZUL_MED, linewidth=1.5, alpha=0.95))

ax.set_title('Dos casos latinoamericanos de capacidades construidas',
             fontsize=13, fontweight='bold', color=AZUL_OSC, pad=12)
ax.text(0.5, -0.04,
        'Brasil con upgrading aeronáutico sistémico (Embraer). '
        'Argentina con nichos de alto valor en tecnología nuclear y espacial (INVAP).',
        transform=ax.transAxes, ha='center', fontsize=9.5,
        style='italic', color=GRIS_TXT)

ax.set_axis_off()
plt.tight_layout()
out_path = OUT / 'mapa_sudamerica.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
