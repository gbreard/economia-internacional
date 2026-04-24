"""
Genera gráfico visual: método insumo-producto de Leontief aplicado al comercio
Versión 2: layout más espaciado, sin solapamientos
"""
import sys
import io
import os
import matplotlib
matplotlib.use('Agg')
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

fig, ax = plt.subplots(1, 1, figsize=(15, 8.5))
ax.set_xlim(0, 15)
ax.set_ylim(0, 9)
ax.axis('off')

# ===== TRES TÍTULOS DE PASO =====
ax.text(2.8, 8.5, 'PASO 1', fontsize=12, fontweight='bold', color=AZUL_MEDIO, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF5FB', edgecolor=AZUL_MEDIO))
ax.text(2.8, 8.0, 'Matriz insumo-producto\n(EE.UU., 1947)', fontsize=9, color=GRIS, ha='center')

ax.text(7.5, 8.5, 'PASO 2', fontsize=12, fontweight='bold', color=AZUL_MEDIO, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF5FB', edgecolor=AZUL_MEDIO))
ax.text(7.5, 8.0, 'Rastrear K y L en\ncada $1M de comercio', fontsize=9, color=GRIS, ha='center')

ax.text(12.2, 8.5, 'PASO 3', fontsize=12, fontweight='bold', color=AZUL_MEDIO, ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF5FB', edgecolor=AZUL_MEDIO))
ax.text(12.2, 8.0, 'Comparar K/L', fontsize=9, color=GRIS, ha='center')

# ===== PASO 1: MINI MATRIZ I-O =====
mx, my = 0.5, 5.0
cw = [1.2, 1.0, 1.0, 1.0]
rh = 0.5

# Headers columna
headers_col = ['', 'Agro', 'Industria', 'Servicios']
for j, (h, w) in enumerate(zip(headers_col, cw)):
    x = mx + sum(cw[:j])
    rect = patches.FancyBboxPatch((x, my + rh + 0.04), w - 0.04, rh,
           boxstyle='round,pad=0.02', facecolor=AZUL_OSCURO, edgecolor='white', linewidth=1)
    ax.add_patch(rect)
    ax.text(x + (w-0.04)/2, my + rh + 0.04 + rh/2, h, fontsize=8,
           fontweight='bold', color='white', ha='center', va='center')

# Filas
rows_data = [
    ('Agro',       ['0.10', '0.25', '0.05'], '#EBF5FB'),
    ('Industria',  ['0.30', '0.15', '0.20'], '#F8F9FA'),
    ('Servicios',  ['0.10', '0.20', '0.10'], '#EBF5FB'),
]
factor_rows = [
    ('Capital (K)', ['20',  '80',  '50'], '#FEF3C7'),
    ('Trabajo (L)', ['60',  '30',  '40'], '#FEF3C7'),
]

for i, (label, vals, bg) in enumerate(rows_data):
    y = my - i * (rh + 0.03)
    rect = patches.FancyBboxPatch((mx, y), cw[0] - 0.04, rh,
           boxstyle='round,pad=0.02', facecolor=AZUL_MEDIO, edgecolor='#ccc', linewidth=0.5)
    ax.add_patch(rect)
    ax.text(mx + (cw[0]-0.04)/2, y + rh/2, label, fontsize=7.5,
           fontweight='bold', color='white', ha='center', va='center')
    for j, (v, w) in enumerate(zip(vals, cw[1:])):
        x = mx + cw[0] + sum(cw[1:j+1])
        rect = patches.FancyBboxPatch((x, y), w - 0.04, rh,
               boxstyle='round,pad=0.02', facecolor=bg, edgecolor='#ddd', linewidth=0.5)
        ax.add_patch(rect)
        ax.text(x + (w-0.04)/2, y + rh/2, v, fontsize=8,
               color='#111827', ha='center', va='center')

# Separador visual
sep_y = my - 3 * (rh + 0.03) + 0.15
ax.plot([mx, mx + sum(cw) - 0.04], [sep_y, sep_y], '--', color=NARANJA, lw=1, alpha=0.5)

for i, (label, vals, bg) in enumerate(factor_rows):
    y = my - (i + 3) * (rh + 0.03) - 0.05
    rect = patches.FancyBboxPatch((mx, y), cw[0] - 0.04, rh,
           boxstyle='round,pad=0.02', facecolor=NARANJA, edgecolor='#ccc', linewidth=0.5)
    ax.add_patch(rect)
    ax.text(mx + (cw[0]-0.04)/2, y + rh/2, label, fontsize=7,
           fontweight='bold', color='white', ha='center', va='center')
    for j, (v, w) in enumerate(zip(vals, cw[1:])):
        x = mx + cw[0] + sum(cw[1:j+1])
        rect = patches.FancyBboxPatch((x, y), w - 0.04, rh,
               boxstyle='round,pad=0.02', facecolor=bg, edgecolor='#ddd', linewidth=0.5)
        ax.add_patch(rect)
        ax.text(x + (w-0.04)/2, y + rh/2, v, fontsize=8,
               color='#111827', ha='center', va='center')

# Nota
ax.text(2.8, 2.5, 'Cada columna = insumos necesarios\npara producir $1 de output\n+ factores primarios (K, L)',
       fontsize=7.5, color=GRIS, ha='center', style='italic')

# ===== PASO 2: RASTREO =====

# Flecha de matriz a cajas
ax.annotate('', xy=(5.8, 6.2), xytext=(4.9, 5.5),
           arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))
ax.annotate('', xy=(5.8, 4.5), xytext=(4.9, 4.5),
           arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))

# Caja exportaciones
box_exp = patches.FancyBboxPatch((5.9, 5.6), 3.2, 1.5, boxstyle='round,pad=0.15',
          facecolor='#D1FAE5', edgecolor=VERDE, linewidth=2)
ax.add_patch(box_exp)
ax.text(7.5, 6.8, '$1 millón de', fontsize=9, ha='center', color=VERDE)
ax.text(7.5, 6.35, 'EXPORTACIONES', fontsize=13, fontweight='bold', ha='center', color=VERDE)
ax.text(7.5, 5.85, '¿Cuánto K y L hay "embebido"?', fontsize=8, ha='center', color=GRIS)

# Caja importaciones
box_imp = patches.FancyBboxPatch((5.9, 3.3), 3.2, 1.5, boxstyle='round,pad=0.15',
          facecolor='#FEE2E2', edgecolor=ROJO, linewidth=2)
ax.add_patch(box_imp)
ax.text(7.5, 4.5, '$1 millón de', fontsize=9, ha='center', color=ROJO)
ax.text(7.5, 4.05, 'SUSTITUTOS DE', fontsize=12, fontweight='bold', ha='center', color=ROJO)
ax.text(7.5, 3.6, 'IMPORTACIÓN', fontsize=12, fontweight='bold', ha='center', color=ROJO)

# ===== PASO 3: RESULTADO =====

# Flechas
ax.annotate('', xy=(9.8, 6.3), xytext=(9.2, 6.3),
           arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
ax.annotate('', xy=(9.8, 4.0), xytext=(9.2, 4.0),
           arrowprops=dict(arrowstyle='->', color=ROJO, lw=2.5))

# Resultado exportaciones
box_res_exp = patches.FancyBboxPatch((9.9, 5.5), 3.5, 1.6, boxstyle='round,pad=0.15',
              facecolor='#D1FAE5', edgecolor=VERDE, linewidth=2)
ax.add_patch(box_res_exp)
ax.text(11.65, 6.75, 'Exportaciones EE.UU.', fontsize=10, fontweight='bold', ha='center', color=VERDE)
ax.text(11.65, 6.15, 'K/L = $14.000', fontsize=16, fontweight='bold', ha='center', color=VERDE)
ax.text(11.65, 5.75, 'por trabajador', fontsize=9, ha='center', color=GRIS)

# Resultado importaciones
box_res_imp = patches.FancyBboxPatch((9.9, 3.0), 3.5, 1.6, boxstyle='round,pad=0.15',
              facecolor='#FEE2E2', edgecolor=ROJO, linewidth=2)
ax.add_patch(box_res_imp)
ax.text(11.65, 4.25, 'Sustitutos de importación', fontsize=10, fontweight='bold', ha='center', color=ROJO)
ax.text(11.65, 3.65, 'K/L = $18.000', fontsize=16, fontweight='bold', ha='center', color=ROJO)
ax.text(11.65, 3.25, 'por trabajador', fontsize=9, ha='center', color=GRIS)

# VS y comparación
ax.text(11.65, 5.25, '$14.000  <  $18.000', fontsize=11, fontweight='bold', color=NARANJA,
       ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=NARANJA, lw=1.5))

# ===== REMATE: LA PARADOJA =====
box_paradoja = patches.FancyBboxPatch((2.5, 0.3), 10, 1.8, boxstyle='round,pad=0.2',
               facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=2.5)
ax.add_patch(box_paradoja)
ax.text(7.5, 1.8, '¿PARADOJA?', fontsize=14, fontweight='bold', ha='center', color=ROJO)
ax.text(7.5, 1.25, 'EE.UU. es el país más CAPITAL-ABUNDANTE del mundo', fontsize=11,
       ha='center', color=AZUL_OSCURO, fontweight='bold')
ax.text(7.5, 0.7, 'Pero sus exportaciones son más TRABAJO-INTENSIVAS que sus importaciones  →  ¡lo contrario de H-O!',
       fontsize=10, ha='center', color=ROJO, fontweight='bold')

plt.tight_layout()
fig.savefig(OUT / 'leontief_metodo.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  + leontief_metodo.png")
