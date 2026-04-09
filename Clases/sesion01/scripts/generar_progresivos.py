"""
Genera graficos progresivos para Sesion 1 (Clase 1).
14 graficos x ~3 pasos = ~43 PNGs.

ALTA PRIORIDAD (9):
  1. dilema_triffin (3 pasos)
  2. eeuu_pib_mundial (3 pasos)
  3. china_exportaciones (3 pasos)
  4. rondas_gatt (3 pasos)
  5. balanza_pagos_estructura (3 pasos)
  6. identidad_ahorro_inversion (3 pasos)
  7. ciclo_argentino (4 pasos)
  8. convertibilidad_timeline (3 pasos)
  9. asia_transformacion (3 pasos)

MEDIA PRIORIDAD (5):
  10. apertura_comercial_fases (3 pasos)
  11. costos_transporte_comunicacion (3 pasos)
  12. trayectorias_regionales (3 pasos)
  13. resumen_indicadores (3 pasos)
  14. indice_colapso (3 pasos)
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import numpy as np
import os, sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === Paleta principal (line charts) ===
AZUL = '#1F4E79'
AZUL_M = '#2E75B6'
CELESTE = '#0EA5E9'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#7F8C8D'
AMARILLO = '#F1C40F'
MORADO = '#8E44AD'
ROJO_CHINA = '#DE2910'
ORO = '#DAA520'

# === Paleta diagramas (patches) ===
D_AZUL = '#1F4E79'
D_AZUL_CL = '#5B9BD5'
D_VERDE = '#70AD47'
D_ROJO = '#C00000'
D_NARANJA = '#ED7D31'
D_GRIS = '#7F7F7F'
D_AMARILLO = '#FFC000'


def estilo_base(fig, ax, fuente):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCC')
    ax.spines['bottom'].set_color('#CCC')
    ax.tick_params(colors='#555', labelsize=10)
    ax.grid(axis='y', alpha=0.3, color='#CCC')
    fig.text(0.5, 0.01, fuente, ha='center', fontsize=8, color='#888', style='italic')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])


def save(fig, name, paso):
    path = os.path.join(OUTPUT_DIR, f'{name}_paso{paso}.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'  \u2713 {name}_paso{paso}.png')


# =====================================================================
# 1. DILEMA DE TRIFFIN (3 pasos)
#    Paso 1: Solo linea de oro
#    Paso 2: + linea de dolares
#    Paso 3: + cruce + Nixon shock + nota
# =====================================================================
def prog_dilema_triffin():
    print("\n[1/14] Dilema de Triffin...")
    years = [1948,1950,1952,1954,1956,1958,1960,1962,1964,1966,1968,1970,1971]
    gold = [24.4,22.8,23.3,21.8,22.1,20.6,17.8,16.1,15.5,13.2,10.9,11.1,10.2]
    dollars = [7.3,8.9,10.5,11.8,13.5,15.2,18.7,21.2,23.8,26.4,31.5,40.2,50.7]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.plot(years, gold, color=ORO, linewidth=2.5, marker='s', markersize=6,
                label='Reservas de oro de EEUU', zorder=5)
        ax.fill_between(years, gold, alpha=0.1, color=ORO)

        if paso >= 2:
            ax.plot(years, dollars, color=AZUL, linewidth=2.5, marker='o', markersize=6,
                    label='Dolares en manos extranjeras', zorder=5)
            ax.fill_between(years, dollars, alpha=0.1, color=AZUL)

        if paso >= 3:
            ax.axvline(x=1960, color=ROJO, linestyle=':', alpha=0.5, linewidth=1.5)
            ax.annotate('Las lineas se cruzan:\nmas dolares afuera\nque oro adentro',
                        xy=(1960, 18), xytext=(1953, 35),
                        fontsize=9, color=ROJO, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5),
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDEDEC',
                                  edgecolor=ROJO, alpha=0.9))
            ax.axvline(x=1971, color=ROJO, linestyle='--', alpha=0.7, linewidth=2)
            ax.text(1971, 52, 'Nixon\ncierra la\nventanilla\n(ago. 1971)',
                    ha='center', fontsize=9, color=ROJO, fontweight='bold')
            ax.text(0.02, 0.02,
                    'Para dar liquidez al mundo, EEUU debia tener deficit.\n'
                    'Pero el deficit erosionaba la confianza en el dolar.',
                    transform=ax.transAxes, fontsize=8.5, color='#555', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#F9F9F9', edgecolor='#CCC'))

        ax.set_title('El dilema de Triffin: la contradiccion del sistema Bretton Woods',
                      fontsize=14, fontweight='bold', color=AZUL, pad=12)
        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('Miles de millones de USD', fontsize=11)
        ax.legend(loc='center left', fontsize=10, framealpha=0.9)
        ax.set_xlim(1946, 1973)
        ax.set_ylim(0, 58)
        estilo_base(fig, ax, 'Fuente: Federal Reserve, BIS')
        save(fig, 'dilema_triffin', paso)


# =====================================================================
# 2. EEUU PIB MUNDIAL (3 pasos)
#    Paso 1: Solo linea EEUU
#    Paso 2: + linea Europa+Japon
#    Paso 3: + anotaciones catching up + fin BW
# =====================================================================
def prog_eeuu_pib_mundial():
    print("\n[2/14] EEUU PIB mundial...")
    years = [1945,1948,1950,1953,1955,1958,1960,1963,1965,1968,1970,1973,1975,1980]
    eeuu = [50,48,41,39,38,36,34,33,32,31,30,27,25,23]
    eur_jap = [10,15,20,23,25,27,29,31,32,33,34,36,35,34]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.fill_between(years, eeuu, alpha=0.15, color=AZUL)
        ax.plot(years, eeuu, color=AZUL, linewidth=2.5, marker='o', markersize=6,
                label='EEUU', zorder=5)
        ax.annotate('EEUU: 50%\n(posguerra)', xy=(1945, 50), xytext=(1949, 48),
                    fontsize=9, color=AZUL, fontweight='bold')

        if paso >= 2:
            ax.fill_between(years, eur_jap, alpha=0.15, color=NARANJA)
            ax.plot(years, eur_jap, color=NARANJA, linewidth=2.5, marker='s', markersize=6,
                    label='Europa Occidental + Japon', zorder=5)

        if paso >= 3:
            ax.annotate('EEUU: 27%', xy=(1973, 27), xytext=(1975, 30),
                        fontsize=9, color=AZUL, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=AZUL, lw=1))
            ax.axvspan(1945, 1971, alpha=0.05, color=AZUL_M, zorder=0)
            ax.axvline(x=1971, color=ROJO, linestyle='--', alpha=0.5, linewidth=1.5)
            ax.text(1971, 51, 'Fin de BW', fontsize=8, color=ROJO, ha='center')
            ax.annotate('Europa y Japon\nrecuperan terreno\n("catching up")',
                        xy=(1965, 32), xytext=(1956, 42),
                        fontsize=9, color=NARANJA, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.2))

        ax.set_title('La paradoja de Bretton Woods: EEUU pierde peso relativo',
                      fontsize=14, fontweight='bold', color=AZUL, pad=12)
        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('Participacion en el PIB mundial (%)', fontsize=11)
        ax.legend(loc='center right', fontsize=10, framealpha=0.9)
        ax.set_xlim(1943, 1982)
        ax.set_ylim(0, 55)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}%'))
        estilo_base(fig, ax, 'Fuente: Maddison Project Database, World Bank')
        save(fig, 'eeuu_pib_mundial', paso)


# =====================================================================
# 3. CHINA EXPORTACIONES (3 pasos)
#    Paso 1: Solo linea EEUU
#    Paso 2: + linea China
#    Paso 3: + anotaciones OMC + cruce
# =====================================================================
def prog_china_exportaciones():
    print("\n[3/14] China exportaciones...")
    years = list(range(1980, 2024))
    china = [
        0.9,1.0,1.1,1.1,1.3,1.4,1.5,1.6,1.7,1.8,
        1.8,2.0,2.2,2.4,2.7,2.9,2.8,3.2,3.3,3.4,
        3.9,4.3,5.0,5.8,6.5,7.3,8.0,8.7,8.9,9.6,
        10.3,10.4,11.1,11.7,12.3,13.7,13.1,12.8,12.7,13.1,
        14.7,15.1,14.4,14.2
    ]
    eeuu = [
        11.0,11.5,10.8,10.5,11.0,10.5,10.0,10.0,11.0,11.5,
        11.3,11.8,11.5,12.0,11.8,11.3,11.5,12.0,12.0,11.5,
        12.3,11.8,10.8,9.8,9.0,8.7,8.6,8.3,8.1,8.5,
        8.4,8.1,8.4,8.4,8.5,9.1,9.1,8.7,8.5,8.6,
        7.9,7.9,8.0,8.3
    ]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(11, 6.5))

        # Paso 1: solo EEUU
        ax.plot(years, eeuu, color=AZUL, linewidth=2, linestyle='--',
                label='EEUU', zorder=5, alpha=0.8)

        if paso >= 2:
            ax.fill_between(years, china, alpha=0.15, color=ROJO_CHINA)
            ax.plot(years, china, color=ROJO_CHINA, linewidth=2.5, label='China', zorder=5)
            ax.text(1982, 1.5, '0.9%\n(1980)', fontsize=8.5, color=ROJO_CHINA, ha='center')
            ax.text(2021, 15.8, '15.1%\n(2021)', fontsize=9, color=ROJO_CHINA,
                    ha='center', fontweight='bold')

        if paso >= 3:
            ax.axvline(x=2001, color=ROJO_CHINA, linestyle=':', alpha=0.6, linewidth=2)
            ax.annotate('China entra\na la OMC\n(2001)', xy=(2001, 4.3), xytext=(1993, 8),
                        fontsize=10, color=ROJO_CHINA, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=ROJO_CHINA, lw=1.5),
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0',
                                  edgecolor=ROJO_CHINA, alpha=0.9))
            ax.annotate('China supera\na EEUU (~2009)', xy=(2009, 9.6), xytext=(2013, 6),
                        fontsize=9, color='#555', fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color='#555', lw=1))

        ax.set_title('El ascenso de China: de actor marginal a "fabrica del mundo"',
                      fontsize=15, fontweight='bold', color=AZUL, pad=12)
        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('Participacion en exportaciones mundiales (%)', fontsize=11)
        ax.legend(loc='center left', fontsize=11, framealpha=0.9)
        ax.set_xlim(1979, 2025)
        ax.set_ylim(0, 18)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}%'))
        estilo_base(fig, ax, 'Fuente: OMC, UNCTAD')
        save(fig, 'china_exportaciones', paso)


# =====================================================================
# 4. RONDAS GATT (3 pasos)
#    Paso 1: Pre-GATT + primeras 3 rondas (Geneva, Annecy, Torquay)
#    Paso 2: + rondas BW (Geneva56, Dillon, Kennedy)
#    Paso 3: + post-BW (Tokyo, Uruguay) + bracket
# =====================================================================
def prog_rondas_gatt():
    print("\n[4/14] Rondas GATT...")
    nombres = ['Pre-GATT\n(1947)','Geneva\n(1947)','Annecy\n(1949)','Torquay\n(1951)',
               'Geneva\n(1956)','Dillon\n(1960-61)','Kennedy\n(1964-67)',
               'Tokyo\n(1973-79)','Uruguay\n(1986-94)']
    aranceles = [22.0, 17.3, 16.0, 15.0, 14.5, 13.0, 8.7, 6.3, 3.9]
    paises = [23, 23, 13, 38, 26, 26, 62, 102, 123]
    colores = [GRIS] + [AZUL_M]*5 + [AZUL] + [NARANJA]*2

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(11, 6))

        # Determinar cuantas barras mostrar
        if paso == 1:
            n_bars = 4  # Pre-GATT + 3 primeras
        elif paso == 2:
            n_bars = 7  # + Geneva56, Dillon, Kennedy
        else:
            n_bars = 9  # todas

        # Siempre dibujar el eje completo
        ax.set_xticks(range(len(nombres)))
        ax.set_xticklabels(nombres, fontsize=8.5)

        bars = ax.bar(range(n_bars), aranceles[:n_bars],
                       color=colores[:n_bars], edgecolor='white', linewidth=0.5, width=0.7)

        for i, (bar, arancel, n_p) in enumerate(zip(bars, aranceles[:n_bars], paises[:n_bars])):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                    f'{arancel}%', ha='center', va='bottom', fontsize=10,
                    fontweight='bold', color=colores[i])
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                    f'{n_p}\npaises', ha='center', va='center', fontsize=7.5,
                    color='white', fontweight='bold')

        if paso >= 3:
            ax.annotate('', xy=(0.5, 24.5), xytext=(6.5, 24.5),
                        arrowprops=dict(arrowstyle='<->', color=AZUL_M, lw=1.5))
            ax.text(3.5, 25.2, 'Periodo Bretton Woods', ha='center', fontsize=9,
                    color=AZUL_M, fontweight='bold')

        ax.set_ylabel('Arancel promedio (%)', fontsize=11)
        ax.set_title('Las rondas del GATT: reduccion progresiva de aranceles',
                      fontsize=15, fontweight='bold', color=AZUL, pad=12)
        ax.set_ylim(0, 26)
        ax.set_xlim(-0.5, 8.5)
        estilo_base(fig, ax, 'Fuente: OMC, Bown & Irwin (2015)')
        save(fig, 'rondas_gatt', paso)


# =====================================================================
# 5. BALANZA DE PAGOS ESTRUCTURA (3 pasos)
#    Paso 1: Solo caja CC
#    Paso 2: + cajas CK y CF + flechas
#    Paso 3: + identidad fundamental
# =====================================================================
def prog_balanza_pagos_estructura():
    print("\n[5/14] Balanza de pagos estructura...")

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 10)
        ax.axis('off')

        ax.text(6, 9.5, 'BALANZA DE PAGOS', fontsize=20, fontweight='bold',
                ha='center', color=D_AZUL)
        ax.text(6, 9.0, 'Registro de todas las transacciones entre un pais y el resto del mundo',
                fontsize=11, ha='center', color=D_GRIS, style='italic')

        main_box = mpatches.FancyBboxPatch((0.5, 0.5), 11, 8,
                    boxstyle='round,pad=0.05', facecolor='white',
                    edgecolor=D_AZUL, linewidth=2)
        ax.add_patch(main_box)

        # CC siempre visible
        cc = mpatches.FancyBboxPatch((1, 5), 3.2, 3, boxstyle='round,pad=0.03',
                    facecolor='#E2F0D9', edgecolor=D_VERDE, linewidth=2)
        ax.add_patch(cc)
        ax.text(2.6, 7.6, 'CUENTA', fontsize=12, fontweight='bold', ha='center', color=D_VERDE)
        ax.text(2.6, 7.2, 'CORRIENTE', fontsize=12, fontweight='bold', ha='center', color=D_VERDE)
        ax.text(2.6, 6.5, '\u2022 Bienes (X - M)', fontsize=9, ha='center')
        ax.text(2.6, 6.1, '\u2022 Servicios', fontsize=9, ha='center')
        ax.text(2.6, 5.7, '\u2022 Rentas (intereses,', fontsize=9, ha='center')
        ax.text(2.6, 5.4, '  dividendos)', fontsize=9, ha='center')

        if paso >= 2:
            # CK
            ck = mpatches.FancyBboxPatch((4.5, 5), 3, 3, boxstyle='round,pad=0.03',
                        facecolor='#FFF2CC', edgecolor=D_NARANJA, linewidth=2)
            ax.add_patch(ck)
            ax.text(6, 7.6, 'CUENTA', fontsize=12, fontweight='bold', ha='center', color=D_NARANJA)
            ax.text(6, 7.2, 'CAPITAL', fontsize=12, fontweight='bold', ha='center', color=D_NARANJA)
            ax.text(6, 6.5, '\u2022 Transferencias', fontsize=9, ha='center')
            ax.text(6, 6.1, '  de capital', fontsize=9, ha='center')
            ax.text(6, 5.7, '\u2022 Activos no', fontsize=9, ha='center')
            ax.text(6, 5.4, '  financieros', fontsize=9, ha='center')

            # CF
            cf = mpatches.FancyBboxPatch((7.8, 5), 3.2, 3, boxstyle='round,pad=0.03',
                        facecolor='#DEEBF7', edgecolor=D_AZUL_CL, linewidth=2)
            ax.add_patch(cf)
            ax.text(9.4, 7.6, 'CUENTA', fontsize=12, fontweight='bold', ha='center', color=D_AZUL)
            ax.text(9.4, 7.2, 'FINANCIERA', fontsize=12, fontweight='bold', ha='center', color=D_AZUL)
            ax.text(9.4, 6.5, '\u2022 Inversion directa', fontsize=9, ha='center')
            ax.text(9.4, 6.1, '\u2022 Inversion cartera', fontsize=9, ha='center')
            ax.text(9.4, 5.7, '\u2022 Prestamos', fontsize=9, ha='center')
            ax.text(9.4, 5.4, '\u2022 Reservas BCRA', fontsize=9, ha='center')

            # Flechas
            ax.annotate('', xy=(4.4, 6.5), xytext=(4.6, 6.5),
                        arrowprops=dict(arrowstyle='<->', color=D_GRIS, lw=1.5))
            ax.annotate('', xy=(7.5, 6.5), xytext=(7.7, 6.5),
                        arrowprops=dict(arrowstyle='<->', color=D_GRIS, lw=1.5))

        if paso >= 3:
            eq = mpatches.FancyBboxPatch((1, 1.5), 10, 2.5, boxstyle='round,pad=0.03',
                        facecolor='#F2F2F2', edgecolor=D_GRIS, linewidth=1)
            ax.add_patch(eq)
            ax.text(6, 3.5, 'IDENTIDAD FUNDAMENTAL', fontsize=11, fontweight='bold',
                    ha='center', color=D_AZUL)
            ax.text(6, 2.8, 'Cuenta Corriente + Cuenta Capital + Cuenta Financiera = 0',
                    fontsize=12, ha='center', fontweight='bold')
            ax.text(6, 2.1, 'Si CC < 0 (deficit), debe financiarse con entrada de capitales (CF > 0)',
                    fontsize=10, ha='center', color=D_GRIS)

        plt.tight_layout()
        save(fig, 'balanza_pagos_estructura', paso)


# =====================================================================
# 6. IDENTIDAD AHORRO-INVERSION (4 pasos)
#    Paso 1: La identidad con variables definidas
#    Paso 2: Los tres balances (cajas con definiciones)
#    Paso 3: El mecanismo causal (cadena de flechas)
#    Paso 4: El caso Argentina
# =====================================================================
def prog_identidad_ahorro_inversion():
    print("\n[6/14] Identidad ahorro-inversion...")

    for paso in range(1, 5):
        fig, ax = plt.subplots(figsize=(14, 11))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 13)
        ax.axis('off')

        # Titulo
        ax.text(7, 12.5, 'LA IDENTIDAD AHORRO-INVERSION', fontsize=22,
                fontweight='bold', ha='center', color=D_AZUL)
        ax.text(7, 12.0, 'De la contabilidad nacional al sector externo',
                fontsize=12, ha='center', color=D_GRIS, style='italic')

        # --- PASO 1: Formula + definiciones ---
        # Formula box (siempre visible)
        formula_box = mpatches.FancyBboxPatch((1, 9.5), 12, 2, boxstyle='round,pad=0.05',
                    facecolor='#F0F0F0', edgecolor=D_AZUL, linewidth=2)
        ax.add_patch(formula_box)
        ax.text(7, 10.5, 'CC  =  ( S_priv  \u2212  I )  +  ( T  \u2212  G )',
                fontsize=22, fontweight='bold', ha='center', va='center',
                family='monospace', color='#333')

        # Definiciones debajo de la formula (siempre visibles)
        defs_y = 9.0
        ax.text(2.5, defs_y, 'CC = Cuenta Corriente', fontsize=12,
                ha='center', color=D_AZUL, fontweight='bold')
        ax.text(5.8, defs_y, 'S_priv = Ahorro privado', fontsize=12,
                ha='center', color=D_VERDE, fontweight='bold')
        ax.text(9.2, defs_y, 'I = Inversion', fontsize=12,
                ha='center', color=D_VERDE, fontweight='bold')
        ax.text(12, defs_y, 'T = Impuestos', fontsize=12,
                ha='center', color=D_NARANJA, fontweight='bold')
        ax.text(2.5, defs_y - 0.5, '(sector externo)', fontsize=11,
                ha='center', color=D_GRIS)
        ax.text(5.8, defs_y - 0.5, '(familias + empresas)', fontsize=11,
                ha='center', color=D_GRIS)
        ax.text(9.2, defs_y - 0.5, '(publica + privada)', fontsize=11,
                ha='center', color=D_GRIS)
        ax.text(12, defs_y - 0.5, 'G = Gasto publico', fontsize=12,
                ha='center', color=D_NARANJA, fontweight='bold')

        # Nota: identidad contable
        ax.text(7, 7.9, 'Es una identidad contable: siempre se cumple, como 1+1=2',
                fontsize=11, ha='center', color=D_GRIS, style='italic')

        if paso >= 2:
            # --- PASO 2: Tres cajas de balances ---
            # Balance Externo (azul)
            b1 = mpatches.FancyBboxPatch((0.5, 4.5), 3.8, 3, boxstyle='round,pad=0.03',
                        facecolor='#DEEBF7', edgecolor=D_AZUL_CL, linewidth=2)
            ax.add_patch(b1)
            ax.text(2.4, 7.0, 'SECTOR', fontsize=13, fontweight='bold', ha='center', color=D_AZUL)
            ax.text(2.4, 6.5, 'EXTERNO', fontsize=13, fontweight='bold', ha='center', color=D_AZUL)
            ax.text(2.4, 5.8, 'CC', fontsize=20, fontweight='bold', ha='center', color='#333')
            ax.text(2.4, 5.2, 'Cuenta Corriente', fontsize=11, ha='center', color=D_GRIS)
            ax.text(2.4, 4.7, 'CC > 0: superavit', fontsize=11, ha='center', color=D_VERDE)

            # Signo =
            ax.text(4.6, 5.8, '=', fontsize=22, fontweight='bold', ha='center', color='#333')

            # Resultado Privado (verde)
            b2 = mpatches.FancyBboxPatch((5.0, 4.5), 4, 3, boxstyle='round,pad=0.03',
                        facecolor='#E2F0D9', edgecolor=D_VERDE, linewidth=2)
            ax.add_patch(b2)
            ax.text(7.0, 7.0, 'RESULTADO', fontsize=13, fontweight='bold', ha='center', color=D_VERDE)
            ax.text(7.0, 6.5, 'PRIVADO', fontsize=13, fontweight='bold', ha='center', color=D_VERDE)
            ax.text(7.0, 5.8, 'S_priv \u2212 I', fontsize=18, fontweight='bold',
                    ha='center', color='#333', family='monospace')
            ax.text(7.0, 5.2, 'Ahorro \u2212 Inversion', fontsize=11, ha='center', color=D_GRIS)
            ax.text(7.0, 4.7, '(familias + empresas)', fontsize=11, ha='center', color=D_GRIS)

            # Signo +
            ax.text(9.3, 5.8, '+', fontsize=22, fontweight='bold', ha='center', color='#333')

            # Resultado Fiscal (naranja)
            b3 = mpatches.FancyBboxPatch((9.7, 4.5), 3.8, 3, boxstyle='round,pad=0.03',
                        facecolor='#FFF2CC', edgecolor=D_NARANJA, linewidth=2)
            ax.add_patch(b3)
            ax.text(11.6, 7.0, 'RESULTADO', fontsize=13, fontweight='bold', ha='center', color=D_NARANJA)
            ax.text(11.6, 6.5, 'FISCAL', fontsize=13, fontweight='bold', ha='center', color=D_NARANJA)
            ax.text(11.6, 5.8, 'T \u2212 G', fontsize=20, fontweight='bold', ha='center', color='#333')
            ax.text(11.6, 5.2, 'Recaudacion \u2212 Gasto', fontsize=11, ha='center', color=D_GRIS)
            ax.text(11.6, 4.7, '(gobierno)', fontsize=11, ha='center', color=D_GRIS)

        if paso >= 3:
            # --- PASO 3: Mecanismo causal (cadena de flechas) ---
            mec_box = mpatches.FancyBboxPatch((0.5, 1.8), 13, 2.3, boxstyle='round,pad=0.05',
                        facecolor='#FFF8F0', edgecolor='#C0C0C0', linewidth=1.5)
            ax.add_patch(mec_box)
            ax.text(7, 3.7, 'EL MECANISMO: del deficit fiscal al deficit externo',
                    fontsize=14, fontweight='bold', ha='center', color=D_AZUL)

            # Cadena con flechas
            pasos_mec = [
                ('Deficit\nfiscal\n(T < G)', D_NARANJA),
                ('\u2192', '#333'),
                ('Mas demanda\ninterna', D_GRIS),
                ('\u2192', '#333'),
                ('Mas\nimportaciones', D_AZUL_CL),
                ('\u2192', '#333'),
                ('Deficit\nexterno\n(CC < 0)', D_ROJO),
                ('\u2192', '#333'),
                ('Necesidad de\nfinanciamiento\nexterno', D_ROJO),
            ]
            x_pos = 1.0
            for txt, col in pasos_mec:
                if txt == '\u2192':
                    ax.text(x_pos, 2.7, txt, fontsize=18, fontweight='bold',
                            ha='center', va='center', color=col)
                    x_pos += 0.7
                else:
                    ax.text(x_pos, 2.7, txt, fontsize=11, fontweight='bold',
                            ha='center', va='center', color=col)
                    x_pos += 1.7

        if paso >= 4:
            # --- PASO 4: Caso Argentina ---
            arg_box = mpatches.FancyBboxPatch((0.5, 0.1), 13, 1.4, boxstyle='round,pad=0.05',
                        facecolor='#FDEDEC', edgecolor=D_ROJO, linewidth=2)
            ax.add_patch(arg_box)
            ax.text(7, 1.1, 'ARGENTINA: deficit fiscal persistente + bajo ahorro privado'
                    '  \u2192  deficit de CC  \u2192  endeudamiento  \u2192  crisis',
                    fontsize=12, ha='center', fontweight='bold', color='#333')
            ax.text(7, 0.5, 'Convertibilidad (1991-2001)  |  Macri (2016-2018)  |  Patron recurrente',
                    fontsize=11, ha='center', color=D_GRIS)

        plt.tight_layout()
        save(fig, 'identidad_ahorro_inversion', paso)


# =====================================================================
# 7. CICLO ARGENTINO (4 pasos)
#    Paso 1: Solo fase 1 (Estabilizacion)
#    Paso 2: + fase 2 (Apreciacion) + flecha 1->2
#    Paso 3: + fase 3 (Crisis) + flecha 2->3
#    Paso 4: + fase 4 (Recuperacion) + flechas 3->4, 4->1 + ejemplos
# =====================================================================
def prog_ciclo_argentino():
    print("\n[7/14] Ciclo argentino...")
    centro_x, centro_y = 7, 6.5
    radio = 3.2

    fases = [
        {'pos': (centro_x, centro_y + radio), 'color': D_VERDE, 'num': '1',
         'titulo': 'ESTABILIZACION', 'desc': 'Ancla cambiaria\nInflacion baja\nConfianza',
         'desc_pos': (centro_x, centro_y + radio + 2.0), 'desc_ha': 'center'},
        {'pos': (centro_x + radio, centro_y), 'color': D_AMARILLO, 'num': '2',
         'titulo': 'APRECIACION', 'desc': 'Peso se encarece\nDeficit comercial\nEndeudamiento',
         'desc_pos': (centro_x + radio + 1.5, centro_y - 1.8), 'desc_ha': 'center'},
        {'pos': (centro_x, centro_y - radio), 'color': D_ROJO, 'num': '3',
         'titulo': 'CRISIS', 'desc': 'Fuga de capitales\nCaen reservas\nDevaluacion',
         'desc_pos': (centro_x, centro_y - radio - 2.0), 'desc_ha': 'center'},
        {'pos': (centro_x - radio, centro_y), 'color': D_AZUL_CL, 'num': '4',
         'titulo': 'RECUPERACION', 'desc': 'TC competitivo\nSuperavit\nCrecimiento',
         'desc_pos': (centro_x - radio - 1.5, centro_y - 1.8), 'desc_ha': 'center'},
    ]

    arrows = [
        # 1 -> 2 (arriba-derecha a derecha)
        ((centro_x + 1.0, centro_y + radio - 0.6), (centro_x + radio - 0.6, centro_y + 1.0)),
        # 2 -> 3 (derecha a abajo-derecha)
        ((centro_x + radio - 0.6, centro_y - 1.0), (centro_x + 1.0, centro_y - radio + 0.6)),
        # 3 -> 4 (abajo-izquierda a izquierda)
        ((centro_x - 1.0, centro_y - radio + 0.6), (centro_x - radio + 0.6, centro_y - 1.0)),
        # 4 -> 1 (izquierda a arriba-izquierda)
        ((centro_x - radio + 0.6, centro_y + 1.0), (centro_x - 1.0, centro_y + radio - 0.6)),
    ]

    for paso in range(1, 5):
        fig, ax = plt.subplots(figsize=(14, 11))
        ax.set_xlim(0, 14)
        ax.set_ylim(-1.5, 14)
        ax.axis('off')

        ax.text(7, 13.3, 'EL CICLO ARGENTINO', fontsize=22, fontweight='bold',
                ha='center', color=D_AZUL)
        ax.text(7, 12.8, 'El patron que se repite cada 10-15 anos', fontsize=12,
                ha='center', color=D_GRIS, style='italic')

        # Circulo de fondo
        circ_bg = plt.Circle((centro_x, centro_y), radio + 0.5, color='#F0F0F0',
                              fill=True, zorder=0)
        ax.add_patch(circ_bg)

        # Dibujar fases hasta el paso actual
        n_fases = min(paso, 4)
        for i in range(n_fases):
            f = fases[i]
            x, y = f['pos']
            circ = plt.Circle((x, y), 1.2, color=f['color'], fill=True, alpha=0.9, zorder=2)
            ax.add_patch(circ)
            ax.text(x, y + 0.5, f['num'], fontsize=24, fontweight='bold',
                    ha='center', va='center', color='white', zorder=3)
            ax.text(x, y - 0.1, f['titulo'], fontsize=11, fontweight='bold',
                    ha='center', va='center', color='white', zorder=3)
            dx, dy = f['desc_pos']
            ax.text(dx, dy, f['desc'], fontsize=12, ha=f['desc_ha'], va='center')

        # Flechas (una menos que fases, + flecha cierre en paso 4)
        arrow_props = dict(arrowstyle='->', color=D_GRIS, lw=2, connectionstyle='arc3,rad=0.2')
        n_arrows = min(paso, 4) - 1  # paso1=0, paso2=1, paso3=2, paso4=3
        if paso >= 4:
            n_arrows = 4  # incluye 4->1
        for i in range(n_arrows):
            src, dst = arrows[i]
            ax.annotate('', xy=dst, xytext=src, arrowprops=arrow_props)

        # Ejemplos solo en paso 4
        if paso >= 4:
            ax.text(7, -0.1, 'EJEMPLOS: 1991-2001 (Convertibilidad) \u2192 2002 (Crisis)',
                    fontsize=13, ha='center', color=D_AZUL, fontweight='bold')
            ax.text(7, -0.6, '2003-2011 (Recuperacion) \u2192 2012-2015 (Apreciacion) \u2192 2018 (Crisis)',
                    fontsize=13, ha='center', color=D_AZUL)
            ax.text(7, -1.1, '\u00bf2024-?: \u00bfEn que fase estamos?',
                    fontsize=13, ha='center', color=D_ROJO, fontweight='bold')

        plt.tight_layout()
        save(fig, 'ciclo_argentino', paso)


# =====================================================================
# 8. CONVERTIBILIDAD TIMELINE (3 pasos)
#    Paso 1: Solo panel TCR
#    Paso 2: + panel CC
#    Paso 3: + panel Reservas
# =====================================================================
def prog_convertibilidad_timeline():
    print("\n[8/14] Convertibilidad timeline...")
    anos = list(range(1991, 2003))
    tcr = [100, 95, 90, 88, 85, 82, 80, 78, 75, 72, 70, 180]
    cc_pib = [0, -2, -3, -4, -4, -3, -4, -5, -4, -3, -1, 8]
    reservas = [8, 12, 15, 17, 20, 22, 25, 26, 27, 25, 15, 10]

    for paso in range(1, 4):
        fig, axes = plt.subplots(3, 1, figsize=(13, 9), sharex=True)

        # Panel 1: TCR (siempre)
        ax1 = axes[0]
        colores_tcr = [D_VERDE if v >= 100 else D_ROJO for v in tcr]
        ax1.bar(anos, tcr, color=colores_tcr, edgecolor='white')
        ax1.axhline(y=100, color='black', linestyle='--', label='Equilibrio')
        ax1.set_ylabel('TCR (1991=100)', fontsize=10)
        ax1.set_title('Convertibilidad: El Ciclo en 3 Indicadores', fontsize=14,
                       fontweight='bold', color=D_AZUL)
        ax1.text(1992, 105, 'Peso cada vez\nmas caro', fontsize=9, color=D_ROJO)
        ax1.text(2001, 150, 'Devaluacion\n200%', fontsize=9, color=D_VERDE, ha='center')
        ax1.legend(loc='upper right')
        ax1.set_ylim(0, 200)

        # Panel 2: CC
        ax2 = axes[1]
        if paso >= 2:
            colores_cc = [D_VERDE if v >= 0 else D_ROJO for v in cc_pib]
            ax2.bar(anos, cc_pib, color=colores_cc, edgecolor='white')
            ax2.axhline(y=0, color='black', linestyle='-')
            ax2.set_ylabel('CC (% PIB)', fontsize=10)
            ax2.text(1995, -3.5, 'Deficit\npersistente', fontsize=9, color=D_ROJO, ha='center')
            ax2.text(2001, 6, 'Superavit por\ncolapso imports', fontsize=8, color=D_VERDE, ha='center')
            ax2.set_ylim(-6, 10)
        else:
            ax2.axis('off')

        # Panel 3: Reservas
        ax3 = axes[2]
        if paso >= 3:
            ax3.fill_between(anos, reservas, color=D_AZUL_CL, alpha=0.7)
            ax3.plot(anos, reservas, color=D_AZUL, linewidth=2, marker='o')
            ax3.set_ylabel('Reservas (USD bn)', fontsize=10)
            ax3.set_xlabel('Ano', fontsize=11)
            ax3.text(1996, 22, 'Acumulacion', fontsize=9, color=D_AZUL)
            ax3.text(2001, 12, 'Fuga', fontsize=9, color=D_ROJO, ha='center')
            ax3.axvspan(2000, 2002, alpha=0.2, color=D_ROJO)
            ax3.set_ylim(0, 30)
        else:
            ax3.axis('off')

        # Crisis zone en paneles visibles
        for i, ax in enumerate(axes):
            if (i == 0) or (i == 1 and paso >= 2) or (i == 2 and paso >= 3):
                ax.axvspan(2001, 2002, alpha=0.1, color=D_AMARILLO)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

        plt.tight_layout()
        save(fig, 'convertibilidad_timeline', paso)


# =====================================================================
# 9. ASIA TRANSFORMACION (3 pasos)
#    Paso 1: Solo barras deficit (1990-1997)
#    Paso 2: + crisis highlight (1997-1998) + barras 1998-1999
#    Paso 3: + barras superavit (2000-2023) + anotaciones
# =====================================================================
def prog_asia_transformacion():
    print("\n[9/14] Asia transformacion...")
    anos = list(range(1990, 2024))
    asia_cc = [-1.5,-2.0,-1.8,-2.5,-2.0,-3.0,-3.5,-4.0,
               4.0,3.5,
               2.5,2.0,3.0,4.0,4.5,5.5,6.5,7.0,5.0,
               4.0,3.0,2.0,2.5,1.5,2.0,2.5,2.0,1.5,1.0,
               1.0,2.0,3.0,1.5,1.0]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(12, 7))

        if paso == 1:
            n = 8  # 1990-1997
        elif paso == 2:
            n = 10  # 1990-1999
        else:
            n = len(anos)

        colores = [D_ROJO if v < 0 else D_VERDE for v in asia_cc[:n]]
        ax.bar(anos[:n], asia_cc[:n], color=colores, width=0.8, edgecolor='white')
        ax.axhline(y=0, color='black', linewidth=1)

        if paso >= 2:
            ax.axvspan(1997, 1998.5, alpha=0.3, color=D_AMARILLO)
            ax.text(1997.7, 6, 'Crisis\nAsiatica', fontsize=9, fontweight='bold',
                    color=D_NARANJA, ha='center')

        if paso == 1:
            ax.annotate('Deficit y\nendeudamiento', xy=(1993, -3), fontsize=10,
                        color=D_ROJO, ha='center', fontweight='bold')

        if paso >= 3:
            ax.annotate('Deficit y\nendeudamiento', xy=(1993, -3), fontsize=10,
                        color=D_ROJO, ha='center', fontweight='bold')
            ax.annotate('Superavit y\nacumulacion\nde reservas', xy=(2005, 5.5), fontsize=10,
                        color=D_VERDE, ha='center', fontweight='bold')
            ax.annotate('', xy=(2002, 3), xytext=(1995, -2),
                        arrowprops=dict(arrowstyle='->', color=D_AZUL, lw=2))

        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('Cuenta Corriente (% PIB)', fontsize=11)
        ax.set_title('Asia Emergente: De Deudores a Acreedores',
                      fontsize=14, fontweight='bold', color=D_AZUL)
        ax.set_xlim(1989, 2025)
        ax.set_ylim(-5, 8)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.text(0.5, -0.1,
                'Despues de la crisis de 1997, Asia nunca mas quiso depender del capital externo. Fuente: FMI WEO',
                transform=ax.transAxes, ha='center', fontsize=9, color=D_GRIS, style='italic')
        plt.tight_layout()
        save(fig, 'asia_transformacion', paso)


# =====================================================================
# 10. APERTURA COMERCIAL FASES (3 pasos)
#     Paso 1: Linea + Fase 1 (Globalizacion)
#     Paso 2: + Fase 2 (Hiperglobalizacion) + eventos
#     Paso 3: + Fase 3 (Slowbalization) + todos los eventos
# =====================================================================
def prog_apertura_comercial_fases():
    print("\n[10/14] Apertura comercial fases...")
    years = list(range(1960, 2024))
    trade_gdp = [
        24.0,23.8,23.5,24.0,24.2,24.0,24.5,24.3,25.0,25.5,
        26.0,26.3,27.0,29.5,33.0,32.5,33.0,33.5,33.0,34.5,
        35.5,35.0,33.5,32.5,33.5,33.0,32.5,33.5,33.8,35.5,
        36.0,36.5,37.0,37.5,38.5,40.0,41.0,43.0,44.0,45.5,
        47.5,46.5,46.0,47.0,50.0,52.5,55.0,56.5,60.5,52.0,
        56.0,58.5,57.5,57.0,57.5,56.5,53.5,55.5,57.5,56.0,
        51.5,55.0,58.0,56.5
    ]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(12, 6.5))

        # Fase 1 siempre
        ax.axvspan(1960, 1986, alpha=0.08, color=CELESTE, zorder=0)
        ax.text(1973, 20, 'Globalizacion\n(+0.19 pp/ano)', ha='center', fontsize=10,
                color=AZUL_M, fontweight='bold')

        if paso >= 2:
            ax.axvspan(1986, 2008, alpha=0.08, color=VERDE, zorder=0)
            ax.text(1997, 20, 'Hiperglobalizacion\n(+0.52 pp/ano)', ha='center',
                    fontsize=10, color=VERDE, fontweight='bold')

        if paso >= 3:
            ax.axvspan(2008, 2024, alpha=0.08, color=NARANJA, zorder=0)
            ax.text(2016, 20, 'Slowbalization\n(\u22120.04 pp/ano)', ha='center',
                    fontsize=10, color=NARANJA, fontweight='bold')

        # Linea siempre completa
        ax.plot(years, trade_gdp, color=AZUL, linewidth=2.5, zorder=5)
        ax.fill_between(years, trade_gdp, alpha=0.1, color=AZUL_M)

        # Eventos
        if paso >= 2:
            eventos_p2 = [
                (1986, 'Ronda Uruguay\ncomienza', VERDE),
                (2001, 'China\nen OMC', ROJO_CHINA),
            ]
            for yr, txt, c in eventos_p2:
                idx = yr - 1960
                val = trade_gdp[idx]
                ax.axvline(x=yr, color=c, linestyle=':', alpha=0.4, linewidth=1)
                ax.annotate(txt, xy=(yr, val), xytext=(yr, val + 5),
                            fontsize=8, color=c, ha='center', fontweight='bold',
                            arrowprops=dict(arrowstyle='->', color=c, lw=1))

        if paso >= 3:
            eventos_p3 = [
                (2008, 'Crisis\nfinanciera', ROJO),
                (2018, 'Guerra\ncomercial', NARANJA),
            ]
            for yr, txt, c in eventos_p3:
                idx = yr - 1960
                val = trade_gdp[idx]
                ax.axvline(x=yr, color=c, linestyle=':', alpha=0.4, linewidth=1)
                ax.annotate(txt, xy=(yr, val), xytext=(yr, val + 5),
                            fontsize=8, color=c, ha='center', fontweight='bold',
                            arrowprops=dict(arrowstyle='->', color=c, lw=1))

        ax.set_title('Apertura comercial mundial: tres fases de la globalizacion',
                      fontsize=15, fontweight='bold', color=AZUL, pad=12)
        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('Comercio (X+M) como % del PIB mundial', fontsize=11)
        ax.set_xlim(1960, 2024)
        ax.set_ylim(15, 68)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}%'))
        estilo_base(fig, ax, 'Fuente: Banco Mundial, FMI')
        save(fig, 'apertura_comercial_fases', paso)


# =====================================================================
# 11. COSTOS TRANSPORTE Y COMUNICACION (3 pasos)
#     Paso 1: Solo flete maritimo
#     Paso 2: + transporte aereo + container
#     Paso 3: + telefono + zona globalizacion + nota
# =====================================================================
def prog_costos_transporte():
    print("\n[11/14] Costos transporte...")
    ys = [1930,1940,1950,1960,1970,1980,1990,2000,2005]
    sea = [100,90,65,48,35,30,28,23,11]
    air = [100,85,55,38,24,20,14,10,8]
    phone = [100,80,50,25,10,5,2.5,0.5,0.1]
    yc = [1956,1960,1970,1980,1990,2000,2005]
    container = [100,70,40,25,18,12,8]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(11, 6.5))

        ax.plot(ys, sea, color=AZUL, linewidth=2.5, marker='o', markersize=5,
                label='Flete maritimo', zorder=5)

        if paso >= 2:
            ax.plot(ys, air, color=NARANJA, linewidth=2.5, marker='s', markersize=5,
                    label='Transporte aereo', zorder=5)
            ax.plot(yc, container, color=ROJO, linewidth=2, marker='D', markersize=5,
                    label='Container (desde 1956)', linestyle='--', zorder=5)

        if paso >= 3:
            ax.plot(ys, phone, color=VERDE, linewidth=2.5, marker='^', markersize=5,
                    label='Llamada telefonica (NY-Londres)', zorder=5)
            ax.annotate('Telecomunicaciones:\ncosto \u2192 0', xy=(2000, 0.5), xytext=(1985, 30),
                        fontsize=9, color=VERDE, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=VERDE, lw=1.2))
            ax.axvspan(1980, 2005, alpha=0.06, color=CELESTE, zorder=0)
            ax.text(1992, 95, 'Era de la globalizacion', fontsize=10, ha='center',
                    color=AZUL_M, fontweight='bold', alpha=0.7)
            ax.text(0.02, 0.15,
                    'Sin esta revolucion tecnologica,\nlas cadenas globales de valor\nno serian posibles',
                    transform=ax.transAxes, fontsize=9, color='#555',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#F9F9F9', edgecolor='#CCC'))

        ax.set_title('Caida de los costos de transporte y comunicacion',
                      fontsize=15, fontweight='bold', color=AZUL, pad=12)
        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('Indice de costo (1930 = 100)', fontsize=11)
        ax.legend(loc='upper right', fontsize=9.5, framealpha=0.9)
        ax.set_xlim(1928, 2008)
        ax.set_ylim(-3, 110)
        estilo_base(fig, ax, 'Fuente: Our World in Data, Bureau of Transportation Statistics (EEUU)')
        save(fig, 'costos_transporte_comunicacion', paso)


# =====================================================================
# 12. TRAYECTORIAS REGIONALES (3 pasos)
#     Paso 1: Solo Europa Occidental
#     Paso 2: + America Latina + Africa Subsahariana
#     Paso 3: + Asia Oriental (la historia del catching up)
# =====================================================================
def prog_trayectorias_regionales():
    print("\n[12/14] Trayectorias regionales...")
    years = [1820,1840,1850,1870,1900,1913,1929,1938,1950,1960,1970,1980,1990,2000,2010,2018]
    europa = [2100,2300,2600,2900,3700,4500,5300,5200,5500,7500,11000,15000,21000,25500,33000,40000]
    latam = [800,900,1000,1100,1500,1800,2100,2200,2500,3000,4500,6500,5500,7500,9000,14000]
    asia = [800,750,700,800,900,1000,1100,1100,1000,1300,2800,4000,6000,8000,13000,16000]
    africa = [600,600,600,700,800,900,1000,1100,1200,1400,1800,2000,1800,2000,2500,3500]

    # Periodos de fondo
    periodos = [
        (1820, 1913, CELESTE, 0.06),
        (1913, 1950, '#E74C3C', 0.06),
        (1950, 1980, VERDE, 0.06),
        (1980, 2020, MORADO, 0.06),
    ]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(14, 7))

        # Fondo de periodos
        for x0, x1, c, a in periodos:
            ax.axvspan(x0, x1, alpha=a, color=c, zorder=0)

        # Europa siempre
        ax.plot(years, europa, color=AZUL, linewidth=2.5, marker='o', markersize=5,
                label='Europa Occidental', zorder=5)

        if paso >= 2:
            ax.plot(years, latam, color=CELESTE, linewidth=2.5, marker='s', markersize=5,
                    label='America Latina', zorder=5)
            ax.plot(years, africa, color=NARANJA, linewidth=2.5, marker='D', markersize=5,
                    label='Africa Subsahariana', zorder=5)

        if paso >= 3:
            ax.plot(years, asia, color='#E74C3C', linewidth=2.5, marker='^', markersize=5,
                    label='Asia Oriental', zorder=5)

        ax.set_title('Trayectorias regionales: convergencia y divergencia',
                      fontsize=15, fontweight='bold', color=AZUL, pad=12)
        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('PIB per capita (USD 2011 PPP)', fontsize=11)
        ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
        ax.set_xlim(1815, 2025)
        ax.set_ylim(0, 43000)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))
        estilo_base(fig, ax, 'Fuente: Maddison Project Database 2020')
        save(fig, 'trayectorias_regionales', paso)


# =====================================================================
# 13. RESUMEN INDICADORES (3 pasos)
#     Paso 1: Headers + indicadores 1-3
#     Paso 2: + indicadores 4-6
#     Paso 3: + indicadores 7-9
# =====================================================================
def prog_resumen_indicadores():
    print("\n[13/14] Resumen indicadores...")
    indicadores = [
        ('1', 'Indice de comercio', 'I_t = 100 * (Com_t / Com_base)', 'Mide crecimiento del comercio'),
        ('2', 'Participacion regional', 's_r = X_r / X_mundo * 100', 'Quien gana/pierde peso'),
        ('3', 'Concentracion (HHI)', 'HHI = Sum(s_i)^2', 'Diversificacion del comercio'),
        ('4', 'Cobertura de datos', '% paises con datos', 'Calidad de las fuentes'),
        ('5', 'Balanza comercial', 'BC = X - M', 'Competitividad comercial'),
        ('6', 'Apertura comercial', '(X + M) / PIB * 100', 'Integracion al mundo'),
        ('7', 'Terminos del intercambio', 'ToT = Px / Pm * 100', 'Poder de compra externo'),
        ('8', 'Cuenta corriente', 'CC / PIB * 100', 'Sostenibilidad externa'),
        ('9', 'Tipo de cambio real', 'TCR = e * P* / P', 'Competitividad precio'),
    ]

    col_starts = [0.02, 0.08, 0.32, 0.68]

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.axis('off')

        ax.text(0.5, 0.95, 'LOS 9 INDICADORES DE INSERCION EXTERNA',
                fontsize=18, fontweight='bold', ha='center', transform=ax.transAxes,
                color=D_AZUL)

        # Headers
        y_start = 0.85
        row_h = 0.08
        headers = ['#', 'Indicador', 'Formula', 'Interpretacion']
        for header, x in zip(headers, col_starts):
            ax.text(x, y_start + 0.03, header, fontsize=11, fontweight='bold',
                    transform=ax.transAxes, color='white',
                    bbox=dict(boxstyle='round', facecolor=D_AZUL, alpha=0.9))

        # Filas
        if paso == 1:
            n_rows = 3
        elif paso == 2:
            n_rows = 6
        else:
            n_rows = 9

        for i in range(n_rows):
            num, nombre, formula, interp = indicadores[i]
            y = y_start - (i + 1) * row_h
            color_fondo = '#F5F5F5' if i % 2 == 0 else 'white'

            rect = mpatches.FancyBboxPatch((0.01, y - 0.02), 0.98, row_h - 0.01,
                    boxstyle='round,pad=0.01', facecolor=color_fondo, edgecolor='#CCC',
                    transform=ax.transAxes)
            ax.add_patch(rect)

            ax.text(col_starts[0] + 0.02, y + 0.02, num, fontsize=11, fontweight='bold',
                    transform=ax.transAxes, color=D_AZUL)
            ax.text(col_starts[1], y + 0.02, nombre, fontsize=10, transform=ax.transAxes)
            ax.text(col_starts[2], y + 0.02, formula, fontsize=9,
                    transform=ax.transAxes, family='monospace')
            ax.text(col_starts[3], y + 0.02, interp, fontsize=9,
                    transform=ax.transAxes, color=D_GRIS)

        plt.tight_layout()
        save(fig, 'resumen_indicadores', paso)


# =====================================================================
# 14. INDICE COLAPSO (3 pasos)
#     Paso 1: Ascenso pre-guerra (1900-1913)
#     Paso 2: + WWI colapso (1914-1920)
#     Paso 3: + recuperacion + Gran Depresion (1921-1938)
# =====================================================================
def prog_indice_colapso():
    print("\n[14/14] Indice colapso...")
    years = list(range(1900, 1939))
    index = [
        61, 62, 63, 65, 67, 70, 75, 78, 77, 79,   # 1900-1909
        83, 88, 93, 100,                             # 1910-1913
        85, 65, 70, 85, 75,                          # 1914-1918
        75, 85, 75, 80, 85, 88,                      # 1919-1924
        91, 95, 100, 111, 131,                       # 1925-1929
        133, 111, 95, 95,                            # 1930-1933
        97, 100, 105, 122, 112                       # 1934-1938
    ]

    key_points = {
        1913: ('Pico pre-guerra\n(1913=100)', 100),
        1918: ('Fin WWI\n-25%', 75),
        1929: ('Pico 1929\n+33%', 131),
        1932: ('Fondo\nDepresion', 95),
    }

    for paso in range(1, 4):
        fig, ax = plt.subplots(figsize=(14, 7))

        # Determinar rango a mostrar
        if paso == 1:
            n = 14  # 1900-1913
        elif paso == 2:
            n = 21  # 1900-1920
        else:
            n = len(years)

        ax.plot(years[:n], index[:n], color=AZUL, linewidth=2.5, zorder=5)
        ax.fill_between(years[:n], index[:n], alpha=0.15, color=AZUL_M)

        # Linea 100
        ax.axhline(y=100, color='gray', linestyle=':', alpha=0.5)

        # Fondo WWI
        if paso >= 2:
            ax.axvspan(1914, 1918, alpha=0.15, color='#E74C3C',
                        label='Primera Guerra Mundial')

        if paso >= 3:
            ax.axvspan(1929, 1933, alpha=0.15, color=D_AMARILLO,
                        label='Gran Depresion')

        # Key points
        for yr, (txt, val) in key_points.items():
            if yr <= years[n-1]:
                ax.plot(yr, val, 'o', color=ROJO, markersize=8, zorder=6)
                offset_y = 12 if val < 120 else -18
                ax.annotate(txt, xy=(yr, val), xytext=(yr + 1, val + offset_y),
                            fontsize=9, fontweight='bold', color='#333',
                            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                                      edgecolor='#999', alpha=0.9))

        ax.set_title('El colapso del comercio mundial (1914-1932)',
                      fontsize=15, fontweight='bold', color=AZUL, pad=12)
        ax.set_xlabel('Ano', fontsize=11)
        ax.set_ylabel('Indice (1913 = 100)', fontsize=11)
        ax.set_xlim(1898, 1940)
        ax.set_ylim(50, 150)
        if paso >= 2:
            ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', alpha=0.3, color='#CCC')
        plt.tight_layout()
        save(fig, 'indice_colapso', paso)


# =====================================================================
# MAIN
# =====================================================================
if __name__ == '__main__':
    print("=" * 60)
    print("GENERANDO GRAFICOS PROGRESIVOS - CLASE 1")
    print("=" * 60)

    # ALTA PRIORIDAD
    prog_dilema_triffin()
    prog_eeuu_pib_mundial()
    prog_china_exportaciones()
    prog_rondas_gatt()
    prog_balanza_pagos_estructura()
    prog_identidad_ahorro_inversion()
    prog_ciclo_argentino()
    prog_convertibilidad_timeline()
    prog_asia_transformacion()

    # MEDIA PRIORIDAD
    prog_apertura_comercial_fases()
    prog_costos_transporte()
    prog_trayectorias_regionales()
    prog_resumen_indicadores()
    prog_indice_colapso()

    print("\n" + "=" * 60)
    print("LISTO! 43 PNGs progresivos generados.")
    print("=" * 60)
