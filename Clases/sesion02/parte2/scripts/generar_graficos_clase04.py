"""
Gráficos para Clase 4 — Ricardo y la ventaja comparativa.

8 gráficos:
1. corn_laws_conflicto.png — Triángulo distributivo
2. costo_oportunidad_tabla.png — Tabla + cálculo de costos de oportunidad
3. ventaja_comparativa_resultado.png — Antes/después: autarquía vs comercio
4. terminos_intercambio.png — Recta numérica con rango 1.33-2
5. ppf_pais_a.png — PPF + línea de intercambio País A
6. ppf_pais_b.png — PPF + línea de intercambio País B
7. resumen_ricardo.png — Diagrama de flujo
8. rca_argentina.png — Composición exportadora Argentina

Datos del modelo:
  Horas por unidad: A: Tela=1, Vino=2 | B: Tela=6, Vino=8
  Dotación PPF: 48 horas cada país
  Precio mundial ejemplo: P_V/P_T = 1.6
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os, sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#7F8C8D'
AMARILLO    = '#F59E0B'


# ====================================================================
# 1. CORN LAWS — CONFLICTO DISTRIBUTIVO
# ====================================================================
def generar_corn_laws():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.0, 1.5)
    ax.axis('off')

    # Título
    ax.text(0, 1.45, 'Las Corn Laws (1815): conflicto distributivo',
            ha='center', va='center', fontsize=16, fontweight='bold', color=AZUL_OSCURO)

    # Triángulo con tres nodos
    # Terratenientes (arriba), Industriales (abajo izq), Trabajadores (abajo der)
    nodes = {
        'Terratenientes\n(renta de la tierra)': (0, 0.85),
        'Industriales\n(ganancias)': (-1.0, -0.35),
        'Trabajadores\n(salarios / costo de vida)': (1.0, -0.35),
    }
    colors = [VERDE, AZUL_MEDIO, NARANJA]
    labels = list(nodes.keys())
    coords = list(nodes.values())

    # Dibujar lados del triángulo
    for i in range(3):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % 3]
        ax.plot([x1, x2], [y1, y2], color='#CCCCCC', linewidth=2, linestyle='--', zorder=1)

    # Nodos
    for i, (label, (x, y)) in enumerate(nodes.items()):
        circle = mpatches.FancyBboxPatch((x - 0.42, y - 0.18), 0.84, 0.36,
                                          boxstyle="round,pad=0.05",
                                          facecolor=colors[i], edgecolor='white',
                                          linewidth=2, zorder=3, alpha=0.9)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=11,
                fontweight='bold', color='white', zorder=4)

    # Corn Laws en el centro (arriba)
    corn_box = mpatches.FancyBboxPatch((-0.55, 0.15), 1.1, 0.32,
                                        boxstyle="round,pad=0.05",
                                        facecolor='#FEF3C7', edgecolor=AMARILLO,
                                        linewidth=2, zorder=5)
    ax.add_patch(corn_box)
    ax.text(0, 0.31, 'CORN LAWS\nProtección al grano',
            ha='center', va='center', fontsize=12, fontweight='bold', color=ROJO, zorder=6)

    # Flechas con efectos
    # Corn Laws → Terratenientes: GANAN
    ax.annotate('', xy=(0, 0.67), xytext=(0, 0.47),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
    ax.text(0.25, 0.58, '↑ Renta SUBE', fontsize=9, color=VERDE, fontweight='bold')

    # Corn Laws → Industriales: PIERDEN
    ax.annotate('', xy=(-0.65, -0.15), xytext=(-0.3, 0.15),
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=2.5))
    ax.text(-1.1, -0.05, '↓ Ganancia\n   BAJA', fontsize=9, color=ROJO, fontweight='bold')

    # Corn Laws → Trabajadores: PIERDEN
    ax.annotate('', xy=(0.65, -0.15), xytext=(0.3, 0.15),
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=2.5))
    ax.text(0.75, -0.05, '↑ Costo vida\n   SUBE', fontsize=9, color=ROJO, fontweight='bold')

    # Cadena causal abajo
    chain_y = -0.7
    steps = ['Protección\ngrano', 'Precio\nalimentos ↑', 'Costo de\nvida ↑',
             'Salarios\npresionados', 'Ganancia\nindustrial ↓']
    step_x = np.linspace(-1.1, 1.1, len(steps))

    for i, (x, step) in enumerate(zip(step_x, steps)):
        color = AMARILLO if i == 0 else ROJO
        box = mpatches.FancyBboxPatch((x - 0.2, chain_y - 0.12), 0.4, 0.24,
                                       boxstyle="round,pad=0.03",
                                       facecolor='#FFF5F5' if i > 0 else '#FEF3C7',
                                       edgecolor=color, linewidth=1.5, zorder=3)
        ax.add_patch(box)
        ax.text(x, chain_y, step, ha='center', va='center', fontsize=7.5,
                fontweight='bold', color='#444444', zorder=4)
        if i < len(steps) - 1:
            ax.annotate('', xy=(step_x[i + 1] - 0.22, chain_y),
                        xytext=(x + 0.22, chain_y),
                        arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))

    # Pie
    ax.text(0, -0.95, 'Ricardo (1817): la ventaja comparativa es el argumento técnico para abrir el comercio de granos',
            ha='center', fontsize=9, color=GRIS, style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'corn_laws_conflicto.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ corn_laws_conflicto.png')


# ====================================================================
# 2. COSTOS DE OPORTUNIDAD — TABLA + CÁLCULOS
# ====================================================================
def generar_costo_oportunidad():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Título
    ax.text(6, 9.7, 'Costos de oportunidad: la clave de Ricardo',
            ha='center', fontsize=16, fontweight='bold', color=AZUL_OSCURO)

    # --- TABLA DE HORAS (arriba) ---
    table_top = 8.8
    ax.text(6, table_top, 'Horas de trabajo por unidad:',
            ha='center', fontsize=11, fontweight='bold', color='#444444')

    # Headers
    cols_x = [2.5, 4.5, 6.5, 8.5]
    headers = ['', 'Tela', 'Vino', '¿Ventaja abs.?']
    for x, h in zip(cols_x, headers):
        ax.text(x, table_top - 0.5, h, ha='center', fontsize=10, fontweight='bold', color=AZUL_OSCURO)

    ax.plot([1.5, 9.5], [table_top - 0.75, table_top - 0.75], color='#CCCCCC', linewidth=1)

    # País A
    row_a = [('País A', AZUL_MEDIO), ('1 h', '#444'), ('2 h', '#444'), ('Ambos ✓', AZUL_MEDIO)]
    for x, (val, col) in zip(cols_x, row_a):
        ax.text(x, table_top - 1.1, val, ha='center', fontsize=10,
                fontweight='bold' if 'País' in val or '✓' in val else 'normal', color=col)

    # País B
    row_b = [('País B', NARANJA), ('6 h', '#444'), ('8 h', '#444'), ('Ninguno —', ROJO)]
    for x, (val, col) in zip(cols_x, row_b):
        ax.text(x, table_top - 1.6, val, ha='center', fontsize=10,
                fontweight='bold' if 'País' in val or '—' in val else 'normal', color=col)

    # Nota: A gana en ambos
    ax.text(10.5, table_top - 1.0, 'A es mejor\nen TODO',
            ha='center', fontsize=9, fontweight='bold', color=ROJO,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7', edgecolor=AMARILLO))

    # --- COSTOS DE OPORTUNIDAD (centro) ---
    ax.text(6, 6.7, '¿Qué SACRIFICA cada país?', ha='center', fontsize=14,
            fontweight='bold', color=ROJO)

    # País A - panel izquierdo
    ax.text(3, 6.0, 'País A', ha='center', fontsize=13, fontweight='bold', color=AZUL_MEDIO)

    calcs_a = [
        ('1 Tela cuesta:', '1h / 2h = 0,5 Vinos'),
        ('1 Vino cuesta:', '2h / 1h = 2 Telas'),
    ]
    for i, (label, calc) in enumerate(calcs_a):
        y = 5.3 - i * 0.8
        ax.text(1.5, y, label, fontsize=10, color='#555', fontweight='bold')
        ax.text(1.5, y - 0.35, calc, fontsize=11, color=AZUL_OSCURO, fontweight='bold')

    # País B - panel derecho
    ax.text(9, 6.0, 'País B', ha='center', fontsize=13, fontweight='bold', color=NARANJA)

    calcs_b = [
        ('1 Tela cuesta:', '6h / 8h = 0,75 Vinos'),
        ('1 Vino cuesta:', '8h / 6h = 1,33 Telas'),
    ]
    for i, (label, calc) in enumerate(calcs_b):
        y = 5.3 - i * 0.8
        ax.text(7.5, y, label, fontsize=10, color='#555', fontweight='bold')
        ax.text(7.5, y - 0.35, calc, fontsize=11, color=NARANJA, fontweight='bold')

    # Línea separadora vertical
    ax.plot([6, 6], [3.5, 6.5], color='#DDDDDD', linewidth=2, linestyle='--')

    # --- CONCLUSIÓN (abajo) ---
    conclusion_y = 2.8
    # Box verde para conclusión
    concl_box = mpatches.FancyBboxPatch((0.8, 1.5), 10.4, 2.2,
                                         boxstyle="round,pad=0.2",
                                         facecolor='#E8F5E9', edgecolor=VERDE,
                                         linewidth=2)
    ax.add_patch(concl_box)

    ax.text(6, 3.3, 'VENTAJA COMPARATIVA', ha='center', fontsize=13,
            fontweight='bold', color=VERDE)

    ax.text(3, 2.6, 'A: Tela → costo 0,5V', ha='center', fontsize=11,
            fontweight='bold', color=AZUL_MEDIO)
    ax.text(3, 2.15, '(menor que B: 0,75V)', ha='center', fontsize=9, color=AZUL_MEDIO)
    ax.text(3, 1.8, '→ A exporta TELA', ha='center', fontsize=11,
            fontweight='bold', color=AZUL_OSCURO)

    ax.text(9, 2.6, 'B: Vino → costo 1,33T', ha='center', fontsize=11,
            fontweight='bold', color=NARANJA)
    ax.text(9, 2.15, '(menor que A: 2T)', ha='center', fontsize=9, color=NARANJA)
    ax.text(9, 1.8, '→ B exporta VINO', ha='center', fontsize=11,
            fontweight='bold', color='#C0392B')

    # Flechas de exportación
    ax.annotate('', xy=(4.5, 2.6), xytext=(3.8, 2.6),
                arrowprops=dict(arrowstyle='->', color=AZUL_MEDIO, lw=2))
    ax.annotate('', xy=(10.2, 2.6), xytext=(9.5, 2.6),
                arrowprops=dict(arrowstyle='->', color=NARANJA, lw=2))

    # Pie
    ax.text(6, 0.9, 'No importa ser el mejor en absoluto — importa en qué sacrificás menos',
            ha='center', fontsize=10, color=GRIS, style='italic', fontweight='bold')
    ax.text(6, 0.4, 'Elaboración propia',
            ha='center', fontsize=8, color='#AAAAAA', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'costo_oportunidad_tabla.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ costo_oportunidad_tabla.png')


# ====================================================================
# 3. VENTAJA COMPARATIVA RESULTADO — AUTARQUÍA vs COMERCIO
# ====================================================================
def generar_ventaja_comparativa_resultado():
    fig = plt.figure(figsize=(12, 7.5))

    fig.text(0.50, 0.97, 'Ventaja comparativa: ambos ganan con el comercio',
             ha='center', va='center', fontsize=15, fontweight='bold', color=AZUL_OSCURO)

    # Datos con 48 horas, reparto 50/50 en autarquía
    # A: 24h tela → 24T, 24h vino → 12V
    # B: 24h tela → 4T, 24h vino → 3V
    categories = ['Tela', 'Vino']
    aut_A = [24, 12]
    aut_B = [4, 3]

    # Con comercio: comparar manteniendo mismo consumo de vino
    # A quiere mantener 12V: produce 48T, compra 12V a 1.6T/V = paga 19.2T
    # A: 48 - 19.2 = 28.8T + 12V (antes: 24T + 12V → +4.8T, mismo V)
    # B quiere mantener 3V: produce 6V, vende 3V a 1.6T/V = 4.8T
    # B: 4.8T + 3V (antes: 4T + 3V → +0.8T, mismo V)
    com_A = [28.8, 12]
    com_B = [4.8, 3]

    x = np.arange(len(categories))
    width = 0.32

    # Panel izquierdo: Autarquía
    ax_aut = fig.add_axes([0.07, 0.08, 0.40, 0.78])

    bars_A = ax_aut.bar(x - width / 2, aut_A, width, label='País A', color=AZUL_MEDIO,
                        edgecolor='white', linewidth=1.5, zorder=3)
    bars_B = ax_aut.bar(x + width / 2, aut_B, width, label='País B', color=NARANJA,
                        edgecolor='white', linewidth=1.5, zorder=3)

    for bar, val in zip(bars_A, aut_A):
        ax_aut.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                    f'{val:g}', ha='center', va='bottom', fontsize=12,
                    fontweight='bold', color=AZUL_OSCURO)
    for bar, val in zip(bars_B, aut_B):
        ax_aut.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                    f'{val:g}', ha='center', va='bottom', fontsize=12,
                    fontweight='bold', color=NARANJA)

    ax_aut.set_title('En autarquía (50/50)', fontsize=13, fontweight='bold', color='#555555', pad=12)
    ax_aut.set_xticks(x)
    ax_aut.set_xticklabels(categories, fontsize=12)
    ax_aut.set_ylabel('Unidades producidas / consumidas', fontsize=9, color='#777777')
    ax_aut.set_ylim(0, 35)
    ax_aut.legend(fontsize=10, loc='upper right')
    ax_aut.text(0.5, 0.93, '48 horas, repartidas\nmitad tela, mitad vino',
                transform=ax_aut.transAxes, ha='center', va='top',
                fontsize=8, color=GRIS, style='italic')

    for spine in ['top', 'right']:
        ax_aut.spines[spine].set_visible(False)
    ax_aut.spines['left'].set_color('#CCCCCC')
    ax_aut.spines['bottom'].set_color('#CCCCCC')
    ax_aut.tick_params(colors='#555555')
    ax_aut.grid(axis='y', alpha=0.3, color='#CCCCCC')

    # Panel derecho: Con comercio
    ax_com = fig.add_axes([0.55, 0.08, 0.40, 0.78])

    bars_A2 = ax_com.bar(x - width / 2, com_A, width, label='País A', color=AZUL_MEDIO,
                         edgecolor='white', linewidth=1.5, zorder=3)
    bars_B2 = ax_com.bar(x + width / 2, com_B, width, label='País B', color=NARANJA,
                         edgecolor='white', linewidth=1.5, zorder=3)

    gains_A = [com_A[i] - aut_A[i] for i in range(2)]
    gains_B = [com_B[i] - aut_B[i] for i in range(2)]

    for bar, val, gain in zip(bars_A2, com_A, gains_A):
        bx = bar.get_x() + bar.get_width() / 2
        by = bar.get_height()
        ax_com.text(bx, by + 0.5, f'{val:g}', ha='center', va='bottom',
                    fontsize=12, fontweight='bold', color=AZUL_OSCURO)
        if gain > 0:
            ax_com.text(bx, by + 3.5, f'+{gain:g}', ha='center', va='bottom',
                        fontsize=10, fontweight='bold', color=VERDE,
                        bbox=dict(boxstyle='round,pad=0.15', facecolor='#E8F5E9',
                                  edgecolor=VERDE, alpha=0.8))
        elif gain < 0:
            ax_com.text(bx, by + 3.5, f'{gain:g}', ha='center', va='bottom',
                        fontsize=10, fontweight='bold', color=ROJO,
                        bbox=dict(boxstyle='round,pad=0.15', facecolor='#FFF5F5',
                                  edgecolor=ROJO, alpha=0.8))

    for bar, val, gain in zip(bars_B2, com_B, gains_B):
        bx = bar.get_x() + bar.get_width() / 2
        by = bar.get_height()
        ax_com.text(bx, by + 0.5, f'{val:g}', ha='center', va='bottom',
                    fontsize=12, fontweight='bold', color=NARANJA)
        if gain > 0:
            ax_com.text(bx, by + 3.5, f'+{gain:g}', ha='center', va='bottom',
                        fontsize=10, fontweight='bold', color=VERDE,
                        bbox=dict(boxstyle='round,pad=0.15', facecolor='#E8F5E9',
                                  edgecolor=VERDE, alpha=0.8))

    ax_com.set_title('Con comercio (P = 1,6 T/V)', fontsize=13, fontweight='bold', color=VERDE, pad=12)
    ax_com.set_xticks(x)
    ax_com.set_xticklabels(categories, fontsize=12)
    ax_com.set_ylim(0, 35)
    ax_com.legend(fontsize=10, loc='upper right')
    ax_com.text(0.5, 0.93, 'A se especializa en tela, B en vino\nMismo consumo de vino + más tela',
                transform=ax_com.transAxes, ha='center', va='top',
                fontsize=8, color=GRIS, style='italic')

    for spine in ['top', 'right']:
        ax_com.spines[spine].set_visible(False)
    ax_com.spines['left'].set_color('#CCCCCC')
    ax_com.spines['bottom'].set_color('#CCCCCC')
    ax_com.tick_params(colors='#555555')
    ax_com.grid(axis='y', alpha=0.3, color='#CCCCCC')

    # Flecha
    fig.text(0.50, 0.47, '→', ha='center', va='center', fontsize=40, color=VERDE, fontweight='bold')
    fig.text(0.50, 0.41, 'Especialización\n+ intercambio', ha='center', va='center',
             fontsize=9, color=VERDE, fontweight='bold')

    # Pie
    fig.text(0.50, 0.01,
             'Elaboración propia  •  Mismo consumo de vino, más tela para ambos. La especialización genera ganancias.',
             ha='center', fontsize=8, color='#888888', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'ventaja_comparativa_resultado.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ ventaja_comparativa_resultado.png')


# ====================================================================
# 4. TÉRMINOS DE INTERCAMBIO — RECTA NUMÉRICA
# ====================================================================
def generar_terminos_intercambio():
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_xlim(0, 3)
    ax.set_ylim(-1.5, 2.5)
    ax.axis('off')

    # Título
    ax.text(1.5, 2.3, 'Términos de intercambio: el rango donde ambos ganan',
            ha='center', fontsize=15, fontweight='bold', color=AZUL_OSCURO)

    ax.text(1.5, 2.05, 'Precio relativo del Vino (en unidades de Tela): P_V / P_T',
            ha='center', fontsize=11, color='#555555')

    # Recta numérica
    line_y = 0.8
    ax.plot([0.3, 2.7], [line_y, line_y], color='#CCCCCC', linewidth=3, zorder=1)

    # Marcas
    marks = {0.5: ('0,5', None, ''),
             1.33: ('1,33', AZUL_MEDIO, 'Autarquía A'),
             1.6: ('1,6', ROJO, 'Precio\nmundial'),
             2.0: ('2,0', NARANJA, 'Autarquía B'),
             2.5: ('2,5', None, '')}

    def val_to_x(val):
        return 0.3 + (val - 0.5) / 2.0 * 2.4

    # Zona de comercio (banda verde)
    x_left = val_to_x(1.33)
    x_right = val_to_x(2.0)
    band = mpatches.FancyBboxPatch((x_left, line_y - 0.25), x_right - x_left, 0.5,
                                    boxstyle="round,pad=0.02",
                                    facecolor='#E8F5E9', edgecolor=VERDE,
                                    linewidth=2, alpha=0.7, zorder=2)
    ax.add_patch(band)
    ax.text((x_left + x_right) / 2, line_y, 'ZONA DE\nCOMERCIO',
            ha='center', va='center', fontsize=10, fontweight='bold', color=VERDE, zorder=3)

    # Marcas de autarquía A y B
    for val, label_below, label_above in [(1.33, '1,33', 'Autarquía A\n(costo V en A)'),
                                           (2.0, '2,0', 'Autarquía B\n(costo V en B)')]:
        xp = val_to_x(val)
        color = AZUL_MEDIO if val < 1.5 else NARANJA
        ax.plot([xp, xp], [line_y - 0.35, line_y + 0.35], color=color, linewidth=3, zorder=4)
        ax.text(xp, line_y - 0.55, label_below, ha='center', fontsize=11,
                fontweight='bold', color=color)
        ax.text(xp, line_y + 0.55, label_above, ha='center', fontsize=9,
                fontweight='bold', color=color)

    # Precio mundial ejemplo
    xp_pw = val_to_x(1.6)
    ax.plot(xp_pw, line_y, 'o', color=ROJO, markersize=15, zorder=5)
    ax.text(xp_pw, line_y - 0.55, '1,6', ha='center', fontsize=12,
            fontweight='bold', color=ROJO)
    ax.text(xp_pw, line_y + 0.55, 'Precio\nmundial', ha='center', fontsize=10,
            fontweight='bold', color=ROJO)

    # Extremos (fuera del rango)
    ax.text(val_to_x(0.7), line_y + 0.55, 'B no quiere\ncomerciar',
            ha='center', fontsize=8, color=GRIS, style='italic')
    ax.text(val_to_x(2.4), line_y + 0.55, 'A no quiere\ncomerciar',
            ha='center', fontsize=8, color=GRIS, style='italic')

    # Explicación abajo
    explain_y = -0.4
    ax.text(0.3, explain_y, '• A (comprador de V): en autarquía, 1V le cuesta 2T.\n'
                             '  Con comercio a 1,6: ahorra 0,4T por cada vino. ✓',
            fontsize=9.5, color=AZUL_OSCURO, va='top')
    ax.text(0.3, explain_y - 0.6, '• B (vendedor de V): en autarquía, 1V le cuesta 1,33T.\n'
                                    '  Con comercio a 1,6: gana 0,27T extra por cada vino. ✓',
            fontsize=9.5, color='#C0392B', va='top')

    # Pie
    ax.text(1.5, -1.4, 'Elaboración propia  •  El rango 1,33 < P < 2 es la condición para que ambos prefieran comerciar',
            ha='center', fontsize=8, color='#888888', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'terminos_intercambio.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ terminos_intercambio.png')


# ====================================================================
# 5. PPF PAÍS A
# ====================================================================
def generar_ppf_pais_a():
    fig, ax = plt.subplots(figsize=(10, 8))

    # PPF: T = 48 - 2V → puntos (V=0,T=48) y (V=24,T=0)
    v_ppf = np.array([0, 24])
    t_ppf = 48 - 2 * v_ppf

    # Línea de intercambio: T = 48 - 1.6V → puntos (V=0,T=48) y (V=30,T=0)
    v_trade = np.array([0, 30])
    t_trade = 48 - 1.6 * v_trade

    # Sombrear ganancia (entre PPF y trade line)
    v_fill = np.linspace(0, 24, 100)
    t_ppf_fill = 48 - 2 * v_fill
    t_trade_fill = 48 - 1.6 * v_fill
    ax.fill_between(v_fill, t_ppf_fill, t_trade_fill,
                    where=(t_trade_fill > t_ppf_fill),
                    alpha=0.15, color=VERDE, zorder=1)

    # PPF
    ax.plot(v_ppf, t_ppf, color=AZUL_MEDIO, linewidth=3, label='PPF País A', zorder=3)

    # Línea de intercambio
    ax.plot(v_trade, t_trade, color=VERDE, linewidth=2.5, linestyle='--',
            label='Línea de intercambio (P=1,6)', zorder=3)

    # Puntos clave
    # Especialización: (V=0, T=48)
    ax.plot(0, 48, 'o', color=AZUL_MEDIO, markersize=10, zorder=5)
    ax.text(1, 47, 'Especialización:\nproduce 48T', fontsize=9, color=AZUL_MEDIO, fontweight='bold')

    # Punto autarquía ejemplo (V=10, T=28)
    ax.plot(10, 28, 's', color=ROJO, markersize=10, zorder=5)
    ax.text(10.8, 27, 'Autarquía:\n(V=10, T=28)', fontsize=9, color=ROJO, fontweight='bold')

    # Punto comercio (V=10, T=32)
    ax.plot(10, 32, '*', color=VERDE, markersize=15, zorder=5)
    ax.text(10.8, 32, 'Comercio:\n(V=10, T=32)', fontsize=9, color=VERDE, fontweight='bold')

    # Flecha de ganancia
    ax.annotate('', xy=(10, 32), xytext=(10, 28),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
    ax.text(8.5, 30, '+4T', fontsize=12, fontweight='bold', color=VERDE,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=VERDE))

    # Extremos PPF
    ax.plot(24, 0, 'o', color=AZUL_MEDIO, markersize=8, zorder=5)
    ax.text(24, 1.5, 'Máx V: 24', fontsize=9, color=AZUL_MEDIO)

    # Etiquetas de ejes
    ax.set_xlabel('Vino (V)', fontsize=13, color='#444444', labelpad=10)
    ax.set_ylabel('Tela (T)', fontsize=13, color='#444444', labelpad=10)
    ax.set_title('País A: PPF y ganancias del comercio', fontsize=15,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    # Texto de ganancia
    ax.text(16, 22, 'Zona de\nganancia\ndel comercio', fontsize=11, color=VERDE,
            fontweight='bold', ha='center', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=VERDE, alpha=0.8))

    # Pendientes
    ax.text(5, 12, 'Pendiente PPF = -2\n(costo oport. interno)',
            fontsize=9, color=AZUL_MEDIO, style='italic')
    ax.text(20, 12, 'Pendiente comercio = -1,6\n(precio mundial)',
            fontsize=9, color=VERDE, style='italic')

    ax.set_xlim(-1, 32)
    ax.set_ylim(-2, 52)
    ax.legend(fontsize=10, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.grid(alpha=0.2, color='#CCCCCC')

    # Pie
    fig.text(0.5, 0.01, 'Elaboración propia  •  L=48h, Tela=1h/u, Vino=2h/u  •  Precio mundial: 1V = 1,6T',
             ha='center', fontsize=8, color='#888888', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'ppf_pais_a.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ ppf_pais_a.png')


# ====================================================================
# 6. PPF PAÍS B
# ====================================================================
def generar_ppf_pais_b():
    fig, ax = plt.subplots(figsize=(10, 8))

    # PPF: T = 8 - (4/3)V → puntos (V=0,T=8) y (V=6,T=0)
    v_ppf = np.array([0, 6])
    t_ppf = 8 - (4 / 3) * v_ppf

    # Línea de intercambio: T = 9.6 - 1.6V → puntos (V=6,T=0) y (V=0,T=9.6)
    v_trade = np.array([0, 6])
    t_trade = 9.6 - 1.6 * v_trade

    # Sombrear ganancia
    v_fill = np.linspace(0, 6, 100)
    t_ppf_fill = 8 - (4 / 3) * v_fill
    t_trade_fill = 9.6 - 1.6 * v_fill
    ax.fill_between(v_fill, t_ppf_fill, t_trade_fill,
                    where=(t_trade_fill > t_ppf_fill),
                    alpha=0.15, color=VERDE, zorder=1)

    # PPF
    ax.plot(v_ppf, t_ppf, color=NARANJA, linewidth=3, label='PPF País B', zorder=3)

    # Línea de intercambio
    v_trade_ext = np.array([0, 6])
    ax.plot(v_trade_ext, 9.6 - 1.6 * v_trade_ext, color=VERDE, linewidth=2.5, linestyle='--',
            label='Línea de intercambio (P=1,6)', zorder=3)

    # Puntos clave
    # Especialización: (V=6, T=0)
    ax.plot(6, 0, 'o', color=NARANJA, markersize=10, zorder=5)
    ax.text(6.2, -0.3, 'Especialización:\nproduce 6V', fontsize=9, color=NARANJA, fontweight='bold',
            ha='center')

    # Punto autarquía ejemplo (V=3, T=4)
    ax.plot(3, 4, 's', color=ROJO, markersize=10, zorder=5)
    ax.text(3.3, 3.6, 'Autarquía:\n(V=3, T=4)', fontsize=9, color=ROJO, fontweight='bold')

    # Punto comercio (V=3, T=4.8)
    ax.plot(3, 4.8, '*', color=VERDE, markersize=15, zorder=5)
    ax.text(3.3, 5.0, 'Comercio:\n(V=3, T=4,8)', fontsize=9, color=VERDE, fontweight='bold')

    # Flecha de ganancia
    ax.annotate('', xy=(3, 4.8), xytext=(3, 4),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
    ax.text(2.0, 4.3, '+0,8T', fontsize=12, fontweight='bold', color=VERDE,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=VERDE))

    # Extremos
    ax.plot(0, 8, 'o', color=NARANJA, markersize=8, zorder=5)
    ax.text(-0.3, 8.3, 'Máx T: 8', fontsize=9, color=NARANJA, ha='center')
    ax.plot(0, 9.6, 'o', color=VERDE, markersize=8, zorder=5)
    ax.text(0.2, 9.9, 'Con comercio: 9,6T', fontsize=9, color=VERDE, fontweight='bold')

    # Zona de ganancia label
    ax.text(2.0, 8.5, 'Zona de\nganancia\ndel comercio', fontsize=10, color=VERDE,
            fontweight='bold', ha='center', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=VERDE, alpha=0.8))

    ax.set_xlabel('Vino (V)', fontsize=13, color='#444444', labelpad=10)
    ax.set_ylabel('Tela (T)', fontsize=13, color='#444444', labelpad=10)
    ax.set_title('País B: el "peor en todo" también gana', fontsize=15,
                 fontweight='bold', color=NARANJA, pad=15)

    # Pendientes
    ax.text(4.5, 3.5, 'Pendiente PPF = -1,33\n(costo oport. interno)',
            fontsize=9, color=NARANJA, style='italic')
    ax.text(0.5, 5.5, 'Pendiente comercio = -1,6\n(precio mundial)',
            fontsize=9, color=VERDE, style='italic')

    ax.set_xlim(-0.8, 7.5)
    ax.set_ylim(-1.0, 11)
    ax.legend(fontsize=10, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.grid(alpha=0.2, color='#CCCCCC')

    fig.text(0.5, 0.01, 'Elaboración propia  •  L=48h, Tela=6h/u, Vino=8h/u  •  Precio mundial: 1V = 1,6T',
             ha='center', fontsize=8, color='#888888', style='italic')

    fig.savefig(os.path.join(OUTPUT_DIR, 'ppf_pais_b.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ ppf_pais_b.png')


# ====================================================================
# 7. RESUMEN RICARDO — DIAGRAMA DE FLUJO
# ====================================================================
def generar_resumen_ricardo():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')

    ax.text(7, 5.7, 'Ricardo: el mecanismo completo',
            ha='center', fontsize=16, fontweight='bold', color=AZUL_OSCURO)

    # Pasos como cajas con flechas
    steps = [
        ('Tecnología\ndistinta', '#F0F4FA', AZUL_MEDIO),
        ('Costos de\noportunidad\ndistintos', '#F0F4FA', AZUL_MEDIO),
        ('Precios relativos\nen autarquía\ndistintos', '#FFF5E6', NARANJA),
        ('Especialización\n(ventaja\ncomparativa)', '#FFF5E6', NARANJA),
        ('Comercio a\nprecio mundial\nintermedio', '#FFF5F5', ROJO),
        ('Ganancias\ndel comercio', '#E8F5E9', VERDE),
    ]

    n = len(steps)
    box_w = 1.8
    box_h = 1.2
    gap = 0.35
    total_w = n * box_w + (n - 1) * gap
    x_start = (14 - total_w) / 2

    for i, (label, bg, border) in enumerate(steps):
        x = x_start + i * (box_w + gap)
        y = 2.8

        box = mpatches.FancyBboxPatch((x, y - box_h / 2), box_w, box_h,
                                       boxstyle="round,pad=0.1",
                                       facecolor=bg, edgecolor=border,
                                       linewidth=2, zorder=3)
        ax.add_patch(box)
        ax.text(x + box_w / 2, y, label, ha='center', va='center',
                fontsize=9, fontweight='bold', color=border, zorder=4)

        # Flecha
        if i < n - 1:
            ax.annotate('', xy=(x + box_w + gap * 0.2, y),
                        xytext=(x + box_w + gap * 0.05, y),
                        arrowprops=dict(arrowstyle='->', color='#999999', lw=2))

    # Números de ejemplo debajo
    examples = [
        'A: T=1h, V=2h\nB: T=6h, V=8h',
        'A: T→0,5V\nB: T→0,75V',
        'A: P_V=2T\nB: P_V=1,33T',
        'A → Tela\nB → Vino',
        '1,33 < P < 2\n(ej: P = 1,6)',
        'Consumo fuera\nde la PPF',
    ]
    for i, ex in enumerate(examples):
        x = x_start + i * (box_w + gap) + box_w / 2
        ax.text(x, 1.5, ex, ha='center', va='center', fontsize=8,
                color=GRIS, style='italic')

    # Conclusión
    concl = mpatches.FancyBboxPatch((1.5, 0.2), 11, 0.7,
                                     boxstyle="round,pad=0.1",
                                     facecolor='#E8F5E9', edgecolor=VERDE,
                                     linewidth=2)
    ax.add_patch(concl)
    ax.text(7, 0.55, 'El comercio nace de diferencias RELATIVAS, no absolutas. '
                      'Ambos países ganan, incluso si uno es "mejor en todo".',
            ha='center', va='center', fontsize=10, fontweight='bold', color=VERDE)

    fig.savefig(os.path.join(OUTPUT_DIR, 'resumen_ricardo.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ resumen_ricardo.png')


# ====================================================================
# 8. RCA ARGENTINA
# ====================================================================
def generar_rca_argentina():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7),
                                    gridspec_kw={'width_ratios': [1, 1]})

    fig.suptitle('Argentina: ventaja comparativa revelada (RCA)',
                 fontsize=15, fontweight='bold', color=AZUL_OSCURO, y=0.97)

    # Panel izquierdo: Composición exportadora Argentina (2019 aprox)
    labels = ['Productos\nprimarios', 'MOA', 'MOI', 'Combustibles\ny energía']
    shares = [22, 35, 28, 15]  # % aprox 2019
    colors_pie = [VERDE, '#27AE60', AZUL_MEDIO, NARANJA]
    explode = [0.05, 0.05, 0, 0]

    wedges, texts, autotexts = ax1.pie(shares, labels=labels, autopct='%1.0f%%',
                                        colors=colors_pie, explode=explode,
                                        startangle=90, textprops={'fontsize': 10},
                                        pctdistance=0.75)
    for at in autotexts:
        at.set_fontweight('bold')
        at.set_color('white')
    ax1.set_title('Composición exportadora\n(circa 2019)', fontsize=12,
                  fontweight='bold', color='#444444')

    # Panel derecho: RCA por sector (barras)
    sectors = ['Soja y\nderivados', 'Cereales', 'Carne\nbovina', 'Aceites\nvegetales',
               'Vehículos', 'Maquinaria', 'Electrónica', 'Química']
    rca_vals = [8.5, 5.2, 3.8, 6.1, 0.6, 0.3, 0.1, 0.5]
    bar_colors = [VERDE if v > 1 else ROJO for v in rca_vals]

    bars = ax2.barh(range(len(sectors)), rca_vals, color=bar_colors,
                    edgecolor='white', linewidth=1, height=0.6, zorder=3)

    # Línea RCA = 1
    ax2.axvline(x=1, color=ROJO, linewidth=2, linestyle='--', zorder=2, alpha=0.7)
    ax2.text(1.1, 7.6, 'RCA = 1', fontsize=9, color=ROJO, fontweight='bold')

    ax2.set_yticks(range(len(sectors)))
    ax2.set_yticklabels(sectors, fontsize=10)
    ax2.set_xlabel('Índice RCA (Balassa)', fontsize=11, color='#444444')
    ax2.set_title('RCA por sector\n(circa 2019)', fontsize=12,
                  fontweight='bold', color='#444444')

    # Valores en barras
    for i, (bar, val) in enumerate(zip(bars, rca_vals)):
        x_pos = bar.get_width() + 0.15
        color = VERDE if val > 1 else ROJO
        ax2.text(x_pos, bar.get_y() + bar.get_height() / 2,
                 f'{val:.1f}', va='center', fontsize=10,
                 fontweight='bold', color=color)

    # Anotaciones
    ax2.text(6.5, 1.5, 'RCA > 1:\nespecialización\n(ventaja revelada)',
             fontsize=9, color=VERDE, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9',
                       edgecolor=VERDE, alpha=0.8))
    ax2.text(6.5, 5.5, 'RCA < 1:\nsin especialización',
             fontsize=9, color=ROJO, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF5F5',
                       edgecolor=ROJO, alpha=0.8))

    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_color('#CCCCCC')
    ax2.spines['bottom'].set_color('#CCCCCC')
    ax2.grid(axis='x', alpha=0.2, color='#CCCCCC')
    ax2.set_xlim(0, 10)
    ax2.invert_yaxis()

    fig.text(0.5, 0.01,
             'Elaboración propia a partir de datos WITS/Banco Mundial  •  '
             'RCA = (Xij/Xi) / (Xwj/Xw)  •  Valores aproximados 2019',
             ha='center', fontsize=8, color='#888888', style='italic')

    plt.tight_layout(rect=[0, 0.03, 1, 0.94])
    fig.savefig(os.path.join(OUTPUT_DIR, 'rca_argentina.png'), dpi=150,
                bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print('✓ rca_argentina.png')


# ====================================================================
# MAIN
# ====================================================================
if __name__ == '__main__':
    print('Generando gráficos Clase 4...\n')
    generar_corn_laws()
    generar_costo_oportunidad()
    generar_ventaja_comparativa_resultado()
    generar_terminos_intercambio()
    generar_ppf_pais_a()
    generar_ppf_pais_b()
    generar_resumen_ricardo()
    generar_rca_argentina()
    print('\n¡Listo! 8 gráficos generados.')
