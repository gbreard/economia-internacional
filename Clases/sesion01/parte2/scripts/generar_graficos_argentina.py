"""
Genera gráficos para el bloque del Caso Argentino.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "graficos"

# Colores
AZUL_OSCURO = '#1F4E79'
AZUL_CLARO = '#5B9BD5'
VERDE = '#70AD47'
ROJO = '#C00000'
NARANJA = '#ED7D31'
GRIS = '#7F7F7F'
AMARILLO = '#FFC000'


def grafico_ciclo_argentino():
    """Diagrama del ciclo argentino de apreciación-crisis."""
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Título
    ax.text(6, 11.5, 'EL CICLO ARGENTINO', fontsize=22, fontweight='bold',
            ha='center', color=AZUL_OSCURO)
    ax.text(6, 10.9, 'El patrón que se repite cada 10-15 años', fontsize=12,
            ha='center', color=GRIS, style='italic')

    # Centro del ciclo
    centro_x, centro_y = 6, 5.5
    radio = 3.5

    # Dibujar círculo de fondo
    circulo = plt.Circle((centro_x, centro_y), radio + 0.5, color='#F0F0F0',
                          fill=True, zorder=0)
    ax.add_patch(circulo)

    # Las 4 fases del ciclo
    fases = [
        {'pos': (centro_x, centro_y + radio), 'color': VERDE, 'num': '1',
         'titulo': 'ESTABILIZACIÓN', 'desc': 'Ancla cambiaria\nInflación baja\nConfianza'},
        {'pos': (centro_x + radio, centro_y), 'color': AMARILLO, 'num': '2',
         'titulo': 'APRECIACIÓN', 'desc': 'Peso se encarece\nDéficit comercial\nEndeudamiento'},
        {'pos': (centro_x, centro_y - radio), 'color': ROJO, 'num': '3',
         'titulo': 'CRISIS', 'desc': 'Fuga de capitales\nCaen reservas\nDevaluación'},
        {'pos': (centro_x - radio, centro_y), 'color': AZUL_CLARO, 'num': '4',
         'titulo': 'RECUPERACIÓN', 'desc': 'TC competitivo\nSuperávit\nCrecimiento'},
    ]

    for fase in fases:
        x, y = fase['pos']
        # Círculo de la fase
        circulo = plt.Circle((x, y), 1.2, color=fase['color'], fill=True,
                              alpha=0.9, zorder=2)
        ax.add_patch(circulo)
        # Número
        ax.text(x, y + 0.5, fase['num'], fontsize=20, fontweight='bold',
                ha='center', va='center', color='white', zorder=3)
        # Título
        ax.text(x, y - 0.1, fase['titulo'], fontsize=9, fontweight='bold',
                ha='center', va='center', color='white', zorder=3)
        # Descripción afuera
        if fase['num'] == '1':
            ax.text(x, y + 2.2, fase['desc'], fontsize=9, ha='center', va='center')
        elif fase['num'] == '2':
            ax.text(x + 2.2, y, fase['desc'], fontsize=9, ha='center', va='center')
        elif fase['num'] == '3':
            ax.text(x, y - 2.2, fase['desc'], fontsize=9, ha='center', va='center')
        elif fase['num'] == '4':
            ax.text(x - 2.2, y, fase['desc'], fontsize=9, ha='center', va='center')

    # Flechas entre fases
    arrow_props = dict(arrowstyle='->', color=GRIS, lw=2, connectionstyle='arc3,rad=0.3')
    # 1 -> 2
    ax.annotate('', xy=(centro_x + 2, centro_y + 2), xytext=(centro_x + 0.8, centro_y + 2.8),
                arrowprops=arrow_props)
    # 2 -> 3
    ax.annotate('', xy=(centro_x + 2.8, centro_y - 0.8), xytext=(centro_x + 2.8, centro_y + 0.8),
                arrowprops=arrow_props)
    # 3 -> 4
    ax.annotate('', xy=(centro_x - 0.8, centro_y - 2.8), xytext=(centro_x + 0.8, centro_y - 2.8),
                arrowprops=arrow_props)
    # 4 -> 1
    ax.annotate('', xy=(centro_x - 2.8, centro_y + 0.8), xytext=(centro_x - 2.8, centro_y - 0.8),
                arrowprops=arrow_props)

    # Ejemplos históricos
    ax.text(6, 1.2, 'EJEMPLOS: 1991-2001 (Convertibilidad) → 2002 (Crisis)',
            fontsize=10, ha='center', color=AZUL_OSCURO, fontweight='bold')
    ax.text(6, 0.7, '2003-2011 (Recuperación) → 2012-2015 (Apreciación) → 2018 (Crisis)',
            fontsize=10, ha='center', color=AZUL_OSCURO)
    ax.text(6, 0.2, '¿2024-?: ¿En qué fase estamos?',
            fontsize=10, ha='center', color=ROJO, fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'ciclo_argentino.png', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('Creado: ciclo_argentino.png')


def grafico_convertibilidad_timeline():
    """Timeline de la Convertibilidad con indicadores clave."""
    fig, axes = plt.subplots(3, 1, figsize=(13, 9), sharex=True)

    años = list(range(1991, 2003))

    # Datos aproximados
    tcr = [100, 95, 90, 88, 85, 82, 80, 78, 75, 72, 70, 180]  # 2002 = devaluación
    cc_pib = [0, -2, -3, -4, -4, -3, -4, -5, -4, -3, -1, 8]  # 2002 = superávit por colapso
    reservas = [8, 12, 15, 17, 20, 22, 25, 26, 27, 25, 15, 10]  # miles de millones USD

    # Panel 1: Tipo de cambio real
    ax1 = axes[0]
    colores_tcr = [VERDE if v >= 100 else ROJO for v in tcr]
    ax1.bar(años, tcr, color=colores_tcr, edgecolor='white')
    ax1.axhline(y=100, color='black', linestyle='--', label='Equilibrio')
    ax1.set_ylabel('TCR (1991=100)', fontsize=10)
    ax1.set_title('Convertibilidad: El Ciclo en 3 Indicadores', fontsize=14,
                  fontweight='bold', color=AZUL_OSCURO)
    ax1.text(1992, 105, 'Peso cada vez\nmás caro', fontsize=9, color=ROJO)
    ax1.text(2001.5, 150, 'Devaluación\n200%', fontsize=9, color=VERDE, ha='center')
    ax1.legend(loc='upper right')
    ax1.set_ylim(0, 200)

    # Panel 2: Cuenta corriente
    ax2 = axes[1]
    colores_cc = [VERDE if v >= 0 else ROJO for v in cc_pib]
    ax2.bar(años, cc_pib, color=colores_cc, edgecolor='white')
    ax2.axhline(y=0, color='black', linestyle='-')
    ax2.set_ylabel('CC (% PIB)', fontsize=10)
    ax2.text(1995, -3.5, 'Déficit\npersistente', fontsize=9, color=ROJO, ha='center')
    ax2.text(2002, 6, 'Superávit por\ncolapso imports', fontsize=8, color=VERDE, ha='center')
    ax2.set_ylim(-6, 10)

    # Panel 3: Reservas
    ax3 = axes[2]
    ax3.fill_between(años, reservas, color=AZUL_CLARO, alpha=0.7)
    ax3.plot(años, reservas, color=AZUL_OSCURO, linewidth=2, marker='o')
    ax3.set_ylabel('Reservas (USD bn)', fontsize=10)
    ax3.set_xlabel('Año', fontsize=11)
    ax3.text(1996, 22, 'Acumulación', fontsize=9, color=AZUL_OSCURO)
    ax3.text(2001, 12, 'Fuga', fontsize=9, color=ROJO, ha='center')
    ax3.axvspan(2000, 2002, alpha=0.2, color=ROJO)
    ax3.set_ylim(0, 30)

    # Marcar crisis
    for ax in axes:
        ax.axvspan(2001, 2002, alpha=0.1, color=AMARILLO)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'convertibilidad_timeline.png', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('Creado: convertibilidad_timeline.png')


def grafico_resumen_indicadores():
    """Tabla visual de los 9 indicadores."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')

    # Título
    ax.text(0.5, 0.95, 'LOS 9 INDICADORES DE INSERCIÓN EXTERNA',
            fontsize=18, fontweight='bold', ha='center', transform=ax.transAxes,
            color=AZUL_OSCURO)

    # Datos de la tabla
    indicadores = [
        ('1', 'Índice de comercio', 'I_t = 100 × (Com_t / Com_base)', 'Mide crecimiento del comercio'),
        ('2', 'Participación regional', 's_r = X_r / X_mundo × 100', 'Quién gana/pierde peso'),
        ('3', 'Concentración (HHI)', 'HHI = Σ(s_i)²', 'Diversificación del comercio'),
        ('4', 'Cobertura de datos', '% países con datos', 'Calidad de las fuentes'),
        ('5', 'Balanza comercial', 'BC = X - M', 'Competitividad comercial'),
        ('6', 'Apertura comercial', '(X + M) / PIB × 100', 'Integración al mundo'),
        ('7', 'Términos del intercambio', 'ToT = Px / Pm × 100', 'Poder de compra externo'),
        ('8', 'Cuenta corriente', 'CC / PIB × 100', 'Sostenibilidad externa'),
        ('9', 'Tipo de cambio real', 'TCR = e × P* / P', 'Competitividad precio'),
    ]

    # Dibujar tabla
    y_start = 0.85
    row_height = 0.08
    col_widths = [0.05, 0.22, 0.35, 0.35]
    col_starts = [0.02, 0.08, 0.32, 0.68]

    # Headers
    headers = ['#', 'Indicador', 'Fórmula', 'Interpretación']
    for j, (header, x) in enumerate(zip(headers, col_starts)):
        ax.text(x, y_start + 0.03, header, fontsize=11, fontweight='bold',
                transform=ax.transAxes, color='white',
                bbox=dict(boxstyle='round', facecolor=AZUL_OSCURO, alpha=0.9))

    # Filas
    for i, (num, nombre, formula, interp) in enumerate(indicadores):
        y = y_start - (i + 1) * row_height
        color_fondo = '#F5F5F5' if i % 2 == 0 else 'white'

        # Fondo de fila
        rect = mpatches.FancyBboxPatch((0.01, y - 0.02), 0.98, row_height - 0.01,
                                        boxstyle='round,pad=0.01',
                                        facecolor=color_fondo, edgecolor='#CCCCCC',
                                        transform=ax.transAxes)
        ax.add_patch(rect)

        # Contenido
        ax.text(col_starts[0] + 0.02, y + 0.02, num, fontsize=11, fontweight='bold',
                transform=ax.transAxes, color=AZUL_OSCURO)
        ax.text(col_starts[1], y + 0.02, nombre, fontsize=10,
                transform=ax.transAxes)
        ax.text(col_starts[2], y + 0.02, formula, fontsize=9,
                transform=ax.transAxes, family='monospace')
        ax.text(col_starts[3], y + 0.02, interp, fontsize=9,
                transform=ax.transAxes, color=GRIS)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'resumen_indicadores.png', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('Creado: resumen_indicadores.png')


def main():
    print("Generando gráficos del Caso Argentino...")
    grafico_ciclo_argentino()
    grafico_convertibilidad_timeline()
    grafico_resumen_indicadores()
    print("\n¡Listo! 3 gráficos creados.")


if __name__ == "__main__":
    main()
