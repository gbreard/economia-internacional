"""
G3 — Las 3 Leyes de Kaldor (esquema conceptual).
Manufactura como motor del crecimiento. Retornos crecientes dinámicos.
Fuente: Kaldor (1966) Causes of the Slow Rate of Economic Growth of the UK.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
GRIS = '#4B5563'
GRIS_CLARO = '#9CA3AF'

fig, ax = plt.subplots(figsize=(12, 7), facecolor='white')
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.set_axis_off()

# Título y subtítulo
ax.text(6, 6.5, 'Las 3 leyes de Kaldor — la manufactura como motor',
        ha='center', fontsize=15, fontweight='bold', color=AZUL_OSC)
ax.text(6, 6.05, 'Por qué importa qué se produce (no solo cuánto)',
        ha='center', fontsize=11, style='italic', color=GRIS)

# Tres cajas, una por ley
boxes = [
    (1.5, 'LEY 1', 'Manufactura\n→ motor del PIB',
     'Cuanto más rápido crece\nla industria,\nmás rápido crece el PIB total',
     AZUL_OSC),
    (5.5, 'LEY 2', 'Verdoorn\n(retornos crecientes)',
     'Cuanto más crece la producción\nmanufacturera,\nmás crece su productividad',
     NARANJA),
    (9.5, 'LEY 3', 'Restricción externa',
     'Sin manufactura competitiva\n→ déficit comercial crónico\n→ Stop-Go',
     VERDE),
]

for x, etiqueta, titulo, texto, color in boxes:
    # Caja con título
    box = FancyBboxPatch((x - 1.5, 2.5), 3, 2.6,
                         boxstyle='round,pad=0.05',
                         facecolor=color, edgecolor=color,
                         linewidth=2, alpha=0.92)
    ax.add_patch(box)

    # Etiqueta (Ley N)
    ax.text(x, 4.85, etiqueta, ha='center', fontsize=11,
            fontweight='bold', color='white')
    # Título
    ax.text(x, 4.3, titulo, ha='center', fontsize=11.5,
            fontweight='bold', color='white')
    # Texto explicativo
    ax.text(x, 3.15, texto, ha='center', fontsize=10,
            color='white')

# Flechas entre cajas
arrow_kwargs = dict(arrowstyle='->', color=GRIS, lw=2.2,
                    mutation_scale=22)
ax.add_patch(FancyArrowPatch((3.05, 3.8), (3.95, 3.8), **arrow_kwargs))
ax.add_patch(FancyArrowPatch((7.05, 3.8), (7.95, 3.8), **arrow_kwargs))

# Texto debajo: implicancia
ax.text(6, 1.8, 'Implicancia',
        ha='center', fontsize=12, fontweight='bold', color=AZUL_OSC)
ax.text(6, 1.2,
        'Las ventajas comparativas se construyen produciendo.\n'
        'El comercio según ventajas estáticas puede consolidar especializaciones\n'
        'de bajo dinamismo tecnológico (commodities, ensamblaje).',
        ha='center', fontsize=11, color=GRIS, style='italic')

# Fuente
ax.text(6, 0.25,
        'Fuente: Kaldor, N. (1966) "Causes of the Slow Rate of Economic Growth of the UK"',
        ha='center', fontsize=8.5, style='italic', color=GRIS_CLARO)

plt.tight_layout()
out_path = OUT / 'leyes_kaldor.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
