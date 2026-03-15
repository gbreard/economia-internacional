"""
Agrega slides de gráficos para indicadores 5, 6 y 7.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"
OUTPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"

# Nuevos slides a insertar
NUEVOS_SLIDES = [
    # Después de Indicador 5 (Balanza comercial) - actualmente slide 12
    {
        "insert_after_titulo": "Indicador 5: Balanza comercial",
        "slides": [
            {
                "tipo": "grafico_texto",
                "titulo": "Balanza comercial Argentina (1960-2023)",
                "subtitulo": None,
                "contenido": [
                    "Déficit en Convertibilidad (1991-2001)",
                    "Superávit récord post-crisis 2002",
                    "Ciclo: peso caro → déficit, peso barato → superávit",
                    "Volatilidad extrema comparado con otros países"
                ],
                "visual": "graficos/balanza_comercial_argentina.png",
                "fuente": "Banco Mundial / INDEC",
                "notas_docente": """LECTURA DEL GRÁFICO (8 minutos)

IDENTIFICAR PERÍODOS:
- Barras verdes = superávit (X > M)
- Barras rojas = déficit (X < M)
- Zona naranja = Convertibilidad
- Zona verde claro = Post-crisis

PUNTOS CLAVE:
1. Convertibilidad: déficit persistente porque el peso estaba sobrevaluado
2. 2002: superávit récord (+15% PIB) por colapso de importaciones + devaluación
3. 2003-2011: superávits sostenidos (commodities + TC competitivo)
4. 2017-2018: vuelve el déficit (apreciación + sequía)

PREGUNTA: "¿Por qué Argentina tuvo el superávit más grande del mundo en 2002?"
RESPUESTA: Combinación de: (1) colapso de importaciones por recesión brutal, (2) tipo de cambio ultra-competitivo post-devaluación, (3) precios de commodities subiendo.

CONEXIÓN CON TEORÍA: Esto muestra que la balanza comercial está muy ligada al tipo de cambio real. Anticipar la clase de TC."""
            },
            {
                "tipo": "grafico_texto",
                "titulo": "Balanza comercial comparada (% PIB)",
                "subtitulo": "Argentina, EEUU, Alemania, China, Brasil",
                "contenido": [
                    "EEUU: déficit persistente (privilegio del dólar)",
                    "Alemania: superávit persistente (competitividad industrial)",
                    "China: superávit desde 2000 (fábrica del mundo)",
                    "Argentina: alta volatilidad (ciclo cambiario)"
                ],
                "visual": "graficos/balanza_comercial_comparativo.png",
                "fuente": "Banco Mundial",
                "notas_docente": """COMPARACIÓN INTERNACIONAL (7 minutos)

PATRONES ESTRUCTURALES:
- EEUU siempre negativo → puede porque emite dólares
- Alemania siempre positivo → modelo exportador
- China positivo desde entrada a OMC (2001)
- Argentina y Brasil: volátiles, dependen del ciclo

PREGUNTA: "¿Por qué EEUU puede tener déficit permanente sin crisis?"
RESPUESTA: Porque emite la moneda de reserva mundial. El mundo quiere dólares.

PREGUNTA: "¿Por qué Alemania tiene superávit permanente?"
RESPUESTA: Industria muy competitiva + salarios moderados + euro débil para su productividad.

CONEXIÓN CON PREBISCH: Los países periféricos (Argentina, Brasil) tienen balanzas volátiles que dependen de precios de commodities. Los centrales (EEUU, Alemania) tienen patrones más estables. Esto conecta con la próxima clase sobre centro-periferia."""
            }
        ]
    },
    # Después de Indicador 6 (Apertura comercial) - actualmente slide 13
    {
        "insert_after_titulo": "Indicador 6: Apertura comercial",
        "slides": [
            {
                "tipo": "grafico_texto",
                "titulo": "Apertura comercial comparada",
                "subtitulo": "El indicador tiene trampas",
                "contenido": [
                    "Singapur: 300-400% (re-exportación)",
                    "Alemania: ~80% (industria exportadora)",
                    "China: 30-40% (creció mucho)",
                    "Argentina y EEUU: 25-35% (economías 'cerradas')",
                    "Países grandes son más 'cerrados' por mercado interno"
                ],
                "visual": "graficos/apertura_comercial.png",
                "fuente": "Banco Mundial",
                "notas_docente": """LECTURA DEL GRÁFICO (10 minutos)

LA TRAMPA DE SINGAPUR:
- ¿Cómo puede tener 350% de apertura si el máximo teórico es 200%?
- Porque es un HUB de re-exportación
- Importa bienes, los procesa mínimamente, los re-exporta
- El mismo bien se cuenta dos veces
- Hong Kong, Países Bajos tienen el mismo fenómeno

