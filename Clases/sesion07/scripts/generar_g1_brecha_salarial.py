"""
G1 — Brecha salarial Norte-Sur en manufactura.
Mecanismo central del intercambio desigual de Emmanuel:
los salarios son la variable que crea la transferencia de valor.

Datos: ILO Global Wage Report 2024-25 + Conference Board ILC (Manufacturing
hourly compensation, USD corrientes).
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

# Salarios manufactureros por hora (USD), ~2022
# Fuente: ILO + Conference Board ILC + estimaciones BLS
paises = [
    ('Alemania', 49, 'norte'),
    ('Estados Unidos', 43, 'norte'),
    ('Italia', 35, 'norte'),
    ('Corea del Sur', 31, 'norte'),
    ('Argentina', 9, 'sur'),
    ('Brasil', 7, 'sur'),
    ('México', 5.5, 'sur'),
    ('China', 7, 'sur'),
    ('Indonesia', 2.5, 'sur'),
    ('Bangladesh', 1.2, 'sur'),
]

# Ordenar de mayor a menor
paises.sort(key=lambda x: -x[1])
nombres = [p[0] for p in paises]
valores = [p[1] for p in paises]
grupos = [p[2] for p in paises]
colores = [AZUL_OSC if g == 'norte' else NARANJA for g in grupos]

fig, ax = plt.subplots(figsize=(11, 6), facecolor='white')

bars = ax.barh(nombres, valores, color=colores, edgecolor='white', linewidth=0.8)
ax.invert_yaxis()  # mayor arriba

# Etiquetas en cada barra
for i, (nombre, valor, grupo) in enumerate(paises):
    ax.text(valor + 0.7, i, f'USD {valor}/h', va='center',
            fontsize=10, color=GRIS, fontweight='bold')

# Línea divisoria visual entre Norte y Sur
# Encontrar el primer "sur"
primer_sur = next(i for i, p in enumerate(paises) if p[2] == 'sur')
ax.axhline(primer_sur - 0.5, color=ROJO, linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(50, primer_sur - 0.5, 'BRECHA salarial', color=ROJO, fontsize=9,
        fontweight='bold', va='center', ha='right')

ax.set_xlabel('Salario por hora en manufactura (USD)', fontsize=11, color=GRIS)
ax.set_xlim(0, 60)
ax.tick_params(axis='y', labelsize=10.5)
ax.tick_params(axis='x', labelsize=9, colors=GRIS)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRIS_CLARO)
ax.spines['bottom'].set_color(GRIS_CLARO)
ax.grid(True, axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Leyenda
from matplotlib.patches import Patch
leg = [
    Patch(facecolor=AZUL_OSC, label='Norte Global'),
    Patch(facecolor=NARANJA, label='Sur Global'),
]
ax.legend(handles=leg, loc='lower right', fontsize=10, framealpha=0.95,
          edgecolor=GRIS_CLARO)

ax.set_title('La brecha salarial Norte-Sur en manufactura (2022)',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: elaboración propia con datos de ILO Global Wage Report 2024-25 y Conference Board ILC. '
         'Manufactura, hourly compensation, USD corrientes.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

# Anotación clave
ax.annotate('Alemania paga\n~40x más que\nBangladesh\npor la misma hora',
            xy=(1.2, 9), xytext=(28, 6.5),
            fontsize=10, fontweight='bold', color=ROJO, ha='center',
            arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.4),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=ROJO, linewidth=1.3, alpha=0.95))

plt.tight_layout(rect=[0, 0.04, 1, 1])
out_path = OUT / 'brecha_salarial_norte_sur.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
