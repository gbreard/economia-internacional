"""
Gráfico del límite de Smith — versión pedagógica (misma lógica que ventaja absoluta v2)
Muestra autarquía (izquierda) y el PROBLEMA cuando A es mejor en todo (derecha vacía).

Datos:
  Horas por unidad:  A: Tela=1, Vino=2 | B: Tela=6, Vino=8
  Dotación: 12 horas cada país

  Autarquía (reparten 50/50):
    A: 6 hs tela → 6 telas,  6 hs vino → 3 vinos
    B: 6 hs tela → 1 tela,   6 hs vino → 0.75 vinos

  ¿Con comercio?: A tiene ventaja absoluta en TODO.
  Según Smith → A debería producir todo. ¿B no exporta nada?
  Pero en la realidad SÍ hay comercio entre países desiguales...
  → La respuesta la da Ricardo (clase 4)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os, sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'graficos')

AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#7F8C8D'
AMARILLO    = '#F59E0B'


def generar():
    fig = plt.figure(figsize=(12, 7.5))

    # ── Título principal ──
    fig.text(0.50, 0.97, '¿Y si un país es mejor en todo?',
             ha='center', va='center', fontsize=15, fontweight='bold', color=ROJO)

    # ── Mini tabla de costos (arriba) ──
    ax_table = fig.add_axes([0.15, 0.78, 0.70, 0.18])
    ax_table.axis('off')
    ax_table.set_xlim(0, 10)
    ax_table.set_ylim(0, 3)

    ax_table.text(1.5, 2.6, 'Costos (horas por unidad):', ha='left', va='center',
                  fontsize=10, fontweight='bold', color='#444444')

    cols = ['', 'Tela', 'Vino', '¿Ventaja?']
    rows_data = [
        ['País A', '1 hs', '2 hs', 'Tela ✓'],
        ['País B', '6 hs', '8 hs', '—'],
    ]

    col_x = [1.8, 3.3, 4.5, 5.7, 7.0]
    row_y = [2.1, 1.5, 0.9]

    for j, label in enumerate(cols):
        ax_table.text(col_x[j] + 0.5, row_y[0], label, ha='center', va='center',
                      fontsize=9, fontweight='bold', color=AZUL_OSCURO)

    ax_table.plot([col_x[0], col_x[-1] + 1.0], [row_y[0] - 0.25, row_y[0] - 0.25],
                  color='#CCCCCC', linewidth=1)

    for i, row in enumerate(rows_data):
        for j, val in enumerate(row):
            if '✓' in val:
                color = AZUL_MEDIO
            elif val == '—':
                color = ROJO
            else:
                color = '#444444'
            weight = 'bold' if j == 0 or '✓' in val or val == '—' else 'normal'
            ax_table.text(col_x[j] + 0.5, row_y[i + 1], val, ha='center', va='center',
                          fontsize=9, fontweight=weight, color=color)

    # Nota: A gana en ambos
    ax_table.text(8.5, 1.8, 'A gana en\nTela Y Vino', ha='center', va='center',
                  fontsize=9, fontweight='bold', color=ROJO,
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7', edgecolor=AMARILLO))
    ax_table.text(8.5, 0.8, 'Dotación:\n12 horas\ncada país', ha='center', va='center',
                  fontsize=8, color=GRIS, style='italic',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#DDDDDD'))

    # ── Panel izquierdo: Autarquía ──
    ax_aut = fig.add_axes([0.07, 0.08, 0.40, 0.62])

    categories = ['Tela', 'Vino']
    aut_A = [6, 3]       # A: 6 hs → 6 telas, 6 hs → 3 vinos
    aut_B = [1, 0.75]    # B: 6 hs → 1 tela, 6 hs → 0.75 vinos

    x = np.arange(len(categories))
    width = 0.32

    bars_A = ax_aut.bar(x - width/2, aut_A, width, label='País A', color=AZUL_MEDIO,
                        edgecolor='white', linewidth=1.5, zorder=3)
    bars_B = ax_aut.bar(x + width/2, aut_B, width, label='País B', color=NARANJA,
                        edgecolor='white', linewidth=1.5, zorder=3)

    for bar, val in zip(bars_A, aut_A):
        ax_aut.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                    f'{val:g}', ha='center', va='bottom', fontsize=12,
                    fontweight='bold', color=AZUL_OSCURO)
    for bar, val in zip(bars_B, aut_B):
        ax_aut.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                    f'{val:g}', ha='center', va='bottom', fontsize=12,
                    fontweight='bold', color=NARANJA)

    ax_aut.set_title('En autarquía', fontsize=13, fontweight='bold', color='#555555', pad=12)
    ax_aut.set_xticks(x)
    ax_aut.set_xticklabels(categories, fontsize=12)
    ax_aut.set_ylabel('Unidades producidas / consumidas', fontsize=9, color='#777777')
    ax_aut.set_ylim(0, 8)
    ax_aut.legend(fontsize=10, loc='upper right')

    ax_aut.text(0.5, 0.93, 'Cada país reparte sus 12 hs\nmitad tela, mitad vino',
                transform=ax_aut.transAxes, ha='center', va='top',
                fontsize=8, color=GRIS, style='italic')

    # Highlight: la diferencia enorme entre A y B
    ax_aut.annotate('A produce\n6× más tela\ny 4× más vino',
                    xy=(0.15, 4.5), fontsize=9, color=ROJO, fontweight='bold',
                    ha='center',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7',
                              edgecolor=AMARILLO, alpha=0.9))

    ax_aut.spines['top'].set_visible(False)
    ax_aut.spines['right'].set_visible(False)
    ax_aut.spines['left'].set_color('#CCCCCC')
    ax_aut.spines['bottom'].set_color('#CCCCCC')
    ax_aut.tick_params(colors='#555555')
    ax_aut.grid(axis='y', alpha=0.3, color='#CCCCCC')

    # ── Panel derecho: ¿Con comercio? (VACÍO con pregunta) ──
    ax_com = fig.add_axes([0.55, 0.08, 0.40, 0.62])
    ax_com.set_xlim(0, 10)
    ax_com.set_ylim(0, 10)
    ax_com.axis('off')

    # Fondo con borde punteado
    border = mpatches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6,
                                      boxstyle="round,pad=0.2",
                                      facecolor='#FAFAFA', edgecolor='#CCCCCC',
                                      linewidth=2, linestyle='--')
    ax_com.add_patch(border)

    ax_com.text(5, 9.3, '¿Con comercio?', ha='center', va='center',
                fontsize=13, fontweight='bold', color=ROJO)

    # Gran signo de interrogación
    ax_com.text(5, 5.5, '?', ha='center', va='center', fontsize=120,
                fontweight='bold', color=ROJO, alpha=0.15)

    # Preguntas
    ax_com.text(5, 6.8, 'A tiene ventaja absoluta\nen AMBOS bienes',
                ha='center', va='center', fontsize=11, fontweight='bold', color='#555555')

    ax_com.text(5, 5.5, '¿Qué exporta B?\n¿En qué se especializa?',
                ha='center', va='center', fontsize=12, fontweight='bold', color=ROJO)

    ax_com.text(5, 4.0, 'Smith no tiene respuesta\npara este caso',
                ha='center', va='center', fontsize=10, color=GRIS, style='italic')

    # Caja con la resolución
    resolucion = mpatches.FancyBboxPatch((1.0, 1.0), 8.0, 2.0,
                                          boxstyle="round,pad=0.2",
                                          facecolor='#E8F5E9', edgecolor=VERDE,
                                          linewidth=2)
    ax_com.add_patch(resolucion)
    ax_com.text(5, 2.3, 'La respuesta la da RICARDO (Clase 4):',
                ha='center', va='center', fontsize=10, fontweight='bold', color=VERDE)
    ax_com.text(5, 1.6, 'No importa quién es más barato en absoluto\nsino qué SACRIFICA cada uno → costo de oportunidad',
                ha='center', va='center', fontsize=9, color='#2E7D32')

    # ── Flecha entre paneles ──
    fig.text(0.50, 0.39, '→', ha='center', va='center', fontsize=40, color=ROJO,
             fontweight='bold')
    fig.text(0.50, 0.33, '¿Especialización?\n¿Intercambio?', ha='center', va='center',
             fontsize=9, color=ROJO, fontweight='bold')

    # ── Pie ──
    fig.text(0.50, 0.01,
             'Elaboración propia  •  El límite de la ventaja absoluta: no explica el comercio entre países muy desiguales',
             ha='center', fontsize=8, color='#888888', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'limite_smith.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ limite_smith.png (v2)')


if __name__ == '__main__':
    generar()
