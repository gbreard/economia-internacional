"""
Curva de la sonrisa (smile curve) — esquema conceptual.
Etapas de la cadena en X, valor agregado en Y.
"""
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np

AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
GRIS = '#4B5563'

# Etapas de la cadena
etapas = ['I+D y\ndiseño', 'Propiedad\nintelectual', 'Componentes\nclave', 'Manufactura\ny ensamble',
          'Logística', 'Marca y\nmarketing', 'Comercialización', 'Servicios\npostventa']

# Valor agregado en cada etapa (escala 0-100)
valor = [85, 80, 50, 25, 30, 75, 85, 70]

x = np.arange(len(etapas))

fig, ax = plt.subplots(figsize=(13, 7.5))

# Curva suavizada (interpolación)
from scipy.interpolate import make_interp_spline
x_smooth = np.linspace(0, len(etapas)-1, 200)
spline = make_interp_spline(x, valor, k=3)
y_smooth = spline(x_smooth)

# Sombreado bajo la curva
ax.fill_between(x_smooth, y_smooth, 0, alpha=0.18, color=AZUL_MEDIO)

# Línea de la sonrisa
ax.plot(x_smooth, y_smooth, color=AZUL_OSCURO, linewidth=3, zorder=4)

# Puntos por etapa
for i, (e, v) in enumerate(zip(etapas, valor)):
    if v > 60:
        color = VERDE
    elif v > 40:
        color = NARANJA
    else:
        color = '#E74C3C'
    ax.scatter(i, v, s=200, color=color, edgecolor='white', linewidth=2, zorder=6)

# Zonas etiquetadas
ax.axvspan(-0.5, 2.5, alpha=0.07, color=VERDE)
ax.axvspan(2.5, 4.5, alpha=0.07, color='#E74C3C')
ax.axvspan(4.5, 7.5, alpha=0.07, color=VERDE)

# Etiquetas de las zonas
ax.text(1, 95, 'PRE-FABRICACIÓN\n(alto valor)', fontsize=11, color=VERDE,
        ha='center', fontweight='bold')
ax.text(3.5, 95, 'FABRICACIÓN\n(bajo valor)', fontsize=11, color='#E74C3C',
        ha='center', fontweight='bold')
ax.text(6, 95, 'POST-FABRICACIÓN\n(alto valor)', fontsize=11, color=VERDE,
        ha='center', fontweight='bold')

# Anotaciones tipo callout
ax.annotate('Apple (diseño + iOS)',
            xy=(0, 85), xytext=(-0.5, 70),
            fontsize=9, color=GRIS,
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.8))
ax.annotate('TSMC, Samsung\n(chips, pantallas)',
            xy=(2, 50), xytext=(1.3, 35),
            fontsize=9, color=GRIS,
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.8))
ax.annotate('Foxconn\n(ensamble)',
            xy=(3, 25), xytext=(3.2, 8),
            fontsize=9, color=GRIS,
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.8))
ax.annotate('Apple Store\n(retail)',
            xy=(6, 85), xytext=(6.4, 65),
            fontsize=9, color=GRIS,
            arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.8))

# Estilo
ax.set_xticks(x)
ax.set_xticklabels(etapas, fontsize=10, color=GRIS)
ax.set_ylabel('Valor agregado capturado (índice)', fontsize=11, color=GRIS)
ax.set_title('Curva de la sonrisa — captura de valor en una cadena global típica',
             fontsize=13, color=AZUL_OSCURO, fontweight='bold', pad=15)

ax.set_ylim(0, 105)
ax.set_xlim(-0.6, 7.6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', left=False, labelleft=False)
ax.tick_params(colors=GRIS)
ax.grid(False)

# Fuente
fig.text(0.02, 0.01,
         'Fuente: Stan Shih (Acer, 1992); formalización Mudambi (2008). Valores ilustrativos.',
         fontsize=8, color=GRIS, style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 1])
out = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'smile_curve.png')
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Generado: {out}')
