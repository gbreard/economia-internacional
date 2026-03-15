"""
Genera los 7 gráficos para la Sesión 5 (U3 pt2).
Paleta: #1F4E79, #2E75B6, #0EA5E9, #E8833A, #27AE60, #E74C3C
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent.parent / "graficos"
OUT.mkdir(exist_ok=True)

# Paleta
AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
AZUL_CEL = '#0EA5E9'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'
NEGRO = '#111827'
FONDO = '#FFFFFF'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Arial', 'Helvetica'],
    'axes.facecolor': FONDO,
    'figure.facecolor': FONDO,
    'text.color': NEGRO,
})


# ============================================================
# 1. arg_bra_autos_2024.png
# ============================================================
def grafico_arg_bra():
    fig, ax = plt.subplots(figsize=(10, 5.5))

    cats = ['Exportaciones\nARG → BRA', 'Importaciones\nARG ← BRA']
    vals = [6000, 5110]
    colors = [AZUL_MED, NARANJA]

    bars = ax.barh(cats, vals, color=colors, height=0.5, edgecolor='white', linewidth=1.5)

    for bar, v in zip(bars, vals):
        ax.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2,
                f'USD {v:,.0f} M', va='center', fontsize=13, fontweight='bold', color=NEGRO)

    ax.set_xlim(0, 7800)
    ax.set_xlabel('Millones de USD', fontsize=11, color=GRIS)
    ax.set_title('Comercio bilateral ARG-BRA en vehículos (HS 87), 2024',
                 fontsize=14, fontweight='bold', color=AZUL_OSC, pad=15)

    # GL callout
    gl = 2 * min(6000, 5110) / (6000 + 5110)
    ax.text(5500, 1.35, f'GL = {gl:.2f}', fontsize=18, fontweight='bold',
            color=FONDO, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=VERDE, edgecolor='none', alpha=0.95))
    ax.text(5500, 1.08, 'IIT muy alto', fontsize=10, color=VERDE, ha='center', fontstyle='italic')

    # Diferencia
    diff = abs(6000 - 5110)
    ax.annotate(f'Diferencia neta:\nUSD {diff:,.0f} M\n(solo {diff/(6000+5110)*100:.0f}% del total)',
                xy=(5555, 0.5), fontsize=9, color=GRIS, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#F3F4F6', edgecolor=GRIS, linewidth=0.5))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(GRIS)
    ax.spines['left'].set_color(GRIS)
    ax.tick_params(colors=GRIS, labelsize=11)

    fig.tight_layout()
    fig.savefig(OUT / 'arg_bra_autos_2024.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ arg_bra_autos_2024.png")


# ============================================================
# 2. vernon_ciclo_producto.png
# ============================================================
def grafico_vernon():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_title('El ciclo del producto de Vernon (1966)',
                 fontsize=15, fontweight='bold', color=AZUL_OSC, pad=20)

    # 3 fases como cajas
    phases = [
        {'x': 0.3, 'w': 3.5, 'label': 'Fase 1\nProducto nuevo',
         'color': AZUL_CEL, 'items': [
             'Innovación e I+D',
             'Producción en país innovador',
             'Mano de obra calificada',
             'Se exporta a países ricos'
         ]},
        {'x': 4.3, 'w': 3.5, 'label': 'Fase 2\nProducto maduro',
         'color': NARANJA, 'items': [
             'Demanda crece en el exterior',
             'IED: plantas en Europa/Japón',
             'Estandarización parcial',
             'Innovador empieza a importar'
         ]},
        {'x': 8.3, 'w': 3.5, 'label': 'Fase 3\nEstandarizado',
         'color': ROJO, 'items': [
             'Producción en países de bajo costo',
             'Tecnología difundida',
             'Bien se vuelve commodity',
             'Innovador importa lo que inventó'
         ]},
    ]

    for p in phases:
        # Header
        rect = FancyBboxPatch((p['x'], 4.6), p['w'], 1.2,
                              boxstyle='round,pad=0.1', facecolor=p['color'],
                              edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(p['x'] + p['w']/2, 5.2, p['label'], ha='center', va='center',
                fontsize=12, fontweight='bold', color='white')

        # Body
        body = FancyBboxPatch((p['x'], 1.8), p['w'], 2.7,
                              boxstyle='round,pad=0.1', facecolor='#F8FAFC',
                              edgecolor=p['color'], linewidth=1.5)
        ax.add_patch(body)

        for i, item in enumerate(p['items']):
            ax.text(p['x'] + 0.25, 4.1 - i * 0.6, f'• {item}',
                    fontsize=9.5, color=NEGRO, va='center')

    # Flechas entre fases
    for x_start in [3.8, 7.8]:
        ax.annotate('', xy=(x_start + 0.5, 5.2), xytext=(x_start, 5.2),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=2.5))

    # Geo labels abajo
    geos = [
        (2.05, 'EEUU', AZUL_CEL),
        (6.05, 'Europa / Japón', NARANJA),
        (10.05, 'Países en\ndesarrollo', ROJO),
    ]
    for x, txt, col in geos:
        ax.text(x, 1.2, txt, ha='center', va='center', fontsize=10,
                fontweight='bold', color=col,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor=col, linewidth=1.5))

    # Timeline arrow
    ax.annotate('', xy=(11.5, 0.4), xytext=(0.5, 0.4),
                arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.5))
    ax.text(6, 0.1, 'Tiempo →', ha='center', fontsize=10, color=GRIS, fontstyle='italic')

    fig.tight_layout()
    fig.savefig(OUT / 'vernon_ciclo_producto.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ vernon_ciclo_producto.png")


# ============================================================
# 3. melitz_seleccion.png
# ============================================================
def grafico_melitz_seleccion():
    fig, ax = plt.subplots(figsize=(11, 5.5))

    # Distribution curve (log-normal style)
    x = np.linspace(0.01, 5, 500)
    from scipy.stats import lognorm
    y = lognorm.pdf(x, s=0.6, scale=1.2)

    ax.plot(x, y, color=AZUL_MED, lw=2.5, zorder=5)
    ax.fill_between(x, y, alpha=0.08, color=AZUL_MED, zorder=3)

    # Thresholds
    c_star = 2.2  # survival threshold
    c_export = 1.2  # export threshold

    # Fill zones
    # Zone 1: Exit (c > c*)
    mask_exit = x >= c_star
    ax.fill_between(x[mask_exit], y[mask_exit], alpha=0.35, color=ROJO, zorder=4, label='Salen del mercado')

    # Zone 2: Local only (c_export < c < c*)
    mask_local = (x >= c_export) & (x < c_star)
    ax.fill_between(x[mask_local], y[mask_local], alpha=0.25, color=NARANJA, zorder=4, label='Venden localmente')

    # Zone 3: Exporters (c < c_export)
    mask_exp = x <= c_export
    ax.fill_between(x[mask_exp], y[mask_exp], alpha=0.3, color=VERDE, zorder=4, label='Exportan')

    # Vertical lines
    ax.axvline(c_star, color=ROJO, ls='--', lw=1.8, zorder=6)
    ax.axvline(c_export, color=VERDE, ls='--', lw=1.8, zorder=6)

    # Labels for thresholds
    y_top = max(y) * 1.05
    ax.text(c_star, y_top + 0.04, '$c^*$\n(umbral\nsupervivencia)',
            ha='center', va='bottom', fontsize=10, color=ROJO, fontweight='bold')
    ax.text(c_export, y_top + 0.04, '$c^* - t$\n(umbral\nexportación)',
            ha='center', va='bottom', fontsize=10, color=VERDE, fontweight='bold')

    # Arrows pointing to zones
    ax.annotate('CIERRAN', xy=(3.2, 0.05), fontsize=11, fontweight='bold',
                color=ROJO, ha='center')
    ax.annotate('VENDEN\nLOCAL', xy=(1.7, 0.12), fontsize=10, fontweight='bold',
                color=NARANJA, ha='center')
    ax.annotate('EXPORTAN', xy=(0.6, 0.15), fontsize=11, fontweight='bold',
                color=VERDE, ha='center')

    ax.set_xlabel('Coste marginal ($c_i$)  →  más alto = menos productiva', fontsize=11, color=GRIS)
    ax.set_ylabel('Número de firmas', fontsize=11, color=GRIS)
    ax.set_title('Melitz: distribución de firmas y umbrales de selección',
                 fontsize=14, fontweight='bold', color=AZUL_OSC, pad=15)

    ax.set_xlim(0, 4.5)
    ax.set_ylim(0, y_top + 0.22)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.legend(loc='upper right', fontsize=9, framealpha=0.9)

    fig.tight_layout()
    fig.savefig(OUT / 'melitz_seleccion.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ melitz_seleccion.png")


# ============================================================
# 4. melitz_apertura.png
# ============================================================
def grafico_melitz_apertura():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), sharey=True)

    from scipy.stats import lognorm
    x = np.linspace(0.01, 5, 500)
    y = lognorm.pdf(x, s=0.6, scale=1.2)

    for idx, (ax, title) in enumerate(zip(axes, ['Antes de la apertura', 'Después de la apertura'])):
        ax.plot(x, y, color=AZUL_MED, lw=2.5, zorder=5)
        ax.fill_between(x, y, alpha=0.06, color=AZUL_MED, zorder=3)

        if idx == 0:
            c_star = 2.5
            # Only two zones: survive vs exit
            mask_survive = x < c_star
            mask_exit = x >= c_star
            ax.fill_between(x[mask_survive], y[mask_survive], alpha=0.2, color=AZUL_CEL, zorder=4)
            ax.fill_between(x[mask_exit], y[mask_exit], alpha=0.3, color=ROJO, zorder=4)
            ax.axvline(c_star, color=ROJO, ls='--', lw=1.8, zorder=6)
            ax.text(c_star, max(y)*1.02, '$c^*$', ha='center', va='bottom',
                    fontsize=12, color=ROJO, fontweight='bold')
            ax.text(1.3, 0.35, 'Todas\nvenden local', ha='center', fontsize=10,
                    color=AZUL_OSC, fontweight='bold')
            ax.text(3.3, 0.04, 'Salen', ha='center', fontsize=10,
                    color=ROJO, fontweight='bold')
        else:
            c_star_new = 2.0  # stricter threshold
            c_export = 1.0
            mask_exp = x <= c_export
            mask_local = (x > c_export) & (x < c_star_new)
            mask_exit = x >= c_star_new
            ax.fill_between(x[mask_exp], y[mask_exp], alpha=0.3, color=VERDE, zorder=4)
            ax.fill_between(x[mask_local], y[mask_local], alpha=0.2, color=NARANJA, zorder=4)
            ax.fill_between(x[mask_exit], y[mask_exit], alpha=0.3, color=ROJO, zorder=4)
            ax.axvline(c_star_new, color=ROJO, ls='--', lw=1.8, zorder=6)
            ax.axvline(c_export, color=VERDE, ls='--', lw=1.8, zorder=6)
            ax.text(c_star_new, max(y)*1.02, "$c^{*'}$", ha='center', va='bottom',
                    fontsize=12, color=ROJO, fontweight='bold')
            ax.text(c_export, max(y)*1.02, '$c^*-t$', ha='center', va='bottom',
                    fontsize=12, color=VERDE, fontweight='bold')

            ax.annotate('Exportan\n(crecen)', xy=(0.5, 0.25), fontsize=9,
                        fontweight='bold', color=VERDE, ha='center')
            ax.annotate('Local', xy=(1.5, 0.25), fontsize=9,
                        fontweight='bold', color=NARANJA, ha='center')
            ax.annotate('Salen\n(más)', xy=(3.0, 0.04), fontsize=9,
                        fontweight='bold', color=ROJO, ha='center')

            # Arrow showing threshold moved left
            ax.annotate('', xy=(c_star_new, max(y)*0.85), xytext=(2.5, max(y)*0.85),
                        arrowprops=dict(arrowstyle='->', color=ROJO, lw=2))
            ax.text(2.25, max(y)*0.78, 'Umbral\nsube', fontsize=8, color=ROJO, ha='center')

        ax.set_title(title, fontsize=12, fontweight='bold', color=AZUL_OSC, pad=10)
        ax.set_xlim(0, 4.5)
        ax.set_xlabel('Coste marginal ($c_i$)', fontsize=10, color=GRIS)
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

    fig.suptitle('Melitz: efecto de la apertura comercial sobre las firmas',
                 fontsize=14, fontweight='bold', color=AZUL_OSC, y=1.02)

    fig.tight_layout()
    fig.savefig(OUT / 'melitz_apertura.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ melitz_apertura.png")


# ============================================================
# 5. evolucion_teorias.png
# ============================================================
def grafico_evolucion_teorias():
    fig, ax = plt.subplots(figsize=(12, 6.5))
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    ax.set_title('Evolución de las teorías del comercio internacional',
                 fontsize=15, fontweight='bold', color=AZUL_OSC, pad=15, y=0.98)

    # Table structure
    cols = [
        {'x': 0.2, 'w': 3.6, 'header': 'Teoría clásica\nRicardo / H-O', 'color': AZUL_MED},
        {'x': 4.2, 'w': 3.6, 'header': 'Nueva teoría\nKrugman (1980)', 'color': NARANJA},
        {'x': 8.2, 'w': 3.6, 'header': 'Firmas heterogéneas\nMelitz (2003)', 'color': VERDE},
    ]

    rows_data = [
        ('Fuente de\ncomercio', [
            'Diferencias entre\npaíses (tecnología\no dotaciones)',
            'Economías de escala\n+ diferenciación\nde productos',
            'Diferencias de\nproductividad\nentre firmas'
        ]),
        ('Tipo de\ncomercio', [
            'Interindustrial\n(vino × tela)',
            'Intraindustrial\n(auto × auto)',
            'Intraindustrial\n+ selección de firmas'
        ]),
        ('Firmas', [
            'Idénticas\ndentro del sector',
            'Idénticas\n(simétricas)',
            'Heterogéneas\n(distintos costes)'
        ]),
        ('Predicción\nclave', [
            'Los países se\nespecializan según\nventaja comparativa',
            'Comercio entre\npaíses similares.\nMás variedades',
            'Solo las más\nproductivas exportan.\nApertura selecciona'
        ]),
    ]

    row_h = 1.35
    header_h = 1.0
    y_start = 6.5

    for col in cols:
        # Header box
        rect = FancyBboxPatch((col['x'], y_start), col['w'], header_h,
                              boxstyle='round,pad=0.08', facecolor=col['color'],
                              edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(col['x'] + col['w']/2, y_start + header_h/2, col['header'],
                ha='center', va='center', fontsize=10.5, fontweight='bold', color='white')

    for r_idx, (row_label, cells) in enumerate(rows_data):
        y = y_start - (r_idx + 1) * row_h
        # Row label
        bg = '#F1F5F9' if r_idx % 2 == 0 else '#FFFFFF'
        label_rect = FancyBboxPatch((-0.1, y), 0.3, row_h,
                                     boxstyle='square,pad=0', facecolor=bg,
                                     edgecolor='none')
        # Actually skip row labels - embed them in first approach

        for c_idx, (col, cell) in enumerate(zip(cols, cells)):
            cell_bg = '#F1F5F9' if r_idx % 2 == 0 else '#FFFFFF'
            rect = FancyBboxPatch((col['x'], y), col['w'], row_h,
                                  boxstyle='round,pad=0.05', facecolor=cell_bg,
                                  edgecolor='#E5E7EB', linewidth=0.8)
            ax.add_patch(rect)
            ax.text(col['x'] + col['w']/2, y + row_h/2, cell,
                    ha='center', va='center', fontsize=9, color=NEGRO)

    # Row labels on the left side - outside the table
    for r_idx, (row_label, _) in enumerate(rows_data):
        y = y_start - (r_idx + 1) * row_h
        ax.text(-0.05, y + row_h/2, row_label, ha='right', va='center',
                fontsize=9.5, fontweight='bold', color=GRIS)

    # Arrows between columns (at header level)
    for x_a in [3.8, 7.8]:
        ax.annotate('', xy=(x_a + 0.4, y_start + header_h/2),
                    xytext=(x_a, y_start + header_h/2),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=2))

    # Bottom note
    ax.text(6, 0.9, 'Cada teoría agrega una capa de realismo — no reemplaza a la anterior',
            ha='center', va='center', fontsize=11, fontstyle='italic', color=GRIS)

    # Source
    ax.text(6, 0.4, 'Basado en Bernard, Jensen, Redding & Schott (2007), Journal of Economic Perspectives',
            ha='center', va='center', fontsize=8.5, color=GRIS)

    fig.tight_layout()
    fig.savefig(OUT / 'evolucion_teorias.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ evolucion_teorias.png")


# ============================================================
# 6. dumping_arbol.png
# ============================================================
def grafico_dumping_arbol():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    def draw_box(x, y, w, h, text, color, fontsize=9, text_color='white', bold=True):
        rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.12',
                              facecolor=color, edgecolor='white', linewidth=1.5, zorder=5)
        ax.add_patch(rect)
        fw = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=fontsize, fontweight=fw, color=text_color, zorder=6)

    def draw_decision(x, y, w, h, text, color='#F1F5F9'):
        # Diamond shape approximation with a box
        rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.1',
                              facecolor=color, edgecolor=AZUL_OSC, linewidth=1.5, zorder=5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=8.5, color=AZUL_OSC, fontweight='bold', zorder=6)

    def arrow(x1, y1, x2, y2, label='', label_pos='mid'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.5), zorder=4)
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx, my + 0.12, label, ha='center', va='bottom',
                    fontsize=8, color=GRIS, fontstyle='italic', zorder=7)

    ax.set_title('Árbol de decisión: del síntoma al instrumento',
                 fontsize=14, fontweight='bold', color=AZUL_OSC, pad=15)

    # Start: symptom
    draw_box(3.5, 7.0, 5, 0.7, 'SÍNTOMA: Importaciones a precio bajo\n+ daño a industria local', AZUL_OSC, fontsize=10)

    # Decision 1
    draw_decision(3.5, 5.8, 5, 0.8, '¿Precio exportación < valor normal?\n(dumping)')
    arrow(6, 7.0, 6, 6.6)

    # Yes → Decision 2
    draw_decision(0.3, 4.2, 4.2, 0.8, '¿Hay daño + nexo causal?')
    arrow(3.5, 6.0, 2.4, 5.0, 'SÍ')

    # Yes → AD
    draw_box(0.5, 2.8, 3.8, 0.8, 'ANTIDUMPING (AD)\nArancel que compensa\nmargen de dumping', VERDE, fontsize=9)
    arrow(2.4, 4.2, 2.4, 3.6, 'SÍ')

    # No from Decision 2 → no action on dumping track
    draw_box(0.5, 1.3, 3.8, 0.7, 'No corresponde AD', '#94A3B8', fontsize=9)
    arrow(0.3, 4.5, 0.3, 2.0)
    ax.text(0.15, 3.25, 'NO', fontsize=8, color=GRIS, fontstyle='italic')

    # No from Decision 1 → Decision 3
    draw_decision(7.5, 4.2, 4.2, 0.8, '¿La causa es subsidio estatal\nmedible?')
    arrow(8.5, 5.8, 9.6, 5.0, 'NO')

    # Yes → CVD
    draw_box(7.7, 2.8, 3.8, 0.8, 'DERECHOS COMPENSATORIOS\n(CVD)\nNeutraliza el subsidio', NARANJA, fontsize=9)
    arrow(9.6, 4.2, 9.6, 3.6, 'SÍ')

    # No → Decision 4
    draw_box(7.7, 1.3, 3.8, 0.8, '¿Aumento súbito +\ndaño serio?', '#F1F5F9',
             fontsize=9, text_color=AZUL_OSC)
    arrow(11.7, 4.5, 11.7, 2.1)
    ax.text(11.85, 3.3, 'NO', fontsize=8, color=GRIS, fontstyle='italic')

    # Salvaguardia result
    draw_box(4.5, 0.2, 3.5, 0.7, 'SALVAGUARDIA\nRestricción temporal', AZUL_CEL, fontsize=9)
    arrow(7.7, 1.55, 8.0, 0.9)
    ax.text(7.5, 1.0, 'SÍ', fontsize=8, color=GRIS, fontstyle='italic')

    fig.tight_layout()
    fig.savefig(OUT / 'dumping_arbol.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ dumping_arbol.png")


# ============================================================
# 7. comercio_tareas.png
# ============================================================
def grafico_comercio_tareas():
    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.axis('off')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)

    ax.set_title('El enfoque de tareas: ¿quién hace cada tarea?',
                 fontsize=14, fontweight='bold', color=AZUL_OSC, pad=15)

    # Central concept: BIEN FINAL
    draw_w, draw_h = 2.8, 0.8
    cx, cy = 5.5, 7.0
    rect = FancyBboxPatch((cx - draw_w/2, cy - draw_h/2), draw_w, draw_h,
                          boxstyle='round,pad=0.12', facecolor=AZUL_OSC, edgecolor='white', linewidth=2, zorder=5)
    ax.add_patch(rect)
    ax.text(cx, cy, 'BIEN FINAL', ha='center', va='center',
            fontsize=13, fontweight='bold', color='white', zorder=6)

    # Tasks (middle row)
    tasks = ['Diseño\nI+D', 'Componentes\nfabricación', 'Ensamblaje', 'Logística\ndistribución', 'Marketing\npost-venta']
    task_colors = [AZUL_CEL, AZUL_MED, NARANJA, VERDE, '#8B5CF6']
    tw, th = 1.7, 0.8
    task_y = 4.8
    task_positions = []

    for i, (t, tc) in enumerate(zip(tasks, task_colors)):
        tx = 0.5 + i * 2.1
        task_positions.append((tx + tw/2, task_y))
        rect = FancyBboxPatch((tx, task_y), tw, th, boxstyle='round,pad=0.08',
                              facecolor=tc, edgecolor='white', linewidth=1.5, zorder=5)
        ax.add_patch(rect)
        ax.text(tx + tw/2, task_y + th/2, t, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='white', zorder=6)
        # Arrow from product to task
        ax.annotate('', xy=(tx + tw/2, task_y + th), xytext=(cx, cy - draw_h/2),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=1, alpha=0.5), zorder=3)

    # "se descompone en TAREAS" label
    ax.text(cx, 6.15, 'Se descompone en TAREAS', ha='center', va='center',
            fontsize=10, fontstyle='italic', color=GRIS)

    # Three options (bottom row)
    options = [
        {'label': 'Trabajador\nlocal', 'color': VERDE, 'icon': '🏠', 'desc': 'Empleo\ndoméstico'},
        {'label': 'Trabajador\nextranjero', 'color': NARANJA, 'icon': '🌐', 'desc': 'Offshoring'},
        {'label': 'Máquina\n/ IA', 'color': ROJO, 'icon': '🤖', 'desc': 'Automatización'},
    ]

    ow, oh = 2.5, 1.0
    opt_y = 1.2
    opt_positions = []

    for i, opt in enumerate(options):
        ox = 1.0 + i * 3.3
        opt_positions.append((ox + ow/2, opt_y + oh))
        rect = FancyBboxPatch((ox, opt_y), ow, oh, boxstyle='round,pad=0.1',
                              facecolor=opt['color'], edgecolor='white', linewidth=2, zorder=5)
        ax.add_patch(rect)
        ax.text(ox + ow/2, opt_y + oh/2 + 0.15, opt['label'], ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=6)
        ax.text(ox + ow/2, opt_y - 0.2, opt['desc'], ha='center', va='top',
                fontsize=9, color=opt['color'], fontstyle='italic')

    # "Para cada tarea" decision box
    dec_w, dec_h = 4, 0.7
    dec_x, dec_y = cx - dec_w/2, 3.0
    rect = FancyBboxPatch((dec_x, dec_y), dec_w, dec_h, boxstyle='round,pad=0.08',
                          facecolor='#F1F5F9', edgecolor=AZUL_OSC, linewidth=1.5, zorder=5)
    ax.add_patch(rect)
    ax.text(cx, dec_y + dec_h/2, '¿Quién la hace?\n(costos relativos + naturaleza de la tarea)',
            ha='center', va='center', fontsize=9, color=AZUL_OSC, fontweight='bold', zorder=6)

    # Arrows from tasks to decision
    for tx, ty in task_positions:
        ax.annotate('', xy=(cx, dec_y + dec_h), xytext=(tx, task_y),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=1, alpha=0.4), zorder=3)

    # Arrows from decision to options
    for ox_c, oy in opt_positions:
        ax.annotate('', xy=(ox_c, oy), xytext=(cx, dec_y),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.3), zorder=4)

    # Source
    ax.text(5.5, 0.15, 'Grossman & Rossi-Hansberg (2008) + Acemoglu & Autor (2011)',
            ha='center', fontsize=8.5, color=GRIS, fontstyle='italic')

    fig.tight_layout()
    fig.savefig(OUT / 'comercio_tareas.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ comercio_tareas.png")


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("Generando gráficos Sesión 5...")
    grafico_arg_bra()
    grafico_vernon()
    grafico_melitz_seleccion()
    grafico_melitz_apertura()
    grafico_evolucion_teorias()
    grafico_dumping_arbol()
    grafico_comercio_tareas()
    print(f"\n✓ 7 gráficos generados en {OUT}")
