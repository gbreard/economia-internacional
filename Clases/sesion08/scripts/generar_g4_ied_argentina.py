"""
IED en Argentina — Stock por país de origen y por sector.
2 subplots integrados.
"""
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np

AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
AZUL_CLARO = '#0EA5E9'
NARANJA = '#E8833A'
VERDE = '#27AE60'
GRIS = '#4B5563'

fig = plt.figure(figsize=(14, 6))

# --- Panel 1: Top países de origen (% del stock) ---
ax1 = plt.subplot(1, 2, 1)
paises = ['EE.UU.', 'España', 'Países Bajos*', 'Brasil', 'Chile', 'Alemania',
          'Suiza', 'Francia', 'China', 'Otros']
pct = [19, 14, 11, 7, 6, 5, 4, 4, 3, 27]
montos = [23.9, 18.3, 14.6, 8.9, 7.6, 6.4, 5.1, 5.1, 3.8, 33.8]  # miles de millones
colores = [AZUL_OSCURO] * 3 + [AZUL_MEDIO] * 6 + ['#BDC3C7']

bars1 = ax1.barh(paises, pct, color=colores, edgecolor='white', linewidth=1.0)
for i, (p, m) in enumerate(zip(pct, montos)):
    ax1.text(p + 0.5, i, f'{p}% (USD {m:.1f} mil M)', va='center', ha='left',
             fontsize=9, color=GRIS)

ax1.invert_yaxis()
ax1.set_title('Stock IED por país de origen — % del total',
              fontsize=12, color=AZUL_OSCURO, fontweight='bold')
ax1.set_xlabel('% del stock total', fontsize=10, color=GRIS)
ax1.set_xlim(0, 35)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(colors=GRIS)
ax1.grid(axis='x', linestyle='--', alpha=0.3)

# Nota sobre Países Bajos
ax1.text(0.02, -0.13, '* Países Bajos: muchas operaciones triangulan vía holdings holandesas (no es inversión "industrial" real)',
         transform=ax1.transAxes, fontsize=8, color=GRIS, style='italic')

# --- Panel 2: Stock IED por sector (USD miles de millones) ---
ax2 = plt.subplot(1, 2, 2)
sectores = ['Manufactura', 'Petróleo, gas\ny minería', 'Servicios financieros',
            'Comercio', 'Otros servicios', 'Resto']
montos_sector = [49.2, 27.0, 18.5, 12.0, 11.5, 9.4]
colors_sect = [AZUL_OSCURO, NARANJA, AZUL_MEDIO, AZUL_CLARO, '#5DADE2', '#BDC3C7']

bars2 = ax2.barh(sectores, montos_sector, color=colors_sect, edgecolor='white', linewidth=1.0)
for i, m in enumerate(montos_sector):
    pct_total = (m / sum(montos_sector)) * 100
    ax2.text(m + 0.8, i, f'USD {m:.1f} mil M  ({pct_total:.0f}%)',
             va='center', ha='left', fontsize=9, color=GRIS)

ax2.invert_yaxis()
ax2.set_title('Stock IED por sector receptor',
              fontsize=12, color=AZUL_OSCURO, fontweight='bold')
ax2.set_xlabel('USD miles de millones', fontsize=10, color=GRIS)
ax2.set_xlim(0, 65)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.tick_params(colors=GRIS)
ax2.grid(axis='x', linestyle='--', alpha=0.3)

# Título y subtítulo
fig.suptitle('IED en Argentina — Stock total al 31/12/2023: USD 127.556 millones',
             fontsize=13, color=AZUL_OSCURO, fontweight='bold', y=0.99)

fig.text(0.5, 0.94, 'Capital: USD 77.093 M + Deuda intra-firma: USD 50.462 M',
         ha='center', fontsize=10, color=GRIS, style='italic')

fig.text(0.02, 0.01, 'Fuente: BCRA — Informe de Inversión Extranjera Directa, 4T 2023',
         fontsize=8, color=GRIS, style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 0.93])
out = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'ied_argentina_origen_sector.png')
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Generado: {out}')
