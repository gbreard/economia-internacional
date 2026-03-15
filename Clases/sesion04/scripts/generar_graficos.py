"""
Genera los 13 gráficos para Clase 7: Rendimientos crecientes, competencia imperfecta y NGE
(6 originales + 7 nuevos para la versión expandida de 4 horas)
"""
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent.parent / "graficos"
OUT.mkdir(exist_ok=True)

# Paleta
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
CELESTE = '#0EA5E9'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'
GRIS_CLARO = '#E5E7EB'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Arial', 'Helvetica'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
})


# ============================================================
# 1. COSTO MEDIO DESCENDENTE
# ============================================================
def grafico_costo_medio():
    fig, ax = plt.subplots(figsize=(8, 5))

    Q = np.linspace(5, 120, 200)
    F = 100
    c = 2
    CMe = F / Q + c
    CMg = np.full_like(Q, c)

    ax.plot(Q, CMe, color=AZUL_OSCURO, linewidth=2.5, label='CMe = F/Q + c')
    ax.plot(Q, CMg, color=ROJO, linewidth=2, linestyle='--', label='CMg = c')

    # Puntos de ejemplo
    for q, label in [(10, 'Q=10\nCMe=12'), (50, 'Q=50\nCMe=4'), (100, 'Q=100\nCMe=3')]:
        cme_val = F / q + c
        ax.plot(q, cme_val, 'o', color=NARANJA, markersize=8, zorder=5)
        ax.annotate(label, (q, cme_val), textcoords="offset points",
                    xytext=(12, 10), fontsize=9, color=NARANJA, fontweight='bold')

    # Zona sombreada entre CMe y CMg
    ax.fill_between(Q, CMg, CMe, alpha=0.1, color=AZUL_MEDIO)
    ax.annotate('Costo fijo\nsin cubrir', xy=(30, 4.5), fontsize=9, color=AZUL_MEDIO,
                fontstyle='italic', ha='center')

    ax.set_xlabel('Cantidad producida (Q)', fontsize=12)
    ax.set_ylabel('Costo por unidad ($)', fontsize=12)
    ax.set_title('Rendimientos crecientes: CMe cae con la escala', fontsize=14,
                 fontweight='bold', color=AZUL_OSCURO)
    ax.set_xlim(0, 125)
    ax.set_ylim(0, 16)
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Nota al pie
    fig.text(0.5, -0.02, 'F = 100 (costo fijo), c = 2 (costo marginal). CMe = F/Q + c',
             ha='center', fontsize=9, color=GRIS, style='italic')

    fig.savefig(OUT / 'costo_medio.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK costo_medio.png')


# ============================================================
# 2. INTERNAS VS EXTERNAS
# ============================================================
def grafico_internas_externas():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

    # --- Panel izquierdo: Internas ---
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Economias de escala INTERNAS\n(a la firma)', fontsize=13,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    # Firma grande en el centro
    big = mpatches.FancyBboxPatch((3, 3.5), 4, 3, boxstyle="round,pad=0.3",
                                   facecolor=AZUL_MEDIO, edgecolor=AZUL_OSCURO, linewidth=2, alpha=0.8)
    ax.add_patch(big)
    ax.text(5, 5, 'FIRMA\nGRANDE', ha='center', va='center', fontsize=13,
            fontweight='bold', color='white')

    # Firmas pequeñas alrededor (tachadas)
    for pos in [(0.5, 8), (8, 8), (0.5, 0.5), (8, 0.5)]:
        small = mpatches.FancyBboxPatch((pos[0], pos[1]), 1.2, 1, boxstyle="round,pad=0.1",
                                         facecolor=GRIS_CLARO, edgecolor=GRIS, linewidth=1, alpha=0.5)
        ax.add_patch(small)
        ax.text(pos[0]+0.6, pos[1]+0.5, 'X', ha='center', va='center',
                fontsize=14, color=ROJO, fontweight='bold')

    # Labels
    ax.text(5, 1.5, 'CMe baja porque la firma\nproduce mas unidades',
            ha='center', fontsize=10, color=GRIS, style='italic')
    ax.text(5, 8.5, 'Competencia imperfecta:\npocas firmas dominan',
            ha='center', fontsize=10, color=ROJO, fontweight='bold')

    # Ejemplos
    ax.text(5, 0.2, 'Ej: autos, farmaceutica, software, aviacion',
            ha='center', fontsize=9, color=AZUL_OSCURO, style='italic')

    # --- Panel derecho: Externas ---
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Economias de escala EXTERNAS\n(al sector/territorio)', fontsize=13,
                 fontweight='bold', color=VERDE, pad=15)

    # Cluster: muchas firmas pequenas agrupadas
    cluster_positions = [(2.5, 5), (4, 6.5), (5.5, 5), (4, 3.5), (3, 4.2), (5, 4.2),
                         (3.5, 5.5), (4.5, 5.5), (6, 6), (2.5, 6.5)]
    for i, (x, y) in enumerate(cluster_positions):
        small = mpatches.FancyBboxPatch((x, y), 0.9, 0.7, boxstyle="round,pad=0.1",
                                         facecolor='#D4EDDA', edgecolor=VERDE, linewidth=1.2)
        ax.add_patch(small)
        ax.text(x+0.45, y+0.35, f'f{i+1}', ha='center', va='center',
                fontsize=8, color=VERDE, fontweight='bold')

    # Elipse alrededor del cluster
    ellipse = mpatches.Ellipse((4.2, 5.2), 6, 5, fill=False,
                                edgecolor=VERDE, linewidth=2, linestyle='--', alpha=0.7)
    ax.add_patch(ellipse)
    ax.text(4.2, 8.5, 'Muchas firmas, pero\nconcentradas en un lugar',
            ha='center', fontsize=10, color=VERDE, fontweight='bold')

    ax.text(4.2, 1.5, 'CMe baja porque el sector/lugar\ntiene proveedores, talento, spillovers',
            ha='center', fontsize=10, color=GRIS, style='italic')

    ax.text(4.2, 0.2, 'Ej: Silicon Valley, distritos italianos, Cordoba autopartes',
            ha='center', fontsize=9, color=VERDE, style='italic')

    fig.suptitle('Dos tipos de economias de escala', fontsize=15, fontweight='bold',
                 color=AZUL_OSCURO, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT / 'internas_externas.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK internas_externas.png')


