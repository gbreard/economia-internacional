"""
Fix script: corrige 3 gráficos de Clase 2
1. limite_smith.png — "Clase 4" → "más adelante"
2. terminos_intercambio_paso{1,2,3}.png — texto solapado en paso 3
3. resumen_ricardo_paso{1,2,3}.png — etiquetas debajo de cajas más grandes
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


# ====================================================================
# 1. LIMITE SMITH — fix "Clase 4" → "más adelante"
# ====================================================================
def fix_limite_smith():
    fig = plt.figure(figsize=(12, 7.5))

    fig.text(0.50, 0.97, '¿Y si un país es mejor en todo?',
             ha='center', va='center', fontsize=15, fontweight='bold', color=ROJO)

    # Mini tabla de costos
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

    ax_table.text(8.5, 1.8, 'A gana en\nTela Y Vino', ha='center', va='center',
                  fontsize=9, fontweight='bold', color=ROJO,
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7', edgecolor=AMARILLO))
    ax_table.text(8.5, 0.8, 'Dotación:\n12 horas\ncada país', ha='center', va='center',
                  fontsize=8, color=GRIS, style='italic',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#DDDDDD'))

    # Panel izquierdo: Autarquía
    ax_aut = fig.add_axes([0.07, 0.08, 0.40, 0.62])

    categories = ['Tela', 'Vino']
    aut_A = [6, 3]
    aut_B = [1, 0.75]

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

    # Panel derecho: ¿Con comercio?
    ax_com = fig.add_axes([0.55, 0.08, 0.40, 0.62])
    ax_com.set_xlim(0, 10)
    ax_com.set_ylim(0, 10)
    ax_com.axis('off')

    border = mpatches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6,
                                      boxstyle="round,pad=0.2",
                                      facecolor='#FAFAFA', edgecolor='#CCCCCC',
                                      linewidth=2, linestyle='--')
    ax_com.add_patch(border)

    ax_com.text(5, 9.3, '¿Con comercio?', ha='center', va='center',
                fontsize=13, fontweight='bold', color=ROJO)

    ax_com.text(5, 5.5, '?', ha='center', va='center', fontsize=120,
                fontweight='bold', color=ROJO, alpha=0.15)

    ax_com.text(5, 6.8, 'A tiene ventaja absoluta\nen AMBOS bienes',
                ha='center', va='center', fontsize=11, fontweight='bold', color='#555555')

    ax_com.text(5, 5.5, '¿Qué exporta B?\n¿En qué se especializa?',
                ha='center', va='center', fontsize=12, fontweight='bold', color=ROJO)

    ax_com.text(5, 4.0, 'Smith no tiene respuesta\npara este caso',
                ha='center', va='center', fontsize=10, color=GRIS, style='italic')

    # *** FIX: "más adelante" en vez de "Clase 4" ***
    resolucion = mpatches.FancyBboxPatch((1.0, 1.0), 8.0, 2.0,
                                          boxstyle="round,pad=0.2",
                                          facecolor='#E8F5E9', edgecolor=VERDE,
                                          linewidth=2)
    ax_com.add_patch(resolucion)
    ax_com.text(5, 2.3, 'La respuesta la da RICARDO (más adelante):',
                ha='center', va='center', fontsize=10, fontweight='bold', color=VERDE)
    ax_com.text(5, 1.6, 'No importa quién es más barato en absoluto\nsino qué SACRIFICA cada uno → costo de oportunidad',
                ha='center', va='center', fontsize=9, color='#2E7D32')

    # Flecha entre paneles
    fig.text(0.50, 0.39, '→', ha='center', va='center', fontsize=40, color=ROJO,
             fontweight='bold')
    fig.text(0.50, 0.33, '¿Especialización?\n¿Intercambio?', ha='center', va='center',
             fontsize=9, color=ROJO, fontweight='bold')

    # Pie
    fig.text(0.50, 0.01,
             'Elaboración propia  •  El límite de la ventaja absoluta: no explica el comercio entre países muy desiguales',
             ha='center', fontsize=8, color='#888888', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'limite_smith.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ limite_smith.png (fix: "más adelante")')


# ====================================================================
# 2. TÉRMINOS DE INTERCAMBIO — progresivos con fix de overlap
# ====================================================================
def _draw_terminos_base(ax, show_pb=False, show_pw=False, show_explain=False):
    """Base para los 3 pasos. Mismo layout, se agregan elementos."""
    ax.set_xlim(0, 3)
    # Más alto para acomodar texto sin overlap
    if show_explain:
        ax.set_ylim(-1.8, 2.5)
    else:
        ax.set_ylim(-1.5, 2.5)

    # Título
    ax.text(1.5, 2.3, 'Términos de intercambio: el rango donde ambos ganan',
            ha='center', fontsize=15, fontweight='bold', color=AZUL_OSCURO)
    ax.text(1.5, 2.05, 'Precio relativo del Vino (en unidades de Tela): Pv / Pt',
            ha='center', fontsize=11, color='#555555')

    line_y = 0.8
    ax.plot([0.3, 2.7], [line_y, line_y], color='#CCCCCC', linewidth=3, zorder=1)

    def val_to_x(val):
        return 0.3 + (val - 0.5) / 2.0 * 2.4

    # Siempre mostrar PA (Autarquía A)
    xp_a = val_to_x(2.0)
    ax.plot(xp_a, line_y, 'o', color=AZUL_MEDIO, markersize=12, zorder=5)
    ax.plot([xp_a, xp_a], [line_y - 0.35, line_y + 0.35], color=AZUL_MEDIO, linewidth=3, zorder=4)
    ax.text(xp_a, line_y - 0.55, '2,0', ha='center', fontsize=11, fontweight='bold', color=AZUL_MEDIO)
    ax.text(xp_a, line_y + 0.55, 'Autarquía A\n(costo V en A)', ha='center', fontsize=9,
            fontweight='bold', color=AZUL_MEDIO)

    if show_pb:
        # PB
        xp_b = val_to_x(1.33)
        ax.plot(xp_b, line_y, 'o', color=NARANJA, markersize=12, zorder=5)
        ax.plot([xp_b, xp_b], [line_y - 0.35, line_y + 0.35], color=NARANJA, linewidth=3, zorder=4)
        ax.text(xp_b, line_y - 0.55, '1,33', ha='center', fontsize=11, fontweight='bold', color=NARANJA)
        ax.text(xp_b, line_y + 0.55, 'Autarquía B\n(costo V en B)', ha='center', fontsize=9,
                fontweight='bold', color=NARANJA)

        # Zona de comercio
        x_left = val_to_x(1.33)
        x_right = val_to_x(2.0)
        band = mpatches.FancyBboxPatch((x_left, line_y - 0.25), x_right - x_left, 0.5,
                                        boxstyle="round,pad=0.02",
                                        facecolor='#E8F5E9', edgecolor=VERDE,
                                        linewidth=2, alpha=0.7, zorder=2)
        ax.add_patch(band)
        ax.text((x_left + x_right) / 2, line_y, 'ZONA DE\nCOMERCIO',
                ha='center', va='center', fontsize=10, fontweight='bold', color=VERDE, zorder=3)

        # Extremos
        ax.text(val_to_x(0.7), line_y + 0.55, 'B no quiere\ncomerciar',
                ha='center', fontsize=8, color=GRIS, style='italic')
        ax.text(val_to_x(2.4), line_y + 0.55, 'A no quiere\ncomerciar',
                ha='center', fontsize=8, color=GRIS, style='italic')

    if show_pw:
        xp_pw = val_to_x(1.6)
        ax.plot(xp_pw, line_y, 'o', color=ROJO, markersize=15, zorder=6)
        ax.text(xp_pw, line_y - 0.55, '1,6', ha='center', fontsize=12,
                fontweight='bold', color=ROJO)
        ax.text(xp_pw, line_y + 0.55, 'Precio\nmundial', ha='center', fontsize=10,
                fontweight='bold', color=ROJO)

    if show_explain:
        # *** FIX: mejor espaciado, dos columnas lado a lado ***
        explain_y = -0.3
        # A (izquierda)
        ax.text(0.3, explain_y,
                '• A (comprador de V): en autarquía, 1V le cuesta 2T.\n'
                '  Con comercio a 1,6: ahorra 0,4T por cada vino. ✓',
                fontsize=9, color=AZUL_OSCURO, va='top')
        # B (debajo, con más separación)
        ax.text(0.3, explain_y - 0.7,
                '• B (vendedor de V): en autarquía, 1V le cuesta 1,33T.\n'
                '  Con comercio a 1,6: gana 0,27T extra por cada vino. ✓',
                fontsize=9, color='#C0392B', va='top')

    # Pie
    pie_y = -1.7 if show_explain else -1.4
    ax.text(1.5, pie_y, 'Elaboración propia  •  El rango 1,33 < P < 2 es la condición para que ambos prefieran comerciar',
            ha='center', fontsize=8, color='#888888', style='italic')


def fix_terminos_intercambio():
    # Paso 1: solo PA
    fig1, ax1 = plt.subplots(figsize=(14, 5.5))
    ax1.axis('off')
    _draw_terminos_base(ax1, show_pb=False, show_pw=False, show_explain=False)
    fig1.savefig(os.path.join(OUTPUT_DIR, 'terminos_intercambio_paso1.png'), dpi=150,
                 bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig1)
    print('✓ terminos_intercambio_paso1.png')

    # Paso 2: + PB + zona
    fig2, ax2 = plt.subplots(figsize=(14, 5.5))
    ax2.axis('off')
    _draw_terminos_base(ax2, show_pb=True, show_pw=False, show_explain=False)
    fig2.savefig(os.path.join(OUTPUT_DIR, 'terminos_intercambio_paso2.png'), dpi=150,
                 bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig2)
    print('✓ terminos_intercambio_paso2.png')

    # Paso 3: + Pw + explicaciones (con fix de overlap)
    fig3, ax3 = plt.subplots(figsize=(14, 6.5))
    ax3.axis('off')
    _draw_terminos_base(ax3, show_pb=True, show_pw=True, show_explain=True)
    fig3.savefig(os.path.join(OUTPUT_DIR, 'terminos_intercambio_paso3.png'), dpi=150,
                 bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig3)
    print('✓ terminos_intercambio_paso3.png')


# ====================================================================
# 3. RESUMEN RICARDO — progresivos con etiquetas más grandes
# ====================================================================
def _draw_resumen_base(ax, n_visible=2, show_conclusion=False):
    """Base para los 3 pasos. n_visible = cuántas cajas mostrar (2, 4, 6)."""
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.5)

    ax.text(7, 6.2, 'Ricardo: el mecanismo completo',
            ha='center', fontsize=16, fontweight='bold', color=AZUL_OSCURO)

    steps = [
        ('Tecnología\ndistinta', AZUL_OSCURO, 'white'),
        ('Costos de\noportunidad\ndistintos', AZUL_MEDIO, 'white'),
        ('Precios relativos\nen autarquía\ndistintos', AZUL_CLARO, 'white'),
        ('Especialización\n(ventaja\ncomparativa)', '#FFF5E6', AZUL_OSCURO),
        ('Comercio a\nprecio mundial\nintermedio', ROJO, 'white'),
        ('Ganancias\ndel comercio', VERDE, 'white'),
    ]

    examples = [
        'A: T=1h, V=2h\nB: T=6h, V=8h',
        'A: T→0,5V\nB: T→0,75V',
        'A: Pv=2T\nB: Pv=1,33T',
        'A → Tela\nB → Vino',
        '1,33 < P < 2\n(ej: P = 1,6)',
        'Consumo fuera\nde la PPF',
    ]

    n = len(steps)
    box_w = 1.7
    box_h = 1.3
    gap = 0.35
    total_w = n * box_w + (n - 1) * gap
    x_start = (14 - total_w) / 2

    for i, (label, bg, text_color) in enumerate(steps):
        x = x_start + i * (box_w + gap)
        y = 3.5

        if i < n_visible:
            # Caja visible
            if bg.startswith('#FFF'):
                # Caja con fondo claro y borde
                box = mpatches.FancyBboxPatch((x, y - box_h / 2), box_w, box_h,
                                               boxstyle="round,pad=0.1",
                                               facecolor=bg, edgecolor=AZUL_OSCURO,
                                               linewidth=2, zorder=3)
            else:
                box = mpatches.FancyBboxPatch((x, y - box_h / 2), box_w, box_h,
                                               boxstyle="round,pad=0.1",
                                               facecolor=bg, edgecolor='white',
                                               linewidth=2, zorder=3)
            ax.add_patch(box)
            ax.text(x + box_w / 2, y, label, ha='center', va='center',
                    fontsize=9.5, fontweight='bold', color=text_color, zorder=4)

            # *** FIX: etiquetas más grandes (10 en vez de 8) ***
            ax.text(x + box_w / 2, y - box_h / 2 - 0.35, examples[i],
                    ha='center', va='top', fontsize=10,
                    color='#555555', style='italic')
        else:
            # Placeholder gris
            box = mpatches.FancyBboxPatch((x, y - box_h / 2), box_w, box_h,
                                           boxstyle="round,pad=0.1",
                                           facecolor='#F0F0F0', edgecolor='#DDDDDD',
                                           linewidth=2, zorder=3)
            ax.add_patch(box)
            ax.text(x + box_w / 2, y, '?', ha='center', va='center',
                    fontsize=24, fontweight='bold', color='#CCCCCC', zorder=4)

        # Flecha entre cajas
        if i < n - 1:
            ax.annotate('', xy=(x + box_w + gap * 0.3, y),
                        xytext=(x + box_w + gap * 0.05, y),
                        arrowprops=dict(arrowstyle='->', color='#999999', lw=2))

    if show_conclusion:
        concl = mpatches.FancyBboxPatch((1.5, 0.5), 11, 0.8,
                                         boxstyle="round,pad=0.1",
                                         facecolor='#E8F5E9', edgecolor=VERDE,
                                         linewidth=2)
        ax.add_patch(concl)
        ax.text(7, 0.9, 'El comercio nace de diferencias RELATIVAS, no absolutas. '
                          'Ambos países ganan, incluso si uno es "mejor en todo".',
                ha='center', va='center', fontsize=10, fontweight='bold', color=VERDE)


def fix_resumen_ricardo():
    # Paso 1: cajas 1-2 visibles
    fig1, ax1 = plt.subplots(figsize=(14, 5.5))
    ax1.axis('off')
    _draw_resumen_base(ax1, n_visible=2, show_conclusion=False)
    fig1.savefig(os.path.join(OUTPUT_DIR, 'resumen_ricardo_paso1.png'), dpi=150,
                 bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig1)
    print('✓ resumen_ricardo_paso1.png')

    # Paso 2: cajas 1-4 visibles
    fig2, ax2 = plt.subplots(figsize=(14, 5.5))
    ax2.axis('off')
    _draw_resumen_base(ax2, n_visible=4, show_conclusion=False)
    fig2.savefig(os.path.join(OUTPUT_DIR, 'resumen_ricardo_paso2.png'), dpi=150,
                 bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig2)
    print('✓ resumen_ricardo_paso2.png')

    # Paso 3: todas + conclusión
    fig3, ax3 = plt.subplots(figsize=(14, 5.5))
    ax3.axis('off')
    _draw_resumen_base(ax3, n_visible=6, show_conclusion=True)
    fig3.savefig(os.path.join(OUTPUT_DIR, 'resumen_ricardo_paso3.png'), dpi=150,
                 bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig3)
    print('✓ resumen_ricardo_paso3.png')


# ====================================================================
# MAIN
# ====================================================================
if __name__ == '__main__':
    print('Corrigiendo gráficos Clase 2...\n')
    fix_limite_smith()
    fix_terminos_intercambio()
    fix_resumen_ricardo()
    print('\n¡Listo! 7 gráficos corregidos.')
