"""
Genera 6 mapas para el bloque de evidencia empirica de la NGE (Sesion 4).

Mapas (PNGs separados):
  1. banana_azul_europa.png        - corredor Londres-Milan resaltado
  2. manufacturing_belt_eeuu.png   - rust belt vs sun belt
  3. china_gdp_coastal.png         - franja costera vs interior
  4. mexico_frontera_norte.png     - frontera norte (maquiladoras / NAFTA / T-MEC)
  5. mundo_espinoso.png            - aglomeraciones globales de innovacion (Florida 2005)
  6. argentina_concentracion.png   - PIB pc por provincia + 7 polos sectoriales

Datos: Natural Earth (datos_compartidos/naturalearth/), descargado una sola vez.
Output: Clases/sesion04/img/
"""

import sys
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from shapely.geometry import box

# UTF-8 stdout en Windows
sys.stdout.reconfigure(encoding='utf-8')

# Paleta UMET
AZUL_OSCURO = '#1F4E79'
AZUL_MEDIO = '#2E75B6'
NARANJA = '#E8833A'
ROJO = '#E74C3C'
VERDE = '#27AE60'
GRIS_BASE = '#E5E7EB'
GRIS_BORDE = '#9CA3AF'
TEXTO = '#111827'

# Rutas
ROOT = Path(__file__).resolve().parents[3]
NE_DIR = ROOT / 'datos_compartidos' / 'naturalearth'
COUNTRIES_SHP = NE_DIR / 'ne_50m_admin_0_countries' / 'ne_50m_admin_0_countries.shp'
ADMIN1_SHP = NE_DIR / 'ne_10m_admin_1_states_provinces' / 'ne_10m_admin_1_states_provinces.shp'
OUT_DIR = ROOT / 'Clases' / 'sesion04' / 'img'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def setup_axes(ax, title, subtitle=None):
    ax.set_axis_off()
    ax.set_title(title, fontsize=18, fontweight='bold', color=TEXTO, pad=14, loc='left')
    if subtitle:
        ax.text(0.0, 1.005, subtitle, transform=ax.transAxes,
                fontsize=11, color='#4B5563', va='bottom')


def add_source(fig, text):
    fig.text(0.01, 0.01, text, fontsize=8, color='#6B7280', ha='left', va='bottom')


# =============================================================================
# 1) BANANA AZUL - Europa
# =============================================================================

