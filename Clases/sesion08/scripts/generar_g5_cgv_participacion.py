"""
Participación en CGV por país — Backward vs Forward.
Scatter plot con cuadrantes interpretativos.
"""
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np

AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'

# Datos aproximados de OECD TiVA (2020) — para fines didácticos
# Backward (FVA share), Forward (DVA in foreign exports)
# Coordenadas ajustadas para evitar solapamiento visual
paises = {
    # Ensambladores asiáticos / europeos del Este (cuadrante derecho)
    'Vietnam':       (47, 22, 'ensamblador'),
    'Corea Sur':     (40, 38, 'ensamblador'),
    'Hungría':       (48, 30, 'ensamblador'),
    'Rep. Checa':    (44, 35, 'ensamblador'),
    'México':        (36, 20, 'ensamblador'),
    'Tailandia':     (38, 25, 'ensamblador'),

    # Proveedores de commodities (cuadrante izquierdo superior)
    'Argentina':     (10, 38, 'proveedor'),
    'Chile':         (18, 48, 'proveedor'),
    'Brasil':        (24, 30, 'proveedor'),
    'Perú':          (14, 42, 'proveedor'),
    'Australia':     (10, 52, 'proveedor'),
    'Arabia Saudita':(15, 58, 'proveedor'),
    'Rusia':         (12, 46, 'proveedor'),

    # Desarrollados balanceados
    'Alemania':      (29, 36, 'desarrollado'),
    'EE.UU.':        (11, 28, 'desarrollado'),
    'Japón':         (16, 33, 'desarrollado'),
    'Francia':       (26, 24, 'desarrollado'),
    'Reino Unido':   (22, 21, 'desarrollado'),

    # China caso especial
    'China':         (20, 26, 'mixto'),
}

color_map = {
    'ensamblador': NARANJA,
    'proveedor': VERDE,
    'desarrollado': AZUL_OSCURO,
    'mixto': ROJO,
}

label_map = {
    'ensamblador': 'Ensamblador (alto backward)',
    'proveedor': 'Proveedor de insumos (alto forward)',
    'desarrollado': 'Desarrollado balanceado',
    'mixto': 'China',
}

fig, ax = plt.subplots(figsize=(12, 8))

# Cuadrantes
ax.axvline(x=30, color=GRIS, linestyle=':', alpha=0.4)
ax.axhline(y=33, color=GRIS, linestyle=':', alpha=0.4)

# Texto en cuadrantes — solo etiquetas pequeñas en esquinas
ax.text(2, 63, 'PROVEEDORES DE INSUMOS\n(commodities, recursos)',
        fontsize=9, color=VERDE, ha='left', va='top', fontweight='bold')
ax.text(55, 63, 'CGV "DOBLE"\n(ensambla Y provee)',
        fontsize=9, color=ROJO, ha='right', va='top', fontweight='bold')
ax.text(2, 3, 'ECONOMÍA CERRADA\n(poca CGV)',
        fontsize=9, color=GRIS, ha='left', va='bottom', fontweight='bold')
ax.text(55, 3, 'ENSAMBLADORES\n(usan insumos extranjeros)',
        fontsize=9, color=NARANJA, ha='right', va='bottom', fontweight='bold')

# Puntos
# Offsets manuales para evitar solapamientos
offsets = {
    'Vietnam':       (1.5, -1.5),
    'Corea Sur':     (1.5, 0.5),
    'Hungría':       (1.5, 0.5),
    'Rep. Checa':    (-1.5, -1.8),
    'México':        (-1.5, -1.8),
    'Tailandia':     (1.5, -0.5),
    'Argentina':     (1.5, 0.5),
    'Chile':         (1.5, 0.5),
    'Brasil':        (1.5, 0.5),
    'Perú':          (-1.5, -1.8),
    'Australia':     (1.5, 0.5),
    'Arabia Saudita':(-1.5, 0.5),
    'Rusia':         (1.5, 0.5),
    'Alemania':      (1.5, 0.5),
    'EE.UU.':        (1.5, 0.5),
    'Japón':         (1.5, 0.5),
    'Francia':       (1.5, 0.5),
    'Reino Unido':   (-1.5, -1.8),
    'China':         (1.5, -1.5),
}

for pais, (bw, fw, tipo) in paises.items():
    color = color_map[tipo]
    ax.scatter(bw, fw, s=130, color=color, edgecolor='white', linewidth=1.5, zorder=5, alpha=0.85)

    off_x, off_y = offsets.get(pais, (1.5, 0.7))
    ax.annotate(pais, xy=(bw, fw), xytext=(bw + off_x, fw + off_y),
                fontsize=9, color=GRIS,
                fontweight='bold' if pais == 'Argentina' else 'normal')

# Estilo
ax.set_xlabel('Participación HACIA ATRÁS (% valor agregado extranjero en exportaciones)',
              fontsize=11, color=GRIS)
ax.set_ylabel('Participación HACIA ADELANTE (% exports usadas como insumo por otros)',
              fontsize=11, color=GRIS)
ax.set_title('Participación en cadenas globales de valor — paises seleccionados (datos ~2020)',
             fontsize=13, color=AZUL_OSCURO, fontweight='bold', pad=15)

# Leyenda
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=NARANJA, markersize=10,
           label='Ensambladores (backward alto)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=VERDE, markersize=10,
           label='Proveedores de insumos (forward alto)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=AZUL_OSCURO, markersize=10,
           label='Desarrollados balanceados'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=ROJO, markersize=10,
           label='China'),
]
ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.13),
          frameon=False, fontsize=9, ncol=4)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(colors=GRIS)
ax.grid(True, linestyle='--', alpha=0.2)
ax.set_xlim(0, 55)
ax.set_ylim(0, 65)

# Fuente
fig.text(0.02, 0.01,
         'Fuente: estimaciones basadas en OECD TiVA Database 2023 (datos 2020); valores aproximados con fines didácticos',
         fontsize=8, color=GRIS, style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 1])
out = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'cgv_participacion_paises.png')
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Generado: {out}')
