"""
Genera linea de tiempo de la concentracion territorial argentina (1880-hoy).
4 fases historicas con causas e indicadores clave de concentracion.

Output: Clases/sesion04/graficos/timeline_concentracion_argentina.png
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

sys.stdout.reconfigure(encoding='utf-8')

# Paleta UMET
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
AZUL_CLARO = '#0EA5E9'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS_BASE = '#E5E7EB'
TEXTO = '#111827'
GRIS_TEXTO = '#4B5563'

OUT_DIR = Path(__file__).resolve().parent.parent / 'graficos'

# Fases historicas
fases = [
    {
        'nombre': '1.\nModelo\nagroexportador',
        'periodo': '1880 - 1930',
        'descripcion': [
            'Pais "abanico":',
            'puerto BA = nodo unico',
            '+ ferrocarriles a la pampa',
            '+ frigorificos en Rosario',
        ],
        'concentracion': 'AMBA emerge como\ncentro absoluto',
        'color': AZUL_MEDIO,
    },
    {
        'nombre': '2.\nIndustrializacion\npor Sustitucion',
        'periodo': '1930 - 1976',
        'descripcion': [
            'Cordon industrial GBA:',
            'textil, metalmecanica',
            'IKA en Cordoba (1955)',
            'YPF: enclaves petroleros',
        ],
        'concentracion': 'AMBA se refuerza,\nCordoba emerge',
        'color': AZUL_OSCURO,
    },
    {
        'nombre': '3.\nApertura y\nreformas',
        'periodo': '1976 - 2002',
        'descripcion': [
            'Desindustrializacion:',
            'cierran textiles, metales',
            'CABA se "terciariza"',
            '(servicios, finanzas)',
        ],
        'concentracion': 'AMBA se concentra\nen servicios',
        'color': NARANJA,
    },
    {
        'nombre': '4.\nSoja, servicios\ne hidrocarburos',
        'periodo': '2002 - hoy',
        'descripcion': [
            'Boom soja: Rosario-SLO',
            'Vaca Muerta (Neuquen)',
            'Software/SBC en CABA',
            'TdF: regimen especial',
        ],
        'concentracion': 'Multipolar pero\naun mas concentrado',
        'color': VERDE,
    },
]

fig, ax = plt.subplots(figsize=(15, 8.5), facecolor='white')
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)
ax.axis('off')

ax.set_title(
    'Argentina: 145 anios de concentracion territorial',
    fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=15, loc='left')
ax.text(0, 9.7, 'Cuatro regimenes economicos, una sola constante: AMBA en el centro',
        fontsize=11, color=GRIS_TEXTO, style='italic')

# Linea de tiempo horizontal
y_line = 8.0
ax.plot([2, 98], [y_line, y_line], color=GRIS_BASE, linewidth=8, solid_capstyle='round')

# Anios clave
anios_x = [4, 28, 53, 78, 96]
anios_label = ['1880', '1930', '1976', '2002', '2024']
for x, lbl in zip(anios_x, anios_label):
    ax.plot(x, y_line, 'o', color=AZUL_OSCURO, markersize=10, zorder=3)
    ax.text(x, y_line + 0.5, lbl, ha='center', fontsize=10,
            fontweight='bold', color=AZUL_OSCURO)

# Cuatro fases - cards
card_y = 4.2  # centro vertical
card_h = 4.6
gap = 1.0
total_w = 96 - 4
card_w = (total_w - 3 * gap) / 4

for i, fase in enumerate(fases):
    x_start = 4 + i * (card_w + gap)
    x_center = x_start + card_w / 2

    # Banda de color superior con nombre de fase
    head_h = 1.4
    head = mpatches.FancyBboxPatch(
        (x_start, card_y + (card_h / 2) - head_h),
        card_w, head_h,
        boxstyle='round,pad=0.0,rounding_size=0.15',
        facecolor=fase['color'], edgecolor=fase['color'])
    ax.add_patch(head)
    ax.text(x_center, card_y + (card_h / 2) - head_h / 2, fase['nombre'],
            ha='center', va='center', fontsize=10,
            fontweight='bold', color='white')

    # Cuerpo de card
    body_h = card_h - head_h
    body = mpatches.FancyBboxPatch(
        (x_start, card_y - card_h / 2),
        card_w, body_h,
        boxstyle='round,pad=0.0,rounding_size=0.15',
        facecolor='white', edgecolor=fase['color'], linewidth=1.5)
    ax.add_patch(body)

    # Periodo
    ax.text(x_center, card_y + body_h / 2 - 0.45,
            fase['periodo'], ha='center', va='center',
            fontsize=10, fontweight='bold', color=fase['color'])

    # Descripcion - lineas
    line_y = card_y + body_h / 2 - 1.1
    for line in fase['descripcion']:
        ax.text(x_center, line_y, line, ha='center', va='center',
                fontsize=8.5, color=TEXTO)
        line_y -= 0.42

    # Concentracion - resaltado al final
    ax.text(x_center, card_y - body_h / 2 + 0.55,
            fase['concentracion'], ha='center', va='center',
            fontsize=8.5, fontweight='bold', color=fase['color'],
            style='italic')

# Flecha de path dependence al pie
ax.annotate('',
            xy=(96, 1.2), xytext=(4, 1.2),
            arrowprops=dict(arrowstyle='->', color=ROJO, lw=2.5))
ax.text(50, 0.6,
        'Path dependence: cada regimen agrega capas a la concentracion existente',
        ha='center', va='center', fontsize=10.5,
        fontweight='bold', color=ROJO, style='italic')

plt.tight_layout()
out = OUT_DIR / 'timeline_concentracion_argentina.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'Generado: {out}')
