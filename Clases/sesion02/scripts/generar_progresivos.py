"""
Genera PNGs progresivos para Clase 2 (Sesión 2).
6 gráficos → 17 PNGs total:
  1. ciclo_mercantilista (3 pasos)
  2. trp_mercantilismo_smith (2 pasos)
  3. division_trabajo_diagrama (3 pasos)
  4. comercio_britanico_1800 (3 pasos)
  5. limite_smith (2 pasos)
  6. rca_argentina (3 pasos)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
import os, sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Paleta ──
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#7F8C8D'
AMARILLO    = '#F1C40F'
MORADO      = '#8E44AD'
AMARILLO_W  = '#F59E0B'


def save(fig, name, paso):
    fname = f'{name}_paso{paso}.png'
    fig.savefig(os.path.join(OUTPUT_DIR, fname), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f'  ✓ {fname}')


# ═══════════════════════════════════════════════════════════════
# 1. CICLO MERCANTILISTA — 3 pasos
# P1: Superávit + Acumulación de oro (con flecha)
# P2: + Poder militar + Control colonias (4 nodos, flechas parciales)
# P3: + Todas las flechas + "JUEGO DE SUMA CERO"
# ═══════════════════════════════════════════════════════════════
def prog_ciclo_mercantilista():
    print('ciclo_mercantilista:')

    nodes = [
        {'label': 'Superávit\ncomercial', 'desc': 'Exportar > Importar', 'color': VERDE, 'angle': 90},
        {'label': 'Acumulación\nde oro', 'desc': 'Metales preciosos', 'color': AMARILLO, 'angle': 0},
        {'label': 'Poder\nmilitar', 'desc': 'Ejército y armada', 'color': ROJO, 'angle': 270},
        {'label': 'Control de\ncolonias', 'desc': 'Mercados cautivos', 'color': MORADO, 'angle': 180},
    ]

    radius = 1.6

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.axis('off')
        ax.set_aspect('equal')

        ax.text(0, 2.7, 'El ciclo mercantilista', ha='center', va='center',
                fontsize=16, fontweight='bold', color=AZUL_OSCURO)

        # Determine visible nodes
        if paso == 1:
            visible = [0, 1]  # Superávit + Oro
        else:
            visible = [0, 1, 2, 3]  # All

        node_positions = []
        for i, node in enumerate(nodes):
            angle_rad = np.radians(node['angle'])
            x = radius * np.cos(angle_rad)
            y = radius * np.sin(angle_rad)
            node_positions.append((x, y))

            if i not in visible:
                continue

            alpha = 0.85
            circle = plt.Circle((x, y), 0.65, facecolor=node['color'], edgecolor='white',
                                linewidth=2, alpha=alpha, zorder=3)
            ax.add_patch(circle)
            ax.text(x, y + 0.08, node['label'], ha='center', va='center',
                    fontsize=10, fontweight='bold', color='white', zorder=4)

            # Description
            if node['angle'] == 90:
                ax.text(x, y + 0.95, node['desc'], ha='center', va='center',
                        fontsize=11, color='#666666', style='italic', zorder=4)
            elif node['angle'] == 270:
                ax.text(x, y - 0.95, node['desc'], ha='center', va='center',
                        fontsize=11, color='#666666', style='italic', zorder=4)
            elif node['angle'] == 0:
                ax.text(x + 1.05, y, node['desc'], ha='left', va='center',
                        fontsize=11, color='#666666', style='italic', zorder=4)
            else:
                ax.text(x - 1.05, y, node['desc'], ha='right', va='center',
                        fontsize=11, color='#666666', style='italic', zorder=4)

        # Arrows
        if paso == 1:
            # Only arrow 0→1
            x1, y1 = node_positions[0]
            x2, y2 = node_positions[1]
            ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=2.5,
                                       connectionstyle='arc3,rad=-0.3'), zorder=2)
        elif paso == 2:
            # Arrows 0→1, 1→2, 2→3
            for i in range(3):
                x1, y1 = node_positions[i]
                x2, y2 = node_positions[(i + 1) % 4]
                ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                            arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=2.5,
                                           connectionstyle='arc3,rad=-0.3'), zorder=2)
        else:  # paso 3
            for i in range(4):
                x1, y1 = node_positions[i]
                x2, y2 = node_positions[(i + 1) % 4]
                ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                            arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=2.5,
                                           connectionstyle='arc3,rad=-0.3'), zorder=2)
            # Center text
            ax.text(0, 0, 'JUEGO DE\nSUMA CERO', ha='center', va='center',
                    fontsize=12, fontweight='bold', color=AZUL_OSCURO, alpha=0.6,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F4F8',
                              edgecolor=AZUL_OSCURO, alpha=0.3))

        fig.text(0.5, 0.02, 'Elaboración propia', ha='center', fontsize=11,
                 color='#888888', style='italic')
        save(fig, 'ciclo_mercantilista', paso)


# ═══════════════════════════════════════════════════════════════
# 2. TRP MERCANTILISMO vs SMITH — 2 pasos
# P1: Solo panel Mercantilismo
# P2: + panel Smith
# ═══════════════════════════════════════════════════════════════
def prog_trp():
    print('trp_mercantilismo_smith:')

    categories = ['Tecnología', 'Reglas', 'Poder']
    merc_values = [2, 8, 10]
    smith_values = [10, 3, 2]
    colors_bars = [AZUL_CLARO, NARANJA, ROJO]

    for paso in range(1, 3):
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))

        # Mercantilismo (always visible)
        ax = axes[0]
        bars = ax.barh(categories, merc_values, color=colors_bars, edgecolor='white', height=0.6)
        ax.set_xlim(0, 12)
        ax.set_title('Mercantilismo', fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=15)
        ax.invert_yaxis()
        for bar, val in zip(bars, merc_values):
            ax.text(val + 0.3, bar.get_y() + bar.get_height()/2, str(val),
                    va='center', fontsize=12, fontweight='bold', color='#555555')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.set_xticks([])
        ax.tick_params(axis='y', labelsize=12, colors='#333333')
        ax.spines['left'].set_color('#CCCCCC')
        ax.text(6, 3.2, 'Poder domina →\nComercio como\ninstrumento estatal',
                ha='center', va='center', fontsize=9, color=GRIS, style='italic')

        # Smith (paso 2 only)
        ax = axes[1]
        if paso >= 2:
            bars = ax.barh(categories, smith_values, color=colors_bars, edgecolor='white', height=0.6)
            ax.set_xlim(0, 12)
            ax.set_title('Adam Smith', fontsize=14, fontweight='bold', color=VERDE, pad=15)
            ax.invert_yaxis()
            for bar, val in zip(bars, smith_values):
                ax.text(val + 0.3, bar.get_y() + bar.get_height()/2, str(val),
                        va='center', fontsize=12, fontweight='bold', color='#555555')
            ax.text(6, 3.2, 'Tecnología domina →\nProductividad y\ndivisión del trabajo',
                    ha='center', va='center', fontsize=9, color=GRIS, style='italic')
        else:
            ax.set_xlim(0, 12)
            ax.set_ylim(-0.5, 3.5)
            ax.text(6, 1.5, '?', ha='center', va='center', fontsize=110,
                    fontweight='bold', color='#DDDDDD')
            ax.set_title('¿Otra visión?', fontsize=14, fontweight='bold', color='#CCCCCC', pad=15)
            ax.invert_yaxis()

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.set_xticks([])
        ax.tick_params(axis='y', labelsize=12, colors='#333333')
        ax.spines['left'].set_color('#CCCCCC')

        fig.suptitle('Tecnología — Reglas — Poder: dos visiones del comercio',
                     fontsize=13, fontweight='bold', color=AZUL_OSCURO, y=0.98)
        fig.text(0.5, 0.01, 'Elaboración propia a partir del marco T-R-P (Clase 1)',
                 ha='center', fontsize=11, color='#888888', style='italic')
        fig.tight_layout(rect=[0, 0.04, 1, 0.93])
        save(fig, 'trp_mercantilismo_smith', paso)


# ═══════════════════════════════════════════════════════════════
# 3. DIVISIÓN DEL TRABAJO — 3 pasos
# P1: Solo primeras 2 cajas (comercio → especialización)
# P2: + productividad + riqueza + retroalimentación
# P3: + 3 razones debajo
# ═══════════════════════════════════════════════════════════════
def prog_division_trabajo():
    print('division_trabajo_diagrama:')

    all_boxes = [
        {'x': 1.2, 'y': 3.2, 'text': 'Comercio\namplía el\nmercado', 'color': AZUL_OSCURO},
        {'x': 3.6, 'y': 3.2, 'text': 'Más\nespecialización', 'color': AZUL_MEDIO},
        {'x': 6.0, 'y': 3.2, 'text': 'Mayor\nproductividad', 'color': AZUL_CLARO},
        {'x': 8.4, 'y': 3.2, 'text': 'Más riqueza\n(bienes y\nservicios)', 'color': VERDE},
    ]
    bw, bh = 1.8, 1.6

    reasons = [
        {'x': 2.5, 'text': '① Destreza:\nrepetir mejora', 'color': AZUL_MEDIO},
        {'x': 5.0, 'text': '② Ahorro de tiempo:\nsin cambiar tareas', 'color': AZUL_MEDIO},
        {'x': 7.5, 'text': '③ Innovación:\nespecialización genera\nmejoras técnicas', 'color': AZUL_MEDIO},
    ]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(10, 5.5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(5, 5.5, 'El mecanismo de Smith: división del trabajo y comercio',
                ha='center', va='center', fontsize=14, fontweight='bold', color=AZUL_OSCURO)

        # Determine visible boxes
        if paso == 1:
            n_visible = 2
        else:
            n_visible = 4

        for i in range(n_visible):
            box = all_boxes[i]
            rect = mpatches.FancyBboxPatch((box['x'] - bw/2, box['y'] - bh/2), bw, bh,
                                            boxstyle="round,pad=0.15",
                                            facecolor=box['color'], edgecolor='white',
                                            linewidth=2, alpha=0.9)
            ax.add_patch(rect)
            ax.text(box['x'], box['y'], box['text'], ha='center', va='center',
                    fontsize=11, fontweight='bold', color='white')

        # Arrows between visible boxes
        for i in range(min(n_visible - 1, 3)):
            ax.annotate('', xy=(all_boxes[i+1]['x'] - bw/2 - 0.05, all_boxes[i+1]['y']),
                        xytext=(all_boxes[i]['x'] + bw/2 + 0.05, all_boxes[i]['y']),
                        arrowprops=dict(arrowstyle='->', color='#555555', lw=2.5))

        # Retroalimentación arrow (paso >= 2)
        if paso >= 2:
            ax.annotate('', xy=(all_boxes[0]['x'], all_boxes[0]['y'] + bh/2 + 0.15),
                        xytext=(all_boxes[3]['x'], all_boxes[3]['y'] + bh/2 + 0.15),
                        arrowprops=dict(arrowstyle='->', color=NARANJA, lw=2,
                                       connectionstyle='arc3,rad=0.3', linestyle='--'))
            ax.text(4.8, 4.7, 'Retroalimentación: más riqueza → más comercio',
                    ha='center', va='center', fontsize=9, color=NARANJA, fontweight='bold')

        # Reasons (paso 3)
        if paso >= 3:
            ax.text(5, 1.35, '¿Por qué la especialización sube la productividad? (Smith)',
                    ha='center', va='center', fontsize=10, fontweight='bold', color='#444444')
            for r in reasons:
                rect = mpatches.FancyBboxPatch((r['x'] - 1.0, 0.1), 2.0, 0.9,
                                                boxstyle="round,pad=0.1",
                                                facecolor='#F0F4F8', edgecolor=r['color'],
                                                linewidth=1.5, alpha=0.8)
                ax.add_patch(rect)
                ax.text(r['x'], 0.55, r['text'], ha='center', va='center',
                        fontsize=9, color='#444444')

        fig.text(0.5, 0.01, 'Elaboración propia basada en A. Smith, La Riqueza de las Naciones (1776)',
                 ha='center', fontsize=11, color='#888888', style='italic')
        save(fig, 'division_trabajo_diagrama', paso)


# ═══════════════════════════════════════════════════════════════
# 4. COMERCIO BRITÁNICO 1800-1870 — 3 pasos
# P1: Solo importaciones
# P2: + exportaciones + total
# P3: + anotaciones (Napoleón, Corn Laws, multiplicador)
# ═══════════════════════════════════════════════════════════════
def prog_comercio_britanico():
    print('comercio_britanico_1800:')

    years = list(range(1800, 1871))
    uk_imp = [216.5, 244.5, 187.5, 203.4, 210.7, 221.7, 195.5, 201.4, 208.2, 271.7,
              326.7, 167.9, 169.6, 192.9, 237.4, 267.3, 196.4, 234.2, 307.8, 206.7,
              198.1, 174.0, 183.2, 215.0, 212.7, 315.8, 212.1, 256.7, 250.4, 230.9,
              239.5, 268.8, 219.6, 248.9, 263.0, 284.7, 361.8, 311.5, 346.4, 401.8,
              406.0, 369.2, 326.2, 302.6, 344.5, 385.3, 376.1, 480.8, 388.5, 429.9,
              443.2, 476.5, 475.5, 643.2, 653.3, 598.6, 731.9, 800.3, 686.9, 752.4,
              882.1, 887.4, 889.8, 963.1, 1080.4, 1057.6, 1189.5, 1118.7, 1195.8, 1204.6,
              1255.0]
    uk_exp = [171.5, 177.9, 205.9, 167.5, 173.9, 165.6, 181.3, 164.6, 172.5, 216.8,
              208.1, 125.6, 150.8, 163.5, 192.9, 253.1, 217.8, 192.4, 209.2, 158.8,
              164.6, 176.9, 184.2, 169.9, 186.9, 187.9, 155.0, 183.6, 181.4, 174.1,
              182.4, 180.8, 177.3, 190.1, 192.9, 229.9, 257.7, 214.6, 244.8, 260.2,
              257.0, 257.4, 227.4, 250.4, 284.8, 292.8, 278.4, 281.9, 257.5, 306.2,
              347.7, 365.5, 382.8, 483.4, 474.6, 472.0, 574.3, 602.8, 566.9, 642.0,
              661.4, 608.1, 604.7, 713.8, 782.2, 809.3, 921.9, 883.1, 878.2, 925.7,
              976.2]
    total = [i + e for i, e in zip(uk_imp, uk_exp)]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(10, 6))

        # Always show imports
        ax.fill_between(years, uk_imp, alpha=0.15, color=AZUL_MEDIO)
        ax.plot(years, uk_imp, color=AZUL_OSCURO, linewidth=2, label='Importaciones', zorder=3)

        if paso >= 2:
            ax.fill_between(years, uk_exp, alpha=0.15, color=VERDE)
            ax.plot(years, uk_exp, color=VERDE, linewidth=2, label='Exportaciones', zorder=3)
            ax.plot(years, total, color=NARANJA, linewidth=2.5, linestyle='--',
                    label='Comercio total', zorder=4)

        if paso >= 3:
            ax.axvline(x=1815, color=GRIS, linestyle=':', alpha=0.5)
            ax.text(1815, 1800, 'Fin guerras\nnapoleónicas\n(1815)', ha='center', fontsize=11, color=GRIS)
            ax.axvline(x=1846, color=GRIS, linestyle=':', alpha=0.5)
            ax.text(1846, 1900, 'Derogación\nCorn Laws\n(1846)', ha='center', fontsize=11, color=GRIS)
            ax.annotate(f'Comercio total\nse multiplica ×{total[-1]/total[0]:.1f}',
                        xy=(1865, total[-1]), xytext=(1835, 2100),
                        fontsize=10, fontweight='bold', color=NARANJA,
                        arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5),
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8F0',
                                  edgecolor=NARANJA, alpha=0.8))

        ax.set_title('Comercio exterior de Gran Bretaña (1800–1870)', fontsize=14,
                     fontweight='bold', color=AZUL_OSCURO, pad=15)
        ax.set_xlabel('Año', fontsize=11, color='#555555')
        ax.set_ylabel('Millones de USD corrientes', fontsize=11, color='#555555')
        ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
        ax.set_ylim(0, 2400)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#CCCCCC')
        ax.spines['bottom'].set_color('#CCCCCC')
        ax.tick_params(colors='#555555', labelsize=10)
        ax.grid(axis='y', alpha=0.3, color='#CCCCCC')
        fig.text(0.5, 0.01, 'Fuente: Federico-Tena World Trade Historical Database (FTWTHD)',
                 ha='center', fontsize=11, color='#888888', style='italic')
        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        save(fig, 'comercio_britanico_1800', paso)


# ═══════════════════════════════════════════════════════════════
# 5. LÍMITE DE SMITH — 2 pasos
# P1: Tabla + autarquía (panel izq) → A es mejor en todo
# P2: + panel derecho con "?" y teaser Ricardo
# ═══════════════════════════════════════════════════════════════
def prog_limite_smith():
    print('limite_smith:')

    for paso in range(1, 3):
        fig = plt.figure(figsize=(12, 7.5))

        fig.text(0.50, 0.97, '¿Y si un país es mejor en todo?',
                 ha='center', va='center', fontsize=15, fontweight='bold', color=ROJO)

        # Mini tabla de costos (always visible)
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
                      bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7', edgecolor=AMARILLO_W))
        ax_table.text(8.5, 0.8, 'Dotación:\n12 horas\ncada país', ha='center', va='center',
                      fontsize=11, color=GRIS, style='italic',
                      bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#DDDDDD'))

        # Panel izquierdo: Autarquía (always visible)
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
                    fontsize=11, color=GRIS, style='italic')
        ax_aut.annotate('A produce\n6× más tela\ny 4× más vino',
                        xy=(0.15, 4.5), fontsize=9, color=ROJO, fontweight='bold', ha='center',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7',
                                  edgecolor=AMARILLO_W, alpha=0.9))
        ax_aut.spines['top'].set_visible(False)
        ax_aut.spines['right'].set_visible(False)
        ax_aut.spines['left'].set_color('#CCCCCC')
        ax_aut.spines['bottom'].set_color('#CCCCCC')
        ax_aut.tick_params(colors='#555555')
        ax_aut.grid(axis='y', alpha=0.3, color='#CCCCCC')

        # Panel derecho
        ax_com = fig.add_axes([0.55, 0.08, 0.40, 0.62])
        ax_com.set_xlim(0, 10)
        ax_com.set_ylim(0, 10)
        ax_com.axis('off')

        if paso == 1:
            # Empty placeholder
            border = mpatches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6,
                                              boxstyle="round,pad=0.2",
                                              facecolor='#FAFAFA', edgecolor='#EEEEEE',
                                              linewidth=2, linestyle='--')
            ax_com.add_patch(border)
            ax_com.text(5, 5, '?', ha='center', va='center', fontsize=120,
                        fontweight='bold', color='#EEEEEE', alpha=0.5)
        else:
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
            resolucion = mpatches.FancyBboxPatch((1.0, 1.0), 8.0, 2.0,
                                                  boxstyle="round,pad=0.2",
                                                  facecolor='#E8F5E9', edgecolor=VERDE, linewidth=2)
            ax_com.add_patch(resolucion)
            ax_com.text(5, 2.3, 'La respuesta la da RICARDO:',
                        ha='center', va='center', fontsize=10, fontweight='bold', color=VERDE)
            ax_com.text(5, 1.6, 'No importa quién es más barato en absoluto\nsino qué SACRIFICA cada uno → costo de oportunidad',
                        ha='center', va='center', fontsize=9, color='#2E7D32')

        # Arrow between panels
        if paso >= 2:
            fig.text(0.50, 0.39, '→', ha='center', va='center', fontsize=40, color=ROJO,
                     fontweight='bold')
            fig.text(0.50, 0.33, '¿Especialización?\n¿Intercambio?', ha='center', va='center',
                     fontsize=9, color=ROJO, fontweight='bold')

        fig.text(0.50, 0.01,
                 'Elaboración propia  •  El límite de la ventaja absoluta',
                 ha='center', fontsize=11, color='#888888', style='italic')
        save(fig, 'limite_smith', paso)


# ═══════════════════════════════════════════════════════════════
# 6. RCA ARGENTINA — 3 pasos
# P1: Solo composición exportadora (pie chart)
# P2: + barras RCA sectores con RCA > 1 (primarios)
# P3: + barras RCA sectores con RCA < 1 (industriales) + anotaciones
# ═══════════════════════════════════════════════════════════════
def prog_rca_argentina():
    print('rca_argentina:')

    labels_pie = ['Productos\nprimarios', 'MOA', 'MOI', 'Combustibles\ny energía']
    shares = [22, 35, 28, 15]
    colors_pie = [VERDE, '#27AE60', AZUL_MEDIO, NARANJA]
    explode = [0.05, 0.05, 0, 0]

    sectors = ['Soja y\nderivados', 'Cereales', 'Carne\nbovina', 'Aceites\nvegetales',
               'Vehículos', 'Maquinaria', 'Electrónica', 'Química']
    rca_vals = [8.5, 5.2, 3.8, 6.1, 0.6, 0.3, 0.1, 0.5]
    bar_colors = [VERDE if v > 1 else ROJO for v in rca_vals]

    for paso in range(1, 4):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7),
                                        gridspec_kw={'width_ratios': [1, 1]})
        fig.suptitle('Argentina: ventaja comparativa revelada (RCA)',
                     fontsize=15, fontweight='bold', color=AZUL_OSCURO, y=0.97)

        # Pie chart always visible
        wedges, texts, autotexts = ax1.pie(shares, labels=labels_pie, autopct='%1.0f%%',
                                            colors=colors_pie, explode=explode,
                                            startangle=90, textprops={'fontsize': 10},
                                            pctdistance=0.75)
        for at in autotexts:
            at.set_fontweight('bold')
            at.set_color('white')
        ax1.set_title('Composición exportadora\n(circa 2019)', fontsize=12,
                      fontweight='bold', color='#444444')

        # RCA bars
        if paso == 1:
            ax2.set_xlim(0, 10)
            ax2.set_ylim(-0.5, 7.5)
            ax2.text(5, 3.5, '¿Qué revela\nel patrón\nexportador?', ha='center', va='center',
                     fontsize=16, fontweight='bold', color='#DDDDDD')
            ax2.set_title('RCA por sector\n(circa 2019)', fontsize=12,
                          fontweight='bold', color='#CCCCCC')
            ax2.axis('off')
        elif paso == 2:
            # Only primarios (first 4)
            n_show = 4
            bars = ax2.barh(range(n_show), rca_vals[:n_show], color=bar_colors[:n_show],
                            edgecolor='white', linewidth=1, height=0.6, zorder=3)
            ax2.axvline(x=1, color=ROJO, linewidth=2, linestyle='--', zorder=2, alpha=0.7)
            ax2.text(1.1, -0.4, 'RCA = 1', fontsize=9, color=ROJO, fontweight='bold')
            ax2.set_yticks(range(n_show))
            ax2.set_yticklabels(sectors[:n_show], fontsize=10)
            ax2.set_xlabel('Índice RCA (Balassa)', fontsize=11, color='#444444')
            ax2.set_title('RCA por sector\n(circa 2019)', fontsize=12,
                          fontweight='bold', color='#444444')
            for i, (bar, val) in enumerate(zip(bars, rca_vals[:n_show])):
                ax2.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2,
                         f'{val:.1f}', va='center', fontsize=10, fontweight='bold', color=VERDE)
            ax2.set_xlim(0, 10)
            ax2.invert_yaxis()
            ax2.spines['top'].set_visible(False)
            ax2.spines['right'].set_visible(False)
            ax2.spines['left'].set_color('#CCCCCC')
            ax2.spines['bottom'].set_color('#CCCCCC')
            ax2.grid(axis='x', alpha=0.2, color='#CCCCCC')
        else:  # paso 3
            n_show = len(sectors)
            bars = ax2.barh(range(n_show), rca_vals, color=bar_colors,
                            edgecolor='white', linewidth=1, height=0.6, zorder=3)
            ax2.axvline(x=1, color=ROJO, linewidth=2, linestyle='--', zorder=2, alpha=0.7)
            ax2.text(1.1, 7.6, 'RCA = 1', fontsize=9, color=ROJO, fontweight='bold')
            ax2.set_yticks(range(n_show))
            ax2.set_yticklabels(sectors, fontsize=10)
            ax2.set_xlabel('Índice RCA (Balassa)', fontsize=11, color='#444444')
            ax2.set_title('RCA por sector\n(circa 2019)', fontsize=12,
                          fontweight='bold', color='#444444')
            for bar, val in zip(bars, rca_vals):
                color = VERDE if val > 1 else ROJO
                ax2.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2,
                         f'{val:.1f}', va='center', fontsize=10, fontweight='bold', color=color)
            ax2.text(6.5, 1.5, 'RCA > 1:\nespecialización\n(ventaja revelada)',
                     fontsize=9, color=VERDE, fontweight='bold',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9',
                               edgecolor=VERDE, alpha=0.8))
            ax2.text(6.5, 5.5, 'RCA < 1:\nsin especialización',
                     fontsize=9, color=ROJO, fontweight='bold',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF5F5',
                               edgecolor=ROJO, alpha=0.8))
            ax2.set_xlim(0, 10)
            ax2.invert_yaxis()
            ax2.spines['top'].set_visible(False)
            ax2.spines['right'].set_visible(False)
            ax2.spines['left'].set_color('#CCCCCC')
            ax2.spines['bottom'].set_color('#CCCCCC')
            ax2.grid(axis='x', alpha=0.2, color='#CCCCCC')

        fig.text(0.5, 0.01,
                 'Elaboración propia a partir de datos WITS/Banco Mundial  •  '
                 'RCA = (Xij/Xi) / (Xwj/Xw)  •  Valores aproximados 2019',
                 ha='center', fontsize=11, color='#888888', style='italic')
        plt.tight_layout(rect=[0, 0.03, 1, 0.94])
        save(fig, 'rca_argentina', paso)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print('Generando PNGs progresivos para Clase 2...\n')
    prog_ciclo_mercantilista()
    prog_trp()
    prog_division_trabajo()
    prog_comercio_britanico()
    prog_limite_smith()
    prog_rca_argentina()
    print('\n¡Listo! 17 PNGs progresivos generados.')
