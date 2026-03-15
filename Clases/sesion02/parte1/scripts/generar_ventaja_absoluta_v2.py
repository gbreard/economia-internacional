"""
Gráfico de ventaja absoluta — versión pedagógica
Muestra el antes (autarquía) y después (comercio) para que se vea la ganancia.

Datos:
  Horas por unidad:  A: Tela=2, Vino=6 | B: Tela=4, Vino=3
  Dotación: 12 horas cada país

  Autarquía (reparten 50/50):
    A: 6 hs tela → 3 telas,  6 hs vino → 1 vino
    B: 6 hs tela → 1.5 telas, 6 hs vino → 2 vinos

  Con comercio (especialización total + intercambio):
    A produce 6 telas, B produce 4 vinos
    Intercambian: A da 3 telas a B por 2 vinos
    A: 3 telas + 2 vinos  (antes: 3 + 1 → gana +1 vino)
    B: 3 telas + 2 vinos  (antes: 1.5 + 2 → gana +1.5 tela)
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


def generar():
    fig = plt.figure(figsize=(12, 7.5))

    # ── Layout: tabla arriba, dos paneles abajo ──
    # Tabla de costos (parte superior)
    ax_table = fig.add_axes([0.15, 0.78, 0.70, 0.18])
    ax_table.axis('off')

    # Título principal
    fig.text(0.50, 0.97, 'Ventaja absoluta: ¿por qué ambos ganan con el comercio?',
             ha='center', va='center', fontsize=15, fontweight='bold', color=AZUL_OSCURO)

    # ── Mini tabla de costos ──
    ax_table.set_xlim(0, 10)
    ax_table.set_ylim(0, 3)

    ax_table.text(1.5, 2.6, 'Costos (horas por unidad):', ha='left', va='center',
                  fontsize=10, fontweight='bold', color='#444444')

    # Tabla compacta
    cols = ['', 'Tela', 'Vino', 'Ventaja']
    rows_data = [
        ['País A', '2 hs', '6 hs', 'Tela ✓'],
        ['País B', '4 hs', '3 hs', 'Vino ✓'],
    ]

    col_x = [1.8, 3.3, 4.5, 5.7, 7.0]
    row_y = [2.1, 1.5, 0.9]

    # Header
    for j, label in enumerate(cols):
        ax_table.text(col_x[j] + 0.5, row_y[0], label, ha='center', va='center',
                      fontsize=9, fontweight='bold', color=AZUL_OSCURO)

    # Línea bajo header
    ax_table.plot([col_x[0], col_x[-1] + 1.0], [row_y[0] - 0.25, row_y[0] - 0.25],
                  color='#CCCCCC', linewidth=1)

    for i, row in enumerate(rows_data):
        for j, val in enumerate(row):
            color = VERDE if '✓' in val else '#444444'
            weight = 'bold' if j == 0 or '✓' in val else 'normal'
            ax_table.text(col_x[j] + 0.5, row_y[i + 1], val, ha='center', va='center',
                          fontsize=9, fontweight=weight, color=color)

    # Nota: dotación
    ax_table.text(8.5, 1.5, 'Dotación:\n12 horas\ncada país', ha='center', va='center',
                  fontsize=8, color=GRIS, style='italic',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#DDDDDD'))

    # ── Panel izquierdo: Autarquía ──
    ax_aut = fig.add_axes([0.07, 0.08, 0.40, 0.62])

    categories = ['Tela', 'Vino']
    aut_A = [3, 1]      # A en autarquía: 6 hs tela → 3, 6 hs vino → 1
    aut_B = [1.5, 2]    # B en autarquía: 6 hs tela → 1.5, 6 hs vino → 2

    x = np.arange(len(categories))
    width = 0.32

    bars_A = ax_aut.bar(x - width/2, aut_A, width, label='País A', color=AZUL_MEDIO,
                        edgecolor='white', linewidth=1.5, zorder=3)
    bars_B = ax_aut.bar(x + width/2, aut_B, width, label='País B', color=NARANJA,
                        edgecolor='white', linewidth=1.5, zorder=3)

    # Valores sobre barras
    for bar, val in zip(bars_A, aut_A):
        ax_aut.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{val}', ha='center', va='bottom', fontsize=12,
                    fontweight='bold', color=AZUL_OSCURO)
    for bar, val in zip(bars_B, aut_B):
        ax_aut.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{val}', ha='center', va='bottom', fontsize=12,
                    fontweight='bold', color=NARANJA)

    ax_aut.set_title('En autarquía', fontsize=13, fontweight='bold', color='#555555', pad=12)
    ax_aut.set_xticks(x)
    ax_aut.set_xticklabels(categories, fontsize=12)
    ax_aut.set_ylabel('Unidades producidas / consumidas', fontsize=9, color='#777777')
    ax_aut.set_ylim(0, 5.5)
    ax_aut.legend(fontsize=10, loc='upper right')

    # Detalle debajo del título
    ax_aut.text(0.5, 0.93, 'Cada país reparte sus 12 hs\nmitad tela, mitad vino',
                transform=ax_aut.transAxes, ha='center', va='top',
                fontsize=8, color=GRIS, style='italic')

    # Estilo
    ax_aut.spines['top'].set_visible(False)
    ax_aut.spines['right'].set_visible(False)
    ax_aut.spines['left'].set_color('#CCCCCC')
    ax_aut.spines['bottom'].set_color('#CCCCCC')
    ax_aut.tick_params(colors='#555555')
    ax_aut.grid(axis='y', alpha=0.3, color='#CCCCCC')

    # ── Panel derecho: Con comercio ──
    ax_com = fig.add_axes([0.55, 0.08, 0.40, 0.62])

    com_A = [3, 2]      # A con comercio: 3 telas + 2 vinos
    com_B = [3, 2]      # B con comercio: 3 telas + 2 vinos

    bars_A2 = ax_com.bar(x - width/2, com_A, width, label='País A', color=AZUL_MEDIO,
                         edgecolor='white', linewidth=1.5, zorder=3)
    bars_B2 = ax_com.bar(x + width/2, com_B, width, label='País B', color=NARANJA,
                         edgecolor='white', linewidth=1.5, zorder=3)

    # Valores sobre barras + indicador de ganancia
    gains_A = [com_A[i] - aut_A[i] for i in range(2)]
    gains_B = [com_B[i] - aut_B[i] for i in range(2)]

    for bar, val, gain in zip(bars_A2, com_A, gains_A):
        bx = bar.get_x() + bar.get_width()/2
        by = bar.get_height()
        ax_com.text(bx, by + 0.1, f'{val}', ha='center', va='bottom',
                    fontsize=12, fontweight='bold', color=AZUL_OSCURO)
        if gain > 0:
            ax_com.text(bx, by + 0.55, f'+{gain:g}', ha='center', va='bottom',
                        fontsize=10, fontweight='bold', color=VERDE,
                        bbox=dict(boxstyle='round,pad=0.15', facecolor='#E8F5E9',
                                  edgecolor=VERDE, alpha=0.8))

    for bar, val, gain in zip(bars_B2, com_B, gains_B):
        bx = bar.get_x() + bar.get_width()/2
        by = bar.get_height()
        ax_com.text(bx, by + 0.1, f'{val}', ha='center', va='bottom',
                    fontsize=12, fontweight='bold', color=NARANJA)
        if gain > 0:
            ax_com.text(bx, by + 0.55, f'+{gain:g}', ha='center', va='bottom',
                        fontsize=10, fontweight='bold', color=VERDE,
                        bbox=dict(boxstyle='round,pad=0.15', facecolor='#E8F5E9',
                                  edgecolor=VERDE, alpha=0.8))

    ax_com.set_title('Con comercio', fontsize=13, fontweight='bold', color=VERDE, pad=12)
    ax_com.set_xticks(x)
    ax_com.set_xticklabels(categories, fontsize=12)
    ax_com.set_ylim(0, 5.5)
    ax_com.legend(fontsize=10, loc='upper right')

    # Detalle
    ax_com.text(0.5, 0.93, 'A se especializa en tela, B en vino\nIntercambian: 3 telas ↔ 2 vinos',
                transform=ax_com.transAxes, ha='center', va='top',
                fontsize=8, color=GRIS, style='italic')

    # Estilo
    ax_com.spines['top'].set_visible(False)
    ax_com.spines['right'].set_visible(False)
    ax_com.spines['left'].set_color('#CCCCCC')
    ax_com.spines['bottom'].set_color('#CCCCCC')
    ax_com.tick_params(colors='#555555')
    ax_com.grid(axis='y', alpha=0.3, color='#CCCCCC')

    # ── Flecha grande entre paneles ──
    fig.text(0.50, 0.39, '→', ha='center', va='center', fontsize=40, color=VERDE,
             fontweight='bold')
    fig.text(0.50, 0.33, 'Especialización\n+ intercambio', ha='center', va='center',
             fontsize=9, color=VERDE, fontweight='bold')

    # ── Conclusión al pie ──
    fig.text(0.50, 0.01,
             'Elaboración propia  •  Ambos países terminan con más (o igual) de cada bien que en autarquía',
             ha='center', fontsize=8, color='#888888', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'ventaja_absoluta_ejemplo.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ ventaja_absoluta_ejemplo.png (v2)')


if __name__ == '__main__':
    generar()
