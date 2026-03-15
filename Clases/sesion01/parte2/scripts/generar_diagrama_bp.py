"""
Genera diagrama de estructura de la Balanza de Pagos.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT = BASE_DIR / "graficos" / "balanza_pagos_estructura.png"

# Colores
AZUL_OSCURO = '#1F4E79'
AZUL_CLARO = '#5B9BD5'
VERDE = '#70AD47'
NARANJA = '#ED7D31'
GRIS = '#7F7F7F'

def main():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Título
    ax.text(6, 9.5, 'BALANZA DE PAGOS', fontsize=20, fontweight='bold',
            ha='center', color=AZUL_OSCURO)
    ax.text(6, 9.0, 'Registro de todas las transacciones entre un país y el resto del mundo',
            fontsize=11, ha='center', color=GRIS, style='italic')

    # Caja principal
    main_box = mpatches.FancyBboxPatch((0.5, 0.5), 11, 8,
                                         boxstyle='round,pad=0.05',
                                         facecolor='white', edgecolor=AZUL_OSCURO, linewidth=2)
    ax.add_patch(main_box)

    # CUENTA CORRIENTE (izquierda)
    cc_box = mpatches.FancyBboxPatch((1, 5), 3.2, 3,
                                       boxstyle='round,pad=0.03',
                                       facecolor='#E2F0D9', edgecolor=VERDE, linewidth=2)
    ax.add_patch(cc_box)
    ax.text(2.6, 7.6, 'CUENTA', fontsize=12, fontweight='bold', ha='center', color=VERDE)
    ax.text(2.6, 7.2, 'CORRIENTE', fontsize=12, fontweight='bold', ha='center', color=VERDE)
    ax.text(2.6, 6.5, '• Bienes (X - M)', fontsize=9, ha='center')
    ax.text(2.6, 6.1, '• Servicios', fontsize=9, ha='center')
    ax.text(2.6, 5.7, '• Rentas (intereses,', fontsize=9, ha='center')
    ax.text(2.6, 5.4, '  dividendos)', fontsize=9, ha='center')

    # CUENTA CAPITAL (centro)
    ck_box = mpatches.FancyBboxPatch((4.5, 5), 3, 3,
                                       boxstyle='round,pad=0.03',
                                       facecolor='#FFF2CC', edgecolor=NARANJA, linewidth=2)
    ax.add_patch(ck_box)
    ax.text(6, 7.6, 'CUENTA', fontsize=12, fontweight='bold', ha='center', color=NARANJA)
    ax.text(6, 7.2, 'CAPITAL', fontsize=12, fontweight='bold', ha='center', color=NARANJA)
    ax.text(6, 6.5, '• Transferencias', fontsize=9, ha='center')
    ax.text(6, 6.1, '  de capital', fontsize=9, ha='center')
    ax.text(6, 5.7, '• Activos no', fontsize=9, ha='center')
    ax.text(6, 5.4, '  financieros', fontsize=9, ha='center')

    # CUENTA FINANCIERA (derecha)
    cf_box = mpatches.FancyBboxPatch((7.8, 5), 3.2, 3,
                                       boxstyle='round,pad=0.03',
                                       facecolor='#DEEBF7', edgecolor=AZUL_CLARO, linewidth=2)
    ax.add_patch(cf_box)
    ax.text(9.4, 7.6, 'CUENTA', fontsize=12, fontweight='bold', ha='center', color=AZUL_OSCURO)
    ax.text(9.4, 7.2, 'FINANCIERA', fontsize=12, fontweight='bold', ha='center', color=AZUL_OSCURO)
    ax.text(9.4, 6.5, '• Inversión directa', fontsize=9, ha='center')
    ax.text(9.4, 6.1, '• Inversión cartera', fontsize=9, ha='center')
    ax.text(9.4, 5.7, '• Préstamos', fontsize=9, ha='center')
    ax.text(9.4, 5.4, '• Reservas BCRA', fontsize=9, ha='center')

    # Ecuación fundamental
    eq_box = mpatches.FancyBboxPatch((1, 1.5), 10, 2.5,
                                       boxstyle='round,pad=0.03',
                                       facecolor='#F2F2F2', edgecolor=GRIS, linewidth=1)
    ax.add_patch(eq_box)
    ax.text(6, 3.5, 'IDENTIDAD FUNDAMENTAL', fontsize=11, fontweight='bold',
            ha='center', color=AZUL_OSCURO)
    ax.text(6, 2.8, 'Cuenta Corriente + Cuenta Capital + Cuenta Financiera = 0',
            fontsize=12, ha='center', fontweight='bold')
    ax.text(6, 2.1, 'Si CC < 0 (déficit), debe financiarse con entrada de capitales (CF > 0)',
            fontsize=10, ha='center', color=GRIS)

    # Flechas conectoras
    ax.annotate('', xy=(4.4, 6.5), xytext=(4.6, 6.5),
                arrowprops=dict(arrowstyle='<->', color=GRIS, lw=1.5))
    ax.annotate('', xy=(7.5, 6.5), xytext=(7.7, 6.5),
                arrowprops=dict(arrowstyle='<->', color=GRIS, lw=1.5))

    plt.tight_layout()
    plt.savefig(OUTPUT, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'Creado: {OUTPUT}')


if __name__ == "__main__":
    main()
