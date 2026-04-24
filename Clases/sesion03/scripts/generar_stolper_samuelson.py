"""
Genera gráfico esquemático: Teorema de Stolper-Samuelson
Muestra la cadena: apertura → precio → sector → factor → distribución
para ambos países lado a lado
"""
import sys
import io
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'

SCRIPT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
OUT = SCRIPT_DIR.parent / 'graficos'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

for ax in [ax1, ax2]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# ===== PAIS A (K-abundante) =====
ax1.set_title('País A (K-abundante)', fontsize=14, fontweight='bold',
             color=AZUL_OSCURO, pad=15)

# Paso 1: Apertura
box1a = patches.FancyBboxPatch((1, 8.2), 8, 1, boxstyle='round,pad=0.15',
                                facecolor='#EBF5FB', edgecolor=AZUL_OSCURO, linewidth=1.5)
ax1.add_patch(box1a)
ax1.text(5, 8.7, 'Apertura comercial  →  sube $P_X/P_Y$', fontsize=10,
        ha='center', va='center', fontweight='bold', color=AZUL_OSCURO)

# Flecha
ax1.annotate('', xy=(5, 7.5), xytext=(5, 8.1),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))

# Paso 2: Sectores
box2a = patches.FancyBboxPatch((0.5, 6.2), 4, 1.2, boxstyle='round,pad=0.15',
                                facecolor='#D1FAE5', edgecolor=VERDE, linewidth=1.5)
ax1.add_patch(box2a)
ax1.text(2.5, 6.8, 'Sector X (K-intensivo)\nSE EXPANDE  ↑', fontsize=9,
        ha='center', va='center', fontweight='bold', color=VERDE)

box2b = patches.FancyBboxPatch((5.5, 6.2), 4, 1.2, boxstyle='round,pad=0.15',
                                facecolor='#FEE2E2', edgecolor=ROJO, linewidth=1.5)
ax1.add_patch(box2b)
ax1.text(7.5, 6.8, 'Sector Y (L-intensivo)\nSE CONTRAE  ↓', fontsize=9,
        ha='center', va='center', fontweight='bold', color=ROJO)

# Flechas
ax1.annotate('', xy=(2.5, 5.5), xytext=(2.5, 6.1),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))
ax1.annotate('', xy=(7.5, 5.5), xytext=(7.5, 6.1),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))

# Paso 3: Factores
box3a = patches.FancyBboxPatch((0.5, 3.8), 4, 1.6, boxstyle='round,pad=0.15',
                                facecolor='#D1FAE5', edgecolor=VERDE, linewidth=2)
ax1.add_patch(box3a)
ax1.text(2.5, 4.85, 'Retorno del Capital', fontsize=9, ha='center',
        fontweight='bold', color=VERDE)
ax1.text(2.5, 4.3, '↑  $r$ sube', fontsize=14, ha='center',
        fontweight='bold', color=VERDE)

box3b = patches.FancyBboxPatch((5.5, 3.8), 4, 1.6, boxstyle='round,pad=0.15',
                                facecolor='#FEE2E2', edgecolor=ROJO, linewidth=2)
ax1.add_patch(box3b)
ax1.text(7.5, 4.85, 'Salario real', fontsize=9, ha='center',
        fontweight='bold', color=ROJO)
ax1.text(7.5, 4.3, '↓  $w$ baja', fontsize=14, ha='center',
        fontweight='bold', color=ROJO)

# Flechas al resultado
ax1.annotate('', xy=(5, 2.8), xytext=(2.5, 3.7),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.5))
ax1.annotate('', xy=(5, 2.8), xytext=(7.5, 3.7),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.5))

# Resultado
box4a = patches.FancyBboxPatch((1.5, 1.5), 7, 1.2, boxstyle='round,pad=0.15',
                                facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=2)
ax1.add_patch(box4a)
ax1.text(5, 2.1, 'Capitalistas GANAN\nTrabajadores PIERDEN', fontsize=11,
        ha='center', va='center', fontweight='bold', color=NARANJA)

