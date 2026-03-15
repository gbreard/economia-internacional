"""
Genera PNGs progresivos para Clase 4 (ex Clase 7): 7 gráficos → 21 PNGs
Cada gráfico mantiene el mismo layout base y solo AGREGA elementos paso a paso.
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
AZUL_MEDIO  = '#2E75B6'
CELESTE     = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#4B5563'
GRIS_CLARO  = '#E5E7EB'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Arial', 'Helvetica'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
})


# ============================================================
# 1. MECANISMO KRUGMAN (4 pasos)
# ============================================================
def prog_mecanismo_krugman():
    steps_data = [
        ('1', 'Preferencia\npor variedad', 'Consumidores\nquieren elegir', CELESTE),
        ('2', 'Costos fijos\npor variedad', 'Cada variedad\ncuesta F (I+D,\ndiseno...)', NARANJA),
        ('3', 'Necesidad\nde escala', 'Producir mucho\npara amortizar F\n-> baja CMe', AZUL_MEDIO),
        ('4', 'Comercio\nagranda mercado', 'Mas variedades\n+ menores costos\n= IIT', VERDE),
    ]

    for paso in range(1, 5):
        fig, ax = plt.subplots(figsize=(11, 5))
        ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis('off')
        ax.set_title('El mecanismo Krugman en 4 pasos', fontsize=15,
                     fontweight='bold', color=AZUL_OSCURO, pad=15)

        box_w, gap, start_x, box_h, y_start = 2.3, 0.5, 0.5, 3.5, 1.2

        for i, (num, title, desc, color) in enumerate(steps_data):
            x = start_x + i * (box_w + gap)

            if i < paso:
                box = mpatches.FancyBboxPatch((x, y_start), box_w, box_h,
                    boxstyle="round,pad=0.3", facecolor=color, edgecolor=color,
                    alpha=0.15, linewidth=2)
                ax.add_patch(box)
                bdr = mpatches.FancyBboxPatch((x, y_start), box_w, box_h,
                    boxstyle="round,pad=0.3", facecolor='none', edgecolor=color, linewidth=2)
                ax.add_patch(bdr)
                circ = mpatches.Circle((x+0.35, y_start+box_h-0.4), 0.25,
                    facecolor=color, edgecolor='white', linewidth=1.5, zorder=5)
                ax.add_patch(circ)
                ax.text(x+0.35, y_start+box_h-0.4, num, ha='center', va='center',
                        fontsize=12, fontweight='bold', color='white', zorder=6)
                ax.text(x+box_w/2, y_start+box_h-0.9, title, ha='center', va='center',
                        fontsize=11, fontweight='bold', color=color)
                ax.text(x+box_w/2, y_start+1.0, desc, ha='center', va='center',
                        fontsize=9, color=GRIS, linespacing=1.3)
            else:
                box = mpatches.FancyBboxPatch((x, y_start), box_w, box_h,
                    boxstyle="round,pad=0.3", facecolor=GRIS_CLARO, edgecolor=GRIS_CLARO,
                    alpha=0.3, linewidth=1)
                ax.add_patch(box)
                ax.text(x+box_w/2, y_start+box_h/2, '?', ha='center', va='center',
                        fontsize=24, color=GRIS, alpha=0.3)

            if i < 3 and i < paso - 1:
                ax.annotate('', xy=(x+box_w+0.1, y_start+box_h/2),
                            xytext=(x+box_w+gap-0.1, y_start+box_h/2),
                            arrowprops=dict(arrowstyle='<-', color=GRIS, lw=2))

        if paso == 4:
            rb = mpatches.FancyBboxPatch((1.5, 0.1), 9, 0.8, boxstyle="round,pad=0.2",
                facecolor='#D4EDDA', edgecolor=VERDE, linewidth=2)
            ax.add_patch(rb)
            ax.text(6, 0.5, 'Resultado: Comercio = mas mercado -> mas escala + mas variedad',
                    ha='center', va='center', fontsize=12, fontweight='bold', color=VERDE)

        fig.savefig(OUT / f'mecanismo_krugman_paso{paso}.png', dpi=150,
                    bbox_inches='tight', facecolor='white')
        plt.close()
        print(f'  OK mecanismo_krugman_paso{paso}.png')


# ============================================================
# 2. CENTRIPETAS VS CENTRIFUGAS (2 pasos)
# ============================================================
def prog_centripetas_centrifugas():
    centripetas = [
        (1.5, 7.5, 'Tamano de\nmercado', '(forward linkage)'),
        (1.5, 5.5, 'Proveedores\nespecializados', '(backward linkage)'),
        (1.5, 3.5, 'Pool de\ntrabajadores', '(thick labor market)'),
        (1.5, 1.5, 'Derrames de\nconocimiento', '(knowledge spillovers)'),
    ]
    centrifugas = [
        (10.5, 7.5, 'Factores\ninmoviles', '(tierra, recursos)'),
        (10.5, 5.5, 'Renta del\nsuelo', '(costo de ubicacion)'),
        (10.5, 3.5, 'Congestion', '(transporte, ambiente)'),
        (10.5, 1.5, 'Competencia\nmas intensa', '(margenes bajos)'),
    ]

    for paso in range(1, 3):
        fig, ax = plt.subplots(figsize=(11, 8))
        ax.set_xlim(0, 12); ax.set_ylim(-0.8, 9.5); ax.axis('off')
        ax.set_title('Fuerzas centripetas vs centrifugas en la NGE',
                     fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=15)

        # Centro — siempre
        centro = mpatches.Circle((6, 4.5), 1.2, facecolor=AZUL_MEDIO,
                                  edgecolor=AZUL_OSCURO, linewidth=2.5, alpha=0.4)
        ax.add_patch(centro)
        ax.text(6, 4.5, 'POLO\nINDUSTRIAL', ha='center', va='center',
                fontsize=11, fontweight='bold', color=AZUL_OSCURO)

        # Centrípetas — siempre
        for x, y, label, sub in centripetas:
            box = mpatches.FancyBboxPatch((x-0.8, y-0.6), 2.2, 1.2,
                boxstyle="round,pad=0.15", facecolor='#DBEAFE',
                edgecolor=AZUL_MEDIO, linewidth=1.5)
            ax.add_patch(box)
            ax.text(x+0.3, y+0.15, label, ha='center', va='center',
                    fontsize=9, fontweight='bold', color=AZUL_OSCURO)
            ax.text(x+0.3, y-0.4, sub, ha='center', va='center',
                    fontsize=7, color=GRIS, style='italic')
            ax.annotate('', xy=(4.8, 4.5), xytext=(2.9, y),
                arrowprops=dict(arrowstyle='->', color=AZUL_MEDIO, lw=1.8,
                                connectionstyle='arc3,rad=0.15'))

        ax.text(1.6, 8.6, 'CENTRIPETAS', ha='center', fontsize=13,
                fontweight='bold', color=AZUL_MEDIO)
        ax.text(1.6, 8.1, '(hacia la concentracion)', ha='center',
                fontsize=9, color=AZUL_MEDIO, style='italic')

        # Reservar espacio para centrífugas (invisible en paso 1)
        alpha_cf = 1.0 if paso >= 2 else 0.0
        for x, y, label, sub in centrifugas:
            box = mpatches.FancyBboxPatch((x-1.4, y-0.6), 2.2, 1.2,
                boxstyle="round,pad=0.15", facecolor='#FEE2E2',
                edgecolor=ROJO, linewidth=1.5, alpha=alpha_cf)
            ax.add_patch(box)
            ax.text(x-0.3, y+0.15, label, ha='center', va='center',
                    fontsize=9, fontweight='bold', color=ROJO, alpha=alpha_cf)
            ax.text(x-0.3, y-0.4, sub, ha='center', va='center',
                    fontsize=7, color=GRIS, style='italic', alpha=alpha_cf)
            ax.annotate('', xy=(9.0, y), xytext=(7.2, 4.5),
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.8,
                                connectionstyle='arc3,rad=-0.15', alpha=alpha_cf),
                alpha=alpha_cf)

        ax.text(10.4, 8.6, 'CENTRIFUGAS', ha='center', fontsize=13,
                fontweight='bold', color=ROJO, alpha=alpha_cf)
        ax.text(10.4, 8.1, '(hacia la dispersion)', ha='center',
                fontsize=9, color=ROJO, style='italic', alpha=alpha_cf)

        # Texto inferior — siempre reservar espacio
        footer_alpha = 1.0 if paso >= 2 else 0.0
        ax.text(6, -0.5,
            'El balance entre estas fuerzas determina la estructura espacial de la economia',
            ha='center', fontsize=10, color=VERDE, fontweight='bold', style='italic',
            alpha=footer_alpha)

        fig.savefig(OUT / f'centripetas_centrifugas_paso{paso}.png', dpi=150,
                    bbox_inches='tight', facecolor='white')
        plt.close()
        print(f'  OK centripetas_centrifugas_paso{paso}.png')


# ============================================================
# 3. BIFURCACION NGE (3 pasos)
# ============================================================
def prog_bifurcacion_nge():
    tau = np.linspace(0.1, 2.5, 200)
    tau_break = 1.2
    mask_low  = tau < tau_break
    mask_high = tau >= tau_break
    rama_sup = np.where(mask_low, 0.5 + 0.5*(1 - tau/tau_break)**0.7, np.nan)
    rama_inf = np.where(mask_low, 0.5 - 0.5*(1 - tau/tau_break)**0.7, np.nan)

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_title('Modelo centro-periferia de Krugman (1991): diagrama de bifurcacion',
                     fontsize=13, fontweight='bold', color=AZUL_OSCURO)
        ax.set_xlabel('Costos de transporte (altos <- -> bajos)', fontsize=12)
        ax.set_ylabel('Participacion manufactura en Region 1', fontsize=12)
        ax.set_xlim(0.1, 2.5); ax.set_ylim(-0.05, 1.05)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.set_yticklabels(['0%', '25%', '50%', '75%', '100%'])
        ax.invert_xaxis()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Paso 1: dispersión
        ax.axvspan(tau_break, 2.5, alpha=0.05, color=AZUL_MEDIO)
        ax.plot(tau[mask_high], np.full(mask_high.sum(), 0.5), color=AZUL_MEDIO,
                linewidth=3, label='Equilibrio estable')
        ax.text(1.85, 0.05, 'DISPERSION\n(simetria)', ha='center', fontsize=10,
                fontweight='bold', color=AZUL_MEDIO, style='italic')
        ax.annotate('50-50\n(reparto igual)', xy=(1.85, 0.52), xytext=(2.0, 0.72),
                    fontsize=9, color=AZUL_MEDIO,
                    arrowprops=dict(arrowstyle='->', color=AZUL_MEDIO, lw=1))

        # Paso 2+: bifurcación + equilibrio inestable
        if paso >= 2:
            ax.plot(tau[mask_low], np.full(mask_low.sum(), 0.5), color=GRIS,
                    linewidth=2, linestyle='--', label='Equilibrio inestable')
            ax.plot(tau_break, 0.5, 'o', color=ROJO, markersize=12, zorder=5)
            ax.annotate('Punto de\nbifurcacion', xy=(tau_break, 0.5),
                        xytext=(tau_break+0.35, 0.65), fontsize=10, fontweight='bold',
                        color=ROJO, arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))

        # Paso 3+: ramas concentración + anotaciones
        # Always render annotations to reserve space (alpha=0 when hidden)
        a3 = 1.0 if paso >= 3 else 0.0
        if paso >= 3:
            ax.axvspan(0.1, tau_break, alpha=0.05, color=NARANJA)
            ax.plot(tau[mask_low], rama_sup[mask_low], color=VERDE, linewidth=3)
            ax.plot(tau[mask_low], rama_inf[mask_low], color=VERDE, linewidth=3)
            ax.text(0.65, 0.05, 'CONCENTRACION\n(centro-periferia)', ha='center',
                    fontsize=10, fontweight='bold', color=NARANJA, style='italic')
        # These bbox annotations extend the canvas — render invisible in early pasos
        ann1 = ax.annotate('Region 1 = centro\n(toda la manufactura)', xy=(0.3, 0.95),
            fontsize=9, color=VERDE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#D4EDDA',
                      edgecolor=VERDE, alpha=0.8 * a3))
        ann1.set_alpha(a3)
        ann2 = ax.annotate('Region 1 = periferia\n(solo agricultura)', xy=(0.3, 0.08),
            fontsize=9, color=VERDE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#D4EDDA',
                      edgecolor=VERDE, alpha=0.8 * a3))
        ann2.set_alpha(a3)

        # Texto inferior — siempre reservar espacio (invisible en pasos 1-2)
        footer_alpha = 1.0 if paso >= 3 else 0.0
        fig.text(0.5, 0.01,
            'La globalizacion (baja de costos de transporte) puede AUMENTAR la concentracion territorial',
            ha='center', fontsize=10, color=ROJO, fontweight='bold', style='italic',
            alpha=footer_alpha)

        ax.legend(loc='center right', fontsize=9, framealpha=0.9)
        fig.savefig(OUT / f'bifurcacion_nge_paso{paso}.png', dpi=150,
                    bbox_inches='tight', facecolor='white')
        plt.close()
        print(f'  OK bifurcacion_nge_paso{paso}.png')


# ============================================================
# 4. GANANCIAS DEL COMERCIO (3 pasos)
# ============================================================
def prog_ganancias_comercio():
    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(10, 5.5))
        ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis('off')
        ax.set_title('Dos ganancias del comercio en Krugman', fontsize=15,
                     fontweight='bold', color=AZUL_OSCURO, pad=15)

        # Variedad — siempre
        b1 = mpatches.FancyBboxPatch((0.5, 3), 4, 3.5, boxstyle="round,pad=0.3",
            facecolor='#EBF5FB', edgecolor=CELESTE, linewidth=2)
        ax.add_patch(b1)
        ax.text(2.5, 6.0, 'Ganancia por', ha='center', fontsize=12, color=CELESTE)
        ax.text(2.5, 5.4, 'VARIEDAD', ha='center', fontsize=16,
                fontweight='bold', color=CELESTE)
        ax.text(2.5, 4.6, 'Mas opciones de\nconsumo e insumos', ha='center',
                fontsize=11, color=GRIS)
        ax.text(2.5, 3.5, 'Modelos, calidades,\nmarcas, disenos', ha='center',
                fontsize=10, color=GRIS, style='italic')

        if paso >= 2:
            b2 = mpatches.FancyBboxPatch((5.5, 3), 4, 3.5, boxstyle="round,pad=0.3",
                facecolor='#FEF3C7', edgecolor=NARANJA, linewidth=2)
            ax.add_patch(b2)
            ax.text(7.5, 6.0, 'Ganancia por', ha='center', fontsize=12, color=NARANJA)
            ax.text(7.5, 5.4, 'ESCALA', ha='center', fontsize=16,
                    fontweight='bold', color=NARANJA)
            ax.text(7.5, 4.6, 'Cada firma produce mas\n-> CMe baja -> precios bajan',
                    ha='center', fontsize=11, color=GRIS)
            ax.text(7.5, 3.5, 'Aunque haya mark-up,\nel costo base es menor',
                    ha='center', fontsize=10, color=GRIS, style='italic')

        if paso >= 3:
            ax.annotate('', xy=(5, 2.2), xytext=(2.5, 2.8),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
            ax.annotate('', xy=(5, 2.2), xytext=(7.5, 2.8),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
            res = mpatches.FancyBboxPatch((2.5, 1), 5, 1.2, boxstyle="round,pad=0.3",
                facecolor='#D4EDDA', edgecolor=VERDE, linewidth=2)
            ax.add_patch(res)
            ax.text(5, 1.6, 'BIENESTAR SUBE', ha='center', fontsize=14,
                    fontweight='bold', color=VERDE)
            ax.text(5, 1.15, '(en promedio -- pero con reasignacion)', ha='center',
                    fontsize=10, color=GRIS, style='italic')
            ax.text(5, 0.3,
                'vs. Ricardo/H-O: ganancia por "mejor asignacion"  |  Krugman: escala + variedad',
                ha='center', fontsize=9, color=AZUL_OSCURO, style='italic')

        fig.savefig(OUT / f'ganancias_comercio_paso{paso}.png', dpi=150,
                    bbox_inches='tight', facecolor='white')
        plt.close()
        print(f'  OK ganancias_comercio_paso{paso}.png')


# ============================================================
# 5. TABLA TEORIAS (4 pasos — columna por columna)
# ============================================================
def prog_tabla_teorias():
    headers = ['', 'Smith\n(1776)', 'Ricardo\n(1817)', 'H-O\n(1930s)', 'Krugman\n(1979)']
    rows = [
        ['Motor del\ncomercio', 'Ventaja\nabsoluta', 'Ventaja\ncomparativa',
         'Dotacion de\nfactores', 'Rendimientos\ncrecientes'],
        ['Tipo de\ncomercio', 'Interindustrial', 'Interindustrial',
         'Interindustrial\n(N-S)', 'Intraindustrial\n(N-N)'],
        ['Estructura\nde mercado', 'Competencia\nperfecta', 'Competencia\nperfecta',
         'Competencia\nperfecta', 'Competencia\nmonopolistica'],
        ['Rendimientos', 'Constantes', 'Constantes', 'Constantes',
         'Crecientes\n(internos)'],
        ['Ganancias', 'Especializacion', 'Mejor\nasignacion',
         'Mejor asignacion\n+ efecto dist.', 'Variedad\n+ escala'],
        ['Ejemplo\ntipico', 'Vino vs pano', 'Vino vs pano\n(ambos ganan)',
         'Soja (ARG) vs\nautos (ALE)', 'VW (ALE) vs\nPeugeot (FRA)'],
    ]
    col_widths = [0.13, 0.18, 0.18, 0.22, 0.22]
    x_positions = [0.03]
    for w in col_widths[:-1]:
        x_positions.append(x_positions[-1] + w)
    row_h = 0.12
    y_start = 0.88

    for paso in range(1, 5):
        active_cols = paso
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.axis('off')
        ax.set_title('Comparacion de teorias del comercio internacional',
                     fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=20)

        # Headers
        hy = y_start + 0.02
        for j, (hdr, xp, cw) in enumerate(zip(headers, x_positions, col_widths)):
            bg = GRIS if j == 0 else (AZUL_OSCURO if j <= active_cols else GRIS_CLARO)
            tc = 'white' if j <= active_cols else GRIS
            ta = 1.0 if j <= active_cols else 0.3
            rect = mpatches.FancyBboxPatch((xp, hy), cw-0.005, row_h+0.02,
                boxstyle="round,pad=0.005", facecolor=bg, edgecolor='white',
                linewidth=1, zorder=5, transform=ax.transAxes)
            ax.add_patch(rect)
            ax.text(xp+cw/2, hy+(row_h+0.02)/2, hdr, ha='center', va='center',
                    fontsize=9, fontweight='bold', color=tc, transform=ax.transAxes,
                    zorder=6, alpha=ta)

        # Data rows
        for i, row in enumerate(rows):
            y = y_start - i * (row_h + 0.005)
            for j, (cell, xp, cw) in enumerate(zip(row, x_positions, col_widths)):
                if j == 0:
                    bg, fc, fw = '#F0F4F8', AZUL_OSCURO, 'bold'
                elif j <= active_cols:
                    if j == active_cols:
                        bg, fc = '#EBF5FB', AZUL_MEDIO
                    else:
                        bg = 'white' if i % 2 == 0 else '#F9FAFB'
                        fc = GRIS
                    fw = 'normal'
                else:
                    bg, fc, fw = '#F9FAFB', GRIS, 'normal'

                alpha_bg = 1.0 if j <= active_cols else 0.4
                rect = mpatches.FancyBboxPatch((xp, y-row_h), cw-0.005, row_h,
                    boxstyle="round,pad=0.003", facecolor=bg, edgecolor=GRIS_CLARO,
                    linewidth=0.5, transform=ax.transAxes, alpha=alpha_bg)
                ax.add_patch(rect)
                if j <= active_cols:
                    ax.text(xp+cw/2, y-row_h/2, cell, ha='center', va='center',
                            fontsize=8, color=fc, fontweight=fw,
                            transform=ax.transAxes, linespacing=1.2)

        if paso == 4:
            fig.text(0.5, 0.01,
                'Las teorias se complementan: cada una explica un aspecto distinto del comercio real',
                ha='center', fontsize=10, color=VERDE, fontweight='bold', style='italic')

        fig.savefig(OUT / f'tabla_teorias_paso{paso}.png', dpi=150,
                    bbox_inches='tight', facecolor='white')
        plt.close()
        print(f'  OK tabla_teorias_paso{paso}.png')


# ============================================================
# 6. CENTRO-PERIFERIA (3 pasos)
# ============================================================
def prog_centro_periferia():
    periferias = [(1.5, 6.5, 0.6), (8.5, 6.5, 0.6), (1.2, 2, 0.5),
                  (8.8, 2, 0.5), (5, 0.8, 0.5)]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis('off')
        ax.set_title('Nueva Geografia Economica: centro-periferia', fontsize=15,
                     fontweight='bold', color=AZUL_OSCURO, pad=15)

        # Centro — siempre
        c1 = mpatches.Circle((5, 4.5), 1.8, facecolor=AZUL_MEDIO,
                              edgecolor=AZUL_OSCURO, linewidth=2.5, alpha=0.3)
        ax.add_patch(c1)
        c2 = mpatches.Circle((5, 4.5), 1.2, facecolor=AZUL_MEDIO,
                              edgecolor=AZUL_OSCURO, linewidth=1.5, alpha=0.5)
        ax.add_patch(c2)
        ax.text(5, 4.8, 'CENTRO', ha='center', va='center', fontsize=14,
                fontweight='bold', color=AZUL_OSCURO)
        ax.text(5, 4.1, 'Industria\nServicios\nInnovacion', ha='center',
                va='center', fontsize=9, color=AZUL_OSCURO)

        if paso >= 2:
            for x, y, r in periferias:
                p = mpatches.Circle((x, y), r, facecolor=GRIS_CLARO,
                                     edgecolor=GRIS, linewidth=1.5, alpha=0.7)
                ax.add_patch(p)
                ax.text(x, y, 'P', ha='center', va='center', fontsize=10,
                        color=GRIS, fontweight='bold')
            for x, y, _ in periferias:
                dx, dy = 5 - x, 4.5 - y
                f = 0.55
                ax.annotate('', xy=(x+dx*f, y+dy*f), xytext=(x+dx*0.15, y+dy*0.15),
                    arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5,
                                    connectionstyle='arc3,rad=0.1'))
            ax.text(1.5, 1.0, 'Periferia:\nmenos industria,\nmenos servicios',
                    ha='center', fontsize=9, color=GRIS, style='italic')

        if paso >= 3:
            ax.text(5, 7.5, 'Causacion acumulativa', ha='center', fontsize=12,
                    fontweight='bold', color=VERDE)
            ax.text(5, 6.95, 'Mas produccion -> mas empleo/mercado -> mas proveedores',
                    ha='center', fontsize=9, color=VERDE, style='italic')
            ax.text(5, 6.55, '-> menores costos -> +produccion',
                    ha='center', fontsize=9, color=VERDE, style='italic')
            ax.text(8.5, 1.0, 'Path dependence:\nla historia\nimporta',
                    ha='center', fontsize=9, color=NARANJA, style='italic')

        fig.savefig(OUT / f'centro_periferia_paso{paso}.png', dpi=150,
                    bbox_inches='tight', facecolor='white')
        plt.close()
        print(f'  OK centro_periferia_paso{paso}.png')


# ============================================================
# 7. TRIADA COMERCIO (2 pasos)
# ============================================================
def prog_triada_comercio():
    bloques = ['UE\n(intra+extra)', 'EEUU', 'Japon', 'Resto\ndel mundo']
    pct_1995 = [39, 15, 11, 35]
    pct_2020 = [33, 10, 4, 53]
    x_pos = np.arange(len(bloques))
    w = 0.35

    for paso in range(1, 3):
        fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
        ax = axes[0]

        # Panel izq: participación — siempre
        bars1 = ax.bar(x_pos-w/2, pct_1995, w, color=AZUL_MEDIO, label='1995', edgecolor='white')
        bars2 = ax.bar(x_pos+w/2, pct_2020, w, color=CELESTE, label='2020', edgecolor='white', alpha=0.8)
        for bar in bars1:
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.8,
                    f'{int(bar.get_height())}%', ha='center', fontsize=9,
                    fontweight='bold', color=AZUL_OSCURO)
        for bar in bars2:
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.8,
                    f'{int(bar.get_height())}%', ha='center', fontsize=9,
                    color=CELESTE, fontweight='bold')
        ax.set_xticks(x_pos); ax.set_xticklabels(bloques, fontsize=10)
        ax.set_ylabel('% de exportaciones mundiales', fontsize=11)
        ax.set_title('Participacion en comercio mundial', fontsize=13,
                     fontweight='bold', color=AZUL_OSCURO)
        ax.set_ylim(0, 58); ax.legend(fontsize=10)
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
        ax.annotate('Triada: 65% en 1995\n47% en 2020', xy=(1, 42), fontsize=10,
                    color=ROJO, fontweight='bold', ha='center',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEE2E2',
                              edgecolor=ROJO, alpha=0.8))

        ax2 = axes[1]
        if paso == 1:
            ax2.axis('off')
            ax2.text(0.5, 0.5, '?', ha='center', va='center', fontsize=50,
                     color=GRIS_CLARO, transform=ax2.transAxes, alpha=0.4)
            ax2.text(0.5, 0.35, 'Y la mayor parte\nes intraindustrial...',
                     ha='center', va='center', fontsize=12, color=GRIS,
                     transform=ax2.transAxes, style='italic')
        else:
            pares = ['UE\ninterna', 'EEUU-\nCanada', 'EEUU-\nUE', 'Japon-\nUE', 'Norte-\nSur']
            gl_vals = [0.65, 0.55, 0.50, 0.45, 0.20]
            colors = [AZUL_MEDIO]*4 + [NARANJA]
            bars = ax2.barh(pares, gl_vals, color=colors, edgecolor='white', height=0.6)
            for bar, val in zip(bars, gl_vals):
                ax2.text(bar.get_width()+0.02, bar.get_y()+bar.get_height()/2,
                         f'{val:.2f}', va='center', fontsize=10, fontweight='bold',
                         color=AZUL_OSCURO)
            ax2.set_xlim(0, 0.85)
            ax2.set_xlabel('Indice Grubel-Lloyd promedio', fontsize=11)
            ax2.set_title('IIT entre miembros de la triada', fontsize=13,
                          fontweight='bold', color=AZUL_OSCURO)
            ax2.spines['top'].set_visible(False); ax2.spines['right'].set_visible(False)
            ax2.axvline(x=0.50, color=GRIS, linestyle='--', alpha=0.5)
            ax2.text(0.51, -0.6, 'GL = 0.50\n(mitad IIT)', fontsize=8,
                     color=GRIS, style='italic')

        fig.suptitle('La triada: comercio masivo entre economias similares',
                     fontsize=15, fontweight='bold', color=AZUL_OSCURO, y=1.02)
        fig.tight_layout()
        fig.savefig(OUT / f'triada_comercio_paso{paso}.png', dpi=150,
                    bbox_inches='tight', facecolor='white')
        plt.close()
        print(f'  OK triada_comercio_paso{paso}.png')


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print('Generando PNGs progresivos para Clase 4...\n')

    print('1/7 mecanismo_krugman (4 pasos)')
    prog_mecanismo_krugman()

    print('2/7 centripetas_centrifugas (2 pasos)')
    prog_centripetas_centrifugas()

    print('3/7 bifurcacion_nge (3 pasos)')
    prog_bifurcacion_nge()

    print('4/7 ganancias_comercio (3 pasos)')
    prog_ganancias_comercio()

    print('5/7 tabla_teorias (4 pasos)')
    prog_tabla_teorias()

    print('6/7 centro_periferia (3 pasos)')
    prog_centro_periferia()

    print('7/7 triada_comercio (2 pasos)')
    prog_triada_comercio()

    total = 4 + 2 + 3 + 3 + 4 + 3 + 2
    print(f'\nOK {total} PNGs progresivos generados en {OUT}')