# ============================================================
# 3. COMERCIO INTRAINDUSTRIAL
# ============================================================
def grafico_comercio_intraindustrial():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_title('Comercio intraindustrial: "ida y vuelta" en el mismo sector',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=15)

    # Pais A
    box_a = mpatches.FancyBboxPatch((0.5, 2), 3.2, 3, boxstyle="round,pad=0.3",
                                     facecolor='#DBEAFE', edgecolor=AZUL_MEDIO, linewidth=2)
    ax.add_patch(box_a)
    ax.text(2.1, 4.5, 'Pais A', ha='center', fontsize=14, fontweight='bold', color=AZUL_OSCURO)
    ax.text(2.1, 3.7, 'Produce:', ha='center', fontsize=10, color=GRIS)
    ax.text(2.1, 3.2, 'Auto modelo a', ha='center', fontsize=11, color=AZUL_MEDIO, fontweight='bold')
    ax.text(2.1, 2.7, 'Auto modelo b', ha='center', fontsize=11, color=AZUL_MEDIO, fontweight='bold')

    # Pais B
    box_b = mpatches.FancyBboxPatch((6.3, 2), 3.2, 3, boxstyle="round,pad=0.3",
                                     facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=2)
    ax.add_patch(box_b)
    ax.text(7.9, 4.5, 'Pais B', ha='center', fontsize=14, fontweight='bold', color=NARANJA)
    ax.text(7.9, 3.7, 'Produce:', ha='center', fontsize=10, color=GRIS)
    ax.text(7.9, 3.2, 'Auto modelo c', ha='center', fontsize=11, color=NARANJA, fontweight='bold')
    ax.text(7.9, 2.7, 'Auto modelo d', ha='center', fontsize=11, color=NARANJA, fontweight='bold')

    # Flechas bidireccionales
    ax.annotate('', xy=(6.1, 4.0), xytext=(3.9, 4.0),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
    ax.annotate('', xy=(3.9, 3.0), xytext=(6.1, 3.0),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))

    # Labels en las flechas
    ax.text(5, 4.4, 'Exporta a, b', ha='center', fontsize=10, color=VERDE, fontweight='bold')
    ax.text(5, 2.5, 'Exporta c, d', ha='center', fontsize=10, color=VERDE, fontweight='bold')

    # Sector label
    sector = mpatches.FancyBboxPatch((3.5, 5.5), 3, 0.8, boxstyle="round,pad=0.2",
                                      facecolor=AZUL_OSCURO, edgecolor=AZUL_OSCURO)
    ax.add_patch(sector)
    ax.text(5, 5.9, 'MISMO SECTOR: Automotriz', ha='center', fontsize=12,
            fontweight='bold', color='white')

    # Nota inferior
    ax.text(5, 1.2, 'No es "lo mismo por lo mismo": son variedades (modelo, calidad, diseno)',
            ha='center', fontsize=10, color=GRIS, style='italic')
    ax.text(5, 0.5, '"No es trigo por vino; es VW por Peugeot"',
            ha='center', fontsize=11, color=AZUL_OSCURO, fontweight='bold', style='italic')

    fig.savefig(OUT / 'comercio_intraindustrial.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK comercio_intraindustrial.png')


