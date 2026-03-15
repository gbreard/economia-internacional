"""
Genera 7 gráficos para la Clase 3: Mercantilistas y Adam Smith
1. Mapa de la Unidad 2 (4 clases)
2. Ciclo mercantilista (superávit→oro→poder→colonias)
3. T-R-P comparativo (mercantilismo vs Smith)
4. División del trabajo (diagrama de flujo)
5. Comercio británico 1800-1870 (datos FTWTHD)
6. Ventaja absoluta (tabla 2x2 + flechas)
7. Límite de Smith (tabla 2x2 + "?")
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
import os, sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Estilo compartido ──────────────────────────────────────────
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#7F8C8D'
AMARILLO    = '#F1C40F'
MORADO      = '#8E44AD'

def estilo_base(fig, ax, fuente_texto):
    """Aplica estilo base consistente"""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.tick_params(colors='#555555', labelsize=10)
    ax.grid(axis='y', alpha=0.3, color='#CCCCCC')
    fig.text(0.5, 0.01, fuente_texto, ha='center', fontsize=8, color='#888888', style='italic')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 1: Mapa de la Unidad 2
# ═══════════════════════════════════════════════════════════════
def grafico_unidad2_mapa():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Título
    ax.text(5, 5.5, 'Unidad 2: ¿Por qué comercian los países?',
            ha='center', va='center', fontsize=16, fontweight='bold', color=AZUL_OSCURO)
    ax.text(5, 5.05, 'Cuatro clases, cuatro respuestas',
            ha='center', va='center', fontsize=11, color=GRIS)

    # Clases como cajas
    clases = [
        {'num': 3, 'titulo': 'Mercantilistas\ny Smith', 'desc': 'Comercio, mercado\ny productividad',
         'color': AZUL_OSCURO, 'highlight': True},
        {'num': 4, 'titulo': 'Ricardo', 'desc': 'Ventaja comparativa\ny costos de oportunidad',
         'color': AZUL_MEDIO, 'highlight': False},
        {'num': 5, 'titulo': 'Modelo\nneoclásico', 'desc': 'Dotaciones de recursos\ny precios relativos',
         'color': AZUL_CLARO, 'highlight': False},
        {'num': 6, 'titulo': 'Heckscher-\nOhlin', 'desc': 'Factores, distribución\ny paradoja de Leontief',
         'color': NARANJA, 'highlight': False},
    ]

    x_positions = [1.3, 3.6, 5.9, 8.2]
    box_w = 2.0
    box_h = 3.2

    for i, (x, c) in enumerate(zip(x_positions, clases)):
        y = 1.6
        alpha = 1.0 if c['highlight'] else 0.7
        lw = 3 if c['highlight'] else 1.5

        # Caja principal
        rect = mpatches.FancyBboxPatch((x - box_w/2, y - box_h/2), box_w, box_h,
                                        boxstyle="round,pad=0.15",
                                        facecolor='white', edgecolor=c['color'],
                                        linewidth=lw, alpha=alpha)
        ax.add_patch(rect)

        # Barra superior con color
        header_h = 0.7
        header_rect = mpatches.FancyBboxPatch((x - box_w/2, y + box_h/2 - header_h), box_w, header_h,
                                               boxstyle="round,pad=0.1",
                                               facecolor=c['color'], edgecolor=c['color'],
                                               linewidth=0)
        ax.add_patch(header_rect)

        # Número de clase
        ax.text(x, y + box_h/2 - header_h/2, f'Clase {c["num"]}',
                ha='center', va='center', fontsize=12, fontweight='bold', color='white')

        # Título
        ax.text(x, y + 0.35, c['titulo'],
                ha='center', va='center', fontsize=11, fontweight='bold', color=c['color'])

        # Descripción
        ax.text(x, y - 0.55, c['desc'],
                ha='center', va='center', fontsize=9, color='#555555')

        # Flecha al siguiente
        if i < 3:
            ax.annotate('', xy=(x_positions[i+1] - box_w/2 - 0.1, y),
                        xytext=(x + box_w/2 + 0.1, y),
                        arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=1.5))

        # Etiqueta "HOY" para clase 3
        if c['highlight']:
            ax.text(x, y - box_h/2 - 0.25, '▲ HOY',
                    ha='center', va='center', fontsize=10, fontweight='bold', color=ROJO)

    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8, color='#888888', style='italic')
    fig.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.savefig(os.path.join(OUTPUT_DIR, 'unidad2_mapa.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('✓ unidad2_mapa.png')


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 2: Ciclo mercantilista
# ═══════════════════════════════════════════════════════════════
def grafico_ciclo_mercantilista():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axis('off')
    ax.set_aspect('equal')

    # Título
    ax.text(0, 2.7, 'El ciclo mercantilista', ha='center', va='center',
            fontsize=16, fontweight='bold', color=AZUL_OSCURO)

    # 4 nodos en círculo
    radius = 1.6
    nodes = [
        {'label': 'Superávit\ncomercial', 'desc': 'Exportar > Importar', 'color': VERDE, 'angle': 90},
        {'label': 'Acumulación\nde oro', 'desc': 'Metales preciosos', 'color': AMARILLO, 'angle': 0},
        {'label': 'Poder\nmilitar', 'desc': 'Ejército y armada', 'color': ROJO, 'angle': 270},
        {'label': 'Control de\ncolonias', 'desc': 'Mercados cautivos', 'color': MORADO, 'angle': 180},
    ]

    node_positions = []
    for node in nodes:
        angle_rad = np.radians(node['angle'])
        x = radius * np.cos(angle_rad)
        y = radius * np.sin(angle_rad)
        node_positions.append((x, y))

        # Círculo del nodo
        circle = plt.Circle((x, y), 0.65, facecolor=node['color'], edgecolor='white',
                            linewidth=2, alpha=0.85, zorder=3)
        ax.add_patch(circle)

        # Texto del nodo
        ax.text(x, y + 0.08, node['label'], ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=4)

        # Descripción fuera del nodo (posiciones fijas para evitar solapamiento)
        if node['angle'] == 90:
            ax.text(x, y + 0.95, node['desc'], ha='center', va='center',
                    fontsize=8, color='#666666', style='italic', zorder=4)
        elif node['angle'] == 270:
            ax.text(x, y - 0.95, node['desc'], ha='center', va='center',
                    fontsize=8, color='#666666', style='italic', zorder=4)
        elif node['angle'] == 0:
            ax.text(x + 1.05, y, node['desc'], ha='left', va='center',
                    fontsize=8, color='#666666', style='italic', zorder=4)
        else:  # 180
            ax.text(x - 1.05, y, node['desc'], ha='right', va='center',
                    fontsize=8, color='#666666', style='italic', zorder=4)

    # Flechas curvas entre nodos
    for i in range(4):
        x1, y1 = node_positions[i]
        x2, y2 = node_positions[(i + 1) % 4]

        # Punto medio desplazado hacia adentro para curva
        mx = (x1 + x2) / 2 * 0.55
        my = (y1 + y2) / 2 * 0.55

        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=2.5,
                                   connectionstyle=f'arc3,rad=-0.3'),
                    zorder=2)

    # Texto central
    ax.text(0, 0, 'JUEGO DE\nSUMA CERO', ha='center', va='center',
            fontsize=12, fontweight='bold', color=AZUL_OSCURO, alpha=0.6,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F4F8', edgecolor=AZUL_OSCURO, alpha=0.3))

    fig.text(0.5, 0.02, 'Elaboración propia', ha='center', fontsize=8, color='#888888', style='italic')
    fig.savefig(os.path.join(OUTPUT_DIR, 'ciclo_mercantilista.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('✓ ciclo_mercantilista.png')


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 3: T-R-P comparativo (mercantilismo vs Smith)
# ═══════════════════════════════════════════════════════════════
def grafico_trp_comparativo():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    categories = ['Tecnología', 'Reglas', 'Poder']

    # Mercantilismo: Poder domina, Reglas altas, Tecnología baja
    merc_values = [2, 8, 10]
    # Smith: Tecnología domina, Reglas bajas (liberalizar), Poder bajo
    smith_values = [10, 3, 2]

    colors_merc = [AZUL_CLARO, NARANJA, ROJO]
    colors_smith = [AZUL_CLARO, NARANJA, ROJO]

    # Mercantilismo
    ax = axes[0]
    bars = ax.barh(categories, merc_values, color=colors_merc, edgecolor='white', height=0.6)
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

    # Texto descriptivo
    ax.text(6, 3.2, 'Poder domina →\nComercio como\ninstrumento estatal',
            ha='center', va='center', fontsize=9, color=GRIS, style='italic')

    # Smith
    ax = axes[1]
    bars = ax.barh(categories, smith_values, color=colors_smith, edgecolor='white', height=0.6)
    ax.set_xlim(0, 12)
    ax.set_title('Adam Smith', fontsize=14, fontweight='bold', color=VERDE, pad=15)
    ax.invert_yaxis()
    for bar, val in zip(bars, smith_values):
        ax.text(val + 0.3, bar.get_y() + bar.get_height()/2, str(val),
                va='center', fontsize=12, fontweight='bold', color='#555555')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticks([])
    ax.tick_params(axis='y', labelsize=12, colors='#333333')
    ax.spines['left'].set_color('#CCCCCC')

    ax.text(6, 3.2, 'Tecnología domina →\nProductividad y\ndivisión del trabajo',
            ha='center', va='center', fontsize=9, color=GRIS, style='italic')

    fig.suptitle('Tecnología — Reglas — Poder: dos visiones del comercio',
                 fontsize=13, fontweight='bold', color=AZUL_OSCURO, y=0.98)
    fig.text(0.5, 0.01, 'Elaboración propia a partir del marco T-R-P (Clase 1)',
             ha='center', fontsize=8, color='#888888', style='italic')
    fig.tight_layout(rect=[0, 0.04, 1, 0.93])
    fig.savefig(os.path.join(OUTPUT_DIR, 'trp_mercantilismo_smith.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('✓ trp_mercantilismo_smith.png')


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 4: División del trabajo (diagrama de flujo)
# ═══════════════════════════════════════════════════════════════
def grafico_division_trabajo():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Título
    ax.text(5, 5.5, 'El mecanismo de Smith: división del trabajo y comercio',
            ha='center', va='center', fontsize=14, fontweight='bold', color=AZUL_OSCURO)

    # Cajas del flujo principal (horizontal)
    boxes = [
        {'x': 1.2, 'y': 3.2, 'text': 'Comercio\namplía el\nmercado', 'color': AZUL_OSCURO},
        {'x': 3.6, 'y': 3.2, 'text': 'Más\nespecialización', 'color': AZUL_MEDIO},
        {'x': 6.0, 'y': 3.2, 'text': 'Mayor\nproductividad', 'color': AZUL_CLARO},
        {'x': 8.4, 'y': 3.2, 'text': 'Más riqueza\n(bienes y\nservicios)', 'color': VERDE},
    ]

    bw = 1.8
    bh = 1.6

    for box in boxes:
        rect = mpatches.FancyBboxPatch((box['x'] - bw/2, box['y'] - bh/2), bw, bh,
                                        boxstyle="round,pad=0.15",
                                        facecolor=box['color'], edgecolor='white',
                                        linewidth=2, alpha=0.9)
        ax.add_patch(rect)
        ax.text(box['x'], box['y'], box['text'], ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

    # Flechas entre cajas
    for i in range(3):
        ax.annotate('', xy=(boxes[i+1]['x'] - bw/2 - 0.05, boxes[i+1]['y']),
                    xytext=(boxes[i]['x'] + bw/2 + 0.05, boxes[i]['y']),
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=2.5))

    # Flecha de retroalimentación (curva arriba)
    ax.annotate('', xy=(boxes[0]['x'], boxes[0]['y'] + bh/2 + 0.15),
                xytext=(boxes[3]['x'], boxes[3]['y'] + bh/2 + 0.15),
                arrowprops=dict(arrowstyle='->', color=NARANJA, lw=2,
                               connectionstyle='arc3,rad=0.3', linestyle='--'))
    ax.text(4.8, 4.7, 'Retroalimentación: más riqueza → más comercio',
            ha='center', va='center', fontsize=9, color=NARANJA, fontweight='bold')

    # Detalle debajo: 3 razones de productividad
    reasons = [
        {'x': 2.5, 'text': '① Destreza:\nrepetir mejora', 'color': AZUL_MEDIO},
        {'x': 5.0, 'text': '② Ahorro de tiempo:\nsin cambiar tareas', 'color': AZUL_MEDIO},
        {'x': 7.5, 'text': '③ Innovación:\nespecialización genera\nmejoras técnicas', 'color': AZUL_MEDIO},
    ]

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
             ha='center', fontsize=8, color='#888888', style='italic')
    fig.savefig(os.path.join(OUTPUT_DIR, 'division_trabajo_diagrama.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('✓ division_trabajo_diagrama.png')


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 5: Comercio británico 1800-1870 (datos FTWTHD)
# ═══════════════════════════════════════════════════════════════
def grafico_comercio_britanico():
    # Datos FTWTHD: UK imports (col 40) y exports (col 82), millones USD corrientes
    # Extraídos de europe_1800_1938_FTWTHD_201710_v01.xlsx
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

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.fill_between(years, uk_imp, alpha=0.15, color=AZUL_MEDIO)
    ax.fill_between(years, uk_exp, alpha=0.15, color=VERDE)
    ax.plot(years, uk_imp, color=AZUL_OSCURO, linewidth=2, label='Importaciones', marker='', zorder=3)
    ax.plot(years, uk_exp, color=VERDE, linewidth=2, label='Exportaciones', marker='', zorder=3)
    ax.plot(years, total, color=NARANJA, linewidth=2.5, linestyle='--', label='Comercio total', zorder=4)

    ax.set_title('Comercio exterior de Gran Bretaña (1800–1870)', fontsize=14,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)
    ax.set_xlabel('Año', fontsize=11, color='#555555')
    ax.set_ylabel('Millones de USD corrientes', fontsize=11, color='#555555')

    # Anotaciones de contexto
    ax.axvline(x=1815, color=GRIS, linestyle=':', alpha=0.5)
    ax.text(1815, 1800, 'Fin guerras\nnapoleónicas\n(1815)', ha='center', fontsize=8, color=GRIS)

    ax.axvline(x=1846, color=GRIS, linestyle=':', alpha=0.5)
    ax.text(1846, 1900, 'Derogación\nCorn Laws\n(1846)', ha='center', fontsize=8, color=GRIS)

    # Anotación de multiplicación
    ax.annotate(f'Comercio total\nse multiplica ×{total[-1]/total[0]:.1f}',
                xy=(1865, total[-1]), xytext=(1835, 2100),
                fontsize=10, fontweight='bold', color=NARANJA,
                arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8F0', edgecolor=NARANJA, alpha=0.8))

    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))

    estilo_base(fig, ax, 'Fuente: Federico-Tena World Trade Historical Database (FTWTHD)')
    fig.savefig(os.path.join(OUTPUT_DIR, 'comercio_britanico_1800.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('✓ comercio_britanico_1800.png')


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 6: Ventaja absoluta (tabla 2x2 + flechas)
# ═══════════════════════════════════════════════════════════════
def grafico_ventaja_absoluta():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Título
    ax.text(5, 6.5, 'Ventaja absoluta: cada país produce lo que hace más barato',
            ha='center', va='center', fontsize=14, fontweight='bold', color=AZUL_OSCURO)
    ax.text(5, 6.05, 'Horas de trabajo necesarias para producir 1 unidad',
            ha='center', va='center', fontsize=11, color=GRIS)

    # Tabla 2x2
    table_x = 2.0
    table_y = 2.8
    cell_w = 2.2
    cell_h = 1.2
    header_h = 0.8

    # Headers de columna
    for j, (label, x_off) in enumerate([('Tela', 0), ('Vino', 1)]):
        x = table_x + (j + 1) * cell_w
        rect = mpatches.FancyBboxPatch((x, table_y + cell_h * 2), cell_w, header_h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=AZUL_OSCURO, edgecolor='white', linewidth=1)
        ax.add_patch(rect)
        ax.text(x + cell_w/2, table_y + cell_h * 2 + header_h/2, label,
                ha='center', va='center', fontsize=13, fontweight='bold', color='white')

    # Headers de fila (A arriba, B abajo — misma posición que datos)
    for i, label in enumerate(['País A', 'País B']):
        y = table_y + (1 - i) * cell_h
        rect = mpatches.FancyBboxPatch((table_x, y), cell_w, cell_h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=AZUL_OSCURO, edgecolor='white', linewidth=1)
        ax.add_patch(rect)
        ax.text(table_x + cell_w/2, y + cell_h/2, label,
                ha='center', va='center', fontsize=13, fontweight='bold', color='white')

    # Datos
    data = [[2, 6], [4, 3]]  # [A tela, A vino], [B tela, B vino]
    highlights = [[(True, VERDE), (False, None)], [(False, None), (True, VERDE)]]  # Ventajas absolutas

    for i in range(2):
        for j in range(2):
            x = table_x + (j + 1) * cell_w
            y = table_y + (1 - i) * cell_h
            is_highlight, color = highlights[i][j]
            fc = '#E8F5E9' if is_highlight else '#F8F9FA'
            ec = VERDE if is_highlight else '#DDDDDD'
            lw = 2.5 if is_highlight else 1

            rect = mpatches.FancyBboxPatch((x, y), cell_w, cell_h,
                                            boxstyle="round,pad=0.05",
                                            facecolor=fc, edgecolor=ec, linewidth=lw)
            ax.add_patch(rect)
            ax.text(x + cell_w/2, y + cell_h/2, f'{data[i][j]} hs',
                    ha='center', va='center', fontsize=16, fontweight='bold',
                    color=VERDE if is_highlight else '#555555')

    # Indicadores de ventaja (a la derecha de la tabla)
    ind_x = table_x + 3 * cell_w + 0.3
    ax.text(ind_x, table_y + 1.5 * cell_h, '← 2 < 4\nA gana en Tela',
            ha='left', va='center', fontsize=9, color=VERDE, fontweight='bold')
    ax.text(ind_x, table_y + 0.5 * cell_h, '← 3 < 6\nB gana en Vino',
            ha='left', va='center', fontsize=9, color=VERDE, fontweight='bold')

    # Flechas de exportación
    arrow_y = table_y - 0.6
    # A exporta tela
    ax.annotate('', xy=(3.0, arrow_y), xytext=(5.0, arrow_y),
                arrowprops=dict(arrowstyle='->', color=AZUL_MEDIO, lw=2.5))
    ax.text(4.0, arrow_y + 0.25, 'A exporta Tela', ha='center', fontsize=10,
            fontweight='bold', color=AZUL_MEDIO)

    # B exporta vino
    ax.annotate('', xy=(7.5, arrow_y), xytext=(5.5, arrow_y),
                arrowprops=dict(arrowstyle='->', color=NARANJA, lw=2.5))
    ax.text(6.5, arrow_y + 0.25, 'B exporta Vino', ha='center', fontsize=10,
            fontweight='bold', color=NARANJA)

    # Resultado
    result_y = arrow_y - 0.7
    rect = mpatches.FancyBboxPatch((2.5, result_y - 0.35), 5, 0.7,
                                    boxstyle="round,pad=0.1",
                                    facecolor='#E8F5E9', edgecolor=VERDE, linewidth=2)
    ax.add_patch(rect)
    ax.text(5, result_y, 'Ambos países ganan: consumen más que en autarquía',
            ha='center', va='center', fontsize=11, fontweight='bold', color=VERDE)

    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8, color='#888888', style='italic')
    fig.savefig(os.path.join(OUTPUT_DIR, 'ventaja_absoluta_ejemplo.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('✓ ventaja_absoluta_ejemplo.png')


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 7: Límite de Smith (A mejor en todo)
# ═══════════════════════════════════════════════════════════════
def grafico_limite_smith():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Título
    ax.text(5, 6.5, '¿Y si un país es mejor en todo?',
            ha='center', va='center', fontsize=14, fontweight='bold', color=ROJO)
    ax.text(5, 6.05, 'Horas de trabajo necesarias para producir 1 unidad',
            ha='center', va='center', fontsize=11, color=GRIS)

    # Tabla 2x2
    table_x = 2.0
    table_y = 3.0
    cell_w = 2.2
    cell_h = 1.2
    header_h = 0.8

    # Headers de columna
    for j, label in enumerate(['Tela', 'Vino']):
        x = table_x + (j + 1) * cell_w
        rect = mpatches.FancyBboxPatch((x, table_y + cell_h * 2), cell_w, header_h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=AZUL_OSCURO, edgecolor='white', linewidth=1)
        ax.add_patch(rect)
        ax.text(x + cell_w/2, table_y + cell_h * 2 + header_h/2, label,
                ha='center', va='center', fontsize=13, fontweight='bold', color='white')

    # Headers de fila
    for i, label in enumerate(['País A', 'País B']):
        y = table_y + (1 - i) * cell_h
        rect = mpatches.FancyBboxPatch((table_x, y), cell_w, cell_h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=AZUL_OSCURO, edgecolor='white', linewidth=1)
        ax.add_patch(rect)
        ax.text(table_x + cell_w/2, y + cell_h/2, label,
                ha='center', va='center', fontsize=13, fontweight='bold', color='white')

    # Datos: A es mejor en todo
    data = [[1, 2], [6, 8]]

    for i in range(2):
        for j in range(2):
            x = table_x + (j + 1) * cell_w
            y = table_y + (1 - i) * cell_h
            # A gana en ambos
            if i == 0:
                fc = '#E3F2FD'
                ec = AZUL_MEDIO
                text_color = AZUL_OSCURO
            else:
                fc = '#FFF3E0'
                ec = NARANJA
                text_color = '#B85C1F'

            rect = mpatches.FancyBboxPatch((x, y), cell_w, cell_h,
                                            boxstyle="round,pad=0.05",
                                            facecolor=fc, edgecolor=ec, linewidth=2)
            ax.add_patch(rect)
            ax.text(x + cell_w/2, y + cell_h/2, f'{data[i][j]} hs',
                    ha='center', va='center', fontsize=16, fontweight='bold', color=text_color)

    # Indicadores (a la derecha de la tabla)
    ind_x = table_x + 3 * cell_w + 0.3
    ax.text(ind_x, table_y + 1.5 * cell_h, '← A gana\n(1 < 6 y 2 < 8)',
            ha='left', va='center', fontsize=9, color=AZUL_MEDIO, fontweight='bold')
    ax.text(ind_x, table_y + 0.5 * cell_h, '← B pierde\nen TODO',
            ha='left', va='center', fontsize=9, color=ROJO, fontweight='bold')

    # Pregunta
    question_y = 1.8
    rect = mpatches.FancyBboxPatch((1.5, question_y - 0.5), 7, 1.2,
                                    boxstyle="round,pad=0.15",
                                    facecolor='#FEF3C7', edgecolor='#F59E0B', linewidth=2)
    ax.add_patch(rect)
    ax.text(5, question_y + 0.25, '⚠  A tiene ventaja absoluta en TODO',
            ha='center', va='center', fontsize=12, fontweight='bold', color='#92400E')
    ax.text(5, question_y - 0.15, '¿B no exporta nada? ¿No hay comercio?',
            ha='center', va='center', fontsize=11, color='#92400E')

    # Teaser Ricardo
    ax.text(5, 0.6, 'La respuesta la da RICARDO → ventaja COMPARATIVA (costos relativos)',
            ha='center', va='center', fontsize=11, fontweight='bold', color=VERDE,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=VERDE, alpha=0.7))

    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8, color='#888888', style='italic')
    fig.savefig(os.path.join(OUTPUT_DIR, 'limite_smith.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('✓ limite_smith.png')


# ═══════════════════════════════════════════════════════════════
# EJECUTAR TODOS
# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print('Generando gráficos para Clase 3...\n')
    grafico_unidad2_mapa()
    grafico_ciclo_mercantilista()
    grafico_trp_comparativo()
    grafico_division_trabajo()
    grafico_comercio_britanico()
    grafico_ventaja_absoluta()
    grafico_limite_smith()
    print('\n¡Todos los gráficos generados!')