# ===== PAIS B (L-abundante) =====
ax2.set_title('País B (L-abundante)', fontsize=14, fontweight='bold',
             color=VERDE, pad=15)

# Paso 1: Apertura
box1b = patches.FancyBboxPatch((1, 8.2), 8, 1, boxstyle='round,pad=0.15',
                                facecolor='#EAFAF1', edgecolor=VERDE, linewidth=1.5)
ax2.add_patch(box1b)
ax2.text(5, 8.7, 'Apertura comercial  →  baja $P_X/P_Y$', fontsize=10,
        ha='center', va='center', fontweight='bold', color=VERDE)

# Flecha
ax2.annotate('', xy=(5, 7.5), xytext=(5, 8.1),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))

# Paso 2: Sectores
box2c = patches.FancyBboxPatch((0.5, 6.2), 4, 1.2, boxstyle='round,pad=0.15',
                                facecolor='#FEE2E2', edgecolor=ROJO, linewidth=1.5)
ax2.add_patch(box2c)
ax2.text(2.5, 6.8, 'Sector X (K-intensivo)\nSE CONTRAE  ↓', fontsize=9,
        ha='center', va='center', fontweight='bold', color=ROJO)

box2d = patches.FancyBboxPatch((5.5, 6.2), 4, 1.2, boxstyle='round,pad=0.15',
                                facecolor='#D1FAE5', edgecolor=VERDE, linewidth=1.5)
ax2.add_patch(box2d)
ax2.text(7.5, 6.8, 'Sector Y (L-intensivo)\nSE EXPANDE  ↑', fontsize=9,
        ha='center', va='center', fontweight='bold', color=VERDE)

# Flechas
ax2.annotate('', xy=(2.5, 5.5), xytext=(2.5, 6.1),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))
ax2.annotate('', xy=(7.5, 5.5), xytext=(7.5, 6.1),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))

# Paso 3: Factores
box3c = patches.FancyBboxPatch((0.5, 3.8), 4, 1.6, boxstyle='round,pad=0.15',
                                facecolor='#FEE2E2', edgecolor=ROJO, linewidth=2)
ax2.add_patch(box3c)
ax2.text(2.5, 4.85, 'Retorno del Capital', fontsize=9, ha='center',
        fontweight='bold', color=ROJO)
ax2.text(2.5, 4.3, '↓  $r$ baja', fontsize=14, ha='center',
        fontweight='bold', color=ROJO)

box3d = patches.FancyBboxPatch((5.5, 3.8), 4, 1.6, boxstyle='round,pad=0.15',
                                facecolor='#D1FAE5', edgecolor=VERDE, linewidth=2)
ax2.add_patch(box3d)
ax2.text(7.5, 4.85, 'Salario real', fontsize=9, ha='center',
        fontweight='bold', color=VERDE)
ax2.text(7.5, 4.3, '↑  $w$ sube', fontsize=14, ha='center',
        fontweight='bold', color=VERDE)

# Flechas al resultado
ax2.annotate('', xy=(5, 2.8), xytext=(2.5, 3.7),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.5))
ax2.annotate('', xy=(5, 2.8), xytext=(7.5, 3.7),
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.5))

# Resultado
box4b = patches.FancyBboxPatch((1.5, 1.5), 7, 1.2, boxstyle='round,pad=0.15',
                                facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=2)
ax2.add_patch(box4b)
ax2.text(5, 2.1, 'Trabajadores GANAN\nCapitalistas PIERDEN', fontsize=11,
        ha='center', va='center', fontweight='bold', color=NARANJA)

# Mensaje central abajo
fig.text(0.5, 0.02, 'El comercio beneficia al factor abundante y perjudica al factor escaso en cada país',
        ha='center', fontsize=11, fontweight='bold', color=ROJO,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEE2E2', edgecolor=ROJO, alpha=0.9))

plt.tight_layout(rect=[0, 0.06, 1, 0.95])
fig.savefig(OUT / 'stolper_samuelson.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  + stolper_samuelson.png")
