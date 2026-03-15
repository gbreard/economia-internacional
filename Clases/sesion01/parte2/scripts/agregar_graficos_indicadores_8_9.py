"""
Agrega slides de gráficos para indicadores 8 y 9.
Similar a agregar_graficos_indicadores.py pero para BP y TC.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"
OUTPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"

# Nuevos slides a insertar
NUEVOS_SLIDES = [
    # Después de Indicador 8 (Cuenta corriente)
    {
        "insert_after_titulo": "Indicador 8: Cuenta corriente (% PIB)",
        "slides": [
            {
                "tipo": "grafico_texto",
                "titulo": "Cuenta corriente Argentina (1990-2024)",
                "subtitulo": "El espejo de los ciclos económicos",
                "contenido": [
                    "Superávit post-crisis 2002 (+8% PIB)",
                    "Déficit en Convertibilidad y 2017-2018",
                    "Correlación con tipo de cambio real",
                    "La CC anticipa las crisis"
                ],
                "visual": "graficos/cc_argentina.png",
                "fuente": "INDEC / BCRA",
                "notas_docente": """LECTURA DEL GRÁFICO - CUENTA CORRIENTE ARGENTINA (10 minutos)

IDENTIFICAR LOS CICLOS:
- Barras verdes = superávit (entraron más dólares de los que salieron)
- Barras rojas = déficit (salieron más dólares de los que entraron)

MOMENTOS CLAVE:

1. CONVERTIBILIDAD (1991-2001):
- Déficit persistente, especialmente 1997-1998
- El peso sobrevaluado abarataba importaciones
- Se financiaba con deuda externa
- PREGUNTA: "¿Por qué no explotó antes de 2001?"
- RESPUESTA: Porque entraba capital (inversiones, privatizaciones, deuda)

2. CRISIS 2002:
- Superávit récord (+8% del PIB)
- No es "buena noticia" - es colapso de importaciones
- La economía se contrajo tanto que no podía importar

3. POST-CRISIS (2003-2011):
- Superávits sostenidos
- TC competitivo + commodities altos
- "Los años dorados" del modelo K

4. DETERIORO (2012-2015):
- Déficit creciente
- Atraso cambiario + caída de commodities
- Cepo cambiario como respuesta

5. MACRISMO (2016-2019):
- Déficit que se financia con deuda
- 2018: crisis cambiaria, FMI
- Patrón similar a Convertibilidad

CONEXIÓN CON INDICADOR 9: El tipo de cambio real EXPLICA estos movimientos. Cuando el peso se aprecia, la CC se deteriora."""
            },
            {
                "tipo": "grafico_texto",
                "titulo": "Desequilibrios globales: EEUU, China, Alemania",
                "subtitulo": "¿Por qué algunos países siempre tienen déficit y otros superávit?",
                "contenido": [
                    "EEUU: déficit estructural desde 1980s",
                    "China: superávit desde entrada a OMC (2001)",
                    "Alemania: superávit récord en eurozona",
                    "Los desequilibrios no se ajustan solos"
                ],
                "visual": "graficos/desequilibrios_globales.png",
                "fuente": "FMI WEO",
                "notas_docente": """DESEQUILIBRIOS GLOBALES - COMPARACIÓN INTERNACIONAL (8 minutos)

¿QUÉ MUESTRA EL GRÁFICO?
- Cuenta corriente como % del PIB para las 3 economías más importantes
- Período: 1980-2024
- Línea en cero = equilibrio

PATRONES ESTRUCTURALES:

1. EEUU (línea roja, siempre abajo):
- Déficit desde los 1980s
- Llegó a -6% del PIB en 2006
- PREGUNTA: "¿Cómo puede EEUU tener déficit 40 años seguidos sin crisis?"
- RESPUESTA: Porque emite la moneda de reserva mundial. El mundo QUIERE dólares.
- Es el "privilegio exorbitante" del dólar

2. CHINA (línea que sube desde 2000):
- Superávit desde entrada a OMC (2001)
- Pico de +10% del PIB en 2007
- Modelo: exportar manufactura barata, acumular reservas
- Bajó después de 2008 porque su mercado interno creció

3. ALEMANIA (línea que sube desde 2000):
- Superávit persistente (+6-8% del PIB)
- Dentro de la eurozona no puede devaluar
- Los otros países europeos se quejan: "Alemania exporta desempleo"

LA PARADOJA:
- El déficit de EEUU financia el superávit de China y Alemania
- Es un equilibrio inestable
- Tensiones comerciales (Trump, aranceles) son síntoma de esto

CONEXIÓN CON ARGENTINA: Nosotros no tenemos el privilegio del dólar. Cuando tenemos déficit, eventualmente explota."""
            }
        ]
    },
    # Después de Indicador 9 (Tipo de cambio real)
    {
        "insert_after_titulo": "Indicador 9: Tipo de cambio real",
        "slides": [
            {
                "tipo": "grafico_texto",
                "titulo": "Tipo de cambio real Argentina (1997-2024)",
                "subtitulo": "El indicador que anticipa las crisis",
                "contenido": [
                    "Base 100 = promedio histórico",
                    "< 100 = peso apreciado (caro en dólares)",
                    "> 100 = peso depreciado (barato en dólares)",
                    "Patrón: apreciación gradual → devaluación brusca"
                ],
                "visual": "graficos/tcr_argentina.png",
                "fuente": "BCRA (ITCRM)",
                "notas_docente": """LECTURA DEL GRÁFICO - TIPO DE CAMBIO REAL (12 minutos)

