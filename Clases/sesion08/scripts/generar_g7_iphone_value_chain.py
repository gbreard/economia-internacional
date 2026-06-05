"""
Caso iPhone — Distribución del valor por actor.
Donut chart + tabla lateral.
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1]})

# --- Donut chart ---
# Datos basados en Kraemer, Linden & Dedrick (2011) - iPhone 4
actores = ['Apple\n(EE.UU.)', 'Componentes\nCorea (Samsung, LG)', 'Componentes\nTaiwán-Japón-EE.UU.',
           'Ensamble\nChina (Foxconn)', 'Otros\n(distribución, etc.)']
pct = [58.5, 13.0, 14.4, 3.6, 10.5]
colores_donut = [AZUL_OSCURO, AZUL_MEDIO, AZUL_CLARO, ROJO, '#BDC3C7']

wedges, texts, autotexts = ax1.pie(pct, labels=actores, autopct='%1.1f%%',
                                     colors=colores_donut, startangle=90,
                                     wedgeprops=dict(width=0.4, edgecolor='white'),
                                     textprops=dict(fontsize=10, color=GRIS),
                                     pctdistance=0.78)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

# Texto central
ax1.text(0, 0.05, 'iPhone 4', fontsize=18, fontweight='bold', ha='center', color=AZUL_OSCURO)
ax1.text(0, -0.15, 'USD 549\nprecio retail', fontsize=11, ha='center', color=GRIS)

ax1.set_title('Distribución del valor capturado\n(iPhone 4, 2010)',
              fontsize=13, color=AZUL_OSCURO, fontweight='bold', pad=15)

# --- Tabla lateral con casos ---
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# Título
ax2.text(5, 9.5, 'Caso iPhone — Datos clave',
         fontsize=13, color=AZUL_OSCURO, fontweight='bold', ha='center')

# Datos en formato tabla
datos = [
    ('Apple captura', '~58,5% del valor', AZUL_OSCURO),
    ('Ensamblador China (Foxconn)', '~3,6% del valor', ROJO),
    ('Componentes asiáticos', '~27% del valor', AZUL_MEDIO),
    ('', '', None),
    ('Foxconn fabrica', '~65% de iPhones globales', GRIS),
    ('Empleados Zhengzhou', '~200.000', GRIS),
    ('Meta Apple India 2026', '25% (hoy ~14%)', GRIS),
    ('TSMC chips ≤7nm', '~90% del mundo', GRIS),
    ('', '', None),
    ('Salario Foxconn (China)', '4-8 USD/h', GRIS),
    ('Margen ensamblador típico', '5-10%', GRIS),
    ('Margen Apple bruto', '~38%', GRIS),
]

y_pos = 8.4
for label, valor, color in datos:
    if label:
        ax2.text(0.5, y_pos, label, fontsize=10, color=GRIS, va='top')
        ax2.text(9.5, y_pos, valor, fontsize=10, color=color if color else GRIS,
                 va='top', ha='right', fontweight='bold')
    y_pos -= 0.55

# Línea separadora
ax2.axhline(y=4.7, xmin=0.05, xmax=0.95, color=GRIS, alpha=0.3, linestyle='--')
ax2.axhline(y=2.5, xmin=0.05, xmax=0.95, color=GRIS, alpha=0.3, linestyle='--')

# Implicancia clave en caja
implicancia = ('La estadística "EE.UU. importa iPhones desde China" oculta '
               'que el grueso del valor lo captura una empresa estadounidense (Apple).')
ax2.text(5, 0.5, implicancia, fontsize=9.5, color=AZUL_OSCURO, ha='center', va='center',
         style='italic', wrap=True,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF8E7', edgecolor=AZUL_OSCURO, alpha=0.9))

# Fuente general
fig.text(0.02, 0.01,
         'Fuente: Kraemer, Linden & Dedrick (2011) "Capturing Value in Global Networks", UC Irvine. '
         'Datos complementarios: Counterpoint Research, reportes Apple/Foxconn/TSMC.',
         fontsize=8, color=GRIS, style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 1])
out = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'iphone_value_chain.png')
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Generado: {out}')
