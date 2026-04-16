#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenera unidad2_mapa.png con 2 sesiones (no 4 clases)."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
CELESTE = '#0EA5E9'
NARANJA = '#E8833A'
ROJO = '#E74C3C'
GRIS = '#4B5563'

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'graficos')

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

ax.text(5, 5.5, 'Unidad 2: ¿Por qué comercian los países?',
        ha='center', va='center', fontsize=18, fontweight='bold', color=AZUL_OSCURO)
ax.text(5, 5.0, 'Dos sesiones, cuatro respuestas',
        ha='center', va='center', fontsize=12, color=GRIS)

sesiones = [
    {'label': 'Sesión 2', 'titulo': 'Mercantilistas\nSmith\nRicardo',
     'desc': 'Comercio como poder\nProductividad y mercado\nVentaja comparativa',
     'color': AZUL_OSCURO, 'highlight': True},
    {'label': 'Sesión 3', 'titulo': 'Modelo neoclásico\nHeckscher-Ohlin',
     'desc': 'Dotaciones de recursos\nFactores y distribución\nParadoja de Leontief',
     'color': CELESTE, 'highlight': False},
]

x_positions = [3, 7]
box_w = 3.2
box_h = 3.5

for i, (x, s) in enumerate(zip(x_positions, sesiones)):
    y = 1.8
    lw = 3 if s['highlight'] else 1.5

    # Caja
    rect = mpatches.FancyBboxPatch((x - box_w/2, y - box_h/2), box_w, box_h,
                                    boxstyle="round,pad=0.15",
                                    facecolor='white', edgecolor=s['color'],
                                    linewidth=lw)
    ax.add_patch(rect)

    # Header
    header_h = 0.7
    header = mpatches.FancyBboxPatch((x - box_w/2, y + box_h/2 - header_h), box_w, header_h,
                                      boxstyle="round,pad=0.1",
                                      facecolor=s['color'], edgecolor=s['color'], linewidth=0)
    ax.add_patch(header)

    ax.text(x, y + box_h/2 - header_h/2, s['label'],
            ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    ax.text(x, y + 0.4, s['titulo'],
            ha='center', va='center', fontsize=13, fontweight='bold', color=s['color'])

    ax.text(x, y - 0.7, s['desc'],
            ha='center', va='center', fontsize=11, color='#555555')

    # Flecha
    if i < 1:
        ax.annotate('', xy=(x_positions[1] - box_w/2 - 0.1, y),
                    xytext=(x + box_w/2 + 0.1, y),
                    arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=2))

    if s['highlight']:
        ax.text(x, y - box_h/2 - 0.3, '▲ HOY',
                ha='center', va='center', fontsize=12, fontweight='bold', color=ROJO)

fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=11, color='#888888', style='italic')
fig.tight_layout(rect=[0, 0.03, 1, 0.97])
fig.savefig(os.path.join(OUT, 'unidad2_mapa.png'), dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print('OK: unidad2_mapa.png')
