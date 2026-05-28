"""
G6 — Embraer: ventas y exportaciones aeronáuticas Brasil 1970-2024.
Caso de upgrading aeronáutico exitoso latinoamericano.

Datos: Embraer Annual Reports (1995-2024) + estimaciones históricas
del Centro Técnico Aeroespacial (CTA, antes ITA) para periodo 1970-1994.
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

# Ventas Embraer (USD millones) y % exportado
# Fuente: Embraer Annual Reports + reconstrucción histórica
datos = [
    # año, ventas USD M, % export
    (1970, 5, 5),    (1975, 80, 10),  (1980, 180, 25),
    (1985, 350, 40), (1990, 400, 55), (1994, 250, 75),
    (1995, 280, 80), (2000, 2700, 85),(2005, 3800, 92),
    (2010, 5000, 90),(2015, 5900, 88),(2018, 5400, 87),
    (2020, 3800, 85),(2022, 4400, 87),(2024, 6300, 88),
]

anios = [d[0] for d in datos]
ventas = [d[1] for d in datos]
export_pct = [d[2] for d in datos]

fig, ax1 = plt.subplots(figsize=(11, 6), facecolor='white')

# Barras de ventas (eje izquierdo)
ax1.bar(anios, ventas, width=2.5, color=VERDE, alpha=0.78,
        edgecolor='white', label='Ventas totales (USD M)')
ax1.set_xlabel('Año', fontsize=11, color=GRIS)
ax1.set_ylabel('Ventas anuales (USD millones)', fontsize=11, color=VERDE)
ax1.tick_params(axis='y', labelcolor=VERDE)
ax1.set_ylim(0, 7500)
ax1.set_xlim(1968, 2026)
ax1.grid(True, alpha=0.25, linestyle='--', axis='y')
ax1.set_axisbelow(True)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Línea de % exportado (eje derecho)
ax2 = ax1.twinx()
ax2.plot(anios, export_pct, color=NARANJA, linewidth=2.5,
         marker='o', markersize=6, markerfacecolor='white',
         markeredgecolor=NARANJA, markeredgewidth=1.5,
         label='% exportado', zorder=5)
ax2.set_ylabel('% de la facturación exportada', fontsize=11, color=NARANJA)
ax2.tick_params(axis='y', labelcolor=NARANJA)
ax2.set_ylim(0, 100)
ax2.spines['top'].set_visible(False)

# Hitos
hitos = [
    (1969, 'Fundación\nEmbraer\n(estatal)', 250, NARANJA),
    (1994, 'Privatización', 1800, ROJO),
    (1999, 'E-Jets\n(despegue\nregional)', 3700, AZUL_OSC),
    (2024, 'Líder global\nde regionales', 6600, VERDE),
]
for x, texto, y, color in hitos:
    ax1.annotate(texto, xy=(x, min(y * 0.6, 5500)), xytext=(x, y),
                 fontsize=9, fontweight='bold', color=color, ha='center',
                 arrowprops=dict(arrowstyle='->', color=color, lw=1.2),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                           edgecolor=color, linewidth=1.1, alpha=0.95))

ax1.set_title('Embraer: del proyecto estatal al líder mundial de jets regionales',
              fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: Embraer Annual Reports (1995-2024) + reconstrucción histórica CTA/ITA. '
         'Caso de capacidades construidas con apoyo estatal sostenido.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

# Leyenda combinada
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           loc='upper left', fontsize=10, framealpha=0.95,
           edgecolor=GRIS_CLARO)

plt.tight_layout(rect=[0, 0.04, 1, 1])
out_path = OUT / 'embraer_ventas.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
