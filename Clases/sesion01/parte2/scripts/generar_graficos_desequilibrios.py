"""
Genera gráficos para el bloque de Desequilibrios Globales.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "graficos"

# Colores consistentes
AZUL_OSCURO = '#1F4E79'
AZUL_CLARO = '#5B9BD5'
VERDE = '#70AD47'
ROJO = '#C00000'
NARANJA = '#ED7D31'
GRIS = '#7F7F7F'
AMARILLO = '#FFC000'


def grafico_mapa_desequilibrios():
    """Gráfico 1: Visualización de quién tiene superávit y quién déficit."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Datos promedio 2010-2020
    paises = ['EEUU', 'Reino\nUnido', 'Australia', 'Brasil', 'China', 'Alemania', 'Japón', 'Arabia\nSaudita']
    valores = [-2.5, -3.5, -2.8, -1.5, 2.0, 7.5, 3.0, 5.0]
    colores = [ROJO if v < 0 else VERDE for v in valores]

    bars = ax.barh(paises, valores, color=colores, edgecolor='white', height=0.7)

    # Línea de cero
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Etiquetas de valor
    for bar, val in zip(bars, valores):
        x_pos = val + 0.3 if val >= 0 else val - 0.3
        ha = 'left' if val >= 0 else 'right'
        ax.text(x_pos, bar.get_y() + bar.get_height()/2, f'{val:+.1f}%',
                va='center', ha=ha, fontsize=10, fontweight='bold')

    # Anotaciones
    ax.annotate('DÉFICIT\n(importan capitales)', xy=(-5, 7.5), fontsize=10,
                color=ROJO, ha='center', fontweight='bold')
    ax.annotate('SUPERÁVIT\n(exportan capitales)', xy=(5, 7.5), fontsize=10,
                color=VERDE, ha='center', fontweight='bold')

    ax.set_xlabel('Cuenta Corriente (% del PIB, promedio 2010-2020)', fontsize=11)
    ax.set_title('Desequilibrios Globales: ¿Quién financia a quién?',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO)
    ax.set_xlim(-8, 10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Nota al pie
    ax.text(0.5, -0.12, 'Los países con superávit (verde) financian a los países con déficit (rojo)',
            transform=ax.transAxes, ha='center', fontsize=9, color=GRIS, style='italic')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'desequilibrios_mapa.png', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('Creado: desequilibrios_mapa.png')


def grafico_dolar_reservas():
    """Gráfico 2: Dominancia del dólar en reservas mundiales."""
    fig, ax = plt.subplots(figsize=(11, 7))

    # Datos de composición de reservas mundiales (FMI COFER)
    años = [1999, 2005, 2010, 2015, 2020, 2024]
    usd = [71, 66, 62, 64, 59, 58]
    eur = [18, 24, 26, 20, 21, 20]
    otras = [11, 10, 12, 16, 20, 22]  # JPY, GBP, CNY, otras

    ax.stackplot(años, usd, eur, otras,
                 labels=['Dólar (USD)', 'Euro (EUR)', 'Otras (JPY, GBP, CNY...)'],
                 colors=[AZUL_OSCURO, NARANJA, GRIS], alpha=0.85)

    # Línea del 50%
    ax.axhline(y=50, color='black', linestyle='--', alpha=0.5)
    ax.text(2024.5, 51, '50%', fontsize=9, color='black')

    # Anotaciones
    ax.annotate('El dólar sigue\ndominando', xy=(2010, 75), fontsize=11,
                color='white', fontweight='bold', ha='center')
    ax.annotate('Yuan chino\ncrece lento', xy=(2022, 10), fontsize=9,
                color='white', ha='center')

    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('% de reservas mundiales', fontsize=11)
    ax.set_title('El "Privilegio Exorbitante": Composición de Reservas Globales',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO)
    ax.set_xlim(1999, 2024)
    ax.set_ylim(0, 100)
    ax.legend(loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Nota
    ax.text(0.5, -0.1, 'EEUU puede tener déficits porque el mundo quiere dólares. Fuente: FMI COFER',
            transform=ax.transAxes, ha='center', fontsize=9, color=GRIS, style='italic')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'dolar_reservas.png', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('Creado: dolar_reservas.png')


def grafico_asia_transformacion():
    """Gráfico 3: Transformación de Asia de deudores a acreedores."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Datos de cuenta corriente % PIB para Asia emergente
    años = list(range(1990, 2024))  # 34 años

    # Datos aproximados basados en FMI (34 valores)
    asia_cc = [-1.5, -2.0, -1.8, -2.5, -2.0, -3.0, -3.5, -4.0,  # 1990-1997 (8)
               4.0, 3.5,  # 1998-1999 (2)
               2.5, 2.0, 3.0, 4.0, 4.5, 5.5, 6.5, 7.0, 5.0,  # 2000-2008 (9)
               4.0, 3.0, 2.0, 2.5, 1.5, 2.0, 2.5, 2.0, 1.5, 1.0,  # 2009-2018 (10)
               1.0, 2.0, 3.0, 1.5, 1.0]  # 2019-2023 (5) = total 34

    # Colores por período
    colores = [ROJO if v < 0 else VERDE for v in asia_cc]

    ax.bar(años, asia_cc, color=colores, width=0.8, edgecolor='white')
    ax.axhline(y=0, color='black', linewidth=1)

    # Zona de crisis
    ax.axvspan(1997, 1998.5, alpha=0.3, color=AMARILLO)
    ax.text(1997.7, 6, 'Crisis\nAsiática', fontsize=9, fontweight='bold',
            color=NARANJA, ha='center')

    # Anotaciones de períodos
    ax.annotate('Déficit y\nendeudamiento', xy=(1993, -3), fontsize=10,
                color=ROJO, ha='center', fontweight='bold')
    ax.annotate('Superávit y\nacumulación\nde reservas', xy=(2005, 5.5), fontsize=10,
                color=VERDE, ha='center', fontweight='bold')

    # Flecha de transformación
    ax.annotate('', xy=(2002, 3), xytext=(1995, -2),
                arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=2))

    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('Cuenta Corriente (% PIB)', fontsize=11)
    ax.set_title('Asia Emergente: De Deudores a Acreedores',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO)
    ax.set_xlim(1989, 2025)
    ax.set_ylim(-5, 8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Nota
    ax.text(0.5, -0.1, 'Después de la crisis de 1997, Asia nunca más quiso depender del capital externo. Fuente: FMI WEO',
            transform=ax.transAxes, ha='center', fontsize=9, color=GRIS, style='italic')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'asia_transformacion.png', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('Creado: asia_transformacion.png')


def main():
    print("Generando gráficos de Desequilibrios Globales...")
    grafico_mapa_desequilibrios()
    grafico_dolar_reservas()
    grafico_asia_transformacion()
    print("\n¡Listo! 3 gráficos creados.")


if __name__ == "__main__":
    main()
