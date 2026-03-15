"""
Genera 5 gráficos para la Etapa 4: Bretton Woods (1945-1971)
1. Boom del comercio de posguerra
2. Rondas del GATT y caída de aranceles
3. Los "30 Gloriosos" (crecimiento por región y período)
4. Dilema de Triffin (reservas de oro vs dólares externos)
5. Participación de EEUU en el PIB mundial
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os, sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Estilo compartido ──────────────────────────────────────────
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO  = '#2E75B6'
AZUL_CLARO  = '#0EA5E9'
NARANJA     = '#E8833A'
VERDE       = '#27AE60'
ROJO        = '#E74C3C'
GRIS        = '#7F8C8D'
AMARILLO    = '#F1C40F'
MORADO      = '#8E44AD'

def estilo_base(fig, ax, fuente_texto):
    """Aplica estilo base consistente"""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.tick_params(colors='#555555', labelsize=10)
    ax.grid(axis='y', alpha=0.3, color='#CCCCCC')
    fig.text(0.5, 0.01, fuente_texto, ha='center', fontsize=8, color='#888888', style='italic')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 1: Boom del comercio de posguerra
# ═══════════════════════════════════════════════════════════════
def grafico_comercio_posguerra():
    # Exportaciones mundiales de mercancías (miles de millones USD corrientes)
    # Fuentes: OMC, UN Statistical Yearbook
    years = [1948, 1950, 1953, 1955, 1958, 1960, 1963, 1965, 1968, 1970, 1973, 1975]
    exports = [58, 61, 82, 94, 108, 128, 154, 186, 239, 316, 579, 873]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.fill_between(years, exports, alpha=0.15, color=AZUL_MEDIO)
    ax.plot(years, exports, color=AZUL_OSCURO, linewidth=2.5, marker='o', markersize=6, zorder=5)

    # Anotar valores clave
    for y, e in [(1948, 58), (1960, 128), (1970, 316), (1973, 579)]:
        ax.annotate(f'${e}B', (y, e), textcoords='offset points',
                   xytext=(0, 14), ha='center', fontsize=9, fontweight='bold', color=AZUL_OSCURO)

    # Marcar Bretton Woods
    ax.axvline(x=1971, color=ROJO, linestyle='--', alpha=0.7, linewidth=1.5)
    ax.text(1971.3, max(exports)*0.75, 'Fin de\nBretton Woods\n(1971)',
            fontsize=9, color=ROJO, va='center')

    # Zona Bretton Woods
    ax.axvspan(1948, 1971, alpha=0.06, color=AZUL_MEDIO)

    ax.set_title('Boom del comercio mundial de posguerra', fontsize=15, fontweight='bold',
                color=AZUL_OSCURO, pad=12)
    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('Exportaciones mundiales\n(miles de millones USD corrientes)', fontsize=11)
    ax.set_xlim(1946, 1977)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${int(x)}'))

    # Nota: x5 en dos décadas
    ax.text(0.05, 0.92, 'El comercio se multiplicó\npor 5 entre 1948 y 1970',
            transform=ax.transAxes, fontsize=10, color=AZUL_OSCURO,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#EBF5FB', edgecolor=AZUL_CLARO, alpha=0.9))

    estilo_base(fig, ax, 'Fuente: OMC — Evolución del comercio mundial de mercancías')

    path = os.path.join(OUTPUT_DIR, 'comercio_posguerra.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 2: Rondas del GATT y caída de aranceles
# ═══════════════════════════════════════════════════════════════
def grafico_rondas_gatt():
    # Rondas del GATT con datos de aranceles promedio (países participantes)
    # Fuente: OMC, Bown & Irwin (2015), WTO website
    rondas = [
        ('Pre-GATT\n(1947)', 1947, 22.0, 23),
        ('Geneva\n(1947)', 1947, 17.3, 23),
        ('Annecy\n(1949)', 1949, 16.0, 13),
        ('Torquay\n(1951)', 1951, 15.0, 38),
        ('Geneva\n(1956)', 1956, 14.5, 26),
        ('Dillon\n(1960-61)', 1961, 13.0, 26),
        ('Kennedy\n(1964-67)', 1967, 8.7, 62),
        ('Tokyo\n(1973-79)', 1979, 6.3, 102),
        ('Uruguay\n(1986-94)', 1994, 3.9, 123),
    ]

    nombres = [r[0] for r in rondas]
    aranceles = [r[2] for r in rondas]
    paises = [r[3] for r in rondas]

    fig, ax = plt.subplots(figsize=(11, 6))

    # Colores: azul para rondas BW, gris para posteriores
    colores = [GRIS] + [AZUL_MEDIO]*5 + [AZUL_OSCURO] + [NARANJA]*2

    bars = ax.bar(range(len(nombres)), aranceles, color=colores, edgecolor='white', linewidth=0.5, width=0.7)

    # Valores sobre las barras
    for i, (bar, arancel, n_paises) in enumerate(zip(bars, aranceles, paises)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{arancel}%', ha='center', va='bottom', fontsize=10, fontweight='bold',
                color=colores[i])
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                f'{n_paises}\npaíses', ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')

    ax.set_xticks(range(len(nombres)))
    ax.set_xticklabels(nombres, fontsize=8.5)
    ax.set_ylabel('Arancel promedio (%)', fontsize=11)
    ax.set_title('Las rondas del GATT: reducción progresiva de aranceles',
                fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_ylim(0, 26)

    # Bracket para período Bretton Woods
    ax.annotate('', xy=(0.5, 24.5), xytext=(6.5, 24.5),
                arrowprops=dict(arrowstyle='<->', color=AZUL_MEDIO, lw=1.5))
    ax.text(3.5, 25.2, 'Período Bretton Woods', ha='center', fontsize=9,
            color=AZUL_MEDIO, fontweight='bold')

    estilo_base(fig, ax, 'Fuente: OMC, Bown & Irwin (2015) — Aranceles promedio de países miembros GATT')

    path = os.path.join(OUTPUT_DIR, 'rondas_gatt.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 3: Los "30 Gloriosos"
# ═══════════════════════════════════════════════════════════════
def grafico_treinta_gloriosos():
    # Tasa de crecimiento anual promedio del PIB per cápita (%)
    # Fuente: Maddison Project Database 2020
    periodos = ['1870-1913', '1913-1950', '1950-1973', '1973-2000']

    # Datos de Maddison (tasas anualizadas promedio)
    datos = {
        'Europa Occ.': [1.3, 0.9, 4.1, 1.9],
        'EEUU':        [1.8, 1.6, 2.4, 1.9],
        'Japón':       [1.5, 0.9, 8.1, 2.1],
        'Am. Latina':  [1.5, 1.4, 2.5, 0.8],
        'Mundo':       [1.3, 0.9, 2.9, 1.4],
    }

    colores = [AZUL_OSCURO, AZUL_CLARO, ROJO, NARANJA, GRIS]

    x = np.arange(len(periodos))
    width = 0.15
    n = len(datos)

    fig, ax = plt.subplots(figsize=(11, 6.5))

    for i, (region, tasas) in enumerate(datos.items()):
        offset = (i - n/2 + 0.5) * width
        bars = ax.bar(x + offset, tasas, width, label=region, color=colores[i],
                     edgecolor='white', linewidth=0.5)
        # Valor sobre barras del período 1950-1973
        ax.text(x[2] + offset, tasas[2] + 0.15, f'{tasas[2]}%',
                ha='center', fontsize=8, fontweight='bold', color=colores[i])

    # Resaltar período 1950-1973
    ax.axvspan(x[2] - 0.45, x[2] + 0.45, alpha=0.08, color=VERDE, zorder=0)
    ax.text(x[2], -0.8, '← Los "30 Gloriosos" →', ha='center', fontsize=10,
            fontweight='bold', color=VERDE)

    ax.set_xticks(x)
    ax.set_xticklabels(periodos, fontsize=11)
    ax.set_ylabel('Crecimiento anual promedio del PIB per cápita (%)', fontsize=10)
    ax.set_title('Los "Treinta Gloriosos": la edad dorada del capitalismo',
                fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
    ax.set_ylim(-1, 9.5)

    # Nota sobre Japón
    ax.annotate('Japón: "milagro\neconómico"', xy=(x[2] + 0.15, 8.1),
               xytext=(x[2] + 0.55, 8.8), fontsize=8.5, color=ROJO,
               arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.2))

    estilo_base(fig, ax, 'Fuente: Maddison Project Database 2020 — Tasas de crecimiento anualizadas')

    path = os.path.join(OUTPUT_DIR, 'treinta_gloriosos.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 4: Dilema de Triffin
# ═══════════════════════════════════════════════════════════════
def grafico_triffin():
    # Reservas de oro de EEUU vs pasivos externos en dólares
    # Fuente: Federal Reserve, BIS, St. Louis Fed
    years = [1948, 1950, 1952, 1954, 1956, 1958, 1960, 1962, 1964, 1966, 1968, 1970, 1971]

    # Reservas de oro de EEUU (miles de millones USD a $35/oz)
    gold = [24.4, 22.8, 23.3, 21.8, 22.1, 20.6, 17.8, 16.1, 15.5, 13.2, 10.9, 11.1, 10.2]

    # Pasivos externos en dólares (miles de millones USD)
    # Incluye dólares en bancos centrales y oficiales extranjeros
    dollar_liabilities = [7.3, 8.9, 10.5, 11.8, 13.5, 15.2, 18.7, 21.2, 23.8, 26.4, 31.5, 40.2, 50.7]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(years, gold, color='#DAA520', linewidth=2.5, marker='s', markersize=6,
            label='Reservas de oro de EEUU', zorder=5)
    ax.fill_between(years, gold, alpha=0.1, color='#DAA520')

    ax.plot(years, dollar_liabilities, color=AZUL_OSCURO, linewidth=2.5, marker='o', markersize=6,
            label='Dólares en manos extranjeras', zorder=5)
    ax.fill_between(years, dollar_liabilities, alpha=0.1, color=AZUL_OSCURO)

    # Encontrar punto de cruce aproximado (~1960)
    ax.axvline(x=1960, color=ROJO, linestyle=':', alpha=0.5, linewidth=1.5)

    # Flecha señalando el cruce
    ax.annotate('Las líneas se cruzan:\nmás dólares afuera\nque oro adentro',
               xy=(1960, 18), xytext=(1953, 35),
               fontsize=9, color=ROJO, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5),
               bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDEDEC', edgecolor=ROJO, alpha=0.9))

    # Marcar Nixon Shock
    ax.axvline(x=1971, color=ROJO, linestyle='--', alpha=0.7, linewidth=2)
    ax.text(1971, 52, 'Nixon\ncierra la\nventanilla\n(ago. 1971)',
            ha='center', fontsize=9, color=ROJO, fontweight='bold')

    ax.set_title('El dilema de Triffin: la contradicción del sistema Bretton Woods',
                fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('Miles de millones de USD', fontsize=11)
    ax.legend(loc='center left', fontsize=10, framealpha=0.9)
    ax.set_xlim(1946, 1973)
    ax.set_ylim(0, 58)

    # Nota explicativa
    ax.text(0.02, 0.02, 'Para dar liquidez al mundo, EEUU debía tener déficit.\n'
            'Pero el déficit erosionaba la confianza en el dólar.',
            transform=ax.transAxes, fontsize=8.5, color='#555555', va='bottom',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F9F9F9', edgecolor='#CCCCCC'))

    estilo_base(fig, ax, 'Fuente: Federal Reserve, BIS — Reservas de oro y pasivos externos de EEUU')

    path = os.path.join(OUTPUT_DIR, 'dilema_triffin.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
# GRÁFICO 5: Participación de EEUU en el PIB mundial
# ═══════════════════════════════════════════════════════════════
def grafico_eeuu_pib():
    # Participación de EEUU en el PIB mundial (%)
    # Fuente: Maddison Project Database, World Bank
    years = [1945, 1948, 1950, 1953, 1955, 1958, 1960, 1963, 1965, 1968, 1970, 1973, 1975, 1980]

    eeuu_share = [50, 48, 41, 39, 38, 36, 34, 33, 32, 31, 30, 27, 25, 23]

    # Participación de Europa Occ. + Japón (convergencia/catching up)
    europa_japon = [10, 15, 20, 23, 25, 27, 29, 31, 32, 33, 34, 36, 35, 34]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.fill_between(years, eeuu_share, alpha=0.15, color=AZUL_OSCURO)
    ax.plot(years, eeuu_share, color=AZUL_OSCURO, linewidth=2.5, marker='o', markersize=6,
            label='EEUU', zorder=5)

    ax.fill_between(years, europa_japon, alpha=0.15, color=NARANJA)
    ax.plot(years, europa_japon, color=NARANJA, linewidth=2.5, marker='s', markersize=6,
            label='Europa Occidental + Japón', zorder=5)

    # Anotar valores clave
    ax.annotate('EEUU: 50%\n(posguerra)', xy=(1945, 50), xytext=(1949, 48),
               fontsize=9, color=AZUL_OSCURO, fontweight='bold')

    ax.annotate('EEUU: 27%', xy=(1973, 27), xytext=(1975, 30),
               fontsize=9, color=AZUL_OSCURO, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=1))

    # Zona Bretton Woods
    ax.axvspan(1945, 1971, alpha=0.05, color=AZUL_MEDIO, zorder=0)
    ax.axvline(x=1971, color=ROJO, linestyle='--', alpha=0.5, linewidth=1.5)
    ax.text(1971, 51, 'Fin de BW', fontsize=8, color=ROJO, ha='center')

    # Nota sobre catching up
    ax.annotate('Europa y Japón\nrecuperan terreno\n("catching up")',
               xy=(1965, 32), xytext=(1956, 42),
               fontsize=9, color=NARANJA, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.2))

    ax.set_title('La paradoja de Bretton Woods: EEUU pierde peso relativo',
                fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_xlabel('Año', fontsize=11)
    ax.set_ylabel('Participación en el PIB mundial (%)', fontsize=11)
    ax.legend(loc='center right', fontsize=10, framealpha=0.9)
    ax.set_xlim(1943, 1982)
    ax.set_ylim(0, 55)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}%'))

    estilo_base(fig, ax, 'Fuente: Maddison Project Database, World Bank — Participación en PIB mundial (USD corrientes)')

    path = os.path.join(OUTPUT_DIR, 'eeuu_pib_mundial.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generando gráficos de Etapa 4: Bretton Woods...")
    grafico_comercio_posguerra()
    grafico_rondas_gatt()
    grafico_treinta_gloriosos()
    grafico_triffin()
    grafico_eeuu_pib()
    print("\n¡5 gráficos de Etapa 4 generados!")