ESTE ES EL GRÁFICO MÁS IMPORTANTE PARA ENTENDER ARGENTINA

¿QUÉ MUESTRA?
- Índice de Tipo de Cambio Real Multilateral (ITCRM) del BCRA
- Base diciembre 2015 = 100 (o promedio histórico)
- VERDE = peso depreciado (competitivo, bueno para exportar)
- ROJO = peso apreciado (caro, malo para exportar)

LOS CICLOS ARGENTINOS:

1. CONVERTIBILIDAD (1997-2001):
- TCR bajo y estable (peso caro)
- El "1 a 1" era insostenible
- Se veía venir: el peso estaba 40% sobrevaluado

2. DEVALUACIÓN 2002:
- Salto de 70 a 200+ (casi 3x)
- Overshooting típico de las crisis
- El peso pasó de muy caro a muy barato

3. RECUPERACIÓN (2003-2008):
- TCR alto = competitividad
- Superávit comercial y fiscal
- Acumulación de reservas

4. APRECIACIÓN GRADUAL (2008-2015):
- Inflación + dólar "planchado"
- El peso se fue apreciando
- Cepo como parche

5. DEVALUACIÓN 2015-2016:
- Salida del cepo
- Salto discreto pero menor que 2002

6. NUEVO CICLO (2016-2019):
- Apreciación rápida (carry trade)
- Crisis 2018
- Vuelta del cepo

7. HOY:
- ¿Dónde estamos en el ciclo?
- Depende del régimen cambiario actual

FRASE CLAVE: "En Argentina, el tipo de cambio sube por ascensor y baja por escalera"
- Devaluaciones bruscas
- Apreciaciones graduales (por inflación)

CONEXIÓN: Cuando el TCR está bajo (zona roja), la cuenta corriente se deteriora. Son dos caras de la misma moneda."""
            },
            {
                "tipo": "grafico_texto",
                "titulo": "Reservas internacionales Argentina",
                "subtitulo": "El colchón contra las crisis",
                "contenido": [
                    "Reservas = capacidad de intervenir en el mercado",
                    "Caen antes de las crisis (2001, 2018)",
                    "Se acumulan en buenos tiempos (2003-2011)",
                    "Nivel actual: ¿suficiente o insuficiente?"
                ],
                "visual": "graficos/reservas_argentina.png",
                "fuente": "BCRA",
                "notas_docente": """RESERVAS INTERNACIONALES - EL TERMÓMETRO DE LA SALUD EXTERNA (8 minutos)

¿QUÉ SON LAS RESERVAS?
- Dólares (y otras divisas) que tiene el Banco Central
- Sirven para: intervenir en el mercado, pagar deuda, importar
- Son el "colchón" contra shocks externos

LECTURA DEL GRÁFICO:

1. PRE-CRISIS 2001:
- Reservas cayendo desde 1999
- El mercado veía que no alcanzaban
- Corrida bancaria → corralito

2. POST-CRISIS (2003-2011):
- Acumulación récord: de USD 10.000M a USD 52.000M
- TC competitivo + superávit comercial
- Se compraban los dólares que sobraban

3. CAÍDA (2011-2015):
- De USD 52.000M a USD 25.000M
- Atraso cambiario + déficit comercial
- Cepo para frenar la sangría

4. MACRISMO (2016-2019):
- Entrada de capitales inicial
- Crisis 2018: caída abrupta
- FMI como prestamista de última instancia

5. ACTUALIDAD:
- ¿Cuántas reservas hay "de verdad"?
- Reservas brutas vs netas
- Pasivos del BCRA

REGLA PRÁCTICA:
- Mínimo deseable: 3 meses de importaciones
- Mejor: 6-12 meses
- Argentina suele estar al límite

CONEXIÓN CON TODO:
- TCR apreciado → déficit comercial → caen reservas → crisis → devaluación → TCR depreciado → superávit → suben reservas → ... (y el ciclo se repite)"""
            }
        ]
    }
]


def main():
    # Leer JSON existente
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    slides = data['slides']

    # Primero, eliminar slides duplicados que ya tienen estos gráficos
    # para evitar repetición (los gráficos estaban en slides 38, 43, 44, 45)
    titulos_a_eliminar = [
        "Cuenta corriente: EEUU, China, Alemania",
        "Tipo de cambio real Argentina (1997-2024)",
        "Cuenta corriente Argentina (1990-2024)",
        "Reservas internacionales Argentina"
    ]

    slides_originales = len(slides)
    slides = [s for s in slides if s['titulo'] not in titulos_a_eliminar]
    eliminados = slides_originales - len(slides)
    if eliminados > 0:
        print(f"Eliminados {eliminados} slides duplicados")

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

    # Mostrar estructura de indicadores 8 y 9
    print("\nIndicadores 8 y 9 con gráficos:")
    for s in slides:
        if any(x in s['titulo'] for x in ['Indicador 8', 'Indicador 9', 'Cuenta corriente', 'Tipo de cambio real', 'Desequilibrios', 'Reservas']):
            visual = s.get('visual', 'sin gráfico')
            if visual is None:
                visual = 'sin gráfico'
            print(f"  Slide {s['numero']}: {s['titulo'][:50]} [{visual}]")


if __name__ == "__main__":
    main()
