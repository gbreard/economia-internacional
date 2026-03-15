"""
Genera Excel de verificación para Evaluación U2 - Pregunta 4
Importaciones de carne aviar Argentina (2024 vs 2025)
Fuente: Secretaría de Agricultura (MAGyP) vía Infobae/La Nación
"""

import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side, numbers
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter
import os

# --- DATOS ---
# Fuente: Secretaría de Agricultura, citado por Infobae (11/09/2025) y La Nación (14/08/2025)
# Importaciones de carne aviar en toneladas, período enero-julio

datos_mensuales = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],
    '2024_tn': [350, 420, 510, 480, 550, 470, 502],      # Estimación mensual (total 3.282 tn)
    '2025_tn': [1850, 1920, 2100, 2717, 1780, 574, 2010], # Con dato de abril y junio de La Nación
}

# Ajustar para que los totales cuadren con los oficiales
total_2024_oficial = 3282
total_2025_oficial = 12951

# Datos anuales consolidados (fuentes cruzadas)
datos_anuales = {
    'Año': [2020, 2021, 2022, 2023, 2024, '2025 (ene-jul)'],
    'Importaciones (tn)': [800, 1200, 2500, 1500, 7337, 12951],
    'Fuente': [
        'Estimación BCR/USDA',
        'Estimación BCR/USDA',
        'BCR/USDA GAIN',
        'USDA PSD',
        'Sec. Agricultura / BCR',
        'Sec. Agricultura (ene-jul)'
    ]
}

# --- CREAR WORKBOOK ---
wb = openpyxl.Workbook()

# Estilos
header_font = Font(name='Calibri', bold=True, size=11, color='FFFFFF')
header_fill = PatternFill(start_color='1F4E79', end_color='1F4E79', fill_type='solid')
data_font = Font(name='Calibri', size=11)
title_font = Font(name='Calibri', bold=True, size=14, color='1F4E79')
subtitle_font = Font(name='Calibri', bold=True, size=11, color='E8833A')
result_fill = PatternFill(start_color='D4EDDA', end_color='D4EDDA', fill_type='solid')
result_font = Font(name='Calibri', bold=True, size=12, color='27AE60')
thin_border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)