# ============================================================
# 4. MECANISMO KRUGMAN EN 4 PASOS
# ============================================================
def grafico_mecanismo_krugman():
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title('El mecanismo Krugman en 4 pasos', fontsize=15,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    steps = [
        ('1', 'Preferencia\npor variedad', 'Consumidores\nquieren elegir', CELESTE),
        ('2', 'Costos fijos\npor variedad', 'Cada variedad\ncuesta F (I+D,\ndiseno...)', NARANJA),
        ('3', 'Necesidad\nde escala', 'Producir mucho\npara amortizar F\n-> baja CMe', AZUL_MEDIO),
        ('4', 'Comercio\nagranda mercado', 'Mas variedades\n+ menores costos\n= IIT', VERDE),
    ]

    box_w = 2.3
    gap = 0.5
    start_x = 0.5
    box_h = 3.5
    y_start = 1.2

    for i, (num, title, desc, color) in enumerate(steps):
        x = start_x + i * (box_w + gap)

        # Caja principal
        box = mpatches.FancyBboxPatch((x, y_start), box_w, box_h,
                                       boxstyle="round,pad=0.3",
                                       facecolor=color, edgecolor=color,
                                       alpha=0.15, linewidth=2)
        ax.add_patch(box)
        # Borde coloreado
        box_border = mpatches.FancyBboxPatch((x, y_start), box_w, box_h,
                                              boxstyle="round,pad=0.3",
                                              facecolor='none', edgecolor=color, linewidth=2)
        ax.add_patch(box_border)

        # Numero
        circle = mpatches.Circle((x + 0.35, y_start + box_h - 0.4), 0.25,
                                  facecolor=color, edgecolor='white', linewidth=1.5, zorder=5)
        ax.add_patch(circle)
        ax.text(x + 0.35, y_start + box_h - 0.4, num, ha='center', va='center',
                fontsize=12, fontweight='bold', color='white', zorder=6)

        # Titulo del paso
        ax.text(x + box_w/2, y_start + box_h - 0.9, title, ha='center', va='center',
                fontsize=11, fontweight='bold', color=color)

        # Descripcion
        ax.text(x + box_w/2, y_start + 1.0, desc, ha='center', va='center',
                fontsize=9, color=GRIS, linespacing=1.3)

        # Flecha entre pasos
        if i < 3:
            ax.annotate('', xy=(x + box_w + 0.1, y_start + box_h/2),
                        xytext=(x + box_w + gap - 0.1, y_start + box_h/2),
                        arrowprops=dict(arrowstyle='<-', color=GRIS, lw=2))

    # Resultado final
    result_box = mpatches.FancyBboxPatch((1.5, 0.1), 9, 0.8, boxstyle="round,pad=0.2",
                                          facecolor='#D4EDDA', edgecolor=VERDE, linewidth=2)
    ax.add_patch(result_box)
    ax.text(6, 0.5, 'Resultado: Comercio = mas mercado -> mas escala + mas variedad',
            ha='center', va='center', fontsize=12, fontweight='bold', color=VERDE)

    fig.savefig(OUT / 'mecanismo_krugman.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK mecanismo_krugman.png')


# ============================================================
# 5. GANANCIAS DEL COMERCIO
# ============================================================
def grafico_ganancias_comercio():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Dos ganancias del comercio en Krugman', fontsize=15,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    # Columna 1: Variedad
    box1 = mpatches.FancyBboxPatch((0.5, 3), 4, 3.5, boxstyle="round,pad=0.3",
                                    facecolor='#EBF5FB', edgecolor=CELESTE, linewidth=2)
    ax.add_patch(box1)
    ax.text(2.5, 6.0, 'Ganancia por', ha='center', fontsize=12, color=CELESTE)
    ax.text(2.5, 5.4, 'VARIEDAD', ha='center', fontsize=16, fontweight='bold', color=CELESTE)
    ax.text(2.5, 4.6, 'Mas opciones de\nconsumo e insumos', ha='center', fontsize=11, color=GRIS)
    ax.text(2.5, 3.5, 'Modelos, calidades,\nmarcas, disenos', ha='center', fontsize=10,
            color=GRIS, style='italic')

    # Columna 2: Escala
    box2 = mpatches.FancyBboxPatch((5.5, 3), 4, 3.5, boxstyle="round,pad=0.3",
                                    facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=2)
    ax.add_patch(box2)
    ax.text(7.5, 6.0, 'Ganancia por', ha='center', fontsize=12, color=NARANJA)
    ax.text(7.5, 5.4, 'ESCALA', ha='center', fontsize=16, fontweight='bold', color=NARANJA)
    ax.text(7.5, 4.6, 'Cada firma produce mas\n-> CMe baja -> precios bajan', ha='center',
            fontsize=11, color=GRIS)
    ax.text(7.5, 3.5, 'Aunque haya mark-up,\nel costo base es menor', ha='center', fontsize=10,
            color=GRIS, style='italic')

    # Flecha hacia resultado
    ax.annotate('', xy=(5, 2.2), xytext=(2.5, 2.8),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
    ax.annotate('', xy=(5, 2.2), xytext=(7.5, 2.8),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))

    # Resultado
    result = mpatches.FancyBboxPatch((2.5, 1), 5, 1.2, boxstyle="round,pad=0.3",
                                      facecolor='#D4EDDA', edgecolor=VERDE, linewidth=2)
    ax.add_patch(result)
    ax.text(5, 1.6, 'BIENESTAR SUBE', ha='center', fontsize=14,
            fontweight='bold', color=VERDE)
    ax.text(5, 1.15, '(en promedio -- pero con reasignacion)', ha='center',
            fontsize=10, color=GRIS, style='italic')

    # Contraste
    ax.text(5, 0.3, 'vs. Ricardo/H-O: ganancia por "mejor asignacion"  |  Krugman: escala + variedad',
            ha='center', fontsize=9, color=AZUL_OSCURO, style='italic')

    fig.savefig(OUT / 'ganancias_comercio.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK ganancias_comercio.png')


# ============================================================
# 6. CENTRO-PERIFERIA
# ============================================================
def grafico_centro_periferia():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Nueva Geografia Economica: centro-periferia', fontsize=15,
                 fontweight='bold', color=AZUL_OSCURO, pad=15)

    # Centro (circulo grande)
    centro = mpatches.Circle((5, 4.5), 1.8, facecolor=AZUL_MEDIO, edgecolor=AZUL_OSCURO,
                              linewidth=2.5, alpha=0.3)
    ax.add_patch(centro)
    centro_inner = mpatches.Circle((5, 4.5), 1.2, facecolor=AZUL_MEDIO, edgecolor=AZUL_OSCURO,
                                    linewidth=1.5, alpha=0.5)
    ax.add_patch(centro_inner)
    ax.text(5, 4.8, 'CENTRO', ha='center', va='center', fontsize=14,
            fontweight='bold', color=AZUL_OSCURO)
    ax.text(5, 4.1, 'Industria\nServicios\nInnovacion', ha='center', va='center',
            fontsize=9, color=AZUL_OSCURO)

    # Periferia (circulos pequenos)
    periferias = [(1.5, 6.5, 0.6), (8.5, 6.5, 0.6), (1.2, 2, 0.5),
                  (8.8, 2, 0.5), (5, 0.8, 0.5)]
    for x, y, r in periferias:
        p = mpatches.Circle((x, y), r, facecolor=GRIS_CLARO, edgecolor=GRIS,
                             linewidth=1.5, alpha=0.7)
        ax.add_patch(p)
        ax.text(x, y, 'P', ha='center', va='center', fontsize=10, color=GRIS, fontweight='bold')

    # Flechas de atraccion hacia el centro
    for x, y, _ in periferias:
        dx = 5 - x
        dy = 4.5 - y
        factor = 0.55
        ax.annotate('', xy=(x + dx*factor, y + dy*factor),
                    xytext=(x + dx*0.15, y + dy*0.15),
                    arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5,
                                    connectionstyle='arc3,rad=0.1'))

    # Causacion acumulativa (circulo de texto)
    ax.text(5, 7.5, 'Causacion acumulativa', ha='center', fontsize=12,
            fontweight='bold', color=VERDE)
    ax.text(5, 7.0, 'Mas produccion -> mas empleo/mercado -> mas proveedores -> menores costos -> +produccion',
            ha='center', fontsize=9, color=VERDE, style='italic')

    # Etiquetas
    ax.text(1.5, 1.0, 'Periferia:\nmenos industria,\nmenos servicios',
            ha='center', fontsize=9, color=GRIS, style='italic')
    ax.text(8.5, 1.0, 'Path dependence:\nla historia\nimporta',
            ha='center', fontsize=9, color=NARANJA, style='italic')

    fig.savefig(OUT / 'centro_periferia.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK centro_periferia.png')