def mapa_banana_azul():
    print('Generando banana_azul_europa.png ...')
    world = gpd.read_file(COUNTRIES_SHP)

    # Paises del corredor de la "banana azul" (Londres -> Benelux -> Rin -> Suiza -> norte de Italia)
    corredor = ['United Kingdom', 'Netherlands', 'Belgium', 'Luxembourg',
                'Germany', 'Switzerland', 'Italy']

    # Recortar al bbox de Europa para evitar que polígonos enormes (Rusia) inflen los bounds
    bbox_eur = box(-12, 35, 32, 62)
    eur = world.clip(bbox_eur).copy()
    eur['en_corredor'] = eur['NAME'].isin(corredor)

    # Reproyectar a LAEA Europa para vista correcta
    eur = eur.to_crs('EPSG:3035')

    fig, ax = plt.subplots(figsize=(11, 9), facecolor='white')

    # Resto de paises
    eur[~eur['en_corredor']].plot(ax=ax, color=GRIS_BASE,
                                   edgecolor='white', linewidth=0.7)
    # Corredor
    eur[eur['en_corredor']].plot(ax=ax, color=AZUL_OSCURO,
                                  edgecolor='white', linewidth=0.7)

    # Etiquetas de ciudades clave (lon, lat) con offsets ajustados para evitar superposicion
    # cada tupla: (nombre, lon, lat, dx, dy, ha)
    ciudades = [
        ('Londres',   -0.13, 51.51, -10,  6, 'right'),
        ('Amsterdam',  4.90, 52.37,   8, 12, 'left'),
        ('Bruselas',   4.35, 50.85, -10, -14, 'right'),
        ('Frankfurt',  8.68, 50.11,  10,  4, 'left'),
        ('Zurich',     8.55, 47.38, -10, -2, 'right'),
        ('Milan',      9.19, 45.46,   8, -8, 'left'),
    ]
    pts = gpd.GeoDataFrame(
        {'name': [c[0] for c in ciudades]},
        geometry=gpd.points_from_xy([c[1] for c in ciudades],
                                     [c[2] for c in ciudades]),
        crs='EPSG:4326'
    ).to_crs('EPSG:3035')

    for (_, row), (name, _, _, dx, dy, ha) in zip(pts.iterrows(), ciudades):
        x, y = row.geometry.x, row.geometry.y
        ax.plot(x, y, marker='o', color='white', markersize=6,
                markeredgecolor=AZUL_OSCURO, markeredgewidth=1.5, zorder=5)
        ax.annotate(name, (x, y), xytext=(dx, dy), textcoords='offset points',
                    fontsize=10, fontweight='bold', color=TEXTO, ha=ha,
                    bbox=dict(boxstyle='round,pad=0.25', fc='white',
                              ec=AZUL_OSCURO, lw=0.8, alpha=0.92), zorder=6)

    # Limites: reproyectar el bbox original al CRS final
    bbox_proj = gpd.GeoSeries([bbox_eur], crs='EPSG:4326').to_crs('EPSG:3035')
    minx, miny, maxx, maxy = bbox_proj.total_bounds
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)

    setup_axes(ax,
               'La Banana Azul: corredor economico europeo',
               'Concentracion industrial, financiera y de servicios avanzados (Londres -> Milan)')

    # Leyenda
    legend = [
        Patch(facecolor=AZUL_OSCURO, edgecolor='white', label='Paises del corredor'),
        Patch(facecolor=GRIS_BASE, edgecolor='white', label='Resto de Europa'),
    ]
    ax.legend(handles=legend, loc='lower left', frameon=True,
              fontsize=10, framealpha=0.95)

    # Fuente se cita en el slide HTML (campo Fuente:), no duplicar en el PNG.

    plt.tight_layout()
    out = OUT_DIR / 'banana_azul_europa.png'
    plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  -> {out}')


# =============================================================================
# 2) MANUFACTURING BELT - EEUU
# =============================================================================

def mapa_manufacturing_belt():
    print('Generando manufacturing_belt_eeuu.png ...')
    states = gpd.read_file(ADMIN1_SHP)
    us = states[states['admin'] == 'United States of America'].copy()

    # Excluir Alaska, Hawaii y territorios para vista continental
    excluir = ['Alaska', 'Hawaii']
    us = us[~us['name'].isin(excluir)]

    # Rust belt clasico (post-industrial, Grandes Lagos)
    rust_belt = ['Pennsylvania', 'Ohio', 'Michigan', 'Indiana', 'Illinois',
                 'Wisconsin', 'West Virginia']

    # Sun belt (sur y suroeste, crecimiento posterior)
    sun_belt = ['California', 'Arizona', 'New Mexico', 'Texas',
                'Oklahoma', 'Arkansas', 'Louisiana', 'Mississippi',
                'Alabama', 'Tennessee', 'Georgia', 'Florida',
                'South Carolina', 'North Carolina', 'Nevada']

    def categorizar(name):
        if name in rust_belt:
            return 'rust'
        if name in sun_belt:
            return 'sun'
        return 'otro'
    us['categoria'] = us['name'].apply(categorizar)

    # Reproyectar a Albers USA (EPSG:5070)
    us = us.to_crs('EPSG:5070')

    fig, ax = plt.subplots(figsize=(11, 7), facecolor='white')

    us[us['categoria'] == 'otro'].plot(ax=ax, color=GRIS_BASE,
                                         edgecolor='white', linewidth=0.6)
    us[us['categoria'] == 'sun'].plot(ax=ax, color=VERDE,
                                        edgecolor='white', linewidth=0.6)
    us[us['categoria'] == 'rust'].plot(ax=ax, color=ROJO,
                                         edgecolor='white', linewidth=0.6)

    # Etiquetas de algunas ciudades clave
    ciudades = [
        ('Detroit', -83.05, 42.33),
        ('Chicago', -87.65, 41.88),
        ('Pittsburgh', -79.99, 40.44),
        ('Houston', -95.37, 29.76),
        ('Atlanta', -84.39, 33.75),
        ('Los Angeles', -118.24, 34.05),
        ('Silicon Valley', -122.08, 37.39),
    ]
    pts = gpd.GeoDataFrame(
        {'name': [c[0] for c in ciudades]},
        geometry=gpd.points_from_xy([c[1] for c in ciudades],
                                     [c[2] for c in ciudades]),
        crs='EPSG:4326'
    ).to_crs('EPSG:5070')

    for (_, row), (name, _, _) in zip(pts.iterrows(), ciudades):
        x, y = row.geometry.x, row.geometry.y
        ax.plot(x, y, marker='o', color='white', markersize=5,
                markeredgecolor=TEXTO, markeredgewidth=1.2, zorder=5)
        ax.annotate(name, (x, y), xytext=(7, 5), textcoords='offset points',
                    fontsize=9, fontweight='bold', color=TEXTO,
                    bbox=dict(boxstyle='round,pad=0.2', fc='white',
                              ec='#9CA3AF', lw=0.6, alpha=0.92), zorder=6)

    minx, miny, maxx, maxy = us.total_bounds
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)

    setup_axes(ax,
               'EEUU: del Rust Belt al Sun Belt',
               'Manufactura tradicional (Grandes Lagos) -> declive -> nuevos polos en el Sur')

    legend = [
        Patch(facecolor=ROJO, edgecolor='white', label='Rust Belt (manufactura tradicional)'),
        Patch(facecolor=VERDE, edgecolor='white', label='Sun Belt (nuevos polos)'),
        Patch(facecolor=GRIS_BASE, edgecolor='white', label='Resto del pais'),
    ]
    ax.legend(handles=legend, loc='lower left', frameon=True,
              fontsize=10, framealpha=0.95)

    # Fuente se cita en el slide HTML (campo Fuente:), no duplicar en el PNG.

    plt.tight_layout()
    out = OUT_DIR / 'manufacturing_belt_eeuu.png'
    plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  -> {out}')