LA TRAMPA DEL TAMAÑO:
- EEUU y Argentina parecen igual de "cerrados" (~30%)
- Pero las razones son MUY diferentes:
  - EEUU: mercado interno gigante, no NECESITA comerciar mucho
  - Argentina: mercado chico pero con historia de proteccionismo

PREGUNTA TRAMPA: "¿Argentina es más abierta que EEUU?"
RESPUESTA: Tienen apertura similar, pero por razones opuestas. EEUU elige no comerciar tanto porque puede producir todo. Argentina comercia poco porque tiene barreras.

DATO: China pasó de 10% (1970) a 65% (2006) y bajó a 35% (2020). ¿Por qué bajó? Porque su mercado interno creció y consume más de lo que produce.

CONEXIÓN: No confundir APERTURA (indicador) con POLÍTICA comercial (libre comercio vs proteccionismo)."""
            }
        ]
    },
    # Después de ToT y el ingreso real - actualmente slide 15
    {
        "insert_after_titulo": "ToT y el ingreso real",
        "slides": [
            {
                "tipo": "grafico_texto",
                "titulo": "Términos del intercambio Argentina (1900-2023)",
                "subtitulo": "Más de un siglo de historia",
                "contenido": [
                    "Verde = mejora (ToT > 100), Rojo = deterioro (ToT < 100)",
                    "1900-1930: ToT altos (belle époque agroexportadora)",
                    "1930-2000: deterioro secular (tesis Prebisch)",
                    "2003-2012: boom de commodities (+50%)",
                    "Post-2012: caída y volatilidad"
                ],
                "visual": "graficos/tot_argentina.png",
                "fuente": "CEPAL / INDEC / Ferreres",
                "notas_docente": """ESTE GRÁFICO ES CLAVE PARA TODO EL CURSO (15 minutos)

LECTURA:
- Línea = ToT de Argentina (2004 = 100)
- Verde = períodos de mejora
- Rojo = períodos de deterioro
- Línea negra en 100 = referencia

HISTORIA EN TRES ACTOS:

ACTO 1 - BELLE ÉPOQUE (1900-1930):
- ToT altos: la carne y el trigo valían mucho
- Argentina entre los 10 países más ricos del mundo
- Pero dependía de un solo mercado (UK) y pocos productos

ACTO 2 - DETERIORO SECULAR (1930-2000):
- Colapso en la Gran Depresión
- Nunca se recupera al nivel previo
- ESTO ES LA TESIS PREBISCH: los ToT de la periferia se deterioran a largo plazo
- ¿Por qué? Porque la demanda de manufacturas crece más que la de commodities

ACTO 3 - BOOM Y CAÍDA (2000-2023):
- Boom de commodities 2003-2012: China demanda soja, minerales
- ToT suben 50% → Argentina se "enriquece" sin producir más
- Caída post-2012 → vuelve la restricción externa

PREGUNTA CENTRAL: "Si los ToT de Argentina hoy están en ~110, igual que en 1950, ¿por qué no somos igual de ricos?"
RESPUESTA: Porque el resto del mundo creció más. Los ToT son relativos.

CONEXIÓN CON PREBISCH: Este gráfico es LA EVIDENCIA de la tesis centro-periferia. Lo vamos a retomar en la clase 11."""
            }
        ]
    }
]


def main():
    # Leer JSON existente
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    slides = data['slides']

    # Procesar cada inserción (de atrás hacia adelante para no afectar índices)
    for insercion in reversed(NUEVOS_SLIDES):
        titulo_buscar = insercion['insert_after_titulo']
        nuevos = insercion['slides']

        # Encontrar el índice del slide después del cual insertar
        idx_insertar = None
        for i, slide in enumerate(slides):
            if slide['titulo'] == titulo_buscar:
                idx_insertar = i + 1
                break

        if idx_insertar is not None:
            # Insertar los nuevos slides
            for j, nuevo_slide in enumerate(nuevos):
                slides.insert(idx_insertar + j, nuevo_slide)
            print(f"Insertados {len(nuevos)} slides después de '{titulo_buscar}'")
        else:
            print(f"ADVERTENCIA: No se encontró slide '{titulo_buscar}'")

    # Renumerar todos los slides
    for i, slide in enumerate(slides):
        slide['numero'] = i + 1

    # Actualizar metadata
    data['slides'] = slides
    data['metadata']['total_slides'] = len(slides)

    # Guardar
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nJSON actualizado: {OUTPUT_JSON}")
    print(f"Total slides: {len(slides)}")

    # Mostrar estructura de indicadores
    print("\nIndicadores con gráficos:")
    for s in slides:
        if 'Indicador' in s['titulo'] or 'Balanza comercial' in s['titulo'] or 'Apertura comercial' in s['titulo'] or 'Términos del intercambio' in s['titulo']:
            visual = s.get('visual', 'sin gráfico')
            print(f"  Slide {s['numero']}: {s['titulo']} [{visual}]")


if __name__ == "__main__":
    main()
