"""
Genera los 7 gráficos para la Clase 5: El modelo neoclásico estándar
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Directorio de salida
OUT = Path(__file__).parent.parent / "graficos"
OUT.mkdir(exist_ok=True)

# Paleta de colores del proyecto
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#4B5563'
GRIS_CLARO  = '#E5E7EB'

def estilo_base():
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

estilo_base()


# ============================================================
# GRÁFICO 1: PPF recta vs PPF curva (Slide 9)
# ============================================================
def grafico_ppf_recta_vs_curva():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Panel 1: PPF Recta (Ricardo)
    x1 = np.array([0, 100])
    y1 = np.array([80, 0])
    ax1.plot(x1, y1, color=AZUL_OSCURO, linewidth=2.5)
    ax1.fill_between(x1, y1, alpha=0.08, color=AZUL_OSCURO)

    # Punto de especialización total
    ax1.plot(100, 0, 'o', color=ROJO, markersize=10, zorder=5)
    ax1.annotate('Especialización\ntotal en Tela', xy=(100, 0), xytext=(60, 25),
                fontsize=9, color=ROJO, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))

    # Costo de oportunidad constante
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
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Panel 2: PPF Curva (Neoclásico)
    theta = np.linspace(0, np.pi/2, 100)
    x2 = 100 * np.cos(theta)**0.7
    y2 = 80 * np.sin(theta)**0.7
    ax2.plot(x2, y2, color=NARANJA, linewidth=2.5)
    ax2.fill_between(x2, y2, alpha=0.08, color=NARANJA)

    # Punto de especialización parcial
    idx = 45
    ax2.plot(x2[idx], y2[idx], 'o', color=ROJO, markersize=10, zorder=5)
    ax2.annotate('Especialización\nparcial', xy=(x2[idx], y2[idx]),
                xytext=(x2[idx]-30, y2[idx]+15),
                fontsize=9, color=ROJO, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5))

    # Tangente en el punto para mostrar costo de oportunidad
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
    ax2.set_title('Neoclásico: 2+ factores (L + K)', fontsize=13, fontweight='bold',
                 color=NARANJA, pad=12)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    fig.suptitle('Frontera de Posibilidades de Producción', fontsize=15,
                fontweight='bold', color=AZUL_OSCURO, y=0.98)

    plt.tight_layout(rect=[0, 0.02, 1, 0.93])
    fig.savefig(OUT / 'ppf_recta_vs_curva.png', dpi=150, bbox_inches='tight',
               facecolor='white')
    plt.close()
    print("  ✓ ppf_recta_vs_curva.png")


# ============================================================
# GRÁFICO 2: Rendimientos decrecientes (Slide 10)
# ============================================================
def grafico_rendimientos_decrecientes():
    fig, ax = plt.subplots(figsize=(10, 6))

    # PPF curva principal
    theta = np.linspace(0, np.pi/2, 200)
    x = 100 * np.cos(theta)**0.65
    y = 80 * np.sin(theta)**0.65
    ax.plot(x, y, color=AZUL_OSCURO, linewidth=2.5, zorder=3)
    ax.fill_between(x, y, alpha=0.05, color=AZUL_OSCURO)

    # Tres puntos para mostrar costo creciente
    indices = [30, 80, 150]
    labels_y = ['Ceder 5A', 'Ceder 10A', 'Ceder 20A']
    colors = [VERDE, NARANJA, ROJO]
    arrow_x_offsets = [15, 20, 12]

    for k, (idx, label, color) in enumerate(zip(indices, labels_y, colors)):
        ax.plot(x[idx], y[idx], 'o', color=color, markersize=9, zorder=5)

    # Segmentos para mostrar costo de oportunidad creciente
    # Movimiento 1: poca tela, bajo costo (zona izquierda de la curva)
    i1, i2 = 20, 45
    dx1 = x[i2] - x[i1]
    dy1 = abs(y[i2] - y[i1])
    ax.annotate('', xy=(x[i2], y[i1]), xytext=(x[i1], y[i1]),
               arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
    ax.annotate('', xy=(x[i2], y[i2]), xytext=(x[i2], y[i1]),
               arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
    ax.text(x[i1] + dx1/2, y[i1]+4, f'+{dx1:.0f}T', ha='center', fontsize=9,
           color=VERDE, fontweight='bold')
    ax.text(x[i2]+4, y[i1] - dy1/2, f'-{dy1:.0f}A', ha='left', fontsize=9,
           color=VERDE, fontweight='bold')

    # Movimiento 2: mucha tela, alto costo (zona derecha, con más espacio)
    i3, i4 = 120, 150
    dx2 = x[i4] - x[i3]
    dy2 = abs(y[i4] - y[i3])
    ax.annotate('', xy=(x[i4], y[i3]), xytext=(x[i3], y[i3]),
               arrowprops=dict(arrowstyle='->', color=ROJO, lw=2))
    ax.annotate('', xy=(x[i4], y[i4]), xytext=(x[i4], y[i3]),
               arrowprops=dict(arrowstyle='->', color=ROJO, lw=2))
    ax.text(x[i3] + (x[i4]-x[i3])/2, y[i3]+4, f'+{abs(dx2):.0f}T', ha='center',
           fontsize=9, color=ROJO, fontweight='bold')
    ax.text(x[i4]-8, y[i3] - dy2/2 - 3, f'-{dy2:.0f}A', ha='center', fontsize=9,
           color=ROJO, fontweight='bold')

    # Caja explicativa
    box_text = ("Al inicio: ganar tela cuesta poco\n"
                "Al final: ganar tela cuesta mucho\n"
                "→ Costo de oportunidad CRECIENTE")
    props = dict(boxstyle='round,pad=0.6', facecolor='#FEF3C7', edgecolor='#F59E0B',
                alpha=0.95)
    ax.text(55, 72, box_text, fontsize=10, bbox=props, color='#92400E',
           va='top', linespacing=1.5)

    ax.set_xlim(-5, 115)
    ax.set_ylim(-8, 90)
    ax.set_xlabel('Tela', fontsize=12, fontweight='bold')
    ax.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
    ax.set_title('Rendimientos decrecientes → costo de oportunidad creciente',
                fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8,
            color=GRIS, style='italic')

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.savefig(OUT / 'rendimientos_decrecientes.png', dpi=150, bbox_inches='tight',
               facecolor='white')
    plt.close()
    print("  ✓ rendimientos_decrecientes.png")


# ============================================================
# GRÁFICO 3: Equilibrio en autarquía (Slide 12)
# ============================================================
def grafico_equilibrio_autarquia():
    fig, ax = plt.subplots(figsize=(9, 7))

    # PPF curva
    theta = np.linspace(0, np.pi/2, 200)
    x_ppf = 100 * np.cos(theta)**0.7
    y_ppf = 80 * np.sin(theta)**0.7
    ax.plot(x_ppf, y_ppf, color=AZUL_OSCURO, linewidth=2.5, label='PPF', zorder=3)
    ax.fill_between(x_ppf, y_ppf, alpha=0.05, color=AZUL_OSCURO)

    # Punto de equilibrio (tangencia) — más central para evitar bordes
    idx_e = 70
    xe, ye = x_ppf[idx_e], y_ppf[idx_e]
    ax.plot(xe, ye, 'o', color=ROJO, markersize=12, zorder=6)
    ax.text(xe+4, ye+2, 'E', fontsize=14, fontweight='bold', color=ROJO)

    # Curva de indiferencia en el punto E (tangente a PPF)
    # U1: pasa por E
    t_ci = np.linspace(15, 100, 200)
    k1 = xe * ye  # constante de la curva tipo hipérbola
    y_ci1 = k1 / t_ci
    mask1 = (y_ci1 > 5) & (y_ci1 < 85)
    ax.plot(t_ci[mask1], y_ci1[mask1], color=VERDE, linewidth=2, linestyle='-',
           label='Curva de indiferencia U₁', zorder=2)
    ax.text(95, k1/95 - 2, 'U₁', fontsize=12, color=VERDE, fontweight='bold')

    # U2: curva más alta (inalcanzable en autarquía)
    k2 = k1 * 1.4
    y_ci2 = k2 / t_ci
    mask2 = (y_ci2 > 5) & (y_ci2 < 85)
    ax.plot(t_ci[mask2], y_ci2[mask2], color=VERDE, linewidth=1.5, linestyle='--',
           alpha=0.5, zorder=2)
    ax.text(95, k2/95 - 2, 'U₂', fontsize=11, color=VERDE, alpha=0.6)
    ax.text(50, 82, '(U₂ inalcanzable en autarquía)', fontsize=8,
           color=VERDE, alpha=0.6, style='italic')

    # Línea de precio relativo (tangente en E)
    dx = x_ppf[idx_e+1] - x_ppf[idx_e-1]
    dy = y_ppf[idx_e+1] - y_ppf[idx_e-1]
    slope = dy / dx
    x_price = np.linspace(xe-25, xe+25, 2)
    y_price = ye + slope * (x_price - xe)
    ax.plot(x_price, y_price, '--', color=NARANJA, linewidth=2, zorder=4,
           label=f'Precio relativo: Pt/Pa')

    # Anotación del precio — a la izquierda de la línea de precios
    ax.annotate(f'Pendiente = Pt/Pa\n(precio de autarquía)',
               xy=(xe-20, ye - slope*20),
               xytext=(20, 30),
               fontsize=9, color=NARANJA, fontweight='bold',
               ha='center',
               arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.2))

    # Líneas punteadas al eje
    ax.plot([xe, xe], [0, ye], ':', color=GRIS, linewidth=1, alpha=0.5)
    ax.plot([0, xe], [ye, ye], ':', color=GRIS, linewidth=1, alpha=0.5)

    ax.set_xlim(-5, 110)
    ax.set_ylim(-5, 90)
    ax.set_xlabel('Tela', fontsize=12, fontweight='bold')
    ax.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
    ax.set_title('Equilibrio en autarquía: PPF ∩ Curva de indiferencia',
                fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.legend(loc='upper right', fontsize=9, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8,
            color=GRIS, style='italic')

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.savefig(OUT / 'equilibrio_autarquia.png', dpi=150, bbox_inches='tight',
               facecolor='white')
    plt.close()
    print("  ✓ equilibrio_autarquia.png")


# ============================================================
# GRÁFICO 4: Dos países en autarquía (Slide 13)
# ============================================================
def grafico_dos_paises_autarquia():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    theta = np.linspace(0, np.pi/2, 200)

    # --- País A: abundante en capital → sesgado a Tela ---
    x_a = 100 * np.cos(theta)**0.55   # más estirado hacia Tela
    y_a = 60 * np.sin(theta)**0.85
    ax1.plot(x_a, y_a, color=AZUL_OSCURO, linewidth=2.5, zorder=3)
    ax1.fill_between(x_a, y_a, alpha=0.05, color=AZUL_OSCURO)

    # Equilibrio A
    idx_a = 65
    xa, ya = x_a[idx_a], y_a[idx_a]
    ax1.plot(xa, ya, 'o', color=ROJO, markersize=10, zorder=5)
    ax1.text(xa+2, ya+3, 'E_A', fontsize=12, fontweight='bold', color=ROJO)

    # CI para A
    ka = xa * ya
    t_ci = np.linspace(20, 95, 200)
    y_ci_a = ka / t_ci
    mask_a = (y_ci_a > 5) & (y_ci_a < 58)
    ax1.plot(t_ci[mask_a], y_ci_a[mask_a], color=VERDE, linewidth=1.5, zorder=2)

    # Tangente (precio relativo) en A — pendiente suave = tela barata
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
    ax1.set_title('País A: abundante en Capital (K)',
                 fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Caja con dotación
    ax1.text(5, 65, 'K/L alto\n→ PPF sesgada\nhacia Tela',
            fontsize=9, color=AZUL_OSCURO, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#DBEAFE',
                     edgecolor=AZUL_MEDIO, alpha=0.9))

    # --- País B: abundante en trabajo → sesgado a Alimentos ---
    x_b = 60 * np.cos(theta)**0.85
    y_b = 100 * np.sin(theta)**0.55
    ax2.plot(x_b, y_b, color=NARANJA, linewidth=2.5, zorder=3)
    ax2.fill_between(x_b, y_b, alpha=0.05, color=NARANJA)

    # Equilibrio B
    idx_b = 65
    xb, yb = x_b[idx_b], y_b[idx_b]
    ax2.plot(xb, yb, 'o', color=ROJO, markersize=10, zorder=5)
    ax2.text(xb+2, yb+3, 'E_B', fontsize=12, fontweight='bold', color=ROJO)

    # CI para B
    kb = xb * yb
    t_ci2 = np.linspace(10, 58, 200)
    y_ci_b = kb / t_ci2
    mask_b = (y_ci_b > 10) & (y_ci_b < 95)
    ax2.plot(t_ci2[mask_b], y_ci_b[mask_b], color=VERDE, linewidth=1.5, zorder=2)

    # Tangente (precio relativo) en B — pendiente empinada = tela cara
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
    ax2.set_title('País B: abundante en Trabajo (L)',
                 fontsize=13, fontweight='bold', color=NARANJA, pad=12)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    ax2.text(35, 112, 'L/K alto\n→ PPF sesgada\nhacia Alimentos',
            fontsize=9, color=NARANJA, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEF3C7',
                     edgecolor=NARANJA, alpha=0.9))

    fig.suptitle('Distintas dotaciones → distintos precios en autarquía',
                fontsize=14, fontweight='bold', color=AZUL_OSCURO, y=0.99)

    # Flecha central indicando diferencia de precios
    fig.text(0.5, 0.03, '← Pt/Pa difiere → base para el comercio →',
            ha='center', fontsize=11, color=ROJO, fontweight='bold')

    plt.tight_layout(rect=[0, 0.06, 1, 0.94])
    fig.savefig(OUT / 'dos_paises_autarquia.png', dpi=150, bbox_inches='tight',
               facecolor='white')
    plt.close()
    print("  ✓ dos_paises_autarquia.png")


# ============================================================
# GRÁFICO 5: Oferta y demanda relativa mundiales (Slide 15)
# ============================================================
def grafico_oferta_demanda_relativa():
    fig, ax = plt.subplots(figsize=(10, 6.5))

    # Eje X: cantidad relativa Qt/Qa
    q = np.linspace(0.2, 3.0, 200)

    # Oferta relativa País A (abundante en K → más tela → OR más a la derecha)
    or_a = 0.3 + 0.6 * q**1.2
    # Oferta relativa País B (abundante en L → menos tela → OR más a la izquierda)
    or_b = 0.5 + 0.9 * q**1.3
    # Oferta relativa mundial (promedio ponderado)
    or_w = 0.4 + 0.75 * q**1.25

    # Demanda relativa (mismos gustos → única)
    dr = 2.5 / q**0.8

    # Graficar
    ax.plot(q, or_a, color=AZUL_OSCURO, linewidth=2.5, label='OR (País A)', zorder=3)
    ax.plot(q, or_b, color=NARANJA, linewidth=2.5, label='OR* (País B)', zorder=3)
    ax.plot(q, or_w, color=VERDE, linewidth=2.5, linestyle='--',
           label='OR mundial', zorder=4)
    ax.plot(q, dr, color=ROJO, linewidth=2.5, label='DR (demanda relativa)', zorder=3)

    # Precios de autarquía (intersección OR_a con DR, OR_b con DR)
    # Encontrar intersecciones numéricamente
    diff_a = or_a - dr
    idx_a = np.where(np.diff(np.sign(diff_a)))[0][0]
    q_a, p_a = q[idx_a], dr[idx_a]

    diff_b = or_b - dr
    idx_b = np.where(np.diff(np.sign(diff_b)))[0][0]
    q_b, p_b = q[idx_b], dr[idx_b]

    diff_w = or_w - dr
    idx_w = np.where(np.diff(np.sign(diff_w)))[0][0]
    q_w, p_w = q[idx_w], dr[idx_w]

    # Marcar precios de autarquía con anotaciones claras (no en eje Y)
    ax.plot(q_a, p_a, 'o', color=AZUL_OSCURO, markersize=8, zorder=6)
    ax.plot([0, q_a], [p_a, p_a], ':', color=AZUL_OSCURO, linewidth=1, alpha=0.5)
    ax.annotate(f'Pa = {p_a:.1f}', xy=(q_a, p_a),
               xytext=(q_a + 0.3, p_a - 0.35),
               fontsize=9, color=AZUL_OSCURO, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=1))

    ax.plot(q_b, p_b, 'o', color=NARANJA, markersize=8, zorder=6)
    ax.plot([0, q_b], [p_b, p_b], ':', color=NARANJA, linewidth=1, alpha=0.5)
    ax.annotate(f'Pb = {p_b:.1f}', xy=(q_b, p_b),
               xytext=(q_b - 0.5, p_b + 0.35),
               fontsize=9, color=NARANJA, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1))

    # Precio mundial
    ax.plot(q_w, p_w, '*', color=VERDE, markersize=15, zorder=7)
    ax.plot([0, q_w], [p_w, p_w], ':', color=VERDE, linewidth=1.5, alpha=0.7)
    ax.text(q_w + 0.15, p_w + 0.25, f'Precio mundial\nPt/Pa = {p_w:.1f}',
           fontsize=10, color=VERDE, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='#D1FAE5',
                    edgecolor=VERDE, alpha=0.9))

    # Zona entre precios de autarquía
    ax.axhspan(p_a, p_b, alpha=0.08, color=ROJO)
    ax.text(2.5, (p_a + p_b)/2, 'Rango de\nprecios', fontsize=9,
           color=ROJO, ha='center', style='italic', alpha=0.7)

    ax.set_xlim(0, 3.2)
    ax.set_ylim(0, 4.5)
    ax.set_xlabel('Cantidad relativa (Qt / Qa)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Precio relativo (Pt / Pa)', fontsize=12, fontweight='bold')
    ax.set_title('Oferta y demanda relativa → precio de equilibrio mundial',
                fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.legend(loc='upper right', fontsize=9, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.5, 0.01, 'Elaboración propia a partir de Lugones (2008), Gráfico G.1.6',
            ha='center', fontsize=8, color=GRIS, style='italic')

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.savefig(OUT / 'oferta_demanda_relativa.png', dpi=150, bbox_inches='tight',
               facecolor='white')
    plt.close()
    print("  ✓ oferta_demanda_relativa.png")


# ============================================================
# GRÁFICO 6: Comercio con PPF curva (Slide 16)
# ============================================================
def grafico_comercio_ppf_curva():
    fig, ax = plt.subplots(figsize=(9, 7))

    # PPF curva
    theta = np.linspace(0, np.pi/2, 200)
    x_ppf = 100 * np.cos(theta)**0.7
    y_ppf = 80 * np.sin(theta)**0.7
    ax.plot(x_ppf, y_ppf, color=AZUL_OSCURO, linewidth=2.5, label='PPF', zorder=3)
    ax.fill_between(x_ppf, y_ppf, alpha=0.05, color=AZUL_OSCURO)

    # Punto E (autarquía): producción = consumo — posición más central
    idx_e = 75
    xe, ye = x_ppf[idx_e], y_ppf[idx_e]
    ax.plot(xe, ye, 'o', color=GRIS, markersize=10, zorder=5)
    ax.text(xe+3, ye+4, 'E (autarquía)', fontsize=9, fontweight='bold', color=GRIS)

    # CI en autarquía
    k1 = xe * ye
    t_ci = np.linspace(18, 100, 200)
    y_ci1 = k1 / t_ci
    mask1 = (y_ci1 > 5) & (y_ci1 < 78)
    ax.plot(t_ci[mask1], y_ci1[mask1], color=GRIS, linewidth=1.5, linestyle='-',
           alpha=0.5, zorder=2)
    ax.text(97, k1/97 - 2, 'U₁', fontsize=10, color=GRIS, alpha=0.6)

    # Punto Q (producción con comercio): se mueve a más tela
    idx_q = 55
    xq, yq = x_ppf[idx_q], y_ppf[idx_q]
    ax.plot(xq, yq, 's', color=AZUL_MEDIO, markersize=11, zorder=5)
    ax.text(xq+3, yq-7, 'Q (producción)', fontsize=9, fontweight='bold', color=AZUL_MEDIO)

    # Línea de precios mundiales (tangente a PPF en Q)
    dx = x_ppf[idx_q+1] - x_ppf[idx_q-1]
    dy = y_ppf[idx_q+1] - y_ppf[idx_q-1]
    slope = dy / dx
    # Extender la línea de precios
    x_price = np.linspace(xq-30, xq+30, 2)
    y_price = yq + slope * (x_price - xq)
    ax.plot(x_price, y_price, '--', color=NARANJA, linewidth=2, zorder=4,
           label='Línea de precios mundiales')

    # Punto C (consumo): sobre la línea de precios, fuera de PPF
    xc = xq - 18  # consume menos tela
    yc = yq + slope * (xc - xq)  # pero más alimentos
    ax.plot(xc, yc, 'D', color=ROJO, markersize=11, zorder=5)
    ax.text(xc-12, yc-3, 'C (consumo)', fontsize=9, fontweight='bold', color=ROJO)

    # CI en C (más alta que U1)
    k2 = xc * yc
    y_ci2 = k2 / t_ci
    mask2 = (y_ci2 > 8) & (y_ci2 < 82)
    ax.plot(t_ci[mask2], y_ci2[mask2], color=VERDE, linewidth=2, zorder=2)
    ax.text(97, k2/97 - 2, 'U₂', fontsize=10, color=VERDE, fontweight='bold')

    # Flechas de exportación e importación
    # Exporta tela: horizontal de C a Q
    mid_y_exp = min(yc, yq) - 3
    ax.annotate('', xy=(xq, mid_y_exp), xytext=(xc, mid_y_exp),
               arrowprops=dict(arrowstyle='<->', color=AZUL_CLARO, lw=2.5))
    ax.text((xq + xc)/2, mid_y_exp - 5, 'Exporta Tela', fontsize=9, ha='center',
           color=AZUL_CLARO, fontweight='bold')

    # Importa alimentos: vertical de Q a C
    mid_x_imp = xc - 3
    ax.annotate('', xy=(mid_x_imp, yc), xytext=(mid_x_imp, yq),
               arrowprops=dict(arrowstyle='<->', color=VERDE, lw=2.5))
    ax.text(mid_x_imp - 10, (yq + yc)/2, 'Importa\nAlim.', fontsize=9, ha='center',
           color=VERDE, fontweight='bold')

    # Caja: "Mayor bienestar"
    ax.text(10, 75, '¡Consume FUERA\nde la PPF!\nU₂ > U₁ → mayor\nbienestar',
           fontsize=9, color=VERDE, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='#D1FAE5',
                    edgecolor=VERDE, alpha=0.9))

    ax.set_xlim(-5, 110)
    ax.set_ylim(-5, 90)
    ax.set_xlabel('Tela', fontsize=12, fontweight='bold')
    ax.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
    ax.set_title('Ganancias del comercio: consumir fuera de la PPF',
                fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.legend(loc='lower left', fontsize=9, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8,
            color=GRIS, style='italic')

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.savefig(OUT / 'comercio_ppf_curva.png', dpi=150, bbox_inches='tight',
               facecolor='white')
    plt.close()
    print("  ✓ comercio_ppf_curva.png")


# ============================================================
# GRÁFICO 7: Resumen Ricardo vs Neoclásico (Slide 18)
# ============================================================
def grafico_resumen_ricardo_vs_neoclasico():
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.axis('off')

    # Tabla comparativa
    categorias = [
        'Factores de\nproducción',
        'PPF',
        'Costo de\noportunidad',
        'Especialización',
        'Fuente de ventaja\ncomparativa',
        'Preferencias del\nconsumidor',
        'Determinación\ndel precio'
    ]

    ricardo = [
        '1 (trabajo)',
        'Recta',
        'Constante',
        'Total\n(todo o nada)',
        'Diferencias de\ntecnología',
        'No aparecen',
        'Solo por costos\n(oferta)'
    ]

    neoclasico = [
        '2+ (trabajo + capital)',
        'Curva (cóncava)',
        'Creciente',
        'Parcial\n(produce ambos)',
        'Diferencias de\ndotaciones',
        'Curvas de\nindiferencia',
        'Oferta + Demanda\n(OR y DR)'
    ]

    n_rows = len(categorias)
    row_h = 0.85
    col_w_cat = 3.0
    col_w_val = 3.8
    x_start = 1.0
    y_start = 6.0

    # Headers — placed ABOVE the first data row (y_start + row_h)
    headers = ['Dimensión', 'Ricardo (1817)', 'Neoclásico estándar']
    header_colors = [GRIS, AZUL_OSCURO, NARANJA]
    header_y = y_start + row_h + 0.1
    x_positions_h = [x_start + col_w_cat/2,
                     x_start + col_w_cat + col_w_val/2,
                     x_start + col_w_cat + col_w_val + 0.3 + col_w_val/2]

    for xp, header, hcolor in zip(x_positions_h, headers, header_colors):
        w = col_w_cat if header == 'Dimensión' else col_w_val
        rect = mpatches.FancyBboxPatch((xp - w/2, header_y),
                                       w, row_h,
                                       boxstyle='round,pad=0.1',
                                       facecolor=hcolor, edgecolor='white',
                                       alpha=0.9, zorder=5)
        ax.add_patch(rect)
        ax.text(xp, header_y + row_h/2, header,
               ha='center', va='center', fontsize=12, fontweight='bold',
               color='white', zorder=6)

    # Rows
    for i in range(n_rows):
        y = y_start - i * row_h
        bg = '#F8FAFC' if i % 2 == 0 else 'white'

        # Categoría
        rect_cat = mpatches.FancyBboxPatch((x_start, y), col_w_cat, row_h-0.05,
                                           boxstyle='round,pad=0.05',
                                           facecolor=bg, edgecolor=GRIS_CLARO)
        ax.add_patch(rect_cat)
        ax.text(x_start + col_w_cat/2, y + row_h/2 - 0.02, categorias[i],
               ha='center', va='center', fontsize=10, fontweight='bold',
               color=AZUL_OSCURO)

        # Ricardo
        x_ric = x_start + col_w_cat
        rect_ric = mpatches.FancyBboxPatch((x_ric, y), col_w_val, row_h-0.05,
                                           boxstyle='round,pad=0.05',
                                           facecolor=bg, edgecolor=GRIS_CLARO)
        ax.add_patch(rect_ric)
        ax.text(x_ric + col_w_val/2, y + row_h/2 - 0.02, ricardo[i],
               ha='center', va='center', fontsize=10, color=AZUL_OSCURO)

        # Neoclásico
        x_neo = x_ric + col_w_val + 0.3
        rect_neo = mpatches.FancyBboxPatch((x_neo, y), col_w_val, row_h-0.05,
                                           boxstyle='round,pad=0.05',
                                           facecolor=bg, edgecolor=GRIS_CLARO)
        ax.add_patch(rect_neo)
        ax.text(x_neo + col_w_val/2, y + row_h/2 - 0.02, neoclasico[i],
               ha='center', va='center', fontsize=10, color=NARANJA,
               fontweight='bold')

    # Pie: lo que comparten
    y_bottom = y_start - n_rows * row_h - 0.3
    total_w = col_w_cat + 2*col_w_val + 0.3
    rect_bottom = mpatches.FancyBboxPatch((x_start, y_bottom), total_w,
                                          row_h + 0.1,
                                          boxstyle='round,pad=0.15',
                                          facecolor='#D1FAE5', edgecolor=VERDE,
                                          alpha=0.9)
    ax.add_patch(rect_bottom)
    ax.text(x_start + total_w/2, y_bottom + (row_h+0.1)/2,
           'EN COMÚN: precios relativos diferentes en autarquía → comercio → ganancias para ambos',
           ha='center', va='center', fontsize=11, fontweight='bold', color=VERDE)

    ax.set_xlim(0, 13)
    ax.set_ylim(y_bottom - 0.5, header_y + row_h + 0.5)

    fig.suptitle('Ricardo vs Modelo neoclásico estándar', fontsize=15,
                fontweight='bold', color=AZUL_OSCURO, y=0.97)
    fig.text(0.5, 0.01, 'Elaboración propia', ha='center', fontsize=8,
            color=GRIS, style='italic')

    plt.tight_layout(rect=[0, 0.02, 1, 0.95])
    fig.savefig(OUT / 'resumen_ricardo_vs_neoclasico.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print("  ✓ resumen_ricardo_vs_neoclasico.png")


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("Generando gráficos para Clase 5...\n")

    grafico_ppf_recta_vs_curva()
    grafico_rendimientos_decrecientes()
    grafico_equilibrio_autarquia()
    grafico_dos_paises_autarquia()
    grafico_oferta_demanda_relativa()
    grafico_comercio_ppf_curva()
    grafico_resumen_ricardo_vs_neoclasico()

    print(f"\n¡Listo! 7 gráficos generados en {OUT}")
