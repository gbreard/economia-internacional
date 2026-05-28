"""
G10 — Concentración global de la cadena de semiconductores avanzados.
TSMC (Taiwán) + Samsung (Corea) concentran casi 100% de los chips <7nm.

Fuente: BCG-SIA (2021) "Strengthening the Global Semiconductor Supply Chain"
+ SEMI World Fab Forecast 2024. Datos de capacidad de fabricación de chips
de tecnología más avanzada (<10nm).
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6), facecolor='white')

# Panel 1: Cuota global de fabricación de chips <7nm (foundry leading-edge)
# Fuente: BCG-SIA 2021, actualizado con SEMI 2024
nodos_paises = ['Taiwán\n(TSMC)', 'Corea del Sur\n(Samsung)', 'EE.UU.\n(Intel)', 'Otros']
nodos_share = [70, 28, 2, 0]  # % de wafers <7nm
colores_p1 = [ROJO, NARANJA, AZUL_OSC, GRIS_CLARO]

bars = ax1.barh(nodos_paises, nodos_share, color=colores_p1,
                edgecolor='white', linewidth=1.5)
ax1.invert_yaxis()
for i, (n, v) in enumerate(zip(nodos_paises, nodos_share)):
    ax1.text(v + 1.5, i, f'{v}%', va='center',
             fontsize=11, fontweight='bold', color=GRIS)

ax1.set_xlim(0, 85)
ax1.set_xlabel('% de capacidad mundial', fontsize=10.5, color=GRIS)
ax1.set_title('Chips lógicos avanzados (<7nm)',
              fontsize=12, fontweight='bold', color=AZUL_OSC, pad=8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color(GRIS_CLARO)
ax1.spines['bottom'].set_color(GRIS_CLARO)
ax1.tick_params(labelsize=10)
ax1.grid(True, axis='x', alpha=0.3, linestyle='--')
ax1.set_axisbelow(True)

# Anotación destacada (la pongo abajo a la derecha para no tapar barras)
ax1.text(50, 2.8,
         '~98% en SOLO 2 países\n(Taiwán + Corea)',
         fontsize=11, fontweight='bold', color=ROJO, ha='center',
         bbox=dict(boxstyle='round,pad=0.45', facecolor='white',
                   edgecolor=ROJO, linewidth=1.5, alpha=0.95))

# Panel 2: Máquinas EUV (litografía ultravioleta extrema)
# Una sola empresa en el mundo: ASML (Países Bajos)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_axis_off()

ax2.text(5, 9, 'Máquinas EUV de fotolitografía',
         ha='center', fontsize=12, fontweight='bold', color=AZUL_OSC)
ax2.text(5, 8.3, '(necesarias para fabricar chips <7nm)',
         ha='center', fontsize=10, color=GRIS, style='italic')

# Círculo gigante "100%"
from matplotlib.patches import Circle
circ = Circle((5, 4.5), 2.5, facecolor=VIOLETA, edgecolor='white',
              linewidth=2, alpha=0.92)
ax2.add_patch(circ)
ax2.text(5, 5, '100%', ha='center', va='center',
         fontsize=30, fontweight='bold', color='white')
ax2.text(5, 3.7, 'ASML\n(Países Bajos)', ha='center', va='center',
         fontsize=12, fontweight='bold', color='white')

ax2.text(5, 1.4,
         'Una sola empresa en el mundo\nfabrica las máquinas necesarias.\nValor por unidad: USD 150-380 M.',
         ha='center', fontsize=10.5, color=GRIS,
         bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                   edgecolor=VIOLETA, linewidth=1.5, alpha=0.95))

# Título general
fig.suptitle('La cadena estratégica de semiconductores — concentración extrema',
             fontsize=14, fontweight='bold', color=AZUL_OSC, y=0.98)

fig.text(0.5, 0.01,
         'Fuente: BCG-SIA (2021) "Strengthening the Global Semiconductor Supply Chain" + SEMI World Fab Forecast 2024.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
out_path = OUT / 'semiconductores_concentracion.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
