"""
Genera gráfico: determinación del precio relativo en autarquía
PPF cóncava + curva de indiferencia tangente + recta de precios
"""
import sys
import io
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Colores
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'

SCRIPT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
OUT = SCRIPT_DIR.parent / 'graficos'

theta = np.linspace(0, np.pi/2, 300)

fig, ax = plt.subplots(1, 1, figsize=(8, 6.5))

# PPF cóncava
x_ppf = 80 * np.cos(theta)**0.7
y_ppf = 70 * np.sin(theta)**0.7
ax.plot(x_ppf, y_ppf, color=AZUL_OSCURO, linewidth=2.5, zorder=3, label='PPF')
ax.fill_between(x_ppf, y_ppf, alpha=0.04, color=AZUL_OSCURO)

# Punto de equilibrio E (tangencia)
idx_e = 120  # punto en la PPF
xe, ye = x_ppf[idx_e], y_ppf[idx_e]
ax.plot(xe, ye, 'o', color=ROJO, markersize=12, zorder=6)
ax.text(xe + 3, ye + 3, 'E', fontsize=14, fontweight='bold', color=ROJO, zorder=7)

# Curva de indiferencia U1 (tangente en E)
k1 = xe * ye  # hipérbola que pasa por E
t_ci = np.linspace(15, 75, 300)
y_ci1 = k1 / t_ci
mask1 = (y_ci1 > 8) & (y_ci1 < 65)
ax.plot(t_ci[mask1], y_ci1[mask1], color=VERDE, linewidth=2, zorder=2, label='Curva de indiferencia $U_1$')
# Etiqueta U1
ci_idx = np.where(mask1)[0][-15]
ax.text(t_ci[ci_idx] + 2, y_ci1[ci_idx] - 2, '$U_1$', fontsize=13, fontweight='bold', color=VERDE)

# Curva de indiferencia U2 (inalcanzable, más arriba)
k2 = k1 * 1.5
t_ci2 = np.linspace(20, 88, 300)
y_ci2 = k2 / t_ci2
mask2 = (y_ci2 > 15) & (y_ci2 < 75)
ax.plot(t_ci2[mask2], y_ci2[mask2], color=VERDE, linewidth=1.5, linestyle='--', alpha=0.5, zorder=2, label='$U_2$ (inalcanzable)')
ci2_indices = np.where(mask2)[0]
if len(ci2_indices) > 10:
    ci2_idx = ci2_indices[-10]
    ax.text(t_ci2[ci2_idx] + 2, y_ci2[ci2_idx] - 2, '$U_2$', fontsize=12, color=VERDE, alpha=0.6)

# Pendiente en E (recta de precios = tangente)
dx = x_ppf[idx_e+1] - x_ppf[idx_e-1]
dy = y_ppf[idx_e+1] - y_ppf[idx_e-1]
slope = dy / dx
x_price = np.linspace(xe - 30, xe + 30, 2)
y_price = ye + slope * (x_price - xe)
ax.plot(x_price, y_price, '--', color=NARANJA, linewidth=2.5, zorder=4, label='Pendiente = $P_T / P_A$')

# Anotación: pendiente = precio relativo
ax.annotate('Pendiente = $P_T / P_A$\n(precio relativo)',
           xy=(xe + 18, ye + slope * 18),
           xytext=(78, 18),
           fontsize=10, fontweight='bold', color=NARANJA,
           ha='center',
           arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5))

# Anotaciones TMT y TMS
ax.annotate('TMT = pendiente PPF\n(lado producción)',
           xy=(x_ppf[idx_e - 30], y_ppf[idx_e - 30]),
           xytext=(8, 25),
           fontsize=9, color=AZUL_OSCURO, fontweight='bold',
           arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=1.2))

ci_left_idx = np.where(mask1)[0][15]
ax.annotate('TMS = pendiente $U_1$\n(lado consumo)',
           xy=(t_ci[ci_left_idx], y_ci1[ci_left_idx]),
           xytext=(8, 12),
           fontsize=9, color=VERDE, fontweight='bold',
           arrowprops=dict(arrowstyle='->', color=VERDE, lw=1.2))

# Caja resumen
ax.text(42, 72, 'En E:  TMT = TMS = $P_T/P_A$  →  Equilibrio de autarquía',
       fontsize=10, fontweight='bold', color=ROJO,
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEE2E2',
                edgecolor=ROJO, alpha=0.9))

# Líneas punteadas a los ejes
ax.plot([xe, xe], [0, ye], ':', color=GRIS, linewidth=1, alpha=0.5)
ax.plot([0, xe], [ye, ye], ':', color=GRIS, linewidth=1, alpha=0.5)

# Ejes
ax.set_xlim(-3, 90)
ax.set_ylim(-3, 78)
ax.set_xlabel('Tela', fontsize=12, fontweight='bold')
ax.set_ylabel('Alimentos', fontsize=12, fontweight='bold')
ax.set_title('Determinación del precio relativo en autarquía',
            fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=12)

# Limpiar ejes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

plt.tight_layout()
fig.savefig(OUT / 'precio_autarquia.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  + precio_autarquia.png")
