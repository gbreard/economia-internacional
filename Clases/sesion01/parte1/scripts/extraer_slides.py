"""
Script para extraer la estructura de slides del contenido parseado del Word
y convertirlo a JSON estructurado
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_TXT = BASE_DIR / "datos" / "clase1_contenido.txt"
OUTPUT_JSON = BASE_DIR / "datos" / "slides_estructurados.json"

def leer_contenido():
    with open(INPUT_TXT, 'r', encoding='utf-8') as f:
        return f.read()

def extraer_slides(contenido):
    """Extrae la estructura de slides del texto"""

    slides = []

    # El deck final de 21 slides está después de "armé el PPT completo de la Clase 1 (21 slides)"
    # Pero la estructura más detallada está en el deck de 22 slides (líneas 874-1058)
    # Vamos a usar esa estructura que tiene más detalle

    # Definición manual basada en el análisis del documento
    slides_data = [
        {
            "numero": 1,
            "tipo": "portada",
            "titulo": "Economía Internacional — Clase 1",
            "subtitulo": "El comercio mundial: auge, colapso y preguntas abiertas",
            "contenido": [],
            "visual": None,
            "notas_docente": "Presentar el curso. Mencionar que esta clase combina medición (indicadores) con historia (etapas del comercio). El objetivo es que salgan pudiendo usar indicadores y describir las grandes fases."
        },
        {
            "numero": 2,
            "tipo": "agenda",
            "titulo": "Agenda de la clase",
            "subtitulo": None,
            "contenido": [
                "Cómo se mide el comercio (4 indicadores)",
                "Serie de largo plazo: qué cambia por etapas",
                "Mapas: rutas y centros de gravedad",
                "Marco analítico: Tecnología + Reglas + Poder"
            ],
            "visual": None,
            "notas_docente": "Explicar que primero vamos a ver las herramientas (indicadores) y después las aplicamos a la historia. La serie de largo plazo es la 'columna vertebral' que conecta todo."
        },
        {
            "numero": 3,
            "tipo": "seccion",
            "titulo": "Bloque A: Medición",
            "subtitulo": "Los indicadores del comercio internacional",
            "contenido": [],
            "visual": None,
            "notas_docente": "Transición al bloque de medición. Enfatizar que sin saber medir no podemos interpretar."
        },
        {
            "numero": 4,
            "tipo": "formula",
            "titulo": "Indicador 1: Índice de comercio mundial",
            "subtitulo": None,
            "contenido": [
                "Fórmula: I_t = 100 × (Comercio_t / Comercio_1913)",
                "1913 = 100 (año base, pico antes de la Primera Guerra)",
                "Si I_t = 50 → comercio es la mitad del de 1913",
                "Si I_t = 200 → comercio es el doble del de 1913"
            ],
            "visual": None,
            "notas_docente": "¿Por qué 1913? Fue el pico de la primera globalización, antes de que las guerras destruyeran el sistema. Usar un índice evita problemas de inflación y permite comparar períodos largos."
        },
        {
            "numero": 5,
            "tipo": "grafico_texto",
            "titulo": "Índice de comercio mundial (1800-1938)",
            "subtitulo": None,
            "contenido": [
                "1800: índice 2.4 (casi nada)",
                "1870: índice 25 (x10 en 70 años)",
                "1913: índice 100 (pico)",
                "1932: índice 74 (colapso -26%)"
            ],
            "visual": "graficos/indice_comercio.png",
            "fuente": "Federico-Tena World Trade Historical Database",
            "notas_docente": "El gráfico muestra las dos fases: crecimiento exponencial 1800-1913 y colapso 1914-1938. Preguntar: '¿Qué pasó en 1914?' y '¿Por qué el comercio no se recuperó en los años 20?'"
        },
        {
            "numero": 6,
            "tipo": "formula",
            "titulo": "Indicador 2: Participación regional",
            "subtitulo": None,
            "contenido": [
                "Fórmula: s_r,t = (X_r,t / X_mundo,t) × 100",
                "Mide: qué porcentaje del comercio mundial tiene cada región",
                "Permite ver quién 'gana' y quién 'pierde' participación",
                "Europa dominó el siglo XIX; Asia creció en el XX"
            ],
            "visual": None,
            "notas_docente": "Este indicador permite ver cambios en la geografía del comercio. La 'globalización' del siglo XIX era básicamente comercio europeo con el mundo."
        },
        {
            "numero": 7,
            "tipo": "grafico_texto",
            "titulo": "Participación regional (1800-1938)",
            "subtitulo": None,
            "contenido": [
                "Europa: 60-70% (domina todo el período)",
                "Américas: 10-20%",
                "Asia: 10-15%",
                "La 'globalización' del XIX era comercio europeo con el mundo"
            ],
            "visual": "graficos/participacion_regional.png",
            "fuente": "FTWTHD",
            "notas_docente": "Enfatizar que 'globalización' es un término engañoso. El comercio era muy concentrado en Europa. Latinoamérica siempre periférica."
        },
        {
            "numero": 8,
            "tipo": "formula",
            "titulo": "Indicador 3: Concentración (HHI)",
            "subtitulo": None,
            "contenido": [
                "Fórmula: HHI_t = Σ(s_i,t)²",
                "HHI cercano a 0 → comercio muy disperso",
                "HHI cercano a 1 → comercio concentrado en pocos",
                "También se usa para medir poder de mercado (antimonopolio)"
            ],
            "visual": None,
            "notas_docente": "Este indicador es más técnico. Sirve para mostrar que el comercio se fue diversificando con el tiempo (más países participan). Conectar con el concepto de 'poder de mercado'."
        },
        {
            "numero": 9,
            "tipo": "grafico_texto",
            "titulo": "Concentración del comercio (HHI)",
            "subtitulo": None,
            "contenido": [
                "1800: HHI alto (pocos países comercian)",
                "1913: HHI más bajo (más países participan)",
                "1930s: sube levemente (bloques comerciales)",
                "La diversificación fue un proceso gradual de 100+ años"
            ],
            "visual": "graficos/hhi.png",
            "fuente": "FTWTHD",
            "notas_docente": "El HHI baja porque más países se incorporan al comercio mundial. Pero ojo: la participación sigue siendo desigual. La suba en los 30s refleja la fragmentación en bloques."
        },
        {
            "numero": 10,
            "tipo": "texto",
            "titulo": "Indicador 4: Cobertura de datos",
            "subtitulo": "Por qué importa la calidad de los datos",
            "contenido": [
                "Más cobertura = datos más confiables",
                "Menos cobertura = estimaciones con más error",
                "Siempre reportar cobertura de las fuentes",
                "Los datos históricos tienen limitaciones"
            ],
            "visual": "graficos/cobertura.png",
            "notas_docente": "Este indicador metodológico es importante para formar pensamiento crítico. Los estudiantes deben entender que los datos no son 'la realidad', son una representación con limitaciones."
        },
        {
            "numero": 11,
            "tipo": "texto",
            "titulo": "Tres advertencias para leer series de comercio",
            "subtitulo": None,
            "contenido": [
                "1. Precios vs cantidades: valores nominales mezclan ambos",
                "2. Comercio 'bruto' puede contar el mismo insumo varias veces",
                "3. Series largas mezclan fuentes de distinta calidad"
            ],
            "visual": None,
            "notas_docente": "Estas advertencias son clave para no sobreinterpretar los datos. Especialmente importante cuando comparamos períodos muy distintos (siglo XIX vs XXI)."
        },
        {
            "numero": 12,
            "tipo": "seccion",
            "titulo": "Bloque B: Historia por etapas",
            "subtitulo": "Anclada en la serie de largo plazo",
            "contenido": [],
            "visual": None,
            "notas_docente": "Transición al bloque histórico. Ahora que tenemos las herramientas, las aplicamos para entender las etapas."
        },
        {
            "numero": 13,
            "tipo": "texto",
            "titulo": "Marco analítico: tres fuerzas",
            "subtitulo": "Para explicar cualquier período del comercio",
            "contenido": [
                "TECNOLOGÍA: ¿Cuánto cuesta mover bienes? (vela→vapor→contenedor)",
                "REGLAS: ¿Quién puede comerciar? (monopolios, aranceles, OMC)",
                "PODER: ¿Quién garantiza estabilidad? (hegemonía, marina, moneda)"
            ],
            "visual": None,
            "notas_docente": "Este marco se va a usar en todo el curso. Las tres fuerzas operan juntas. Si una falla, el sistema se quiebra. Cada teoría del comercio enfatiza alguna de estas fuerzas."
        },
        {
            "numero": 14,
            "tipo": "texto",
            "titulo": "Cinco etapas del comercio internacional",
            "subtitulo": "Timeline con medida asociada",
            "contenido": [
                "1. Ibérico-colonial (1500-1650): monopolios, rutas globales",
                "2. Hegemonía UK / 1ª globalización (1800-1914): libre comercio, vapor",
                "3. Colapso (1914-1945): guerras, proteccionismo, bloques",
                "4. Hegemonía EEUU (1945-2008): instituciones, liberalización",
                "5. Slowbalization (2008-hoy): tensiones, reconfiguración"
            ],
            "visual": None,
            "notas_docente": "Esta periodización es una simplificación didáctica. La idea es que cada etapa tiene una configuración distinta de tecnología, reglas y poder."
        },
        {
            "numero": 15,
            "tipo": "grafico_texto",
            "titulo": "Etapa 1: Economía-mundo ibérica (1500-1650)",
            "subtitulo": None,
            "contenido": [
                "Portugal: ruta del Cabo → Asia (especias)",
                "España: Atlántico → América (plata)",
                "Modelo: monopolios estatales (Casa de Contratación)",
                "El Estado absorbe riesgos y captura rentas"
            ],
            "visual": "img/rutas_ibericas.png",
            "fuente": "Mapas históricos",
            "notas_docente": "Esta etapa muestra un modelo muy diferente al actual. No hay 'libre comercio', hay monopolios. El Estado es el actor principal. Las empresas privadas (VOC holandesa) recién aparecen después."
        },
        {
            "numero": 16,
            "tipo": "grafico_texto",
            "titulo": "El Galeón de Manila: primera ruta global",
            "subtitulo": None,
            "contenido": [
                "Ruta: Manila → Acapulco → España",
                "Comerciaba: seda china, especias, porcelana",
                "Pago: plata americana",
                "Primera conexión regular Asia-América-Europa (1565-1815)"
            ],
            "visual": "img/galeon_manila.png",
            "fuente": "Ilustración histórica",
            "notas_docente": "El Galeón de Manila es un caso fascinante de comercio triangular pre-industrial. La plata americana financiaba las compras en Asia. Mostrar cómo el comercio conectaba continentes antes de la revolución industrial."
        },
        {
            "numero": 17,
            "tipo": "grafico_texto",
            "titulo": "Etapa 2: Primera globalización (1800-1914)",
            "subtitulo": "UK como centro del sistema",
            "contenido": [
                "Revolución del transporte: vapor (-60% costo flete)",
                "Ferrocarril conecta interiores",
                "Canal de Suez (1869) acorta rutas",
                "Tecnología + libre comercio + patrón oro + Royal Navy"
            ],
            "visual": "img/vapor_randmcnally_1917.jpg",
            "fuente": "Rand McNally, 1917",
            "notas_docente": "Esta es la etapa de crecimiento exponencial que vimos en el gráfico. Gran Bretaña lidera: tiene la tecnología, impone las reglas (libre comercio unilateral), y tiene el poder naval para garantizar las rutas."
        },
        {
            "numero": 18,
            "tipo": "grafico_texto",
            "titulo": "El telégrafo: la primera internet",
            "subtitulo": None,
            "contenido": [
                "Información en minutos (vs meses por barco)",
                "Precios se arbitran globalmente",
                "Contratos a distancia posibles",
                "Para 1900: 300.000 km de cables submarinos"
            ],
            "visual": "img/cables_eastern_1901.png",
            "fuente": "Eastern Telegraph Company, 1901",
            "notas_docente": "El telégrafo es un caso perfecto de cómo la tecnología cambia el comercio. Antes, un comerciante no sabía los precios en destino hasta llegar. Con el telégrafo, puede arbitrar en tiempo real."
        },
        {
            "numero": 19,
            "tipo": "grafico_texto",
            "titulo": "Etapa 3: Colapso (1914-1945)",
            "subtitulo": None,
            "contenido": [
                "1914-18: Primera Guerra Mundial",
                "1920s: recuperación parcial, vuelta al patrón oro",
                "1929-33: crack + espiral proteccionista",
                "1930s: fragmentación en bloques comerciales"
            ],
            "visual": "graficos/indice_colapso.png",
            "fuente": "FTWTHD",
            "notas_docente": "El colapso fue rápido y profundo. No fue solo la guerra; fue la combinación de guerra + mala política monetaria + proteccionismo + crisis financiera. Las tres fuerzas fallaron juntas."
        },
        {
            "numero": 20,
            "tipo": "grafico_texto",
            "titulo": "El poder detrás del comercio",
            "subtitulo": "Hegemonía británica y su colapso",
            "contenido": [
                "Royal Navy: supremacía naval 1815-1914",
                "Patrón oro: libra como moneda de reserva",
                "Pax Britannica: rutas marítimas seguras",
                "¿Por qué colapsó? Guerras agotaron a GB, EEUU no asumió el rol hasta 1945"
            ],
            "visual": "img/navy_league_1922.jpg",
            "fuente": "Navy League, 1922",
            "notas_docente": "Este slide conecta comercio con poder. El libre comercio del siglo XIX no fue 'natural'; fue sostenido por el poder británico. Sin hegemón que garantice las reglas, el sistema se fragmenta."
        },
        {
            "numero": 21,
            "tipo": "seccion",
            "titulo": "Cierre",
            "subtitulo": None,
            "contenido": [],
            "visual": None,
            "notas_docente": "Transición al cierre."
        },
        {
            "numero": 22,
            "tipo": "texto",
            "titulo": "Resumen: qué vimos hoy",
            "subtitulo": None,
            "contenido": [
                "4 indicadores: índice, participación, HHI, cobertura",
                "5 etapas históricas: ibérica → UK → colapso → EEUU → hoy",
                "Marco analítico: Tecnología + Reglas + Poder",
                "El comercio no crece linealmente: hay auges y colapsos"
            ],
            "visual": None,
            "notas_docente": "Recapitular los puntos principales. Enfatizar que los indicadores y los hechos estilizados están conectados: los indicadores nos permiten VER los patrones; el marco analítico nos permite EXPLICARLOS."
        },
        {
            "numero": 23,
            "tipo": "texto",
            "titulo": "Próxima clase",
            "subtitulo": "Clase 2: Balanza de pagos y tipo de cambio",
            "contenido": [
                "Más indicadores: cuenta corriente, tipo de cambio real",
                "Desequilibrios globales: EEUU, China, Alemania",
                "El caso argentino: el ciclo de apreciación-crisis",
                "Lectura: revisar programa"
            ],
            "visual": None,
            "notas_docente": "Anticipar que en la clase 2 completamos el 'kit de herramientas' con indicadores de balanza de pagos y tipo de cambio, y los aplicamos a casos contemporáneos."
        },
        {
            "numero": 24,
            "tipo": "cierre",
            "titulo": "¿Preguntas?",
            "subtitulo": "Economía Internacional | UMET | 2026",
            "contenido": [],
            "visual": None,
            "notas_docente": "Abrir espacio para preguntas."
        }
    ]

    return slides_data


def main():
    print("Extrayendo estructura de slides...")

    slides = extraer_slides(None)

    # Crear estructura final
    resultado = {
        "metadata": {
            "clase": "Clase 1",
            "titulo": "El comercio mundial: auge, colapso y preguntas abiertas",
            "duracion": "2 horas",
            "total_slides": len(slides)
        },
        "slides": slides
    }

    # Guardar JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"JSON guardado: {OUTPUT_JSON}")
    print(f"Total slides: {len(slides)}")

    # Resumen por tipo
    tipos = {}
    for s in slides:
        t = s['tipo']
        tipos[t] = tipos.get(t, 0) + 1

    print("\nSlides por tipo:")
    for t, c in sorted(tipos.items()):
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
