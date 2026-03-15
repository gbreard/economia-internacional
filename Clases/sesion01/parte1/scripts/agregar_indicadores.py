"""
Script para agregar indicadores faltantes: Apertura, ToT, Balanza comercial
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"
OUTPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"  # Sobrescribir

# Nuevos slides de indicadores para insertar después del slide 11 (advertencias)
NUEVOS_INDICADORES = [
    {
        "tipo": "formula",
        "titulo": "Indicador 5: Balanza comercial",
        "subtitulo": "El más simple",
        "contenido": [
            "Fórmula: BC = X - M",
            "BC > 0 → SUPERÁVIT comercial (exporta más de lo que importa)",
            "BC < 0 → DÉFICIT comercial (importa más de lo que exporta)",
            "OJO: a nivel mundial, la suma debería ser ~0 (pero hay errores de medición)"
        ],
        "visual": None,
        "notas_docente": "Es el indicador más básico. Sirve para introducir la idea de saldo. Aclarar que superávit no es necesariamente 'bueno' ni déficit 'malo' - depende del contexto."
    },
    {
        "tipo": "formula",
        "titulo": "Indicador 6: Apertura comercial",
        "subtitulo": "Qué tan integrado está un país",
        "contenido": [
            "Fórmula: Apertura = (X + M) / PIB × 100",
            "Mide qué proporción del PIB se comercia con el mundo",
            "Argentina ~30%, EEUU ~25%, Alemania ~90%, Singapur ~300%",
            "Países grandes tienden a ser menos 'abiertos' (comercian más internamente)"
        ],
        "visual": None,
        "notas_docente": "Este indicador tiene trampas: Singapur tiene 300% porque re-exporta mucho (el comercio pasa por ahí). Países grandes como EEUU o Brasil son 'cerrados' porque su mercado interno es enorme. No confundir apertura con política comercial."
    },
    {
        "tipo": "formula",
        "titulo": "Indicador 7: Términos del intercambio (ToT)",
        "subtitulo": "El precio relativo de lo que exportamos vs importamos",
        "contenido": [
            "Fórmula: ToT = (Px / Pm) × 100",
            "Px = índice de precios de exportación",
            "Pm = índice de precios de importación",
            "ToT sube → mejora: con las mismas exportaciones compramos más importaciones",
            "ToT baja → deterioro: necesitamos exportar más para comprar lo mismo"
        ],
        "visual": None,
        "notas_docente": "Los ToT son clave para países exportadores de commodities como Argentina. Cuando sube el precio de la soja, mejoran los ToT. Prebisch y Singer argumentaron que los ToT de la periferia se deterioran a largo plazo (tesis estructuralista que veremos después)."
    },
    {
        "tipo": "texto",
        "titulo": "ToT y el ingreso real",
        "subtitulo": "Por qué importan los términos del intercambio",
        "contenido": [
            "Si ToT mejora → el país se 'enriquece' sin producir más",
            "Si ToT empeora → el país se 'empobrece' aunque produzca igual",
            "Ejemplo: Argentina 2003-2012 (boom de commodities → ToT +40%)",
            "Ejemplo: Argentina 2012-2015 (caída de commodities → ToT -20%)",
            "Los ToT explican parte del ciclo económico en países primario-exportadores"
        ],
        "visual": None,
        "notas_docente": "Conectar con la experiencia reciente. El boom de commodities de los 2000s mejoró los ToT de Argentina y permitió crecimiento y superávit comercial. Cuando cayeron los precios, volvió la restricción externa. Preguntar: '¿Qué pasa si sube el precio de lo que exportamos pero también sube el costo de la energía que importamos?'"
    }
]


def main():
    # Leer JSON existente
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Encontrar la posición después del slide 11 (advertencias)
    # y antes del slide 12 (sección Historia)
    slides_antes = [s for s in data['slides'] if s['numero'] <= 11]
    slides_despues = [s for s in data['slides'] if s['numero'] >= 12]

    # Insertar nuevos indicadores
    nuevos_slides = []
    numero_actual = 11
    for slide in NUEVOS_INDICADORES:
        numero_actual += 1
        slide['numero'] = numero_actual
        nuevos_slides.append(slide)

    # Renumerar slides posteriores
    offset = len(NUEVOS_INDICADORES)
    for slide in slides_despues:
        slide['numero'] += offset

    # Reconstruir lista completa
    data['slides'] = slides_antes + nuevos_slides + slides_despues

    # Actualizar metadata
    data['metadata']['total_slides'] = len(data['slides'])

    # Actualizar el slide de resumen de indicadores
    for slide in data['slides']:
        if slide['titulo'] == "Resumen: 6 indicadores de inserción externa":
            slide['titulo'] = "Resumen: 9 indicadores de inserción externa"
            slide['contenido'] = [
                "COMERCIO HISTÓRICO:",
                "1. Índice de comercio (crecimiento vs año base)",
                "2. Participación regional (quién gana/pierde peso)",
                "3. HHI (concentración)",
                "4. Cobertura (calidad de datos)",
                "5. Balanza comercial (X - M)",
                "6. Apertura comercial ((X+M)/PIB)",
                "7. Términos del intercambio (Px/Pm)",
                "SECTOR EXTERNO CONTEMPORÁNEO:",
                "8. Cuenta corriente (% PIB)",
                "9. Tipo de cambio real (competitividad)"
            ]
            slide['notas_docente'] = "Este es el 'kit completo' de herramientas. Con estos 9 indicadores pueden analizar la inserción externa de cualquier país. Los primeros 7 sirven para análisis histórico y comparativo; los últimos 2 para análisis macroeconómico contemporáneo."

    # Guardar
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"JSON actualizado: {OUTPUT_JSON}")
    print(f"Total slides: {len(data['slides'])}")
    print(f"Indicadores agregados: {len(NUEVOS_INDICADORES)}")

    # Mostrar estructura de indicadores
    print("\nIndicadores en la presentación:")
    for s in data['slides']:
        if 'Indicador' in s['titulo']:
            print(f"  Slide {s['numero']}: {s['titulo']}")


if __name__ == "__main__":
    main()
