"""
Genera los 7 gráficos para Clase 6: Heckscher-Ohlin
"""
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

OUT = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(OUT, exist_ok=True)

# Paleta
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
AZUL_CLARO = '#0EA5E9'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'


def estilo_base(ax, titulo='', xlabel='', ylabel=''):
    ax.set_title(titulo, fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=12)
    ax.set_xlabel(xlabel, fontsize=11, color=GRIS)
    ax.set_ylabel(ylabel, fontsize=11, color=GRIS)
    ax.tick_params(colors=GRIS, labelsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')


# ========== 1. PPF de dos países con dotaciones diferentes ==========
def grafico_dotaciones_ppf():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # País A: K-abundante → PPF sesgada hacia X (K-intensivo)
    t = np.linspace(0, 1, 200)
    xa = 100 * (1 - t**1.8)  # más capacidad en X
    ya = 65 * t**0.8

    # País B: L-abundante → PPF sesgada hacia Y (L-intensivo)
    xb = 60 * (1 - t**0.8)
    yb = 100 * t**1.8  # más capacidad en Y

    # País A
    ax1.plot(xa, ya, color=AZUL_OSCURO, linewidth=2.5)
    ax1.fill_between(xa, ya, alpha=0.08, color=AZUL_MEDIO)
    # Punto de autarquía A
    idx_a = 80
    ax1.plot(xa[idx_a], ya[idx_a], 'o', color=NARANJA, markersize=10, zorder=5)
    ax1.annotate('$E^A$ (autarquía)', xy=(xa[idx_a], ya[idx_a]),
                 xytext=(xa[idx_a]-25, ya[idx_a]+8), fontsize=10, color=NARANJA,
                 arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5))
    # Precio relativo A (tangente)
    ax1.plot([85, 20], [10, 55], '--', color=ROJO, linewidth=1.5, alpha=0.7)
    ax1.text(22, 57, '$P_X/P_Y$ bajo\n(X barato)', fontsize=9, color=ROJO, ha='left')

    estilo_base(ax1, 'País A (K-abundante)', 'Bien X (K-intensivo)', 'Bien Y (L-intensivo)')
    ax1.set_xlim(-5, 110)
    ax1.set_ylim(-5, 75)
    # Info box
    ax1.text(60, 65, 'K/L alto\n→ X relativamente\n   barato', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#EBF5FB', edgecolor=AZUL_MEDIO),
             ha='center', va='top')

    # País B
    ax2.plot(xb, yb, color=VERDE, linewidth=2.5)
    ax2.fill_between(xb, yb, alpha=0.08, color=VERDE)
    # Punto de autarquía B
    idx_b = 120
    ax2.plot(xb[idx_b], yb[idx_b], 'o', color=NARANJA, markersize=10, zorder=5)
    ax2.annotate('$E^B$ (autarquía)', xy=(xb[idx_b], yb[idx_b]),
                 xytext=(xb[idx_b]+5, yb[idx_b]-12), fontsize=10, color=NARANJA,
                 arrowprops=dict(arrowstyle='->', color=NARANJA, lw=1.5))
    # Precio relativo B (tangente)
    ax2.plot([50, 10], [20, 80], '--', color=ROJO, linewidth=1.5, alpha=0.7)
    ax2.text(12, 83, '$P_X/P_Y$ alto\n(X caro)', fontsize=9, color=ROJO, ha='left')

    estilo_base(ax2, 'País B (L-abundante)', 'Bien X (K-intensivo)', 'Bien Y (L-intensivo)')
    ax2.set_xlim(-5, 70)
    ax2.set_ylim(-5, 110)
    ax2.text(40, 100, 'K/L bajo\n→ Y relativamente\n   barato', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#EAFAF1', edgecolor=VERDE),
             ha='center', va='top')

    fig.suptitle('Dotaciones y precios relativos en autarquía', fontsize=15,
                 fontweight='bold', color=AZUL_OSCURO, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.93])
    fig.text(0.5, 0.01, 'Fuente: Elaboración propia', ha='center', fontsize=8, color=GRIS)
    plt.savefig(os.path.join(OUT, 'dotaciones_ppf.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('  ✓ dotaciones_ppf.png')


# ========== 2. Precio mundial y patrón de comercio ==========
def grafico_precio_mundial():
    fig, ax = plt.subplots(figsize=(12, 5))

    # Línea de precios
    y_line = 0.5
    ax.plot([0, 10], [y_line, y_line], '-', color='#cccccc', linewidth=2, zorder=1)

    # Tres puntos de precio
    pa = 2.0   # País A: Px/Py bajo
    pw = 5.0   # Precio mundial
    pb = 8.0   # País B: Px/Py alto

    ax.plot(pa, y_line, 'o', color=AZUL_OSCURO, markersize=18, zorder=5)
    ax.plot(pw, y_line, 's', color=NARANJA, markersize=18, zorder=5)
    ax.plot(pb, y_line, 'o', color=VERDE, markersize=18, zorder=5)

    ax.text(pa, y_line + 0.15, '$(P_X/P_Y)^A$', fontsize=13, ha='center',
            fontweight='bold', color=AZUL_OSCURO)
    ax.text(pa, y_line - 0.15, 'Bajo\n(X barato en A)', fontsize=9, ha='center',
            color=AZUL_OSCURO, va='top')

    ax.text(pw, y_line + 0.15, '$P^W$', fontsize=14, ha='center',
            fontweight='bold', color=NARANJA)
    ax.text(pw, y_line - 0.15, 'Precio\nmundial', fontsize=9, ha='center',
            color=NARANJA, va='top')

    ax.text(pb, y_line + 0.15, '$(P_X/P_Y)^B$', fontsize=13, ha='center',
            fontweight='bold', color=VERDE)
    ax.text(pb, y_line - 0.15, 'Alto\n(X caro en B)', fontsize=9, ha='center',
            color=VERDE, va='top')

    # Flechas de efecto
    # País A: sube Px/Py → exporta X
    ax.annotate('', xy=(pw - 0.3, y_line - 0.45), xytext=(pa + 0.3, y_line - 0.45),
                arrowprops=dict(arrowstyle='->', color=AZUL_OSCURO, lw=2))
    ax.text((pa + pw) / 2, y_line - 0.55, 'A: sube $P_X/P_Y$\n→ exporta X',
            fontsize=10, ha='center', color=AZUL_OSCURO, fontweight='bold')

    # País B: baja Px/Py → exporta Y
    ax.annotate('', xy=(pw + 0.3, y_line - 0.45), xytext=(pb - 0.3, y_line - 0.45),
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
    ax.text((pb + pw) / 2, y_line - 0.55, 'B: baja $P_X/P_Y$\n→ exporta Y',
            fontsize=10, ha='center', color=VERDE, fontweight='bold')

    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.2, 1.0)
    ax.axis('off')
    ax.set_title('Apertura comercial: precio mundial entre precios de autarquía',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=15)

    fig.text(0.5, 0.02, 'Fuente: Elaboración propia', ha='center', fontsize=8, color=GRIS)
    plt.savefig(os.path.join(OUT, 'precio_mundial_ho.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('  ✓ precio_mundial_ho.png')


# ========== 3. Stolper-Samuelson: cadena causal ==========
def grafico_stolper_samuelson():
    fig, ax = plt.subplots(figsize=(13, 6))

    # Cadena de cajas con flechas
    boxes = [
        ('↑ $P_X/P_Y$\n(precio relativo)', 1.0),
        ('Sector X\nse expande', 3.0),
        ('↑ demanda\nde K', 5.0),
        ('↑ r (retorno\nal capital)', 7.0),
        ('↓ w (salario\nreal)', 9.0),
    ]

    box_w = 1.6
    box_h = 0.7
    y_center = 0.5

    for label, x in boxes:
        color = AZUL_OSCURO if x < 7 else (VERDE if x == 7 else ROJO)
        facecolor = '#EBF5FB' if x < 7 else ('#EAFAF1' if x == 7 else '#FDEDEC')
        rect = mpatches.FancyBboxPatch((x - box_w/2, y_center - box_h/2), box_w, box_h,
                                        boxstyle='round,pad=0.1', facecolor=facecolor,
                                        edgecolor=color, linewidth=2, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y_center, label, fontsize=11, ha='center', va='center',
                fontweight='bold', color=color, zorder=4)

    # Flechas entre cajas
    for i in range(len(boxes) - 1):
        x_from = boxes[i][1] + box_w/2 + 0.05
        x_to = boxes[i+1][1] - box_w/2 - 0.05
        ax.annotate('', xy=(x_to, y_center), xytext=(x_from, y_center),
                    arrowprops=dict(arrowstyle='->', color=GRIS, lw=2.5))

    # Resumen abajo
    # País A
    ax.text(3.5, -0.3, 'País A (K-abundante):', fontsize=11, fontweight='bold',
            color=AZUL_OSCURO, ha='center')
    ax.text(3.5, -0.5, 'Sube $P_X$ → Gana K / Pierde L', fontsize=10,
            color=AZUL_OSCURO, ha='center')

    # País B
    ax.text(7.5, -0.3, 'País B (L-abundante):', fontsize=11, fontweight='bold',
            color=VERDE, ha='center')
    ax.text(7.5, -0.5, 'Baja $P_X$ → Gana L / Pierde K', fontsize=10,
            color=VERDE, ha='center')

    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.75, 1.3)
    ax.axis('off')
    ax.set_title('Stolper-Samuelson: cadena causal del precio al ingreso',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=15)

    fig.text(0.5, 0.02, 'Fuente: Elaboración propia', ha='center', fontsize=8, color=GRIS)
    plt.savefig(os.path.join(OUT, 'stolper_samuelson_cadena.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('  ✓ stolper_samuelson_cadena.png')


# ========== 4. Rybczynski: efecto sobre producción ==========
def grafico_rybczynski():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Escenario 1: ↑K
    categorias = ['Bien X\n(K-intensivo)', 'Bien Y\n(L-intensivo)']
    antes = [50, 50]
    despues = [80, 35]

    x_pos = np.arange(len(categorias))
    width = 0.3

    bars1 = ax1.bar(x_pos - width/2, antes, width, color=AZUL_MEDIO, label='Antes', alpha=0.7)
    bars2 = ax1.bar(x_pos + width/2, despues, width, color=NARANJA, label='Después de ↑K')

    # Flechas de cambio
    ax1.annotate('↑↑', xy=(0 + width/2, 82), fontsize=16, fontweight='bold',
                 color=VERDE, ha='center')
    ax1.annotate('↓', xy=(1 + width/2, 37), fontsize=16, fontweight='bold',
                 color=ROJO, ha='center')

    estilo_base(ax1, 'Shock: ↑ Capital (K)', '', 'Producción')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(categorias, fontsize=10)
    ax1.set_ylim(0, 100)
    ax1.legend(fontsize=9, loc='upper right')
    ax1.text(0.5, 92, 'Más K → X sube más\nque proporcionalmente,\nY cae', fontsize=9,
             ha='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEF9E7',
                                    edgecolor=NARANJA), transform=ax1.transData)

    # Escenario 2: ↑L
    despues2 = [35, 80]

    bars3 = ax2.bar(x_pos - width/2, antes, width, color=AZUL_MEDIO, label='Antes', alpha=0.7)
    bars4 = ax2.bar(x_pos + width/2, despues2, width, color=VERDE, label='Después de ↑L')

    ax2.annotate('↓', xy=(0 + width/2, 37), fontsize=16, fontweight='bold',
                 color=ROJO, ha='center')
    ax2.annotate('↑↑', xy=(1 + width/2, 82), fontsize=16, fontweight='bold',
                 color=VERDE, ha='center')

    estilo_base(ax2, 'Shock: ↑ Trabajo (L)', '', 'Producción')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(categorias, fontsize=10)
    ax2.set_ylim(0, 100)
    ax2.legend(fontsize=9, loc='upper right')
    ax2.text(0.5, 92, 'Más L → Y sube más\nque proporcionalmente,\nX cae', fontsize=9,
             ha='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#EAFAF1',
                                    edgecolor=VERDE), transform=ax2.transData)

    fig.suptitle('Teorema de Rybczynski: shock de dotaciones → cambio estructural',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO, y=0.98)
    plt.tight_layout(rect=[0, 0.04, 1, 0.93])
    fig.text(0.5, 0.01, 'Fuente: Elaboración propia', ha='center', fontsize=8, color=GRIS)
    plt.savefig(os.path.join(OUT, 'rybczynski_efecto.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('  ✓ rybczynski_efecto.png')


# ========== 5. Paradoja de Leontief ==========
def grafico_leontief():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Datos estilizados del paper de Leontief (1953)
    # K/L ratio en dólares de capital por trabajador-año
    categorias = ['Exportaciones\nEE.UU.', 'Sustitutos de\nimportaciones']
    kl_ratio = [14015, 18185]  # Datos aprox. del paper original

    colors = [AZUL_OSCURO, ROJO]
    bars = ax.bar(categorias, kl_ratio, color=colors, width=0.5, edgecolor='white', linewidth=2)

    # Valores sobre las barras
    for bar, val in zip(bars, kl_ratio):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 300,
                f'${val:,}', fontsize=13, fontweight='bold', ha='center',
                color=bar.get_facecolor())

    # Anotaciones
    # Predicción H-O — a la izquierda para no tapar el valor de la barra 2
    ax.annotate('Predicción H-O:\nExportaciones > Importaciones\n(EE.UU. es K-abundante)',
                xy=(0, 14300), xytext=(-0.35, 20000),
                fontsize=10, color=VERDE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=VERDE, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#EAFAF1', edgecolor=VERDE))

    # Hallazgo real — arriba a la derecha
    ax.annotate('Hallazgo real:\nExportaciones < Importaciones\n→ ¡PARADOJA!',
                xy=(1, 18500), xytext=(1.15, 22000),
                fontsize=10, color=ROJO, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ROJO, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FDEDEC', edgecolor=ROJO))

    estilo_base(ax, '', '', 'Capital por trabajador (USD)')
    ax.set_ylim(0, 24500)
    ax.set_title('Paradoja de Leontief (1953): K/L en comercio de EE.UU.',
                 fontsize=14, fontweight='bold', color=AZUL_OSCURO, pad=12)

    fig.text(0.5, 0.01, 'Fuente: Leontief (1953), datos de EE.UU. 1947', ha='center',
             fontsize=8, color=GRIS)
    plt.savefig(os.path.join(OUT, 'leontief_paradoja.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('  ✓ leontief_paradoja.png')


# ========== 6. Tabla comparativa de teoremas H-O ==========
def grafico_teoremas_tabla():
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.axis('off')

    # Definir tabla
    headers = ['Teorema', 'Qué mueve', 'Qué predice', 'Resultado clave']
    data = [
        ['Heckscher-\nOhlin', 'Dotaciones\nrelativas', 'Patrón de\ncomercio',
         'Exporta el bien intensivo\nen el factor abundante'],
        ['Stolper-\nSamuelson', 'Precio relativo\nde bienes', 'Distribución\ndel ingreso',
         'Gana el factor del bien\ncuyo precio sube'],
        ['Rybczynski', 'Dotación de\nfactores', 'Estructura\nproductiva',
         'Sube producción del bien\nintensivo en el factor que crece'],
        ['FPE', 'Comercio\nde bienes', 'Precios de\nfactores',
         'Tienden a igualarse w y r\nentre países (bajo supuestos)'],
    ]

    n_rows = len(data)
    n_cols = len(headers)
    col_widths = [0.15, 0.18, 0.18, 0.35]
    row_h = 0.16
    y_start = 0.65

    # Headers
    header_y = y_start + row_h + 0.02
    x_cursor = 0.07
    for j, (header, w) in enumerate(zip(headers, col_widths)):
        rect = mpatches.FancyBboxPatch((x_cursor, header_y), w, row_h,
                                        boxstyle='round,pad=0.02', facecolor=AZUL_OSCURO,
                                        edgecolor='white', linewidth=1, zorder=5)
        ax.add_patch(rect)
        ax.text(x_cursor + w/2, header_y + row_h/2, header, fontsize=11,
                fontweight='bold', color='white', ha='center', va='center', zorder=6)
        x_cursor += w + 0.02

    # Filas de datos
    row_colors = ['#EBF5FB', '#F8F9FA', '#EBF5FB', '#F8F9FA']
    text_colors = [AZUL_OSCURO, GRIS, AZUL_OSCURO, GRIS]

    for i, (row, bg_color) in enumerate(zip(data, row_colors)):
        y = y_start - i * (row_h + 0.02)
        x_cursor = 0.07
        for j, (cell, w) in enumerate(zip(row, col_widths)):
            # Primera columna con color especial
            if j == 0:
                fc = AZUL_MEDIO
                tc = 'white'
                fw = 'bold'
            else:
                fc = bg_color
                tc = '#111827'
                fw = 'normal'

            rect = mpatches.FancyBboxPatch((x_cursor, y), w, row_h,
                                            boxstyle='round,pad=0.02', facecolor=fc,
                                            edgecolor='#cccccc', linewidth=0.5, zorder=3)
            ax.add_patch(rect)
            ax.text(x_cursor + w/2, y + row_h/2, cell, fontsize=9.5,
                    fontweight=fw, color=tc, ha='center', va='center', zorder=4)
            x_cursor += w + 0.02

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.05, 1.0)
    ax.set_title('Los teoremas del modelo Heckscher-Ohlin',
                 fontsize=15, fontweight='bold', color=AZUL_OSCURO, pad=15)

    plt.savefig(os.path.join(OUT, 'teoremas_ho_tabla.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('  ✓ teoremas_ho_tabla.png')


# ========== 7. Argentina: composición de exportaciones ==========
def grafico_argentina_exportaciones():
    fig, ax = plt.subplots(figsize=(11, 6))

    # Datos estilizados de composición de exportaciones argentinas (~2022-2023)
    categorias = [
        'Productos\nprimarios',
        'MOA\n(Manuf. Origen\nAgropecuario)',
        'MOI\n(Manuf. Origen\nIndustrial)',
        'Combustibles\ny energía'
    ]
    valores = [22, 35, 28, 15]  # Porcentajes aproximados
    intensidad = ['Tierra/\nRecursos', 'Tierra/\nRecursos +\nCapital', 'Capital/\nTrabajo\ncalificado', 'Recursos\nnaturales']
    colores = [VERDE, AZUL_MEDIO, NARANJA, ROJO]

    bars = ax.bar(categorias, valores, color=colores, width=0.6, edgecolor='white', linewidth=2)

    # Valores sobre barras
    for bar, val in zip(bars, valores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{val}%', fontsize=13, fontweight='bold', ha='center',
                color=bar.get_facecolor())

    # Intensidad factorial dentro de las barras (parte inferior)
    for bar, intens, color in zip(bars, intensidad, colores):
        ax.text(bar.get_x() + bar.get_width()/2, 2,
                intens, fontsize=7.5, ha='center', va='bottom', color='white',
                style='italic', fontweight='bold')

    estilo_base(ax, '', '', '% del total exportado')
    ax.set_ylim(0, 45)
    ax.set_title('Argentina: composición de exportaciones por intensidad factorial',
                 fontsize=13, fontweight='bold', color=AZUL_OSCURO, pad=12)

    # Caja resumen
    ax.text(0.98, 0.95, 'Lectura H-O: ~57% de exportaciones\nson intensivas en tierra/recursos\n(factor abundante de Argentina)',
            transform=ax.transAxes, fontsize=9, va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEF9E7', edgecolor=NARANJA))

    fig.text(0.5, 0.01, 'Fuente: INDEC / Banco Mundial (datos estilizados, ~2022-2023)',
             ha='center', fontsize=8, color=GRIS)
    plt.savefig(os.path.join(OUT, 'argentina_exportaciones.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print('  ✓ argentina_exportaciones.png')


# ========== MAIN ==========
if __name__ == '__main__':
    print('Generando gráficos Clase 6...\n')
    grafico_dotaciones_ppf()
    grafico_precio_mundial()
    grafico_stolper_samuelson()
    grafico_rybczynski()
    grafico_leontief()
    grafico_teoremas_tabla()
    grafico_argentina_exportaciones()
    print(f'\n✓ Todos los gráficos generados en: {OUT}')
