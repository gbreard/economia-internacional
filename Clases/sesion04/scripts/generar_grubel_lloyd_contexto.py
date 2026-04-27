"""
Genera gráfico: contexto histórico del índice Grubel-Lloyd
Panel izq: crecimiento comercio intra-CEE post-1957
Panel der: GL index por país CEE 1965-1975 (datos RBA 1991)
"""
import sys
import io
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), gridspec_kw={'width_ratios': [1, 1.3]})

# ===== PANEL IZQUIERDO: Crecimiento comercio intra-CEE =====
years_trade = [1958, 1962, 1965, 1968, 1972, 1975]
# Índice base 1958=100, se cuadruplicó para 1968
trade_index = [100, 200, 280, 400, 520, 600]

ax1.fill_between(years_trade, trade_index, alpha=0.15, color=AZUL_MEDIO)
ax1.plot(years_trade, trade_index, 'o-', color=AZUL_MEDIO, linewidth=2.5, markersize=8)

# Anotaciones
ax1.axvline(x=1957, color=NARANJA, linestyle='--', alpha=0.7, linewidth=1.5)
ax1.annotate('Tratado\nde Roma\n(1957)', xy=(1957, 150), fontsize=8, color=NARANJA,
            ha='right', fontweight='bold')

ax1.axvline(x=1968, color=VERDE, linestyle='--', alpha=0.7, linewidth=1.5)
ax1.annotate('Aranceles\neliminados\n(1968)', xy=(1968, 500), fontsize=8, color=VERDE,
            ha='center', fontweight='bold')

ax1.annotate('x4', xy=(1968, 400), fontsize=16, fontweight='bold', color=ROJO,
            ha='left', va='center',
            xytext=(1969.5, 430),
            arrowprops=dict(arrowstyle='->', color=ROJO, lw=2))

ax1.set_xlabel('Año', fontsize=10)
ax1.set_ylabel('Índice (1958 = 100)', fontsize=10)
ax1.set_title('Comercio intra-CEE\nse cuadruplicó en 10 años', fontsize=13,
             fontweight='bold', color=AZUL_OSCURO)
ax1.set_ylim(0, 700)
ax1.set_xlim(1955, 1977)
ax1.grid(axis='y', alpha=0.3)

# ===== PANEL DERECHO: GL index por país CEE 1965-1975 =====
# Datos: RBA Research Discussion Paper 9110 (1991)
countries = ['Bélgica', 'Francia', 'Alemania', 'Países Bajos', 'Italia']
gl_1965 = [40, 39, 37, 38, 31]
gl_1975 = [50, 50, 47, 43, 38]

x = np.arange(len(countries))
width = 0.35

bars1 = ax2.bar(x - width/2, gl_1965, width, label='1965', color=AZUL_MEDIO, alpha=0.7, edgecolor='white')
bars2 = ax2.bar(x + width/2, gl_1975, width, label='1975', color=NARANJA, edgecolor='white')

# Valores sobre barras
for bar, val in zip(bars1, gl_1965):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val}%', ha='center', va='bottom', fontsize=9, color=AZUL_MEDIO, fontweight='bold')
for bar, val in zip(bars2, gl_1975):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val}%', ha='center', va='bottom', fontsize=9, color=NARANJA, fontweight='bold')

# Flechas de incremento
for i in range(len(countries)):
    delta = gl_1975[i] - gl_1965[i]
    ax2.annotate(f'+{delta}pp', xy=(x[i] + width/2, gl_1975[i] + 5),
                fontsize=8, color=VERDE, fontweight='bold', ha='center')

ax2.set_xticks(x)
ax2.set_xticklabels(countries, fontsize=9)
ax2.set_ylabel('Índice Grubel-Lloyd (%)', fontsize=10)
ax2.set_title('La "sorpresa": el comercio creció\nDENTRO de los mismos sectores', fontsize=13,
             fontweight='bold', color=AZUL_OSCURO)
ax2.set_ylim(0, 65)
ax2.legend(fontsize=10, loc='upper right')
ax2.grid(axis='y', alpha=0.3)

# Nota al pie
ax2.text(0.5, -0.12, 'IIT como % del comercio total de manufacturas (SITC 3 dígitos)',
        transform=ax2.transAxes, fontsize=8, color=GRIS, ha='center', style='italic')

fig.suptitle('¿Qué vieron Grubel y Lloyd? La integración europea no generó especialización inter-sectorial',
            fontsize=12, fontweight='bold', color=AZUL_OSCURO, y=1.02)

plt.tight_layout()
fig.savefig(OUT / 'grubel_lloyd_contexto.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  + grubel_lloyd_contexto.png")
