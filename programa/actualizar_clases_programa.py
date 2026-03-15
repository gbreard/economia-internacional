"""
Reescribe Clases del programa.docx: de 20 clases a 12 sesiones de 4 horas.
Genera una tabla nueva con título, subtítulo e introducción.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from pathlib import Path

path = Path(r"C:\Users\gbrea\OneDrive\Documentos\UMET\Economia Intenacional\programa\Clases del programa.docx")

# ========================================
# DATOS DE LAS 12 SESIONES
# ========================================
sessions = [
    {
        "sesion": "1",
        "fecha": "19/03",
        "unidad": "Unidad 1",
        "tema": "Hechos estilizados históricos, balanza de pagos y tipo de cambio",
        "desc": (
            "Primera parte: Presentación del curso. Indicadores de comercio mundial, "
            "periodización histórica (economía-mundo ibérica → hegemonía británica → "
            "crisis 1914-1945 → Bretton Woods → globalización financiera). Articulación "
            "entre comercio, poder, tecnología y reglas. "
            "Segunda parte: Introducción a la balanza de pagos (cuenta corriente y "
            "financiera). Tipo de cambio nominal y real. Competitividad externa y saldo "
            "comercial. Enfoques desarrollistas sobre tipo de cambio y estructura productiva."
        ),
    },
    {
        "sesion": "2",
        "fecha": "26/03",
        "unidad": "Unidad 2",
        "tema": "Mercantilistas, Smith, Ricardo y ventajas comparativas",
        "desc": (
            "Primera parte: Contexto histórico del debate mercantilismo vs. Smith. "
            "Ventajas absolutas, división del trabajo y especialización internacional. "
            "Segunda parte: Modelo ricardiano: supuestos, FPP, costos de oportunidad. "
            "Equilibrio en autarquía y con comercio. Ganancias del comercio. "
            "Índice de ventaja comparativa revelada (Balassa)."
        ),
    },
    {
        "sesion": "3",
        "fecha": "09/04",
        "unidad": "Unidad 2",
        "tema": "Modelo neoclásico estándar y Heckscher-Ohlin",
        "desc": (
            "Primera parte: Paso de Ricardo a la visión neoclásica. Dotación de recursos, "
            "curvas de transformación, oferta y demanda relativa. Precios relativos en "
            "autarquía y con comercio. "
            "Segunda parte: Modelo H-O, teoremas de Stolper-Samuelson y Rybczynski. "
            "Movilidad internacional de factores. Paradoja de Leontief y evidencia empírica. "
            "Cierra Unidad 2."
        ),
    },
    {
        "sesion": "4",
        "fecha": "16/04",
        "unidad": "Unidad 3",
        "tema": "Rendimientos crecientes, competencia imperfecta y nueva geografía económica",
        "desc": (
            "Limitaciones de la competencia perfecta para explicar el comercio entre países "
            "similares. Competencia monopolística a la Krugman: variedades, tamaño del "
            "mercado, comercio Norte-Norte. Comercio intraindustrial: definición, tipos "
            "(horizontal/vertical), índice de Grubel-Lloyd, determinantes. Evidencia comparada "
            "y caso Mercosur automotriz. Home-market effect. Nueva geografía económica: "
            "fuerzas centrípetas y centrífugas, concentración territorial, caso Argentina."
        ),
    },
    {
        "sesion": "5",
        "fecha": "23/04",
        "unidad": "Unidad 3",
        "tema": "IIT en profundidad, ciclo del producto, firmas heterogéneas y dumping",
        "desc": (
            "Determinantes del comercio intraindustrial, caso Argentina-Brasil en profundidad. "
            "Teoría del ciclo del producto (Vernon): innovación, estandarización y traslado "
            "de la producción. Modelos de firmas heterogéneas (Melitz): productividad, costos "
            "de entrada, selección de exportadores. Dumping: discriminación de precios "
            "internacional, medidas antidumping, reglas OMC. Cierra Unidad 3."
        ),
    },
    {
        "sesion": "6",
        "fecha": "30/04",
        "unidad": "Unidad 4",
        "tema": "Prebisch, centro-periferia y deterioro de los términos del intercambio",
        "desc": (
            "Visión estructuralista latinoamericana: centro-periferia, especialización "
            "productiva y desarrollo desigual. Industrialización por sustitución de "
            "importaciones (ISI). Tesis Prebisch-Singer sobre deterioro de los términos "
            "del intercambio: fundamentos teóricos, evidencia histórica y consecuencias "
            "para países primario-exportadores."
        ),
    },
    {
        "sesion": "7",
        "fecha": "07/05",
        "unidad": "Unidad 4",
        "tema": "Intercambio desigual, ventajas dinámicas e innovación",
        "desc": (
            "Teoría del intercambio desigual (Emmanuel): diferencias internacionales de "
            "salarios, apropiación de valor, comercio Norte-Sur. Ventajas comparativas "
            "dinámicas: learning by doing, acumulación de capacidades, política industrial. "
            "Perspectiva neoschumpeteriana: innovación, path dependence, upgrading. "
            "Efectos del comercio y el cambio tecnológico sobre empleo y desigualdad "
            "salarial. Cierra Unidad 4."
        ),
    },
    {
        "sesion": "8",
        "fecha": "14/05",
        "unidad": "Unidad 5",
        "tema": "Movilidad de factores, empresas transnacionales e IED",
        "desc": (
            "Movilidad internacional de factores: del teorema de igualación del precio de "
            "los factores a la movilidad efectiva de capital (IED) y trabajo (migración, "
            "brain drain, remesas). Empresas transnacionales como organizadoras del comercio "
            "mundial. Motivaciones de la IED (recursos, mercados, eficiencia, activos "
            "estratégicos). Modos de entrada y efectos en países receptores. Introducción "
            "a cadenas globales de valor: participación, posición, gobernanza, upgrading."
        ),
    },
    {
        "sesion": "9",
        "fecha": "21/05",
        "unidad": "Unidad 5",
        "tema": "Cadenas globales de valor en América Latina y Argentina",
        "desc": (
            "CGV en profundidad: captura de valor, trampas de bajo valor agregado, "
            "estrategias de upgrading. Estudios de caso de inserción en CGV en América "
            "Latina y Argentina. Posiciones típicas (ensamblaje, commodities, servicios). "
            "Oportunidades y límites para el desarrollo. Rol de la política productiva, "
            "comercial y cambiaria. Cierra Unidad 5."
        ),
    },
    {
        "sesion": "10",
        "fecha": "28/05",
        "unidad": "Unidad 6",
        "tema": "Instrumentos de política comercial e integración económica regional",
        "desc": (
            "Aranceles (específicos y ad valorem), protección efectiva. Cuotas, subsidios, "
            "medidas no arancelarias. Medidas de defensa comercial: antidumping, "
            "compensatorias, salvaguardias. Efectos sobre precios, producción, consumo y "
            "bienestar. Integración económica: motivaciones, tipos (ZLC, unión aduanera, "
            "mercado común, unión económica/monetaria). Creación y desviación de comercio. "
            "Unión Europea y Mercosur. Cierra Unidad 6."
        ),
    },
    {
        "sesion": "11",
        "fecha": "04/06",
        "unidad": "Unidad 7",
        "tema": "Crisis 2008, guerra comercial, transición verde y caso argentino",
        "desc": (
            "Crisis financiera global 2008-2009 y su impacto sobre el comercio. "
            "«Slowbalization»: relocalización, near-shoring y friend-shoring. Guerra "
            "comercial y tecnológica EEUU-China: aranceles, restricciones tecnológicas, "
            "reconfiguración de cadenas. Transición energética: bienes verdes, minerales "
            "críticos, mecanismos de ajuste de carbono en frontera. Comercio exterior "
            "argentino: estructura exportadora/importadora, tipo de cambio real, restricción "
            "externa, Mercosur y desafíos de inserción. Cierra Unidad 7."
        ),
    },
    {
        "sesion": "12",
        "fecha": "11/06",
        "unidad": "—",
        "tema": "Coloquio final grupal",
        "desc": (
            "Presentaciones grupales de casos de inserción internacional. Los grupos "
            "exponen y defienden el análisis de un sector, cadena productiva o país, "
            "integrando conceptos del curso (comercio, CGV, política comercial, tipo "
            "de cambio). Evaluación: aprobado/desaprobado."
        ),
    },
]

# ========================================
# CREAR DOCUMENTO
# ========================================
doc = Document()

# Configurar estilo Normal
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

# --- Título ---
title_para = doc.add_paragraph()
title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_para.space_after = Pt(4)
run = title_para.add_run("Plan de Sesiones – Economía Internacional (48 horas, 12 sesiones)")
run.bold = True
run.font.size = Pt(16)
run.font.name = 'Calibri'

# --- Subtítulo ---
sub_para = doc.add_paragraph()
sub_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub_para.space_after = Pt(8)
run = sub_para.add_run("(Con énfasis en comercio internacional, tipo de cambio, desarrollo e inserción externa)")
run.italic = True
run.font.size = Pt(11)
run.font.name = 'Calibri'

# --- Introducción ---
intro_para = doc.add_paragraph()
intro_para.space_after = Pt(12)
parts = [
    ("Este plan organiza las ", False),
    ("12 sesiones de 4 horas", True),
    (" del curso de ", False),
    ("Economía Internacional", True),
    (" en relación con las 7 unidades temáticas del programa. "
     "Cada fila indica la unidad, el tema principal y una breve descripción "
     "del contenido de la sesión.", False),
]
for text, bold in parts:
    run = intro_para.add_run(text)
    run.bold = bold
    run.font.size = Pt(11)
    run.font.name = 'Calibri'

# --- Tabla ---
table = doc.add_table(rows=1 + len(sessions), cols=5, style='Table Grid')
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.autofit = True

# Anchos de columna aproximados
widths = [Cm(1.5), Cm(2.0), Cm(2.5), Cm(5.0), Cm(9.0)]
for row in table.rows:
    for i, cell in enumerate(row.cells):
        cell.width = widths[i]

# Header
header_texts = ["Sesión", "Fecha", "Unidad", "Tema principal", "Descripción breve"]
header_row = table.rows[0]
for i, text in enumerate(header_texts):
    cell = header_row.cells[i]
    cell.text = ""
    para = cell.paragraphs[0]
    run = para.add_run(text)
    run.bold = True
    run.font.size = Pt(10)
    run.font.name = 'Calibri'
    # Fondo gris claro para header
    shading = cell._element.find(qn('w:tcPr'))
    if shading is None:
        tcPr = cell._element.makeelement(qn('w:tcPr'), {})
        cell._element.insert(0, tcPr)
    else:
        tcPr = shading
    shd = tcPr.makeelement(qn('w:shd'), {
        qn('w:val'): 'clear',
        qn('w:color'): 'auto',
        qn('w:fill'): 'D9E2F3',
    })
    tcPr.append(shd)

# Data rows
for ri, s in enumerate(sessions):
    row = table.rows[ri + 1]
    values = [s["sesion"], s["fecha"], s["unidad"], s["tema"], s["desc"]]
    for ci, val in enumerate(values):
        cell = row.cells[ci]
        cell.text = ""
        para = cell.paragraphs[0]
        run = para.add_run(val)
        run.font.size = Pt(9)
        run.font.name = 'Calibri'
        # Centrar columnas de sesión y fecha
        if ci in (0, 1):
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER

# ========================================
# GUARDAR
# ========================================
doc.save(str(path))
print(f"✓ Documento guardado: {path}")
print(f"  - {len(sessions)} sesiones en tabla")
print(f"  - Título, subtítulo e introducción incluidos")

# Verificación
print("\n=== VERIFICACIÓN ===\n")
doc2 = Document(str(path))
print(f"Párrafos: {len(doc2.paragraphs)}")
print(f"Tablas: {len(doc2.tables)}")
if doc2.tables:
    t = doc2.tables[0]
    print(f"Filas: {len(t.rows)} (1 header + {len(t.rows)-1} sesiones)")
    print(f"\nContenido:")
    for ri, row in enumerate(t.rows):
        cells = [c.text[:50] for c in row.cells]
        print(f"  [{ri}] {cells[0]:>6} | {cells[1]:<12} | {cells[2]}")