# =============================================================================
# 3) CHINA - costa vs interior
# =============================================================================

def mapa_china_costa():
    print('Generando china_gdp_coastal.png ...')
    states = gpd.read_file(ADMIN1_SHP)
    cn = states[states['admin'] == 'China'].copy()

    # Provincias costeras (~60% del PIB industrial en ~15% del territorio)
    # Norte a sur: Liaoning, Hebei (incluye Beijing y Tianjin), Shandong,
    # Jiangsu, Shanghai, Zhejiang, Fujian, Guangdong, Hainan
    costeras = ['Liaoning', 'Hebei', 'Beijing', 'Tianjin', 'Shandong',
                'Jiangsu', 'Shanghai', 'Zhejiang', 'Fujian', 'Guangdong',
                'Hainan']
    # Polos especificos para etiquetar
    cn['costera'] = cn['name'].isin(costeras)

    # Reproyectar a Albers Equal Area centrado en China
    china_aea = ('+proj=aea +lat_0=35 +lon_0=105 +lat_1=25 +lat_2=47 '
                 '+x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs')
    cn = cn.to_crs(china_aea)

    fig, ax = plt.subplots(figsize=(11, 8), facecolor='white')

    cn[~cn['costera']].plot(ax=ax, color=GRIS_BASE,
                              edgecolor='white', linewidth=0.5)
    cn[cn['costera']].plot(ax=ax, color=AZUL_OSCURO,
                             edgecolor='white', linewidth=0.5)

    # Etiquetas de polos clave
    ciudades = [
        ('Beijing', 116.40, 39.90),
        ('Shanghai', 121.47, 31.23),
        ('Shenzhen', 114.06, 22.54),
        ('Guangzhou', 113.26, 23.13),
        ('Tianjin', 117.20, 39.13),
    ]
    pts = gpd.GeoDataFrame(
        {'name': [c[0] for c in ciudades]},
        geometry=gpd.points_from_xy([c[1] for c in ciudades],
                                     [c[2] for c in ciudades]),
        crs='EPSG:4326'
    ).to_crs(china_aea)

    # Offsets por ciudad (dx, dy en puntos) para evitar superposicion
    offsets = {
        'Beijing':   (10,   8),
        'Tianjin':   (12, -10),
        'Shanghai':  (12,   0),
        'Guangzhou': (-12, -8),
        'Shenzhen':  (12,  -2),
    }
    for (_, row), (name, _, _) in zip(pts.iterrows(), ciudades):
        x, y = row.geometry.x, row.geometry.y
        dx, dy = offsets.get(name, (8, 6))
        ha = 'left' if dx > 0 else 'right'
        ax.plot(x, y, marker='o', color='white', markersize=6,
                markeredgecolor=AZUL_OSCURO, markeredgewidth=1.5, zorder=5)
        ax.annotate(name, (x, y), xytext=(dx, dy), textcoords='offset points',
                    fontsize=10, fontweight='bold', color=TEXTO, ha=ha,
                    bbox=dict(boxstyle='round,pad=0.25', fc='white',
                              ec=AZUL_OSCURO, lw=0.8, alpha=0.92), zorder=6)

    minx, miny, maxx, maxy = cn.total_bounds
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)

    setup_axes(ax,
               'China: la franja costera concentra la industria exportadora',
               '~60% del PIB industrial en ~15% del territorio - delta del Rio Perla y delta del Yangtze')

    legend = [
        Patch(facecolor=AZUL_OSCURO, edgecolor='white', label='Provincias costeras'),
        Patch(facecolor=GRIS_BASE, edgecolor='white', label='Interior'),
    ]
    ax.legend(handles=legend, loc='lower left', frameon=True,
              fontsize=10, framealpha=0.95)

    # Fuente se cita en el slide HTML (campo Fuente:), no duplicar en el PNG.

    plt.tight_layout()
    out = OUT_DIR / 'china_gdp_coastal.png'
    plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  -> {out}')


