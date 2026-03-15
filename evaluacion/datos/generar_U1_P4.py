"""
Genera U1_P4_apertura_comercial.xlsx
Datos: Trade (% of GDP) para Argentina, China y Alemania, 2000-2022
Fuente: Banco Mundial (NE.TRD.GNFS.ZS)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from pathlib import Path

wb = Workbook()

# ==================== HOJA 1: DATOS ====================
ws = wb.active
ws.title = "Datos"

# Datos del Banco Mundial (NE.TRD.GNFS.ZS) — descargados febrero 2026
datos = {
    "Argentina": {
        2000: 22.62, 2001: 21.85, 2002: 41.75, 2003: 40.64, 2004: 40.69,
        2005: 40.55, 2006: 40.43, 2007: 40.95, 2008: 40.40, 2009: 34.06,
        2010: 34.97, 2011: 35.21, 2012: 30.53, 2013: 29.33, 2014: 28.41,
        2015: 22.49, 2016: 26.09, 2017: 25.29, 2018: 30.76, 2019: 32.63,
        2020: 30.20, 2021: 33.08, 2022: 31.58
    },
    "China": {
        2000: 39.01, 2001: 38.08, 2002: 42.19, 2003: 51.08, 2004: 58.64,
        2005: 61.36, 2006: 63.57, 2007: 61.27, 2008: 56.71, 2009: 44.42,
        2010: 49.85, 2011: 49.95, 2012: 47.48, 2013: 45.92, 2014: 44.07,
        2015: 38.70, 2016: 36.18, 2017: 36.95, 2018: 36.89, 2019: 35.20,
        2020: 34.04, 2021: 36.52, 2022: 37.44
    },
    "Alemania": {
        2000: 59.20, 2001: 59.56, 2002: 58.33, 2003: 58.91, 2004: 62.91,
        2005: 66.95, 2006: 72.76, 2007: 74.88, 2008: 76.11, 2009: 66.14,
        2010: 73.89, 2011: 78.43, 2012: 79.33, 2013: 77.59, 2014: 76.85,
        2015: 77.76, 2016: 76.01, 2017: 77.45, 2018: 79.13, 2019: 79.07,
        2020: 72.93, 2021: 79.92, 2022: 88.79
    }
}

anios = list(range(2000, 2023))
paises = ["Argentina", "China", "Alemania"]

# Encabezados
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)

ws.cell(row=1, column=1, value="Año").font = header_font
ws.cell(row=1, column=1).fill = header_fill
ws.cell(row=1, column=1).border = border
for j, pais in enumerate(paises):
    cell = ws.cell(row=1, column=j+2, value=f"{pais} (% PIB)")
    cell.font = header_font
    cell.fill = header_fill
    cell.border = border

for i, anio in enumerate(anios):
    ws.cell(row=i+2, column=1, value=anio).border = border
    for j, pais in enumerate(paises):
        cell = ws.cell(row=i+2, column=j+2, value=round(datos[pais][anio], 2))
        cell.number_format = '0.00'
        cell.border = border

# Fuente
ws.cell(row=26, column=1, value="Fuente: Banco Mundial — Trade (% of GDP) [NE.TRD.GNFS.ZS]")
ws.cell(row=26, column=1).font = Font(italic=True, color="666666")

# Ancho de columnas
ws.column_dimensions['A'].width = 8
for j in range(2, 5):
    ws.column_dimensions[get_column_letter(j)].width = 20


# ==================== HOJA 2: CÁLCULOS ====================
ws2 = wb.create_sheet("Cálculos")

ws2.cell(row=1, column=1, value="Promedios por sub-período").font = Font(bold=True, size=14)

# Encabezados tabla
for j, header in enumerate(["País", "Promedio 2000-2007", "Promedio 2015-2022", "Diferencia (pp)"]):
    cell = ws2.cell(row=3, column=j+1, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.border = border

for i, pais in enumerate(paises):
    row = 4 + i
    p1_vals = [datos[pais][a] for a in range(2000, 2008)]
    p2_vals = [datos[pais][a] for a in range(2015, 2023)]
    prom1 = sum(p1_vals) / len(p1_vals)
    prom2 = sum(p2_vals) / len(p2_vals)
    diff = prom2 - prom1

    ws2.cell(row=row, column=1, value=pais).border = border
    ws2.cell(row=row, column=1).font = Font(bold=True)

    cell_p1 = ws2.cell(row=row, column=2, value=round(prom1, 1))
    cell_p1.number_format = '0.0'
    cell_p1.border = border

    cell_p2 = ws2.cell(row=row, column=3, value=round(prom2, 1))
    cell_p2.number_format = '0.0'
    cell_p2.border = border

    cell_diff = ws2.cell(row=row, column=4, value=round(diff, 1))
    cell_diff.number_format = '+0.0;-0.0;0.0'
    cell_diff.border = border
    if diff < 0:
        cell_diff.font = Font(bold=True, color="CC0000")
    else:
        cell_diff.font = Font(bold=True, color="27AE60")

# Respuesta
ws2.cell(row=8, column=1, value="RESPUESTA CORRECTA: b)").font = Font(bold=True, size=12, color="1F4E79")
ws2.cell(row=9, column=1, value="China tuvo la mayor caída (~15 pp). No se 'cerró': su PIB creció más rápido que su comercio.")
ws2.cell(row=9, column=1).font = Font(italic=True)

ws2.column_dimensions['A'].width = 16
ws2.column_dimensions['B'].width = 22
ws2.column_dimensions['C'].width = 22
ws2.column_dimensions['D'].width = 18


# ==================== HOJA 3: GRÁFICO ====================
ws3 = wb.create_sheet("Gráfico")

# Copiar datos para el gráfico
ws3.cell(row=1, column=1, value="Año")
for j, pais in enumerate(paises):
    ws3.cell(row=1, column=j+2, value=pais)

for i, anio in enumerate(anios):
    ws3.cell(row=i+2, column=1, value=anio)
    for j, pais in enumerate(paises):
        ws3.cell(row=i+2, column=j+2, value=round(datos[pais][anio], 2))

# Gráfico de líneas
chart = LineChart()
chart.title = "Apertura comercial (Trade % GDP) — 2000-2022"
chart.y_axis.title = "% del PIB"
chart.x_axis.title = "Año"
chart.style = 10
chart.width = 28
chart.height = 16

colors = ["0EA5E9", "E74C3C", "1F4E79"]
for j, pais in enumerate(paises):
    data = Reference(ws3, min_col=j+2, min_row=1, max_row=24)
    cats = Reference(ws3, min_col=1, min_row=2, max_row=24)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)

for idx, series in enumerate(chart.series):
    series.graphicalProperties.line.width = 25000
    series.graphicalProperties.line.solidFill = colors[idx]

ws3.add_chart(chart, "A27")

# Gráfico de barras con diferencias
ws3.cell(row=28, column=7, value="País")
ws3.cell(row=28, column=8, value="Cambio (pp)")
for i, pais in enumerate(paises):
    p1_vals = [datos[pais][a] for a in range(2000, 2008)]
    p2_vals = [datos[pais][a] for a in range(2015, 2023)]
    diff = sum(p2_vals)/len(p2_vals) - sum(p1_vals)/len(p1_vals)
    ws3.cell(row=29+i, column=7, value=pais)
    ws3.cell(row=29+i, column=8, value=round(diff, 1))

bar_chart = BarChart()
bar_chart.title = "Cambio en apertura promedio: 2000-07 vs 2015-22 (pp)"
bar_chart.y_axis.title = "Puntos porcentuales"
bar_chart.style = 10
bar_chart.width = 20
bar_chart.height = 14

data_ref = Reference(ws3, min_col=8, min_row=28, max_row=31)
cats_ref = Reference(ws3, min_col=7, min_row=29, max_row=31)
bar_chart.add_data(data_ref, titles_from_data=True)
bar_chart.set_categories(cats_ref)

ws3.add_chart(bar_chart, "G2")


# Guardar
output = Path(__file__).parent / "U1_P4_apertura_comercial.xlsx"
wb.save(output)
print(f"Generado: {output}")
print(f"Hojas: Datos, Cálculos, Gráfico")
