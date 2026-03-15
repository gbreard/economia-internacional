"""
Actualiza automáticamente la agenda (slide 2) basándose en los bloques del JSON.
Debe ejecutarse ANTES de generar el HTML.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
JSON_PATH = BASE_DIR / "datos" / "slides_clase1y2.json"


def extraer_bloques(slides):
    """Extrae los bloques de la presentación."""
    bloques = []
    for s in slides:
        titulo = s.get('titulo', '')
        if titulo.startswith('Bloque ') and ':' in titulo:
            # Extraer letra y nombre: "Bloque A: Medición" -> "A. Medición"
            partes = titulo.split(':', 1)
            letra = partes[0].replace('Bloque ', '').strip()
            nombre = partes[1].strip()
            bloques.append((letra, nombre, s['numero']))
    return bloques


def generar_contenido_agenda(bloques, slides):
    """Genera el contenido de la agenda basado en los bloques."""
    contenido = []

    for letra, nombre, num_slide in bloques:
        # Buscar información adicional según el bloque
        if letra == 'A':
            # Contar indicadores en el bloque A
            indicadores = sum(1 for s in slides if 'Indicador' in s.get('titulo', '') and s['numero'] < 20)
            item = f"{letra}. {nombre}: {indicadores} indicadores del comercio"
        elif letra == 'B':
            item = f"{letra}. {nombre}: 5 etapas del comercio mundial"
        elif letra == 'C':
            item = f"{letra}. {nombre}: cuenta corriente y flujos externos"
        elif letra == 'D':
            item = f"{letra}. {nombre}: nominal vs real, el ITCRM"
        elif letra == 'E':
            item = f"{letra}. {nombre}: EEUU, China, Alemania"
        elif letra == 'F':
            item = f"{letra}. {nombre}: el ciclo apreciación-crisis"
        else:
            item = f"{letra}. {nombre}"

        contenido.append(item)

    return contenido


def generar_notas_agenda(bloques):
    """Genera las notas del docente para la agenda."""
    notas = ["EXPLICAR LA ESTRUCTURA (3 minutos)", ""]
    notas.append(f"La clase tiene {len(bloques)} bloques que van de lo general a lo particular:")
    notas.append("")

    descripciones = {
        'A': "Los indicadores que usamos para analizar el comercio. Es el 'kit de herramientas' del curso.",
        'B': "Las etapas del comercio mundial, desde las rutas ibéricas hasta hoy. Marco: Tecnología + Reglas + Poder.",
        'C': "Cómo se registran los flujos de divisas. Cuenta corriente como indicador clave.",
        'D': "La diferencia entre nominal y real. El tipo de cambio real multilateral (ITCRM).",
        'E': "Por qué EEUU siempre tiene déficit y China/Alemania superávit. Implicancias globales.",
        'F': "El 'ciclo argentino' de apreciación-crisis-devaluación. Aplicación de todos los indicadores."
    }

    for letra, nombre, _ in bloques:
        desc = descripciones.get(letra, nombre)
        notas.append(f"BLOQUE {letra} - {nombre.upper()}: {desc}")
        notas.append("")

    notas.append("Al final de estas dos clases van a poder:")
    notas.append("1. Calcular e interpretar los 9 indicadores")
    notas.append("2. Describir las 5 etapas históricas del comercio")
    notas.append("3. Explicar el ciclo argentino de apreciación-crisis")
    notas.append("4. Usar el marco Tecnología-Reglas-Poder para analizar cualquier período")

    return "\n".join(notas)


def main():
    # Leer JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    slides = data['slides']

    # Extraer bloques
    bloques = extraer_bloques(slides)
    print(f"Bloques encontrados: {len(bloques)}")
    for letra, nombre, num in bloques:
        print(f"  {letra}. {nombre} (slide {num})")

    # Generar nuevo contenido de agenda
    nuevo_contenido = generar_contenido_agenda(bloques, slides)
    nuevas_notas = generar_notas_agenda(bloques)

    # Actualizar slide de agenda (slide 2)
    for s in slides:
        if s['numero'] == 2 and s['tipo'] == 'agenda':
            s['contenido'] = nuevo_contenido
            s['notas_docente'] = nuevas_notas
            print(f"\nAgenda actualizada:")
            for item in nuevo_contenido:
                print(f"  - {item}")
            break

    # Guardar
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nJSON guardado: {JSON_PATH}")


if __name__ == "__main__":
    main()