# =============================================================================
# 4) MEXICO - frontera norte (maquiladoras / NAFTA / T-MEC)
# =============================================================================

def mapa_mexico_frontera():
    print('Generando mexico_frontera_norte.png ...')
    states = gpd.read_file(ADMIN1_SHP)
    mx = states[states['admin'] == 'Mexico'].copy()

    # Estados fronterizos con EEUU (oeste a este)
    fronterizos_postal = ['BC', 'SO', 'CH', 'CO', 'NL', 'TM']
    mx['fronterizo'] = mx['postal'].isin(fronterizos_postal)

    # Reproyectar a Lambert Conformal Conic Mexico (EPSG:6362) o Albers custom
    mx_aea = ('+proj=aea +lat_0=24 +lon_0=-102 +lat_1=17 +lat_2=29 '
              '+x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs')
    mx = mx.to_crs(mx_aea)

    fig, ax = plt.subplots(figsize=(11, 7.5), facecolor='white')

    mx[~mx['fronterizo']].plot(ax=ax, color=GRIS_BASE,
                                 edgecolor='white', linewidth=0.5)
    mx[mx['fronterizo']].plot(ax=ax, color=NARANJA,
                                edgecolor='white', linewidth=0.5)

    # Ciudades clave de la franja maquiladora
    ciudades = [
        ('Tijuana',         -117.04, 32.51),
        ('Mexicali',        -115.47, 32.62),
        ('Cd. Juarez',      -106.42, 31.69),
        ('Monterrey',       -100.31, 25.69),
        ('Reynosa',          -98.28, 26.05),
        ('Matamoros',        -97.50, 25.88),
    ]
    pts = gpd.GeoDataFrame(
        {'name': [c[0] for c in ciudades]},
        geometry=gpd.points_from_xy([c[1] for c in ciudades],
                                     [c[2] for c in ciudades]),
        crs='EPSG:4326'
    ).to_crs(mx_aea)

    offsets = {
        'Tijuana':    (12,  -8),
        'Mexicali':   (12, -20),
        'Cd. Juarez': (10,   8),
        'Monterrey':  (-12, -8),
        'Reynosa':    (12,  14),
        'Matamoros':  (12,  -8),
    }
    for (_, row), (name, _, _) in zip(pts.iterrows(), ciudades):
        x, y = row.geometry.x, row.geometry.y
        dx, dy = offsets.get(name, (8, 6))
        ha = 'left' if dx > 0 else 'right'
        ax.plot(x, y, marker='o', color='white', markersize=6,
                markeredgecolor=NARANJA, markeredgewidth=1.5, zorder=5)
        ax.annotate(name, (x, y), xytext=(dx, dy), textcoords='offset points',
                    fontsize=10, fontweight='bold', color=TEXTO, ha=ha,
                    bbox=dict(boxstyle='round,pad=0.25', fc='white',
                              ec=NARANJA, lw=0.8, alpha=0.92), zorder=6)

    # Etiqueta "EEUU" arriba para contexto
    minx, miny, maxx, maxy = mx.total_bounds
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)
    # Banda EEUU (sombreado claro arriba indicando que la franja es la frontera)
    ax.text(0.5, 0.97, '↑ Estados Unidos', transform=ax.transAxes,
            ha='center', va='top', fontsize=11, fontweight='bold',
            color='#4B5563', style='italic')

    setup_axes(ax,
               'Mexico: la frontera norte como polo industrial',
               'Maquiladoras (1965) -> NAFTA (1994) -> T-MEC (2020) - autopartes y electronica')

    legend = [
        Patch(facecolor=NARANJA, edgecolor='white', label='Estados fronterizos (cluster maquilador)'),
        Patch(facecolor=GRIS_BASE, edgecolor='white', label='Resto de Mexico'),
    ]
    ax.legend(handles=legend, loc='lower left', frameon=True,
              fontsize=10, framealpha=0.95)

    # Fuente se cita en el slide HTML (campo Fuente:), no duplicar en el PNG.

    plt.tight_layout()
    out = OUT_DIR / 'mexico_frontera_norte.png'
    plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  -> {out}')