# ============================================================
# 7. LA TRIADA - COMERCIO ENTRE GIGANTES SIMILARES (NUEVO)
# ============================================================
def grafico_triada_comercio():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # Panel izquierdo: participacion en exportaciones mundiales
    ax = axes[0]
    bloques = ['UE\n(intra+extra)', 'EEUU', 'Japon', 'Resto\ndel mundo']
    pct_1995 = [39, 15, 11, 35]
    pct_2020 = [33, 10, 4, 53]
    x = np.arange(len(bloques))
    w = 0.35

    bars1 = ax.bar(x - w/2, pct_1995, w, color=AZUL_MEDIO, label='1995', edgecolor='white')
    bars2 = ax.bar(x + w/2, pct_2020, w, color=CELESTE, label='2020', edgecolor='white', alpha=0.8)

    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{int(bar.get_height())}%', ha='center', fontsize=9, fontweight='bold', color=AZUL_OSCURO)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{int(bar.get_height())}%', ha='center', fontsize=9, color=CELESTE, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(bloques, fontsize=10)
    ax.set_ylabel('% de exportaciones mundiales', fontsize=11)
    ax.set_title('Participacion en comercio mundial', fontsize=13, fontweight='bold', color=AZUL_OSCURO)
    ax.set_ylim(0, 50)
    ax.legend(fontsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Anotacion triada
    ax.annotate('Triada: 65% en 1995\n47% en 2020',
                xy=(1, 42), fontsize=10, color=ROJO, fontweight='bold',
                ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEE2E2', edgecolor=ROJO, alpha=0.8))

    # Panel derecho: indice IIT por par
    ax2 = axes[1]
    pares = ['UE\ninterna', 'EEUU-\nCanada', 'EEUU-\nUE', 'Japon-\nUE', 'Norte-\nSur']
    gl_values = [0.65, 0.55, 0.50, 0.45, 0.20]
    colors = [AZUL_MEDIO, AZUL_MEDIO, AZUL_MEDIO, AZUL_MEDIO, NARANJA]

    bars = ax2.barh(pares, gl_values, color=colors, edgecolor='white', height=0.6)
    for bar, val in zip(bars, gl_values):
        ax2.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2,
                 f'{val:.2f}', va='center', fontsize=10, fontweight='bold', color=AZUL_OSCURO)

    ax2.set_xlim(0, 0.85)
    ax2.set_xlabel('Indice Grubel-Lloyd promedio', fontsize=11)
    ax2.set_title('IIT entre miembros de la triada', fontsize=13, fontweight='bold', color=AZUL_OSCURO)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Linea de referencia
    ax2.axvline(x=0.50, color=GRIS, linestyle='--', alpha=0.5)
    ax2.text(0.51, -0.6, 'GL = 0.50\n(mitad IIT)', fontsize=8, color=GRIS, style='italic')

    fig.suptitle('La triada: comercio masivo entre economias similares',
                 fontsize=15, fontweight='bold', color=AZUL_OSCURO, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT / 'triada_comercio.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK triada_comercio.png')


# ============================================================
# 8. TABLA COMPARATIVA DE TEORIAS (NUEVO)
# ============================================================
def grafico_tabla_teorias():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('off')

    # Datos de la tabla
    headers = ['', 'Smith\n(1776)', 'Ricardo\n(1817)', 'H-O\n(1930s)', 'Krugman\n(1979)']
    rows = [
        ['Motor del\ncomercio', 'Ventaja\nabsoluta', 'Ventaja\ncomparativa', 'Dotacion de\nfactores', 'Rendimientos\ncrecientes'],
        ['Tipo de\ncomercio', 'Interindustrial', 'Interindustrial', 'Interindustrial\n(N-S)', 'Intraindustrial\n(N-N)'],
        ['Estructura\nde mercado', 'Competencia\nperfecta', 'Competencia\nperfecta', 'Competencia\nperfecta', 'Competencia\nmonopolistica'],
        ['Rendimientos', 'Constantes', 'Constantes', 'Constantes', 'Crecientes\n(internos)'],
        ['Ganancias', 'Especializacion', 'Mejor\nasignacion', 'Mejor asignacion\n+ efecto dist.', 'Variedad\n+ escala'],
        ['Ejemplo\ntipico', 'Vino vs pano', 'Vino vs pano\n(ambos ganan)', 'Soja (ARG) vs\nautos (ALE)', 'VW (ALE) vs\nPeugeot (FRA)'],
    ]

    n_cols = len(headers)
    n_rows = len(rows)

    col_widths = [0.13, 0.18, 0.18, 0.22, 0.22]
    x_positions = [0.03]
    for w in col_widths[:-1]:
        x_positions.append(x_positions[-1] + w)

    row_h = 0.12
    y_start = 0.88

    # Header
    header_y = y_start + 0.02
    for j, (header, x_pos, cw) in enumerate(zip(headers, x_positions, col_widths)):
        bg_color = AZUL_OSCURO if j > 0 else GRIS
        rect = mpatches.FancyBboxPatch((x_pos, header_y), cw - 0.005, row_h + 0.02,
                                        boxstyle="round,pad=0.005", facecolor=bg_color,
                                        edgecolor='white', linewidth=1, zorder=5,
                                        transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x_pos + cw/2, header_y + (row_h + 0.02)/2, header,
                ha='center', va='center', fontsize=9, fontweight='bold', color='white',
                transform=ax.transAxes, zorder=6)

    # Rows
    for i, row in enumerate(rows):
        y = y_start - i * (row_h + 0.005)
        for j, (cell, x_pos, cw) in enumerate(zip(row, x_positions, col_widths)):
            if j == 0:
                bg = '#F0F4F8'
                fc = AZUL_OSCURO
                fw = 'bold'
            elif j == 4:  # Krugman column highlight
                bg = '#EBF5FB'
                fc = AZUL_MEDIO
                fw = 'normal'
            else:
                bg = 'white' if i % 2 == 0 else '#F9FAFB'
                fc = GRIS
                fw = 'normal'

            rect = mpatches.FancyBboxPatch((x_pos, y - row_h), cw - 0.005, row_h,
                                            boxstyle="round,pad=0.003", facecolor=bg,
                                            edgecolor=GRIS_CLARO, linewidth=0.5,
                                            transform=ax.transAxes)
            ax.add_patch(rect)
            ax.text(x_pos + cw/2, y - row_h/2, cell,
                    ha='center', va='center', fontsize=8, color=fc, fontweight=fw,
                    transform=ax.transAxes, linespacing=1.2)

    ax.set_title('Comparacion de teorias del comercio internacional',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=20)

    # Nota al pie
    fig.text(0.5, 0.01, 'Las teorias se complementan: cada una explica un aspecto distinto del comercio real',
             ha='center', fontsize=10, color=VERDE, fontweight='bold', style='italic')

    fig.savefig(OUT / 'tabla_teorias.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK tabla_teorias.png')


# ============================================================
# 9. GRUBEL-LLOYD EJEMPLO (NUEVO)
# ============================================================
def grafico_grubel_lloyd_ejemplo():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

    # Panel izquierdo: ejemplo visual
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('Formula e interpretacion', fontsize=13, fontweight='bold', color=AZUL_OSCURO)

    # Formula
    formula_box = mpatches.FancyBboxPatch((0.5, 7.5), 9, 1.5, boxstyle="round,pad=0.3",
                                           facecolor='#EBF5FB', edgecolor=AZUL_MEDIO, linewidth=2)
    ax.add_patch(formula_box)
    ax.text(5, 8.5, 'GL = 1  -  |X - M| / (X + M)', ha='center', va='center',
            fontsize=16, fontweight='bold', color=AZUL_OSCURO, family='monospace')
    ax.text(5, 7.8, 'X = exportaciones del sector,  M = importaciones del sector',
            ha='center', fontsize=9, color=GRIS)

    # Ejemplo 1: autos
    ex1 = mpatches.FancyBboxPatch((0.5, 4.2), 4, 2.8, boxstyle="round,pad=0.2",
                                   facecolor='#D4EDDA', edgecolor=VERDE, linewidth=1.5)
    ax.add_patch(ex1)
    ax.text(2.5, 6.5, 'AUTOS', ha='center', fontsize=12, fontweight='bold', color=VERDE)
    ax.text(2.5, 5.9, 'X = 80,  M = 60', ha='center', fontsize=10, color=GRIS)
    ax.text(2.5, 5.3, '|80 - 60| / (80 + 60)', ha='center', fontsize=10, color=GRIS)
    ax.text(2.5, 4.7, 'GL = 1 - 20/140 = 0,86', ha='center', fontsize=12,
            fontweight='bold', color=VERDE)

    # Ejemplo 2: soja
    ex2 = mpatches.FancyBboxPatch((5.5, 4.2), 4, 2.8, boxstyle="round,pad=0.2",
                                   facecolor='#FEE2E2', edgecolor=ROJO, linewidth=1.5)
    ax.add_patch(ex2)
    ax.text(7.5, 6.5, 'SOJA', ha='center', fontsize=12, fontweight='bold', color=ROJO)
    ax.text(7.5, 5.9, 'X = 100,  M = 0', ha='center', fontsize=10, color=GRIS)
    ax.text(7.5, 5.3, '|100 - 0| / (100 + 0)', ha='center', fontsize=10, color=GRIS)
    ax.text(7.5, 4.7, 'GL = 1 - 100/100 = 0', ha='center', fontsize=12,
            fontweight='bold', color=ROJO)

    # Escala de interpretacion
    ax.annotate('', xy=(9.5, 2.5), xytext=(0.5, 2.5),
                arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))
    # Gradiente de color en la barra
    for i in range(50):
        x_pos = 0.5 + i * 9/50
        ratio = i / 50
        r = int(231 * (1 - ratio) + 39 * ratio)  # VERDE=#27AE60
        g = int(76 * (1 - ratio) + 174 * ratio)
        b = int(60 * (1 - ratio) + 96 * ratio)
        ax.plot([x_pos, x_pos + 9/50], [2.3, 2.3], color=f'#{r:02x}{g:02x}{b:02x}',
                linewidth=8, solid_capstyle='butt')

    ax.text(0.5, 1.7, 'GL = 0', ha='center', fontsize=10, fontweight='bold', color=ROJO)
    ax.text(0.5, 1.1, 'Puro\ninterindustrial', ha='center', fontsize=8, color=GRIS)
    ax.text(5, 1.7, 'GL = 0,5', ha='center', fontsize=10, fontweight='bold', color=GRIS)
    ax.text(5, 1.1, 'Mixto', ha='center', fontsize=8, color=GRIS)
    ax.text(9.5, 1.7, 'GL = 1', ha='center', fontsize=10, fontweight='bold', color=VERDE)
    ax.text(9.5, 1.1, 'Puro\nintraindustrial', ha='center', fontsize=8, color=GRIS)

    # Panel derecho: barras por sector
    ax2 = axes[1]
    sectores = ['Soja', 'Minerales', 'Quimicos', 'Maquinaria', 'Autopartes', 'Autos']
    gl_vals = [0.02, 0.15, 0.45, 0.52, 0.68, 0.86]
    colores = [ROJO if v < 0.3 else (NARANJA if v < 0.5 else VERDE) for v in gl_vals]

    bars = ax2.barh(sectores, gl_vals, color=colores, edgecolor='white', height=0.6)
    for bar, val in zip(bars, gl_vals):
        ax2.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2,
                 f'{val:.2f}', va='center', fontsize=10, fontweight='bold', color=AZUL_OSCURO)

    ax2.set_xlim(0, 1.05)
    ax2.set_xlabel('Indice Grubel-Lloyd', fontsize=11)
    ax2.set_title('GL por sector (ejemplo ilustrativo)', fontsize=13,
                  fontweight='bold', color=AZUL_OSCURO)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    ax2.axvline(x=0.5, color=GRIS, linestyle='--', alpha=0.5)

    fig.suptitle('Indice de Grubel-Lloyd: midiendo el comercio intraindustrial',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT / 'grubel_lloyd_ejemplo.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK grubel_lloyd_ejemplo.png')


