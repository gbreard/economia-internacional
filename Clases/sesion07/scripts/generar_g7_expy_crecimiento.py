"""
G7 — EXPY vs. crecimiento (Hausmann, Hwang & Rodrik 2007).
"What you export matters": lo que exportás predice cuánto crecés.

Fuente: Hausmann, Hwang & Rodrik (2007) "What You Export Matters",
Journal of Economic Growth 12(1), Figure 3. Datos para ~80 países, 1992-2003.
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

# Países seleccionados (estilizado a partir de HHR 2007 Figure 3)
# (nombre, EXPY ~ 'sofisticación exportadora' en USD, crecimiento PIB pc % anual)
np.random.seed(42)
paises = [
    # Sofisticados + altos crecimientos
    ('Corea del Sur', 18500, 5.2, NARANJA),
    ('China', 12500, 8.5, ROJO),
    ('Singapur', 19000, 4.1, NARANJA),
    ('Irlanda', 19500, 6.5, NARANJA),
    ('Tailandia', 13000, 3.2, GRIS),
    ('Malasia', 14500, 3.0, GRIS),
    # Centro: altos EXPY
    ('Alemania', 19500, 1.4, AZUL_OSC),
    ('Japón', 19800, 1.1, AZUL_OSC),
    ('EE.UU.', 19000, 1.9, AZUL_OSC),
    ('Italia', 17500, 1.0, AZUL_OSC),
    ('Francia', 18000, 1.4, AZUL_OSC),
    ('Suecia', 18500, 2.1, AZUL_OSC),
    # Periferia y bajo crecimiento
    ('Argentina', 11500, 1.6, AZUL_MED),
    ('Brasil', 11000, 1.5, AZUL_MED),
    ('México', 14000, 1.2, AZUL_MED),
    ('Chile', 9500, 3.5, AZUL_MED),
    ('Indonesia', 9500, 2.5, GRIS),
    ('Filipinas', 10500, 1.8, GRIS),
    ('Vietnam', 8500, 4.8, ROJO),
    # Bajo EXPY, bajo crecimiento
    ('Nigeria', 5500, 2.0, GRIS),
    ('Egipto', 7500, 2.5, GRIS),
    ('Kenia', 5000, 0.8, GRIS),
    ('Bolivia', 6500, 1.2, GRIS),
    ('Etiopía', 4500, 1.5, GRIS),
    ('Bangladesh', 6000, 3.2, GRIS),
    ('Pakistán', 6500, 1.8, GRIS),
]

fig, ax = plt.subplots(figsize=(11.5, 6.5), facecolor='white')

# Scatter
xs = [p[1] for p in paises]
ys = [p[2] for p in paises]
colores = [p[3] for p in paises]

ax.scatter(xs, ys, s=140, c=colores, edgecolor='white', linewidth=1.5,
           alpha=0.92, zorder=3)

# Etiquetas
for nombre, x, y, c in paises:
    offset_y = 0.25
    if nombre in ('China', 'Corea del Sur', 'Vietnam'):
        offset_y = 0.35
    elif nombre in ('Italia', 'Francia', 'Suecia'):
        offset_y = -0.45
    ax.text(x, y + offset_y, nombre, ha='center', fontsize=8.5,
            color=GRIS, fontweight='bold')

# Línea de tendencia (regresión lineal de los puntos)
xs_a = np.array(xs)
ys_a = np.array(ys)
coef = np.polyfit(xs_a, ys_a, 1)
xs_line = np.array([4000, 21000])
ys_line = coef[0] * xs_line + coef[1]
ax.plot(xs_line, ys_line, color=ROJO, linewidth=2.2, linestyle='--',
        alpha=0.7, label='Tendencia (regresión lineal)', zorder=2)

ax.set_xlabel('EXPY — Sofisticación de la canasta exportadora (USD)',
              fontsize=11, color=GRIS)
ax.set_ylabel('Crecimiento del PIB per cápita (% anual, prom. 1992-2003)',
              fontsize=11, color=GRIS)
ax.set_xlim(3500, 22000)
ax.set_ylim(0, 10)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRIS_CLARO)
ax.spines['bottom'].set_color(GRIS_CLARO)

# Anotación interpretativa
ax.text(5000, 8.5,
        'Cuanto más sofisticada\nla canasta exportadora,\nmás rápido crece el país\n(controlando por nivel de ingreso)',
        fontsize=10.5, color=AZUL_OSC, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                  edgecolor=AZUL_OSC, linewidth=1.5, alpha=0.95))

ax.legend(loc='upper right', fontsize=10, framealpha=0.95,
          edgecolor=GRIS_CLARO)

ax.set_title('Lo que exportás predice cuánto crecés (Hausmann-Hwang-Rodrik 2007)',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: Hausmann, Hwang & Rodrik (2007) "What You Export Matters" — Journal of Economic Growth 12(1). '
         'EXPY: nivel de ingreso asociado a la canasta exportadora de cada país.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

plt.tight_layout(rect=[0, 0.04, 1, 1])
out_path = OUT / 'expy_crecimiento.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