# =============================================================================
# 5) MUNDO ESPINOSO - aglomeraciones globales de innovacion (Florida 2005)
# =============================================================================

def mapa_mundo_espinoso():
    print('Generando mundo_espinoso.png ...')
    world = gpd.read_file(COUNTRIES_SHP)

    # Excluir Antartida para vista
    world = world[world['CONTINENT'] != 'Antarctica'].copy()

    # Reproyectar a Robinson (proyeccion estandar para mapamundis tematicos)
    robinson = '+proj=robin +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs'
    world = world.to_crs(robinson)

    # Ciudades-cluster de innovacion: (nombre, lon, lat, tier)
    # Tier 1 = mega-cluster (radio grande), Tier 2 = principal, Tier 3 = emergente
    ciudades = [
        # Tier 1 - mega-clusters
        ('Bay Area',     -122.42, 37.77, 1),
        ('NY-Boston',     -73.94, 41.00, 1),
        ('Londres',        -0.13, 51.51, 1),
        ('Tokyo',         139.69, 35.68, 1),
        ('Shanghai',      121.47, 31.23, 1),
        # Tier 2 - principales
        ('Los Angeles',  -118.24, 34.05, 2),
        ('Seattle',      -122.33, 47.61, 2),
        ('Paris',           2.35, 48.86, 2),
        ('Berlin',         13.40, 52.52, 2),
        ('Beijing',       116.40, 39.90, 2),
        ('Shenzhen-HK',   114.16, 22.50, 2),
        ('Seul',          126.98, 37.57, 2),
        ('Singapur',      103.82,  1.35, 2),
        # Tier 3 - emergentes
        ('Toronto',       -79.38, 43.65, 3),
        ('Estocolmo',      18.07, 59.33, 3),
        ('Tel Aviv',       34.78, 32.08, 3),
        ('Dubai',          55.27, 25.20, 3),
        ('Bangalore',      77.59, 12.97, 3),
        ('Sydney',        151.21, -33.87, 3),
        ('Sao Paulo',     -46.63, -23.55, 3),
        ('CDMX',          -99.13, 19.43, 3),
    ]
    pts = gpd.GeoDataFrame(
        {'name': [c[0] for c in ciudades],
         'tier': [c[3] for c in ciudades]},
        geometry=gpd.points_from_xy([c[1] for c in ciudades],
                                     [c[2] for c in ciudades]),
        crs='EPSG:4326'
    ).to_crs(robinson)

    fig, ax = plt.subplots(figsize=(14, 7), facecolor='white')

    # Mundo en gris claro
    world.plot(ax=ax, color=GRIS_BASE, edgecolor='white', linewidth=0.4)

    # Puntos por tier (tamaño proporcional al peso del cluster)
    tier_sizes = {1: 380, 2: 200, 3: 100}
    tier_colors = {1: AZUL_OSCURO, 2: AZUL_MEDIO, 3: AZUL_OSCURO}
    for tier in [3, 2, 1]:  # graficar tier 1 al final para que quede arriba
        sub = pts[pts['tier'] == tier]
        ax.scatter(sub.geometry.x, sub.geometry.y,
                   s=tier_sizes[tier], color=tier_colors[tier],
                   edgecolor='white', linewidth=1.5, alpha=0.85, zorder=5)

    # Etiquetas - solo Tier 1 y selectos tier 2
    label_offsets = {
        'Bay Area':    (-15,  -22),
        'NY-Boston':   (10,   12),
        'Londres':     (-5,   14),
        'Tokyo':       (12,    0),
        'Shanghai':    (-8,  -22),
        'Los Angeles': (-12, -16),
        'Paris':       (-2,  -18),
        'Berlin':      (10,    8),
        'Beijing':     (10,   16),
        'Shenzhen-HK': (12,   -8),
        'Seul':        (-10,  16),
        'Singapur':    (10,  -12),
        'Toronto':     (-12, -14),
        'Estocolmo':   (8,    10),
        'Tel Aviv':    (10,    8),
        'Dubai':       (10,  -10),
        'Bangalore':   (10,   -2),
        'Sydney':      (-10, -14),
        'Sao Paulo':   (-12,  -8),
        'CDMX':        (-12, -10),
        'Seattle':     (-12,   8),
    }
    for (_, row) in pts.iterrows():
        name = row['name']
        x, y = row.geometry.x, row.geometry.y
        dx, dy = label_offsets.get(name, (8, 6))
        ha = 'left' if dx > 0 else 'right'
        size = 9 if row['tier'] == 1 else 8
        weight = 'bold' if row['tier'] == 1 else 'normal'
        ax.annotate(name, (x, y), xytext=(dx, dy), textcoords='offset points',
                    fontsize=size, fontweight=weight, color=TEXTO, ha=ha,
                    bbox=dict(boxstyle='round,pad=0.2', fc='white',
                              ec='#9CA3AF', lw=0.6, alpha=0.92), zorder=6)

    ax.set_axis_off()
    setup_axes(ax,
               'El mundo "espinoso": donde se concentra la innovacion global',
               'La globalizacion no aplano el mundo - lo hizo mas concentrado en pocas mega-aglomeraciones (Florida 2005)')

    # Leyenda manual
    from matplotlib.lines import Line2D
    legend_pts = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=AZUL_OSCURO,
               markersize=18, label='Mega-cluster (top 5)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=AZUL_MEDIO,
               markersize=13, label='Cluster principal'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=AZUL_OSCURO,
               markersize=9, label='Cluster emergente'),
    ]
    ax.legend(handles=legend_pts, loc='lower left', frameon=True,
              fontsize=9, framealpha=0.95)

    # Fuente se cita en el slide HTML (campo Fuente:), no duplicar en el PNG.

    plt.tight_layout()
    out = OUT_DIR / 'mundo_espinoso.png'
    plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  -> {out}')


