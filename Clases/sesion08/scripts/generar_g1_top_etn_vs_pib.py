"""
Top empresas Fortune Global 500 (2024) vs PIB de países latinoamericanos (2024).
Genera barras horizontales mixtas — empresas en azul, países en naranja.
"""
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Paleta
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
GRIS = '#4B5563'

# Datos (USD miles de millones)
items = [
    ('Walmart',          648, 'empresa'),
    ('Argentina',        638, 'pais'),
    ('Amazon',           575, 'empresa'),
    ('State Grid (CH)',  546, 'empresa'),
    ('Saudi Aramco',     495, 'empresa'),
    ('Sinopec (CH)',     430, 'empresa'),
    ('Colombia',         419, 'pais'),
    ('CNPC (CH)',        422, 'empresa'),
    ('Apple',            383, 'empresa'),
    ('UnitedHealth',     372, 'empresa'),
    ('Berkshire',        364, 'empresa'),
    ('CVS Health',       358, 'empresa'),
    ('Chile',            330, 'pais'),
    ('Perú',             289, 'pais'),
    ('Ecuador',          125, 'pais'),
    ('Venezuela',        120, 'pais'),
    ('Cuba',             107, 'pais'),
    ('Uruguay',           81, 'pais'),
    ('Bolivia',           55, 'pais'),
    ('Paraguay',          44, 'pais'),
]

# Ordenar por valor descendente
items.sort(key=lambda x: x[1], reverse=True)

labels = [it[0] for it in items]
values = [it[1] for it in items]
tipos = [it[2] for it in items]
colores = [AZUL_OSCURO if t == 'empresa' else NARANJA for t in tipos]

# --- Plot ---
fig, ax = plt.subplots(figsize=(13, 9))

y_pos = np.arange(len(labels))
bars = ax.barh(y_pos, values, color=colores, edgecolor='white', linewidth=0.8)

# Etiquetas con valor al final de cada barra
for i, (val, t) in enumerate(zip(values, tipos)):
    ax.text(val + 8, i, f'{val:,}', va='center', ha='left',
            fontsize=9, color=GRIS, fontweight='bold' if t == 'pais' else 'normal')

# Estilo
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=10)
ax.invert_yaxis()
ax.set_xlabel('Ingresos anuales / PIB nominal (USD miles de millones)', fontsize=11, color=GRIS)
ax.set_title('Top empresas globales vs PIB de países latinoamericanos (2024)',
             fontsize=13, color=AZUL_OSCURO, fontweight='bold', pad=15)

# Leyenda
empresa_patch = patches.Patch(color=AZUL_OSCURO, label='Empresa (Fortune Global 500)')
pais_patch = patches.Patch(color=NARANJA, label='País (PIB nominal, Banco Mundial)')
ax.legend(handles=[empresa_patch, pais_patch], loc='lower right', frameon=False, fontsize=10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='x', colors=GRIS)
ax.tick_params(axis='y', colors=GRIS)
ax.grid(axis='x', linestyle='--', alpha=0.3)
ax.set_xlim(0, max(values) * 1.15)

# Anotación clave
ax.annotate('Walmart factura más\nque el PIB de Argentina',
            xy=(640, 1), xytext=(720, 4),
            fontsize=10, color=AZUL_OSCURO, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=1.2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF8E7', edgecolor=AZUL_OSCURO))

# Fuente
fig.text(0.02, 0.01, 'Fuente: Fortune Global 500 (2024), datos FY2023 | Banco Mundial WDI, PIB nominal 2024',
         fontsize=8, color=GRIS, style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 1])
out = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'top_etn_vs_pib_paises.png')
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Generado: {out}')
