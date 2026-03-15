"""
Genera PNGs progresivos para graficos dinamicos de la Clase 3.
Cada grafico se genera en N pasos: base_paso1.png, base_paso2.png, etc.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent.parent / "graficos"
OUT.mkdir(exist_ok=True)

# Paleta
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#4B5563'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Arial', 'Helvetica'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.grid': False,
})

def limpiar_ejes(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def estilo_ho(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')
    ax.tick_params(colors=GRIS, labelsize=9)


# ============================================================
# 1. PPF recta vs curva (Slide 9) - 2 pasos
# ============================================================
def ppf_recta_vs_curva(paso):
    if paso == 1:
        fig, ax1 = plt.subplots(1, 1, figsize=(7, 5.5))
    else:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Panel Ricardo (siempre)
    x1 = np.array([0, 100])
    y1 = np.array([80, 0])
    ax1.plot(x1, y1, color=AZUL_OSCURO, linewidth=2.5)
    ax1.fill_between(x1, y1, alpha=0.08, color=AZUL_OSCURO)
    ax1.plot(100, 0, 'o', color=ROJO, markersize=10, zorder=5)
    ax1.annotate('Especializacion\ntotal en Tela', xy=(100, 0), xytext=(60, 25),
                fontsize=9, color=ROJO, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))
    ax1.annotate('Costo de oportunidad\nconstante = 0,8 A/T',
                xy=(50, 40), xytext=(10, 55),
                fontsize=9, color=GRIS, style='italic',
                arrowprops=dict(arrowstyle='->', color=GRIS, lw=1))
    ax1.set_xlim(-5, 115)
    ax1.set_ylim(-5, 95)
    ax1.set_xlabel('Tela', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
    ax1.set_title('Ricardo: 1 factor (trabajo)', fontsize=13, fontweight='bold',
                 color=AZUL_OSCURO, pad=12)
    limpiar_ejes(ax1)

    if paso == 2:
        theta = np.linspace(0, np.pi/2, 100)
        x2 = 100 * np.cos(theta)**0.7
        y2 = 80 * np.sin(theta)**0.7
        ax2.plot(x2, y2, color=NARANJA, linewidth=2.5)
        ax2.fill_between(x2, y2, alpha=0.08, color=NARANJA)
        idx = 45
        ax2.plot(x2[idx], y2[idx], 'o', color=ROJO, markersize=10, zorder=5)
        ax2.annotate('Especializacion\nparcial', xy=(x2[idx], y2[idx]),
                    xytext=(x2[idx]-30, y2[idx]+15),
                    fontsize=9, color=ROJO, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))
        dx = x2[idx+1] - x2[idx-1]
        dy = y2[idx+1] - y2[idx-1]
        slope = dy / dx
        x_tang = np.linspace(x2[idx]-20, x2[idx]+20, 2)
        y_tang = y2[idx] + slope * (x_tang - x2[idx])
        ax2.plot(x_tang, y_tang, '--', color=GRIS, linewidth=1.2, alpha=0.7)
        ax2.annotate('Costo de oportunidad\ncreciente', xy=(25, 20),
                    fontsize=9, color=GRIS, style='italic')
        ax2.set_xlim(-5, 115)
        ax2.set_ylim(-5, 95)
        ax2.set_xlabel('Tela', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
        ax2.set_title('Neoclasico: 2+ factores (L + K)', fontsize=13, fontweight='bold',
                     color=NARANJA, pad=12)
        limpiar_ejes(ax2)

    suptitle = 'PPF con un solo factor: Modelo de Ricardo' if paso == 1 else 'Frontera de Posibilidades de Produccion'
    fig.suptitle(suptitle, fontsize=15, fontweight='bold', color=AZUL_OSCURO, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.93])
    fig.savefig(OUT / f'ppf_recta_vs_curva_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  + ppf_recta_vs_curva_paso{paso}.png")


# ============================================================
# 2. Dos paises en autarquia (Slide 13) - 2 pasos
# ============================================================
def dos_paises_autarquia(paso):
    theta = np.linspace(0, np.pi/2, 200)

    if paso == 1:
        fig, ax1 = plt.subplots(1, 1, figsize=(7, 5.5))
    else:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Pais A (siempre)
    x_a = 100 * np.cos(theta)**0.55
    y_a = 60 * np.sin(theta)**0.85
    ax1.plot(x_a, y_a, color=AZUL_OSCURO, linewidth=2.5, zorder=3)
    ax1.fill_between(x_a, y_a, alpha=0.05, color=AZUL_OSCURO)
    idx_a = 65
    xa, ya = x_a[idx_a], y_a[idx_a]
    ax1.plot(xa, ya, 'o', color=ROJO, markersize=10, zorder=5)
    ax1.text(xa+2, ya+3, 'E_A', fontsize=12, fontweight='bold', color=ROJO)
    ka = xa * ya
    t_ci = np.linspace(20, 95, 200)
    y_ci_a = ka / t_ci
    mask_a = (y_ci_a > 5) & (y_ci_a < 58)
    ax1.plot(t_ci[mask_a], y_ci_a[mask_a], color=VERDE, linewidth=1.5, zorder=2)
    dx = x_a[idx_a+1] - x_a[idx_a-1]
    dy = y_a[idx_a+1] - y_a[idx_a-1]
    slope_a = dy / dx
    x_pa = np.linspace(xa-28, xa+28, 2)
    y_pa = ya + slope_a * (x_pa - xa)
    ax1.plot(x_pa, y_pa, '--', color=NARANJA, linewidth=2, zorder=4)
    ax1.text(xa+22, ya + slope_a*22 - 5, f'Pt/Pa bajo\n(tela barata)',
            fontsize=9, color=NARANJA, fontweight='bold', ha='center')
    ax1.set_xlim(-5, 115)
    ax1.set_ylim(-5, 70)
    ax1.set_xlabel('Tela', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
    ax1.set_title('Pais A: abundante en Capital (K)',
                 fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)
    limpiar_ejes(ax1)
    ax1.text(5, 65, 'K/L alto\n-> PPF sesgada\nhacia Tela',
            fontsize=9, color=AZUL_OSCURO, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#DBEAFE',
                     edgecolor=AZUL_MEDIO, alpha=0.9))

    if paso == 2:
        x_b = 60 * np.cos(theta)**0.85
        y_b = 100 * np.sin(theta)**0.55
        ax2.plot(x_b, y_b, color=NARANJA, linewidth=2.5, zorder=3)
        ax2.fill_between(x_b, y_b, alpha=0.05, color=NARANJA)
        idx_b = 65
        xb, yb = x_b[idx_b], y_b[idx_b]
        ax2.plot(xb, yb, 'o', color=ROJO, markersize=10, zorder=5)
        ax2.text(xb+2, yb+3, 'E_B', fontsize=12, fontweight='bold', color=ROJO)
        kb = xb * yb
        t_ci2 = np.linspace(10, 58, 200)
        y_ci_b = kb / t_ci2
        mask_b = (y_ci_b > 10) & (y_ci_b < 95)
        ax2.plot(t_ci2[mask_b], y_ci_b[mask_b], color=VERDE, linewidth=1.5, zorder=2)
        dx2 = x_b[idx_b+1] - x_b[idx_b-1]
        dy2 = y_b[idx_b+1] - y_b[idx_b-1]
        slope_b = dy2 / dx2
        x_pb = np.linspace(xb-18, xb+18, 2)
        y_pb = yb + slope_b * (x_pb - xb)
        ax2.plot(x_pb, y_pb, '--', color=AZUL_MEDIO, linewidth=2, zorder=4)
        ax2.text(xb-5, yb + slope_b*(-5) + 5, f'Pt/Pa alto\n(tela cara)',
                fontsize=9, color=AZUL_MEDIO, fontweight='bold', ha='center')
        ax2.set_xlim(-5, 75)
        ax2.set_ylim(-5, 120)
        ax2.set_xlabel('Tela', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
        ax2.set_title('Pais B: abundante en Trabajo (L)',
                     fontsize=13, fontweight='bold', color=NARANJA, pad=12)
        limpiar_ejes(ax2)
        ax2.text(35, 112, 'L/K alto\n-> PPF sesgada\nhacia Alimentos',
                fontsize=9, color=NARANJA, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEF3C7',
                         edgecolor=NARANJA, alpha=0.9))
        fig.text(0.5, 0.03, '<- Pt/Pa difiere -> base para el comercio ->',
                ha='center', fontsize=11, color=ROJO, fontweight='bold')

    suptitle = ('Pais A: dotaciones y precio en autarquia' if paso == 1
                else 'Distintas dotaciones -> distintos precios en autarquia')
    fig.suptitle(suptitle, fontsize=14, fontweight='bold', color=AZUL_OSCURO, y=0.99)
    plt.tight_layout(rect=[0, 0.06 if paso == 2 else 0.02, 1, 0.94])
    fig.savefig(OUT / f'dos_paises_autarquia_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  + dos_paises_autarquia_paso{paso}.png")


# ============================================================
# 3. Comercio con PPF curva (Slide 16) - 3 pasos
# ============================================================
def comercio_ppf_curva(paso):
    fig, ax = plt.subplots(figsize=(9, 7))

    theta = np.linspace(0, np.pi/2, 200)
    x_ppf = 100 * np.cos(theta)**0.7
    y_ppf = 80 * np.sin(theta)**0.7
    ax.plot(x_ppf, y_ppf, color=AZUL_OSCURO, linewidth=2.5, label='PPF', zorder=3)
    ax.fill_between(x_ppf, y_ppf, alpha=0.05, color=AZUL_OSCURO)

    # E (autarquia) - siempre
    idx_e = 75
    xe, ye = x_ppf[idx_e], y_ppf[idx_e]
    e_color = GRIS if paso > 1 else ROJO
    ax.plot(xe, ye, 'o', color=e_color, markersize=10, zorder=5)
    ax.text(xe+3, ye+4, 'E (autarquia)', fontsize=9, fontweight='bold', color=e_color)

    # CI U1 - siempre
    k1 = xe * ye
    t_ci = np.linspace(18, 100, 200)
    y_ci1 = k1 / t_ci
    mask1 = (y_ci1 > 5) & (y_ci1 < 78)
    ax.plot(t_ci[mask1], y_ci1[mask1], color=GRIS, linewidth=1.5, alpha=0.5, zorder=2)
    ax.text(97, k1/97 - 2, 'U\u2081', fontsize=10, color=GRIS, alpha=0.6)

    # Q y slope (needed for pasos 2-3)
    idx_q = 55
    xq, yq = x_ppf[idx_q], y_ppf[idx_q]
    dx_p = x_ppf[idx_q+1] - x_ppf[idx_q-1]
    dy_p = y_ppf[idx_q+1] - y_ppf[idx_q-1]
    slope = dy_p / dx_p

    if paso >= 2:
        ax.plot(xq, yq, 's', color=AZUL_MEDIO, markersize=11, zorder=5)
        ax.text(xq+3, yq-7, 'Q (produccion)', fontsize=9, fontweight='bold', color=AZUL_MEDIO)
        x_price = np.linspace(xq-30, xq+30, 2)
        y_price = yq + slope * (x_price - xq)
        ax.plot(x_price, y_price, '--', color=NARANJA, linewidth=2, zorder=4,
               label='Linea de precios mundiales')

    if paso >= 3:
        xc = xq - 18
        yc = yq + slope * (xc - xq)
        ax.plot(xc, yc, 'D', color=ROJO, markersize=11, zorder=5)
        ax.text(xc-12, yc-3, 'C (consumo)', fontsize=9, fontweight='bold', color=ROJO)

        k2 = xc * yc
        y_ci2 = k2 / t_ci
        mask2 = (y_ci2 > 8) & (y_ci2 < 82)
        ax.plot(t_ci[mask2], y_ci2[mask2], color=VERDE, linewidth=2, zorder=2)
        ax.text(97, k2/97 - 2, 'U\u2082', fontsize=10, color=VERDE, fontweight='bold')

        mid_y_exp = min(yc, yq) - 3
        ax.annotate('', xy=(xq, mid_y_exp), xytext=(xc, mid_y_exp),
                   arrowprops=dict(arrowstyle='<->', color=AZUL_CLARO, lw=2.5))
        ax.text((xq + xc)/2, mid_y_exp - 5, 'Exporta Tela', fontsize=9, ha='center',
               color=AZUL_CLARO, fontweight='bold')

        mid_x_imp = xc - 3
        ax.annotate('', xy=(mid_x_imp, yc), xytext=(mid_x_imp, yq),
                   arrowprops=dict(arrowstyle='<->', color=VERDE, lw=2.5))
        ax.text(mid_x_imp - 10, (yq + yc)/2, 'Importa\nAlim.', fontsize=9, ha='center',
               color=VERDE, fontweight='bold')

        ax.text(10, 75, 'Consume FUERA\nde la PPF!\nU\u2082 > U\u2081 -> mayor\nbienestar',
               fontsize=9, color=VERDE, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='#D1FAE5',
                        edgecolor=VERDE, alpha=0.9))

    ax.set_xlim(-5, 110)
    ax.set_ylim(-5, 90)
    ax.set_xlabel('Tela', fontsize=12, fontweight='bold')
    ax.set_ylabel('Alimentos', fontsize=12, fontweight='bold')

    titles = {
        1: 'Equilibrio de autarquia: produccion = consumo',
        2: 'Apertura: ajuste de produccion al precio mundial',
        3: 'Ganancias del comercio: consumir fuera de la PPF'
    }
    ax.set_title(titles[paso], fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.legend(loc='lower left', fontsize=9, framealpha=0.9)
    limpiar_ejes(ax)

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.savefig(OUT / f'comercio_ppf_curva_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  + comercio_ppf_curva_paso{paso}.png")


# ============================================================
# 4. Dotaciones PPF (Slide 23) - 2 pasos
# ============================================================
def dotaciones_ppf(paso):
    t = np.linspace(0, 1, 200)

    if paso == 1:
        fig, ax1 = plt.subplots(1, 1, figsize=(7, 5.5))
    else:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Pais A (siempre)
    xa = 100 * (1 - t**1.8)
    ya = 65 * t**0.8
    ax1.plot(xa, ya, color=AZUL_OSCURO, linewidth=2.5)
    ax1.fill_between(xa, ya, alpha=0.08, color=AZUL_MEDIO)
    idx_a = 80
    ax1.plot(xa[idx_a], ya[idx_a], 'o', color=NARANJA, markersize=10, zorder=5)
    ax1.annotate('$E^A$ (autarquia)', xy=(xa[idx_a], ya[idx_a]),
                 xytext=(xa[idx_a]-25, ya[idx_a]+8), fontsize=10, color=NARANJA,
                 arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5))
    ax1.plot([85, 20], [10, 55], '--', color=ROJO, linewidth=1.5, alpha=0.7)
    ax1.text(22, 57, '$P_X/P_Y$ bajo\n(X barato)', fontsize=9, color=ROJO, ha='left')
    ax1.set_title('Pais A (K-abundante)', fontsize=14, fontweight='bold',
                 color=AZUL_OSCURO, pad=12)
    ax1.set_xlabel('Bien X (K-intensivo)', fontsize=11, color=GRIS)
    ax1.set_ylabel('Bien Y (L-intensivo)', fontsize=11, color=GRIS)
    estilo_ho(ax1)
    ax1.set_xlim(-5, 110)
    ax1.set_ylim(-5, 75)
    ax1.text(60, 65, 'K/L alto\n-> X relativamente\n   barato', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#EBF5FB',
                      edgecolor=AZUL_MEDIO), ha='center', va='top')

    if paso == 2:
        xb = 60 * (1 - t**0.8)
        yb = 100 * t**1.8
        ax2.plot(xb, yb, color=VERDE, linewidth=2.5)
        ax2.fill_between(xb, yb, alpha=0.08, color=VERDE)
        idx_b = 120
        ax2.plot(xb[idx_b], yb[idx_b], 'o', color=NARANJA, markersize=10, zorder=5)
        ax2.annotate('$E^B$ (autarquia)', xy=(xb[idx_b], yb[idx_b]),
                     xytext=(xb[idx_b]+5, yb[idx_b]-12), fontsize=10, color=NARANJA,
                     arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5))
        ax2.plot([50, 10], [20, 80], '--', color=ROJO, linewidth=1.5, alpha=0.7)
        ax2.text(12, 83, '$P_X/P_Y$ alto\n(X caro)', fontsize=9, color=ROJO, ha='left')
        ax2.set_title('Pais B (L-abundante)', fontsize=14, fontweight='bold',
                     color=AZUL_OSCURO, pad=12)
        ax2.set_xlabel('Bien X (K-intensivo)', fontsize=11, color=GRIS)
        ax2.set_ylabel('Bien Y (L-intensivo)', fontsize=11, color=GRIS)
        estilo_ho(ax2)
        ax2.set_xlim(-5, 70)
        ax2.set_ylim(-5, 110)
        ax2.text(40, 100, 'K/L bajo\n-> Y relativamente\n   barato', fontsize=9,
                 bbox=dict(boxstyle='round,pad=0.4', facecolor='#EAFAF1',
                          edgecolor=VERDE), ha='center', va='top')

    suptitle = ('Pais A: dotaciones y precios en autarquia' if paso == 1
                else 'Dotaciones y precios relativos en autarquia')
    fig.suptitle(suptitle, fontsize=15, fontweight='bold', color=AZUL_OSCURO, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.93])
    fig.text(0.5, 0.01, 'Fuente: Elaboracion propia', ha='center', fontsize=8, color=GRIS)
    fig.savefig(OUT / f'dotaciones_ppf_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  + dotaciones_ppf_paso{paso}.png")


# ============================================================
# 5. Precio mundial H-O (Slide 24) - 3 pasos
# ============================================================
def precio_mundial_ho(paso):
    fig, ax = plt.subplots(figsize=(12, 5))

    y_line = 0.5
    ax.plot([0, 10], [y_line, y_line], '-', color='#cccccc', linewidth=2, zorder=1)

    pa, pw, pb = 2.0, 5.0, 8.0

    # Paso 1: solo PA
    ax.plot(pa, y_line, 'o', color=AZUL_OSCURO, markersize=18, zorder=5)
    ax.text(pa, y_line + 0.15, '$(P_X/P_Y)^A$', fontsize=13, ha='center',
            fontweight='bold', color=AZUL_OSCURO)
    ax.text(pa, y_line - 0.15, 'Bajo\n(X barato en A)', fontsize=9, ha='center',
            color=AZUL_OSCURO, va='top')

    if paso >= 2:
        ax.plot(pb, y_line, 'o', color=VERDE, markersize=18, zorder=5)
        ax.text(pb, y_line + 0.15, '$(P_X/P_Y)^B$', fontsize=13, ha='center',
                fontweight='bold', color=VERDE)
        ax.text(pb, y_line - 0.15, 'Alto\n(X caro en B)', fontsize=9, ha='center',
                color=VERDE, va='top')

    if paso >= 3:
        ax.plot(pw, y_line, 's', color=NARANJA, markersize=18, zorder=5)
        ax.text(pw, y_line + 0.15, '$P^W$', fontsize=14, ha='center',
                fontweight='bold', color=NARANJA)
        ax.text(pw, y_line - 0.15, 'Precio\nmundial', fontsize=9, ha='center',
                color=NARANJA, va='top')

        ax.annotate('', xy=(pw - 0.3, y_line - 0.45), xytext=(pa + 0.3, y_line - 0.45),
                    arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=2))
        ax.text((pa + pw) / 2, y_line - 0.55, 'A: sube $P_X/P_Y$\n-> exporta X',
                fontsize=10, ha='center', color=AZUL_OSCURO, fontweight='bold')
        ax.annotate('', xy=(pw + 0.3, y_line - 0.45), xytext=(pb - 0.3, y_line - 0.45),
                    arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
        ax.text((pb + pw) / 2, y_line - 0.55, 'B: baja $P_X/P_Y$\n-> exporta Y',
                fontsize=10, ha='center', color=VERDE, fontweight='bold')

    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.8 if paso >= 3 else -0.2, 1.0)
    ax.axis('off')

    titles = {
        1: 'Precio de autarquia: Pais A (K-abundante)',
        2: 'Precios de autarquia: base para el comercio',
        3: 'Apertura comercial: precio mundial entre precios de autarquia'
    }
    ax.set_title(titles[paso], fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=15)

    fig.text(0.5, 0.02, 'Fuente: Elaboracion propia', ha='center', fontsize=8, color=GRIS)
    fig.savefig(OUT / f'precio_mundial_ho_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  + precio_mundial_ho_paso{paso}.png")


# ============================================================
# 6. Stolper-Samuelson cadena (Slide 27) - 4 pasos
# ============================================================
def stolper_samuelson_cadena(paso):
    fig, ax = plt.subplots(figsize=(13, 6))

    all_boxes = [
        ('$\\uparrow P_X/P_Y$\n(precio relativo)', 1.0),
        ('Sector X\nse expande', 3.0),
        ('$\\uparrow$ demanda\nde K', 5.0),
        ('$\\uparrow$ r (retorno\nal capital)', 7.0),
        ('$\\downarrow$ w (salario\nreal)', 9.0),
    ]

    n_boxes_map = {1: 1, 2: 2, 3: 3, 4: 5}
    n_show = n_boxes_map[paso]

    box_w = 1.6
    box_h = 0.7
    y_center = 0.5

    for i, (label, x) in enumerate(all_boxes[:n_show]):
        color = AZUL_OSCURO if x < 7 else (VERDE if x == 7 else ROJO)
        facecolor = '#EBF5FB' if x < 7 else ('#EAFAF1' if x == 7 else '#FDEDEC')
        rect = mpatches.FancyBboxPatch((x - box_w/2, y_center - box_h/2), box_w, box_h,
                                        boxstyle='round,pad=0.1', facecolor=facecolor,
                                        edgecolor=color, linewidth=2, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y_center, label, fontsize=11, ha='center', va='center',
                fontweight='bold', color=color, zorder=4)

    for i in range(n_show - 1):
        x_from = all_boxes[i][1] + box_w/2 + 0.05
        x_to = all_boxes[i+1][1] - box_w/2 - 0.05
        ax.annotate('', xy=(x_to, y_center), xytext=(x_from, y_center),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=2.5))

    if paso == 4:
        ax.text(3.5, -0.3, 'Pais A (K-abundante):', fontsize=11, fontweight='bold',
                color=AZUL_OSCURO, ha='center')
        ax.text(3.5, -0.5, 'Sube $P_X$ -> Gana K / Pierde L', fontsize=10,
                color=AZUL_OSCURO, ha='center')
        ax.text(7.5, -0.3, 'Pais B (L-abundante):', fontsize=11, fontweight='bold',
                color=VERDE, ha='center')
        ax.text(7.5, -0.5, 'Baja $P_X$ -> Gana L / Pierde K', fontsize=10,
                color=VERDE, ha='center')

    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.75 if paso == 4 else -0.1, 1.3)
    ax.axis('off')

    titles = {
        1: 'Stolper-Samuelson: cambio en el precio relativo',
        2: 'Stolper-Samuelson: expansion sectorial',
        3: 'Stolper-Samuelson: demanda de factores',
        4: 'Stolper-Samuelson: cadena causal del precio al ingreso'
    }
    ax.set_title(titles[paso], fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=15)

    fig.text(0.5, 0.02, 'Fuente: Elaboracion propia', ha='center', fontsize=8, color=GRIS)
    fig.savefig(OUT / f'stolper_samuelson_cadena_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  + stolper_samuelson_cadena_paso{paso}.png")


# ============================================================
# 7. Rybczynski efecto (Slide 29) - 2 pasos
# ============================================================
def rybczynski_efecto(paso):
    if paso == 1:
        fig, ax1 = plt.subplots(1, 1, figsize=(7, 5.5))
    else:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    categorias = ['Bien X\n(K-intensivo)', 'Bien Y\n(L-intensivo)']
    antes = [50, 50]
    x_pos = np.arange(len(categorias))
    width = 0.3

    # Panel 1: aumento K (siempre)
    despues1 = [80, 35]
    ax1.bar(x_pos - width/2, antes, width, color=AZUL_MEDIO, label='Antes', alpha=0.7)
    ax1.bar(x_pos + width/2, despues1, width, color=NARANJA, label='Despues de $\\uparrow$K')
    ax1.annotate('$\\uparrow\\uparrow$', xy=(0 + width/2, 82), fontsize=16,
                fontweight='bold', color=VERDE, ha='center')
    ax1.annotate('$\\downarrow$', xy=(1 + width/2, 37), fontsize=16,
                fontweight='bold', color=ROJO, ha='center')
    ax1.set_title('Shock: $\\uparrow$ Capital (K)', fontsize=14, fontweight='bold',
                 color=AZUL_OSCURO, pad=12)
    ax1.set_ylabel('Produccion', fontsize=11, color=GRIS)
    estilo_ho(ax1)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(categorias, fontsize=10)
    ax1.set_ylim(0, 100)
    ax1.legend(fontsize=9, loc='upper right')
    ax1.text(0.5, 92, 'Mas K -> X sube mas\nque proporcionalmente,\nY cae', fontsize=9,
             ha='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEF9E7',
                                    edgecolor=NARANJA), transform=ax1.transData)

    if paso == 2:
        despues2 = [35, 80]
        ax2.bar(x_pos - width/2, antes, width, color=AZUL_MEDIO, label='Antes', alpha=0.7)
        ax2.bar(x_pos + width/2, despues2, width, color=VERDE, label='Despues de $\\uparrow$L')
        ax2.annotate('$\\downarrow$', xy=(0 + width/2, 37), fontsize=16,
                    fontweight='bold', color=ROJO, ha='center')
        ax2.annotate('$\\uparrow\\uparrow$', xy=(1 + width/2, 82), fontsize=16,
                    fontweight='bold', color=VERDE, ha='center')
        ax2.set_title('Shock: $\\uparrow$ Trabajo (L)', fontsize=14, fontweight='bold',
                     color=AZUL_OSCURO, pad=12)
        ax2.set_ylabel('Produccion', fontsize=11, color=GRIS)
        estilo_ho(ax2)
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(categorias, fontsize=10)
        ax2.set_ylim(0, 100)
        ax2.legend(fontsize=9, loc='upper right')
        ax2.text(0.5, 92, 'Mas L -> Y sube mas\nque proporcionalmente,\nX cae', fontsize=9,
                 ha='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#EAFAF1',
                                        edgecolor=VERDE), transform=ax2.transData)

    suptitle = ('Rybczynski: aumento de capital -> cambio en composicion' if paso == 1
                else 'Teorema de Rybczynski: shock de dotaciones -> cambio estructural')
    fig.suptitle(suptitle, fontsize=14, fontweight='bold', color=AZUL_OSCURO, y=0.98)
    plt.tight_layout(rect=[0, 0.04, 1, 0.93])
    fig.text(0.5, 0.01, 'Fuente: Elaboracion propia', ha='center', fontsize=8, color=GRIS)
    fig.savefig(OUT / f'rybczynski_efecto_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  + rybczynski_efecto_paso{paso}.png")


# ============================================================
# 8. Rendimientos decrecientes (Slide 10) - 2 pasos
#    Paso 1: movimiento en zona plana (costo bajo)
#    Paso 2: movimiento en zona empinada (costo alto)
# ============================================================
def rendimientos_decrecientes(paso):
    fig, ax = plt.subplots(figsize=(10, 6))

    # PPF curva (misma en ambos pasos)
    theta = np.linspace(0, np.pi/2, 200)
    x = 100 * np.cos(theta)**0.65
    y = 80 * np.sin(theta)**0.65
    ax.plot(x, y, color=AZUL_OSCURO, linewidth=2.5, zorder=3)
    ax.fill_between(x, y, alpha=0.05, color=AZUL_OSCURO)

    if paso == 1:
        # Movimiento en zona plana: poco costo de oportunidad
        i1, i2 = 20, 45
        dx1 = x[i2] - x[i1]
        dy1 = abs(y[i2] - y[i1])
        ax.plot(x[i1], y[i1], 'o', color=VERDE, markersize=10, zorder=5)
        ax.plot(x[i2], y[i2], 'o', color=VERDE, markersize=10, zorder=5)
        # Flecha horizontal: ganancia de tela
        ax.annotate('', xy=(x[i2], y[i1]), xytext=(x[i1], y[i1]),
                   arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
        # Flecha vertical: costo en alimentos
        ax.annotate('', xy=(x[i2], y[i2]), xytext=(x[i2], y[i1]),
                   arrowprops=dict(arrowstyle='->', color=VERDE, lw=2.5))
        ax.text(x[i1] + dx1/2, y[i1]+5, f'+{dx1:.0f} Tela', ha='center', fontsize=11,
               color=VERDE, fontweight='bold')
        ax.text(x[i2]+5, y[i1] - dy1/2, f'-{dy1:.0f} Alim.', ha='left', fontsize=11,
               color=VERDE, fontweight='bold')
        # Caja explicativa
        box_text = "Zona plana de la PPF\nGanar tela cuesta POCO alimento\n→ Costo de oportunidad BAJO"
        props = dict(boxstyle='round,pad=0.6', facecolor='#D1FAE5', edgecolor=VERDE, alpha=0.95)
        ax.text(55, 40, box_text, fontsize=11, bbox=props, color='#065F46',
               va='top', linespacing=1.5)
        ax.set_title('Rendimientos decrecientes: zona de bajo costo',
                    fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)

    elif paso == 2:
        # Movimiento en zona empinada: alto costo de oportunidad
        i3, i4 = 130, 155
        dx2 = abs(x[i4] - x[i3])
        dy2 = abs(y[i4] - y[i3])
        ax.plot(x[i3], y[i3], 'o', color=ROJO, markersize=10, zorder=5)
        ax.plot(x[i4], y[i4], 'o', color=ROJO, markersize=10, zorder=5)
        # Flecha horizontal: ganancia de tela
        ax.annotate('', xy=(x[i4], y[i3]), xytext=(x[i3], y[i3]),
                   arrowprops=dict(arrowstyle='->', color=ROJO, lw=2.5))
        # Flecha vertical: costo en alimentos
        ax.annotate('', xy=(x[i4], y[i4]), xytext=(x[i4], y[i3]),
                   arrowprops=dict(arrowstyle='->', color=ROJO, lw=2.5))
        ax.text(x[i3] + (x[i4]-x[i3])/2, y[i3]+5, f'+{dx2:.0f} Tela', ha='center', fontsize=11,
               color=ROJO, fontweight='bold')
        ax.text(x[i4]+3, y[i3] - dy2/2, f'-{dy2:.0f} Alim.', ha='left', fontsize=11,
               color=ROJO, fontweight='bold')
        # Caja explicativa
        box_text = "Zona empinada de la PPF\nGanar tela cuesta MUCHO alimento\n→ Costo de oportunidad ALTO"
        props = dict(boxstyle='round,pad=0.6', facecolor='#FEE2E2', edgecolor=ROJO, alpha=0.95)
        ax.text(20, 40, box_text, fontsize=11, bbox=props, color='#991B1B',
               va='top', linespacing=1.5)
        ax.set_title('Rendimientos decrecientes: zona de alto costo',
                    fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)

    ax.set_xlim(-5, 115)
    ax.set_ylim(-8, 90)
    ax.set_xlabel('Tela', fontsize=12, fontweight='bold')
    ax.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
    limpiar_ejes(ax)
    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8,
            color=GRIS, style='italic')
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.savefig(OUT / f'rendimientos_decrecientes_paso{paso}.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ rendimientos_decrecientes_paso{paso}.png")


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("Generando graficos progresivos para Clase 3...\n")

    print("1. PPF recta vs curva (2 pasos)")
    for p in range(1, 3):
        ppf_recta_vs_curva(p)

    print("\n2. Dos paises en autarquia (2 pasos)")
    for p in range(1, 3):
        dos_paises_autarquia(p)

    print("\n3. Comercio con PPF curva (3 pasos)")
    for p in range(1, 4):
        comercio_ppf_curva(p)

    print("\n4. Dotaciones PPF (2 pasos)")
    for p in range(1, 3):
        dotaciones_ppf(p)

    print("\n5. Precio mundial H-O (3 pasos)")
    for p in range(1, 4):
        precio_mundial_ho(p)

    print("\n6. Stolper-Samuelson cadena (4 pasos)")
    for p in range(1, 5):
        stolper_samuelson_cadena(p)

    print("\n7. Rybczynski efecto (2 pasos)")
    for p in range(1, 3):
        rybczynski_efecto(p)

    print("\n8. Rendimientos decrecientes (2 pasos)")
    for p in range(1, 3):
        rendimientos_decrecientes(p)

    print(f"\n20 graficos progresivos generados en {OUT}")