# =============================================================================
# 6) ARGENTINA - concentracion territorial (PIB per capita + polos)
# =============================================================================

def mapa_argentina_concentracion():
    print('Generando argentina_concentracion.png ...')
    states = gpd.read_file(ADMIN1_SHP)
    ar = states[states['admin'] == 'Argentina'].copy()

    # Tiers de PBG per capita (INDEC PBG provincial 2022, estilizado)
    # Alto: CABA + provincias hidrocarburiferas + electronica TdF
    tier_alto = ['AR-C', 'AR-V', 'AR-Z', 'AR-Q', 'AR-U']
    # Medio: Pampa humeda + Mendoza/SL/LP/RN
    tier_medio = ['AR-B', 'AR-X', 'AR-S', 'AR-M', 'AR-D', 'AR-L', 'AR-R']
    # Bajo: NOA + NEA + San Juan + Entre Rios
    # (todo el resto cae aca implicitamente)

    def tier_provincia(iso):
        if iso in tier_alto:
            return 'alto'
        if iso in tier_medio:
            return 'medio'
        return 'bajo'
    ar['tier'] = ar['iso_3166_2'].apply(tier_provincia)

    # Albers Equal Area centrada en Argentina
    ar_aea = ('+proj=aea +lat_0=-35 +lon_0=-65 +lat_1=-25 +lat_2=-50 '
              '+x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs')
    ar = ar.to_crs(ar_aea)

    fig, ax = plt.subplots(figsize=(8, 12), facecolor='white')

    # Tiers - escala azul UMET (mas oscuro = mayor PBG)
    colores_tier = {'alto': '#1F4E79', 'medio': '#7FA8C9', 'bajo': '#E5E7EB'}
    for tier, color in colores_tier.items():
        ar[ar['tier'] == tier].plot(ax=ax, color=color,
                                      edgecolor='white', linewidth=0.6)

    # Polos sectoriales con etiqueta y color por tipo de actividad
    polos = [
        # (nombre, sector, lon, lat, color_pin)
        ('CABA',         'Servicios/finanzas', -58.38, -34.61, NARANJA),
        ('Rosario',      'Agroexportador',     -60.66, -32.95, VERDE),
        ('Cordoba',      'Automotriz',         -64.18, -31.42, NARANJA),
        ('Mendoza',      'Vitivinicultura',    -68.85, -32.89, VERDE),
        ('Bahia Blanca', 'Petroquimico',       -62.27, -38.72, NARANJA),
        ('Neuquen-VM',   'Hidrocarburos',      -68.06, -38.95, ROJO),
        ('Ushuaia',      'Electronica',        -68.30, -54.81, NARANJA),
    ]
    pts = gpd.GeoDataFrame(
        {'name':   [p[0] for p in polos],
         'sector': [p[1] for p in polos],
         'color':  [p[4] for p in polos]},
        geometry=gpd.points_from_xy([p[2] for p in polos],
                                     [p[3] for p in polos]),
        crs='EPSG:4326'
    ).to_crs(ar_aea)

    offsets = {
        'CABA':         (12,  -8),
        'Rosario':      (12,  10),
        'Cordoba':      (-12,  6),
        'Mendoza':      (-12, -6),
        'Bahia Blanca': (12, -12),
        'Neuquen-VM':   (-12,  8),
        'Ushuaia':      (12,   6),
    }
    for (_, row), (name, sector, _, _, col) in zip(pts.iterrows(), polos):
        x, y = row.geometry.x, row.geometry.y
        dx, dy = offsets.get(name, (10, 6))
        ha = 'left' if dx > 0 else 'right'
        ax.plot(x, y, marker='o', color=col, markersize=10,
                markeredgecolor='white', markeredgewidth=1.5, zorder=5)
        ax.annotate(f'{name}\n({sector})', (x, y),
                    xytext=(dx, dy), textcoords='offset points',
                    fontsize=8, fontweight='bold', color=TEXTO, ha=ha,
                    bbox=dict(boxstyle='round,pad=0.25', fc='white',
                              ec=col, lw=1.0, alpha=0.94), zorder=6)

    minx, miny, maxx, maxy = ar.total_bounds
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)

    setup_axes(ax,
               'Argentina: concentracion territorial y polos especializados',
               'PBG per capita por provincia + polos sectoriales')

    legend_pbg = [
        Patch(facecolor=colores_tier['alto'],  edgecolor='white',
              label='PBG p.c. alto'),
        Patch(facecolor=colores_tier['medio'], edgecolor='white',
              label='PBG p.c. medio'),
        Patch(facecolor=colores_tier['bajo'],  edgecolor='white',
              label='PBG p.c. bajo'),
    ]
    ax.legend(handles=legend_pbg, loc='upper right', frameon=True,
              fontsize=9, framealpha=0.95, title='Concentracion economica',
              title_fontsize=9)

    plt.tight_layout()
    out = OUT_DIR / 'argentina_concentracion.png'
    plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  -> {out}')


if __name__ == '__main__':
    mapa_banana_azul()
    mapa_manufacturing_belt()
    mapa_china_costa()
    mapa_mexico_frontera()
    mapa_mundo_espinoso()
    mapa_argentina_concentracion()
    print('Listo.')
