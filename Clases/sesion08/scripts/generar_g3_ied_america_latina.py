"""
IED en América Latina 2024 — por país receptor + por origen + por sector.
3 subplots integrados.
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
ROJO = '#E74C3C'
GRIS = '#4B5563'

fig = plt.figure(figsize=(15, 6))

# --- Panel 1: Por país receptor ---
ax1 = plt.subplot(1, 3, 1)
paises = ['Brasil', 'México', 'Colombia', 'Chile', 'Argentina', 'Otros']
porcentajes = [38, 24, 7, 7, 6, 18]
variaciones = ['+14%', '+48%', '-15%', '-32%', '-53%', '-']
colors_paises = [AZUL_OSCURO, AZUL_MEDIO, AZUL_CLARO, '#5DADE2', NARANJA, '#BDC3C7']

bars1 = ax1.barh(paises, porcentajes, color=colors_paises, edgecolor='white', linewidth=1.2)
for i, (p, v) in enumerate(zip(porcentajes, variaciones)):
    color_v = VERDE if v.startswith('+') else (ROJO if v.startswith('-') else GRIS)
    ax1.text(p + 1, i, f'{p}%', va='center', ha='left', fontsize=10, color=GRIS, fontweight='bold')
    ax1.text(p + 7, i, f'({v})', va='center', ha='left', fontsize=9, color=color_v, style='italic')

ax1.invert_yaxis()
ax1.set_title('Por país receptor', fontsize=12, color=AZUL_OSCURO, fontweight='bold')
ax1.set_xlabel('% del total regional', fontsize=10, color=GRIS)
ax1.set_xlim(0, 55)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(colors=GRIS)
ax1.grid(axis='x', linestyle='--', alpha=0.3)

# --- Panel 2: Por país de origen ---
ax2 = plt.subplot(1, 3, 2)
origenes = ['EE.UU.', 'Europa\n(esp+ned+ale)', 'AL\nintraregional', 'China', 'Otros']
origen_pct = [38, 25, 12, 9, 16]
colors_origen = [AZUL_OSCURO, AZUL_MEDIO, NARANJA, ROJO, '#BDC3C7']

wedges, texts, autotexts = ax2.pie(origen_pct, labels=origenes, autopct='%1.0f%%',
                                     colors=colors_origen, startangle=90,
                                     wedgeprops=dict(width=0.5, edgecolor='white'),
                                     textprops=dict(fontsize=10, color=GRIS))
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax2.set_title('Por país de origen del capital', fontsize=12, color=AZUL_OSCURO, fontweight='bold')

# --- Panel 3: Por sector ---
ax3 = plt.subplot(1, 3, 3)
sectores = ['Manufactura', 'Servicios', 'Recursos\nnaturales']
sector_pct = [43.6, 40.4, 16.0]
colors_sect = [AZUL_OSCURO, AZUL_MEDIO, NARANJA]

bars3 = ax3.bar(sectores, sector_pct, color=colors_sect, edgecolor='white', linewidth=1.2, width=0.6)
for bar, pct in zip(bars3, sector_pct):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{pct}%',
             ha='center', va='bottom', fontsize=11, color=GRIS, fontweight='bold')

ax3.set_title('Por sector', fontsize=12, color=AZUL_OSCURO, fontweight='bold')
ax3.set_ylabel('% del total regional', fontsize=10, color=GRIS)
ax3.set_ylim(0, 55)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.tick_params(colors=GRIS)
ax3.grid(axis='y', linestyle='--', alpha=0.3)

# Título general
fig.suptitle('IED en América Latina y el Caribe — Total 2024: USD 188.962 millones (+7,1% vs 2023)',
             fontsize=13, color=AZUL_OSCURO, fontweight='bold', y=0.99)

fig.text(0.02, 0.01, 'Fuente: CEPAL — La Inversión Extranjera Directa en AL y el Caribe 2025 (datos 2024)',
         fontsize=8, color=GRIS, style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 0.95])
out = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'ied_america_latina_2024.png')
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Generado: {out}')