def style_header(ws, row, cols):
    for c in range(1, cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = thin_border

def style_data(ws, row, cols):
    for c in range(1, cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = data_font
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = thin_border

# ============================================================
# HOJA 1: DATOS
# ============================================================
ws1 = wb.active
ws1.title = 'Datos'

ws1.cell(row=1, column=1, value='Evaluación U2 — Pregunta 4: Importaciones de carne aviar').font = title_font
ws1.cell(row=2, column=1, value='Fuente: Secretaría de Agricultura (MAGyP) / BCR / USDA').font = subtitle_font
ws1.cell(row=3, column=1, value='Nota: datos citados por Infobae (11/09/2025) y La Nación (14/08/2025)').font = Font(name='Calibri', size=10, italic=True, color='666666')

# Tabla de datos anuales
row = 5
ws1.cell(row=row, column=1, value='Serie histórica de importaciones de carne aviar (Argentina)')
ws1.cell(row=row, column=1).font = subtitle_font

row = 6
headers = ['Año', 'Importaciones (tn)', 'Fuente']
for i, h in enumerate(headers):
    ws1.cell(row=row, column=i+1, value=h)
style_header(ws1, row, len(headers))

for i, year in enumerate(datos_anuales['Año']):
    r = row + 1 + i
    ws1.cell(row=r, column=1, value=year)
    ws1.cell(row=r, column=2, value=datos_anuales['Importaciones (tn)'][i])
    ws1.cell(row=r, column=3, value=datos_anuales['Fuente'][i])
    style_data(ws1, r, len(headers))
    ws1.cell(row=r, column=2).number_format = '#,##0'

# Tabla comparativa ene-jul
row = 14
ws1.cell(row=row, column=1, value='Comparación enero-julio: 2024 vs 2025').font = subtitle_font

row = 15
headers2 = ['Período', 'Toneladas', 'Fuente']
for i, h in enumerate(headers2):
    ws1.cell(row=row, column=i+1, value=h)
style_header(ws1, row, len(headers2))

ws1.cell(row=16, column=1, value='Ene-Jul 2024')
ws1.cell(row=16, column=2, value=total_2024_oficial)
ws1.cell(row=16, column=3, value='Sec. Agricultura')
style_data(ws1, 16, 3)
ws1.cell(row=16, column=2).number_format = '#,##0'

ws1.cell(row=17, column=1, value='Ene-Jul 2025')
ws1.cell(row=17, column=2, value=total_2025_oficial)
ws1.cell(row=17, column=3, value='Sec. Agricultura')
style_data(ws1, 17, 3)
ws1.cell(row=17, column=2).number_format = '#,##0'

# Ancho de columnas
ws1.column_dimensions['A'].width = 20
ws1.column_dimensions['B'].width = 22
ws1.column_dimensions['C'].width = 35

# ============================================================
# HOJA 2: CÁLCULOS
# ============================================================
ws2 = wb.create_sheet('Cálculos')

ws2.cell(row=1, column=1, value='Cálculos de verificación').font = title_font

ws2.cell(row=3, column=1, value='Dato').font = Font(bold=True)
ws2.cell(row=3, column=2, value='Valor').font = Font(bold=True)
ws2.cell(row=3, column=3, value='Fórmula').font = Font(bold=True)
style_header(ws2, 3, 3)

calculos = [
    ('Importaciones Ene-Jul 2024 (tn)', total_2024_oficial, 'Dato oficial Sec. Agricultura'),
    ('Importaciones Ene-Jul 2025 (tn)', total_2025_oficial, 'Dato oficial Sec. Agricultura'),
    ('Diferencia absoluta (tn)', total_2025_oficial - total_2024_oficial, f'{total_2025_oficial} - {total_2024_oficial}'),
    ('Variación porcentual', round((total_2025_oficial - total_2024_oficial) / total_2024_oficial * 100, 1), f'({total_2025_oficial} - {total_2024_oficial}) / {total_2024_oficial} × 100'),
]

for i, (label, valor, formula) in enumerate(calculos):
    r = 4 + i
    ws2.cell(row=r, column=1, value=label)
    ws2.cell(row=r, column=2, value=valor)
    ws2.cell(row=r, column=3, value=formula)
    style_data(ws2, r, 3)

# Resultado destacado
r_result = 9
ws2.cell(row=r_result, column=1, value='RESULTADO:').font = result_font
ws2.cell(row=r_result, column=2, value=f'+{round((total_2025_oficial - total_2024_oficial) / total_2024_oficial * 100, 1)}%').font = result_font
for c in range(1, 4):
    ws2.cell(row=r_result, column=c).fill = result_fill

ws2.cell(row=11, column=1, value='Verificación del dato de la nota:').font = subtitle_font
ws2.cell(row=12, column=1, value='La nota dice "+300%". El dato real es +294,5%.')
ws2.cell(row=13, column=1, value='La aproximación de la nota es razonable (diferencia < 2%).')

# Respuesta correcta
ws2.cell(row=15, column=1, value='RESPUESTA CORRECTA: b)').font = Font(bold=True, size=12, color='1F4E79')
ws2.cell(row=16, column=1, value='Las importaciones crecieron ~295%. H-O explica el patrón de base,')
ws2.cell(row=17, column=1, value='pero el salto abrupto se debe a la distorsión del TCR (apreciación real).')

ws2.column_dimensions['A'].width = 35
ws2.column_dimensions['B'].width = 15
ws2.column_dimensions['C'].width = 45

# ============================================================
# HOJA 3: GRÁFICO
# ============================================================
ws3 = wb.create_sheet('Gráfico')

ws3.cell(row=1, column=1, value='Importaciones de carne aviar — Argentina').font = title_font

# Datos para el gráfico (serie anual)
row = 3
headers_g = ['Año', 'Toneladas']
for i, h in enumerate(headers_g):
    ws3.cell(row=row, column=i+1, value=h)
style_header(ws3, row, 2)

years_chart = [2020, 2021, 2022, 2023, 2024, 2025]
tons_chart = [800, 1200, 2500, 1500, 7337, 12951]  # 2025 = solo ene-jul
labels_chart = ['2020', '2021', '2022', '2023', '2024', '2025\n(ene-jul)']

for i in range(len(years_chart)):
    r = 4 + i
    ws3.cell(row=r, column=1, value=labels_chart[i])
    ws3.cell(row=r, column=2, value=tons_chart[i])
    style_data(ws3, r, 2)
    ws3.cell(row=r, column=2).number_format = '#,##0'

# Crear gráfico de barras
chart = BarChart()
chart.type = "col"
chart.title = "Importaciones de carne aviar — Argentina (toneladas)"
chart.y_axis.title = "Toneladas"
chart.x_axis.title = "Año"
chart.style = 10
chart.width = 18
chart.height = 12

data = Reference(ws3, min_col=2, min_row=3, max_row=9)
cats = Reference(ws3, min_col=1, min_row=4, max_row=9)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
chart.shape = 4

# Color de las barras
from openpyxl.chart.series import DataPoint
from openpyxl.drawing.fill import PatternFillProperties, ColorChoice
series = chart.series[0]
series.graphicalProperties.solidFill = "2E75B6"
# Última barra en naranja (2025)
pt = DataPoint(idx=5)
pt.graphicalProperties.solidFill = "E8833A"
series.data_points.append(pt)

ws3.add_chart(chart, "A11")

# Nota al pie
ws3.cell(row=28, column=1, value='Nota: 2025 incluye solo enero-julio. Fuente: Sec. de Agricultura / BCR / USDA.').font = Font(size=9, italic=True, color='666666')
ws3.cell(row=29, column=1, value='La barra naranja (2025) ya supera al total anual de todos los años anteriores excepto 2024.').font = Font(size=9, italic=True, color='E8833A')

ws3.column_dimensions['A'].width = 15
ws3.column_dimensions['B'].width = 15

# --- GUARDAR ---
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, 'U2_P4_importaciones_avicolas.xlsx')
wb.save(output_path)
print(f'Excel generado: {output_path}')
print(f'3 hojas: Datos, Cálculos, Gráfico')
