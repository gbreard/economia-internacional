"""
Flujos globales de IED 1990-2024.
Serie temporal con hitos marcados.
"""
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np

AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
NARANJA = '#E8833A'
ROJO = '#E74C3C'
GRIS = '#4B5563'

# Datos UNCTAD WIR (estimaciones con interpolación para años intermedios)
# Fuentes verificadas: 1990 (~203), 2000 (~1400), 2007 (1833 pico), 2015 (1760), 2020 (~1000), 2022 (~1300), 2023 (1300), 2024 (1500)
anos = list(range(1990, 2025))
ied = [
    # 1990-1995
    203, 230, 175, 220, 260, 340,
    # 1996-2000
    400, 490, 705, 1075, 1400,
    # 2001-2005
    830, 625, 565, 720, 980,
    # 2006-2010
    1460, 1833, 1490, 1185, 1340,
    # 2011-2015
    1565, 1510, 1430, 1300, 1760,
    # 2016-2020
    1870, 1430, 1495, 1480, 1000,
    # 2021-2024
    1580, 1300, 1300, 1500,
]

# Verificar que tienen la misma longitud
assert len(anos) == len(ied), f"Anos: {len(anos)}, IED: {len(ied)}"

fig, ax = plt.subplots(figsize=(13, 7))

# Línea principal con shading
ax.fill_between(anos, ied, alpha=0.15, color=AZUL_MEDIO)
ax.plot(anos, ied, color=AZUL_OSCURO, linewidth=2.5, marker='o', markersize=4, zorder=3)

# Hitos importantes con posiciones de etiquetas ajustadas
hitos = [
    (2000, 1400, 'Pico\ndot-com',       (0, 180)),
    (2007, 1833, 'Récord histórico\n(pre-crisis)',  (0, 150)),
    (2015, 1760, 'Segundo pico',        (-1, 200)),
    (2020, 1000, 'COVID-19',            (0, -180)),
    (2024, 1500, '2024: USD\n1.500 mil M', (-0.5, 250)),
]

for ano, valor, label, (off_x, off_y) in hitos:
    ax.scatter(ano, valor, s=90, color=NARANJA, zorder=5, edgecolor='white', linewidth=1.5)
    ax.annotate(label, xy=(ano, valor), xytext=(ano + off_x, valor + off_y),
                fontsize=9, color=GRIS, ha='center', fontweight='bold')

# Zonas sombreadas para crisis (más sutiles)
ax.axvspan(2008, 2009, alpha=0.10, color=ROJO)
ax.text(2008.5, 50, 'Crisis subprime', fontsize=8, color=ROJO, ha='center', style='italic')

ax.axvspan(2020, 2020.5, alpha=0.10, color=ROJO)

# Banda destacando slowbalization (sin texto encima de hitos)
ax.axvspan(2015, 2024, alpha=0.05, color=ROJO)
ax.text(2019.5, 350, 'Slowbalization (2015→)', fontsize=10, color=ROJO,
        style='italic', ha='center', fontweight='bold')

ax.set_xlabel('Año', fontsize=11, color=GRIS)
ax.set_ylabel('Flujo anual de IED (USD miles de millones)', fontsize=11, color=GRIS)
ax.set_title('Flujos globales de Inversión Extranjera Directa (1990-2024)',
             fontsize=13, color=AZUL_OSCURO, fontweight='bold', pad=15)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(colors=GRIS)
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_xlim(1989, 2025)
ax.set_ylim(0, 2200)

# Fuente
fig.text(0.02, 0.01, 'Fuente: UNCTAD World Investment Report (varios años, 1990-2024)',
         fontsize=8, color=GRIS, style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 1])
out = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'flujos_ied_mundiales_1990_2024.png')
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Generado: {out}')
