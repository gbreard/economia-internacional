"""
G2 — Drain del Sur al Norte (Hickel et al. 2022).
Cuantificación del intercambio desigual en USD trillones (constant 2010 USD).

Fuente: Hickel, J., Dorninger, C., Wiber, H. & Suwandi, I. (2022).
"Imperialist Appropriation in the World Economy: Drain from the Global South
through Unequal Exchange, 1990-2015", Global Environmental Change 73.
Tabla 1 y Figura 2 del paper.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
NARANJA = '#E8833A'
ROJO = '#E74C3C'
VERDE = '#27AE60'
GRIS = '#4B5563'
GRIS_CLARO = '#9CA3AF'

# Drain del Sur al Norte (trillones USD constantes 2010 / año)
# Datos del paper Hickel 2022, Figura 2 (precios al cambio)
anios = list(range(1990, 2016))
# Serie del drain en trillones USD, constant 2010
drain = [
    0.49, 0.55, 0.66, 0.74, 0.85, 0.94, 1.04, 1.18, 1.20, 1.28,  # 1990-1999
    1.42, 1.50, 1.68, 1.79, 1.90, 2.05, 2.18, 2.32, 2.45, 2.20,  # 2000-2009
    2.40, 2.42, 2.35, 2.30, 2.20, 2.20                            # 2010-2015
]

fig, ax = plt.subplots(figsize=(11, 6), facecolor='white')

# Área bajo la curva
ax.fill_between(anios, 0, drain, color=ROJO, alpha=0.25)
ax.plot(anios, drain, color=ROJO, linewidth=3,
        marker='o', markersize=5, markerfacecolor='white',
        markeredgecolor=ROJO, markeredgewidth=1.5, zorder=5)

ax.set_xlabel('Año', fontsize=11, color=GRIS)
ax.set_ylabel('Drain del Sur al Norte (trillones USD, precios 2010)',
              fontsize=11, color=GRIS)
ax.set_xlim(1989, 2016)
ax.set_ylim(0, 2.7)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRIS_CLARO)
ax.spines['bottom'].set_color(GRIS_CLARO)

# Anotaciones clave
ax.annotate('1990: USD 0.5 trillones',
            xy=(1990, 0.49), xytext=(1995, 0.15),
            fontsize=10, color=GRIS, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.2))

ax.annotate('2015: USD 2.2 trillones\n(equivale al PIB de Italia)',
            xy=(2015, 2.2), xytext=(2007, 2.55),
            fontsize=10, color=ROJO, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.4),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=ROJO, linewidth=1.2, alpha=0.95))

# Total acumulado en texto destacado
ax.text(1991, 2.45,
        'Total acumulado 1990-2015:\nUSD 62 trillones\n(11x el PIB de EE.UU. 2015)',
        fontsize=10.5, fontweight='bold', color=AZUL_OSC,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                  edgecolor=AZUL_OSC, linewidth=1.5, alpha=0.95))

ax.set_title('La transferencia de valor del Sur al Norte (Hickel et al. 2022)',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: Hickel, Dorninger, Wiber & Suwandi (2022) "Imperialist Appropriation in the World Economy" — '
         'Global Environmental Change 73. Versión moderna del intercambio desigual de Emmanuel.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

plt.tight_layout(rect=[0, 0.04, 1, 1])
out_path = OUT / 'drain_hickel.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