# ============================================================
# 10. IIT COMPARADO POR REGION (NUEVO)
# ============================================================
def grafico_iit_comparado():
    fig, ax = plt.subplots(figsize=(10, 5.5))

    regiones = ['UE\ninterna', 'EEUU-\nCanada', 'Triada\n(intra)', 'Mercosur\n(global)',
                'Mercosur\nautos', 'Norte-\nSur']
    gl_values = [0.65, 0.55, 0.50, 0.35, 0.75, 0.20]
    colores = [AZUL_MEDIO, AZUL_MEDIO, CELESTE, NARANJA, VERDE, ROJO]

    bars = ax.bar(regiones, gl_values, color=colores, edgecolor='white', width=0.65)

    for bar, val in zip(bars, gl_values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.2f}', ha='center', fontsize=11, fontweight='bold', color=AZUL_OSCURO)

    ax.set_ylabel('Indice Grubel-Lloyd promedio', fontsize=12)
    ax.set_title('Comercio intraindustrial por region/bloque',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO)
    ax.set_ylim(0, 0.95)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Linea de referencia
    ax.axhline(y=0.5, color=GRIS, linestyle='--', alpha=0.5, linewidth=1)
    ax.text(5.5, 0.52, 'GL = 0.50 (mitad IIT)', fontsize=9, color=GRIS, style='italic')

    # Anotaciones
    ax.annotate('Economias similares\n+ alta integracion\n= alto IIT',
                xy=(0, 0.65), xytext=(0.5, 0.85),
                fontsize=9, color=AZUL_OSCURO, ha='center',
                arrowprops=dict(arrowstyle='->', color=AZUL_MEDIO, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#DBEAFE', edgecolor=AZUL_MEDIO, alpha=0.8))

    ax.annotate('Caso Mercosur\nautos: GL alto\npor regimen PAM',
                xy=(4, 0.75), xytext=(4.5, 0.88),
                fontsize=9, color=VERDE, ha='center',
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#D4EDDA', edgecolor=VERDE, alpha=0.8))

    fig.text(0.5, -0.02, 'Fuentes: Brulhart (2009), Lucangeli (2007), OECD. Valores aproximados.',
             ha='center', fontsize=9, color=GRIS, style='italic')

    fig.savefig(OUT / 'iit_comparado.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK iit_comparado.png')


# ============================================================
# 11. MERCOSUR AUTOS (NUEVO)
# ============================================================
def grafico_mercosur_autos():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # Panel izquierdo: comercio bilateral automotriz
    ax = axes[0]
    anios = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    # Datos aproximados en miles de millones de USD
    exp_arg_bra = [4.8, 3.5, 5.2, 4.5, 3.8, 2.1, 4.2, 5.0, 4.5]  # ARG -> BRA
    exp_bra_arg = [5.5, 4.0, 5.8, 4.8, 3.2, 1.8, 3.8, 5.5, 5.0]  # BRA -> ARG

    ax.plot(anios, exp_arg_bra, 'o-', color=CELESTE, linewidth=2, markersize=6,
            label='Argentina -> Brasil')
    ax.plot(anios, exp_bra_arg, 's-', color=NARANJA, linewidth=2, markersize=6,
            label='Brasil -> Argentina')

    # Sombrear area de solapamiento
    lower = [min(a, b) for a, b in zip(exp_arg_bra, exp_bra_arg)]
    ax.fill_between(anios, 0, lower, alpha=0.15, color=VERDE, label='Solapamiento (IIT)')

    ax.set_xlabel('Ano', fontsize=11)
    ax.set_ylabel('Miles de millones de USD', fontsize=11)
    ax.set_title('Comercio automotriz bilateral', fontsize=13, fontweight='bold', color=AZUL_OSCURO)
    ax.legend(fontsize=9, loc='upper left')
    ax.set_ylim(0, 7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Anotacion COVID
    ax.annotate('COVID-19', xy=(2020, 2.1), xytext=(2020.5, 0.8),
                fontsize=9, color=ROJO, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))

    # Panel derecho: especializacion
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Especializacion por variedades', fontsize=13, fontweight='bold', color=AZUL_OSCURO)

    # Argentina
    arg_box = mpatches.FancyBboxPatch((0.5, 5.5), 4, 3.5, boxstyle="round,pad=0.3",
                                       facecolor='#DBEAFE', edgecolor=CELESTE, linewidth=2)
    ax2.add_patch(arg_box)
    ax2.text(2.5, 8.5, 'ARGENTINA', ha='center', fontsize=13, fontweight='bold', color=CELESTE)
    ax2.text(2.5, 7.6, 'Pickups y utilitarios:', ha='center', fontsize=10, color=GRIS)
    ax2.text(2.5, 7.0, 'Toyota Hilux', ha='center', fontsize=10, color=AZUL_OSCURO, fontweight='bold')
    ax2.text(2.5, 6.5, 'VW Amarok', ha='center', fontsize=10, color=AZUL_OSCURO, fontweight='bold')
    ax2.text(2.5, 6.0, 'Ford Ranger', ha='center', fontsize=10, color=AZUL_OSCURO, fontweight='bold')

    # Brasil
    bra_box = mpatches.FancyBboxPatch((5.5, 5.5), 4, 3.5, boxstyle="round,pad=0.3",
                                       facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=2)
    ax2.add_patch(bra_box)
    ax2.text(7.5, 8.5, 'BRASIL', ha='center', fontsize=13, fontweight='bold', color=NARANJA)
    ax2.text(7.5, 7.6, 'Sedanes y SUVs:', ha='center', fontsize=10, color=GRIS)
    ax2.text(7.5, 7.0, 'VW Polo/Virtus', ha='center', fontsize=10, color=NARANJA, fontweight='bold')
    ax2.text(7.5, 6.5, 'Fiat Cronos/Argo', ha='center', fontsize=10, color=NARANJA, fontweight='bold')
    ax2.text(7.5, 6.0, 'Chevrolet Tracker', ha='center', fontsize=10, color=NARANJA, fontweight='bold')

    # Flechas
    ax2.annotate('', xy=(5.3, 7.5), xytext=(4.7, 7.5),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
    ax2.annotate('', xy=(4.7, 6.5), xytext=(5.3, 6.5),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))

    # Caja de GL
    gl_box = mpatches.FancyBboxPatch((2, 2.5), 6, 2.2, boxstyle="round,pad=0.3",
                                      facecolor='#D4EDDA', edgecolor=VERDE, linewidth=2)
    ax2.add_patch(gl_box)
    ax2.text(5, 4.0, 'GL sector automotriz ~ 0,75', ha='center', fontsize=14,
             fontweight='bold', color=VERDE)
    ax2.text(5, 3.2, 'Regimen PAM: comercio administrado\ncon coeficiente flex (compensacion)',
             ha='center', fontsize=10, color=GRIS)

    # Clave
    ax2.text(5, 1.5, 'No es ventaja comparativa: es especializacion\nen variedades con escala ampliada',
             ha='center', fontsize=10, color=AZUL_OSCURO, fontweight='bold', style='italic')

    fig.suptitle('Caso Mercosur autos: Krugman en accion',
                 fontsize=15, fontweight='bold', color=AZUL_OSCURO, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT / 'mercosur_autos.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK mercosur_autos.png')


# ============================================================
# 12. FUERZAS CENTRIPETAS VS CENTRIFUGAS (NUEVO)
# ============================================================
def grafico_centripetas_centrifugas():
    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Titulo
    ax.set_title('Fuerzas centripetas vs centrifugas en la NGE',
                 fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=15)

    # Centro: ciudad/polo
    centro = mpatches.Circle((6, 4.5), 1.2, facecolor=AZUL_MEDIO, edgecolor=AZUL_OSCURO,
                              linewidth=2.5, alpha=0.4)
    ax.add_patch(centro)
    ax.text(6, 4.5, 'POLO\nINDUSTRIAL', ha='center', va='center', fontsize=11,
            fontweight='bold', color=AZUL_OSCURO)

    # Fuerzas centripetas (flechas hacia adentro) - lado izquierdo
    centripetas = [
        (1.5, 7.5, 'Tamano de\nmercado', '(forward linkage)'),
        (1.5, 5.5, 'Proveedores\nespecializados', '(backward linkage)'),
        (1.5, 3.5, 'Pool de\ntrabajadores', '(thick labor market)'),
        (1.5, 1.5, 'Derrames de\nconocimiento', '(knowledge spillovers)'),
    ]

    for x, y, label, sub in centripetas:
        # Caja
        box = mpatches.FancyBboxPatch((x - 0.8, y - 0.6), 2.2, 1.2, boxstyle="round,pad=0.15",
                                       facecolor='#DBEAFE', edgecolor=AZUL_MEDIO, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + 0.3, y + 0.15, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color=AZUL_OSCURO)
        ax.text(x + 0.3, y - 0.4, sub, ha='center', va='center', fontsize=7, color=GRIS,
                style='italic')
        # Flecha hacia el centro
        ax.annotate('', xy=(4.8, 4.5), xytext=(2.9, y),
                    arrowprops=dict(arrowstyle='->', color=AZUL_MEDIO, lw=1.8,
                                    connectionstyle='arc3,rad=0.15'))

    # Fuerzas centrifugas (flechas hacia afuera) - lado derecho
    centrifugas = [
        (10.5, 7.5, 'Factores\ninmoviles', '(tierra, recursos)'),
        (10.5, 5.5, 'Renta del\nsuelo', '(costo de ubicacion)'),
        (10.5, 3.5, 'Congestion', '(transporte, ambiente)'),
        (10.5, 1.5, 'Competencia\nmas intensa', '(margenes bajos)'),
    ]

    for x, y, label, sub in centrifugas:
        box = mpatches.FancyBboxPatch((x - 1.4, y - 0.6), 2.2, 1.2, boxstyle="round,pad=0.15",
                                       facecolor='#FEE2E2', edgecolor=ROJO, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x - 0.3, y + 0.15, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color=ROJO)
        ax.text(x - 0.3, y - 0.4, sub, ha='center', va='center', fontsize=7, color=GRIS,
                style='italic')
        # Flecha desde el centro hacia afuera
        ax.annotate('', xy=(9.0, y), xytext=(7.2, 4.5),
                    arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.8,
                                    connectionstyle='arc3,rad=-0.15'))

    # Labels laterales
    ax.text(1.6, 8.6, 'CENTRIPETAS', ha='center', fontsize=13, fontweight='bold',
            color=AZUL_MEDIO)
    ax.text(1.6, 8.1, '(hacia la concentracion)', ha='center', fontsize=9,
            color=AZUL_MEDIO, style='italic')
    ax.text(10.4, 8.6, 'CENTRIFUGAS', ha='center', fontsize=13, fontweight='bold',
            color=ROJO)
    ax.text(10.4, 8.1, '(hacia la dispersion)', ha='center', fontsize=9,
            color=ROJO, style='italic')

    # Nota inferior
    fig.text(0.5, -0.01, 'El balance entre estas fuerzas determina la estructura espacial de la economia',
             ha='center', fontsize=10, color=VERDE, fontweight='bold', style='italic')

    fig.savefig(OUT / 'centripetas_centrifugas.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK centripetas_centrifugas.png')


# ============================================================
# 13. BIFURCACION NGE - MODELO CENTRO-PERIFERIA (NUEVO)
# ============================================================
def grafico_bifurcacion_nge():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Eje X: costos de transporte (tau) - de alto a bajo (izq a der)
    # Eje Y: participacion de la manufactura en Region 1

    tau = np.linspace(0.1, 2.5, 200)

    # Equilibrio simetrico (inestable en zona de bifurcacion)
    eq_simetrico = np.full_like(tau, 0.5)

    # Punto de bifurcacion
    tau_break = 1.2

    # Rama estable superior (centro en Region 1)
    mask_low = tau < tau_break
    rama_sup = np.where(mask_low, 0.5 + 0.5 * (1 - tau/tau_break)**0.7, np.nan)

    # Rama estable inferior (centro en Region 2)
    rama_inf = np.where(mask_low, 0.5 - 0.5 * (1 - tau/tau_break)**0.7, np.nan)

    # Rama simetrica estable (tau alto)
    mask_high = tau >= tau_break
    rama_sim_estable = np.where(mask_high, 0.5, np.nan)

    # Rama simetrica inestable (tau bajo)
    rama_sim_inestable = np.where(mask_low, 0.5, np.nan)

    # Dibujar
    ax.plot(tau[mask_high], rama_sim_estable[mask_high], color=AZUL_MEDIO, linewidth=3,
            label='Equilibrio estable')
    ax.plot(tau[mask_low], rama_sim_inestable[mask_low], color=GRIS, linewidth=2,
            linestyle='--', label='Equilibrio inestable')
    ax.plot(tau[mask_low], rama_sup[mask_low], color=VERDE, linewidth=3)
    ax.plot(tau[mask_low], rama_inf[mask_low], color=VERDE, linewidth=3)

    # Punto de bifurcacion
    ax.plot(tau_break, 0.5, 'o', color=ROJO, markersize=12, zorder=5)
    ax.annotate('Punto de\nbifurcacion', xy=(tau_break, 0.5), xytext=(tau_break + 0.35, 0.65),
                fontsize=10, fontweight='bold', color=ROJO,
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))

    # Zonas sombreadas
    ax.axvspan(0.1, tau_break, alpha=0.05, color=NARANJA)
    ax.axvspan(tau_break, 2.5, alpha=0.05, color=AZUL_MEDIO)

    # Labels de zonas
    ax.text(0.65, 0.05, 'CONCENTRACION\n(centro-periferia)', ha='center', fontsize=10,
            fontweight='bold', color=NARANJA, style='italic')
    ax.text(1.85, 0.05, 'DISPERSION\n(simetria)', ha='center', fontsize=10,
            fontweight='bold', color=AZUL_MEDIO, style='italic')

    # Anotaciones en las ramas
    ax.annotate('Region 1 = centro\n(toda la manufactura)', xy=(0.3, 0.95),
                fontsize=9, color=VERDE, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#D4EDDA', edgecolor=VERDE, alpha=0.8))
    ax.annotate('Region 1 = periferia\n(solo agricultura)', xy=(0.3, 0.08),
                fontsize=9, color=VERDE, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#D4EDDA', edgecolor=VERDE, alpha=0.8))
    ax.annotate('50-50\n(reparto igual)', xy=(1.85, 0.52), xytext=(2.0, 0.72),
                fontsize=9, color=AZUL_MEDIO,
                arrowprops=dict(arrowstyle='->', color=AZUL_MEDIO, lw=1))

    ax.set_xlabel('Costos de transporte (altos <- -> bajos)', fontsize=12)
    ax.set_ylabel('Participacion manufactura en Region 1', fontsize=12)
    ax.set_title('Modelo centro-periferia de Krugman (1991): diagrama de bifurcacion',
                 fontsize=13, fontweight='bold', color=AZUL_OSCURO)
    ax.set_xlim(0.1, 2.5)
    ax.set_ylim(-0.05, 1.05)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(['0%', '25%', '50%', '75%', '100%'])

    # Invertir eje X (tau alto a la izquierda = mas costos)
    ax.invert_xaxis()

    ax.legend(loc='center right', fontsize=9, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.5, -0.03, 'La globalizacion (baja de costos de transporte) puede AUMENTAR la concentracion territorial',
             ha='center', fontsize=10, color=ROJO, fontweight='bold', style='italic')

    fig.savefig(OUT / 'bifurcacion_nge.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print('OK bifurcacion_nge.png')


# ============================================================
# GENERAR TODOS
# ============================================================
if __name__ == '__main__':
    print('Generando graficos para Clase 7 (version expandida)...\n')

    # Originales (6)
    grafico_costo_medio()
    grafico_internas_externas()
    grafico_comercio_intraindustrial()
    grafico_mecanismo_krugman()
    grafico_ganancias_comercio()
    grafico_centro_periferia()

    # Nuevos (7)
    grafico_triada_comercio()
    grafico_tabla_teorias()
    grafico_grubel_lloyd_ejemplo()
    grafico_iit_comparado()
    grafico_mercosur_autos()
    grafico_centripetas_centrifugas()
    grafico_bifurcacion_nge()

    print(f'\nOK Todos los graficos generados en {OUT}')
