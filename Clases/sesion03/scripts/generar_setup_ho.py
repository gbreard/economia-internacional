"""
Genera gráfico esquemático: setup 2×2×2 del modelo Heckscher-Ohlin
Diagrama visual con los dos países, dos bienes, dos factores
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
CELESTE = '#0EA5E9'

SCRIPT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
OUT = SCRIPT_DIR.parent / 'graficos'

fig, ax = plt.subplots(1, 1, figsize=(11, 6.5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 7)
ax.axis('off')

# Título
ax.text(5.5, 6.6, 'Modelo Heckscher-Ohlin: setup 2×2×2', fontsize=16,
       fontweight='bold', color=AZUL_OSCURO, ha='center', va='top')

# ===== PAIS A (izquierda) =====
box_a = patches.FancyBboxPatch((0.5, 2.5), 4, 3.5, boxstyle='round,pad=0.15',
                                facecolor='#EBF5FB', edgecolor=AZUL_OSCURO, linewidth=2)
ax.add_patch(box_a)
ax.text(2.5, 5.7, 'País A', fontsize=14, fontweight='bold', color=AZUL_OSCURO, ha='center')
ax.text(2.5, 5.25, 'K/L alto  →  abundante en Capital', fontsize=10,
       color=AZUL_MEDIO, ha='center', fontweight='bold')

# Factores de A
ax.text(1.3, 4.5, 'K', fontsize=20, fontweight='bold', color=AZUL_OSCURO, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=AZUL_OSCURO, linewidth=1.5))
ax.text(1.3, 4.0, '(abundante)', fontsize=8, color=AZUL_OSCURO, ha='center')
ax.text(3.7, 4.5, 'L', fontsize=20, fontweight='bold', color=GRIS, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=GRIS, linewidth=1.5))
ax.text(3.7, 4.0, '(escaso)', fontsize=8, color=GRIS, ha='center')

# Bienes de A
ax.text(1.5, 3.2, 'Bien X', fontsize=11, fontweight='bold', color=AZUL_OSCURO, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#DBEAFE', edgecolor=AZUL_MEDIO))
ax.text(1.5, 2.75, 'K-intensivo\ncosto BAJO', fontsize=8, color=AZUL_OSCURO, ha='center')

ax.text(3.5, 3.2, 'Bien Y', fontsize=11, fontweight='bold', color=GRIS, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#F3F4F6', edgecolor=GRIS))
ax.text(3.5, 2.75, 'L-intensivo\ncosto ALTO', fontsize=8, color=GRIS, ha='center')

# ===== PAIS B (derecha) =====
box_b = patches.FancyBboxPatch((6.5, 2.5), 4, 3.5, boxstyle='round,pad=0.15',
                                facecolor='#EAFAF1', edgecolor=VERDE, linewidth=2)
ax.add_patch(box_b)
ax.text(8.5, 5.7, 'País B', fontsize=14, fontweight='bold', color=VERDE, ha='center')
ax.text(8.5, 5.25, 'K/L bajo  →  abundante en Trabajo', fontsize=10,
       color=VERDE, ha='center', fontweight='bold')

# Factores de B
ax.text(7.3, 4.5, 'K', fontsize=20, fontweight='bold', color=GRIS, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=GRIS, linewidth=1.5))
ax.text(7.3, 4.0, '(escaso)', fontsize=8, color=GRIS, ha='center')
ax.text(9.7, 4.5, 'L', fontsize=20, fontweight='bold', color=VERDE, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=VERDE, linewidth=1.5))
ax.text(9.7, 4.0, '(abundante)', fontsize=8, color=VERDE, ha='center')

# Bienes de B
ax.text(7.5, 3.2, 'Bien X', fontsize=11, fontweight='bold', color=GRIS, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#F3F4F6', edgecolor=GRIS))
ax.text(7.5, 2.75, 'K-intensivo\ncosto ALTO', fontsize=8, color=GRIS, ha='center')

ax.text(9.5, 3.2, 'Bien Y', fontsize=11, fontweight='bold', color=VERDE, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#D1FAE5', edgecolor=VERDE))
ax.text(9.5, 2.75, 'L-intensivo\ncosto BAJO', fontsize=8, color=VERDE, ha='center')

# ===== FLECHA CENTRAL: COMERCIO =====
ax.annotate('', xy=(6.3, 4.2), xytext=(4.7, 4.2),
           arrowprops=dict(arrowstyle='->', color=NARANJA, lw=2.5))
ax.annotate('', xy=(4.7, 3.4), xytext=(6.3, 3.4),
           arrowprops=dict(arrowstyle='->', color=NARANJA, lw=2.5))
ax.text(5.5, 4.5, 'A exporta X', fontsize=9, fontweight='bold', color=NARANJA, ha='center')
ax.text(5.5, 3.1, 'B exporta Y', fontsize=9, fontweight='bold', color=NARANJA, ha='center')

# ===== SUPUESTOS (abajo) =====
supuestos_box = patches.FancyBboxPatch((1, 0.3), 9, 1.8, boxstyle='round,pad=0.15',
                                        facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=1.5)
ax.add_patch(supuestos_box)
ax.text(5.5, 1.85, 'Supuestos clave', fontsize=11, fontweight='bold', color=NARANJA, ha='center')
ax.text(3.2, 1.35, '• Misma tecnología en A y B\n• Competencia perfecta\n• Rendimientos constantes a escala',
       fontsize=9, color=GRIS, va='top')
ax.text(7.8, 1.35, '• Factores móviles dentro del país\n• Factores inmóviles entre países\n• Mismas preferencias en A y B',
       fontsize=9, color=GRIS, va='top')

# ===== PREDICCIÓN H-O (centro abajo) =====
ax.text(5.5, 0.1, 'Predicción H-O:  cada país exporta el bien intensivo en su factor abundante',
       fontsize=10, fontweight='bold', color=ROJO, ha='center',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEE2E2', edgecolor=ROJO, alpha=0.9))

plt.tight_layout()
fig.savefig(OUT / 'setup_ho.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  + setup_ho.png")
