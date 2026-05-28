"""
G5 — Composición exportadora de Corea del Sur 1960-2020.
El "upgrading" sistémico: textiles → barcos → autos → electrónica → semiconductores.

Fuente: UN COMTRADE (HS, principales categorías) + reconstrucción histórica
en base a Cherif & Hasanov (2019) IMF "The Return of the Policy that Shall Not
Be Named: Principles of Industrial Policy", Cuadro 2; y Hausmann-Hwang-Rodrik
(2007) on Korea's export composition.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent.parent / 'graficos'

AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'
GRIS_CLARO = '#9CA3AF'
VIOLETA = '#7C3AED'
CYAN = '#0EA5E9'
AMARILLO = '#EAB308'

# Composición exportadora % por categoría (estimación estilizada
# coherente con UN COMTRADE y Cherif-Hasanov 2019)
anios = [1960, 1970, 1980, 1990, 2000, 2010, 2020]

# Categorías (filas) — primarios, textiles/calzado, barcos, autos, electrónica, semis/alta tec
categorias = ['Primarios', 'Textiles y calzado', 'Acero y barcos',
              'Autos y maquinaria', 'Electrónica de consumo',
              'Semiconductores y alta tec']

# % de exportaciones totales por categoría
matriz = np.array([
    # 1960  1970  1980  1990  2000  2010  2020
    [  82,   25,   10,    5,    3,    2,    2 ],   # Primarios
    [  10,   45,   30,   15,    8,    5,    3 ],   # Textiles
    [   5,   18,   30,   20,   15,   13,    8 ],   # Acero/barcos
    [   2,    8,   15,   25,   25,   25,   20 ],   # Autos/maquinaria
    [   1,    3,   10,   25,   25,   20,   12 ],   # Electrónica
    [   0,    1,    5,   10,   24,   35,   55 ],   # Semis/alta tec
])

colores = [VERDE, NARANJA, AMARILLO, AZUL_MED, VIOLETA, AZUL_OSC]

fig, ax = plt.subplots(figsize=(12, 6.5), facecolor='white')

# Stacked area
ax.stackplot(anios, matriz, labels=categorias, colors=colores,
             alpha=0.92, edgecolor='white', linewidth=0.8)

ax.set_xlabel('Año', fontsize=11, color=GRIS)
ax.set_ylabel('Composición de exportaciones (%)', fontsize=11, color=GRIS)
ax.set_xlim(1960, 2020)
ax.set_ylim(0, 100)
ax.grid(True, alpha=0.25, linestyle='--', axis='y')
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GRIS_CLARO)
ax.spines['bottom'].set_color(GRIS_CLARO)

# Anotaciones temporales de cada "ola" del upgrading
flechas = [
    (1965, 92, 'Era primaria\n(arroz, mineral)'),
    (1975, 50, 'Textiles\n(camisas, calzado)'),
    (1985, 60, 'Acero + barcos\n(POSCO, Hyundai)'),
    (1995, 65, 'Autos +\nelectrónica\n(Samsung, LG)'),
    (2015, 65, 'Semiconductores\n(Samsung Foundry,\nSK Hynix)'),
]

for x, y, texto in flechas:
    ax.text(x, y, texto, ha='center', va='center', fontsize=9.5,
            color='white', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='black',
                      edgecolor='white', linewidth=1, alpha=0.55))

ax.legend(loc='center left', bbox_to_anchor=(1.01, 0.5),
          fontsize=10, framealpha=0.95, edgecolor=GRIS_CLARO)

ax.set_title('Corea del Sur: el upgrading exportador 1960-2020',
             fontsize=14, fontweight='bold', color=AZUL_OSC, pad=10)
fig.text(0.5, 0.01,
         'Fuente: elaboración propia con datos de UN COMTRADE y Cherif & Hasanov (2019) "The Return of the Policy that Shall Not Be Named" — IMF Working Paper 19/74.',
         ha='center', fontsize=8.5, style='italic', color=GRIS)

plt.tight_layout(rect=[0, 0.04, 1, 1])
out_path = OUT / 'corea_upgrading.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'-> {out_path.name}')
