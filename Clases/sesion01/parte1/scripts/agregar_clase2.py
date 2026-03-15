"""
Script para agregar slides de Clase 2 al JSON existente
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_JSON = BASE_DIR / "datos" / "slides_estructurados.json"
OUTPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"

# Slides de Clase 2 para agregar
SLIDES_CLASE2 = [
    # Sección: Indicadores de Balanza de Pagos
    {
        "tipo": "seccion",
        "titulo": "Bloque C: Balanza de Pagos",
        "subtitulo": "Indicadores del sector externo",
        "contenido": [],
        "visual": None,
        "notas_docente": "Transición al bloque de balanza de pagos. Ahora pasamos de comercio de bienes a una visión más completa del sector externo."
    },
    {
        "tipo": "texto",
        "titulo": "¿Qué es la balanza de pagos?",
        "subtitulo": "Registro de transacciones con el resto del mundo",
        "contenido": [
            "CUENTA CORRIENTE: comercio de bienes y servicios, rentas, transferencias",
            "CUENTA CAPITAL: transferencias de capital, activos no financieros",
            "CUENTA FINANCIERA: inversión directa, de cartera, reservas",
            "Principio contable: la BP siempre 'cierra' (suma cero)"
        ],
        "visual": None,
        "notas_docente": "La BP es el 'balance' de un país con el mundo. Es como el estado de resultados y flujo de fondos de una empresa, pero para un país. El principio de partida doble garantiza que siempre cierre."
    },
    {
        "tipo": "formula",
        "titulo": "Indicador 5: Cuenta corriente (% PIB)",
        "subtitulo": None,
        "contenido": [
            "Fórmula: CC = (X - M + Rentas + Transferencias) / PIB × 100",
            "CC > 0 → SUPERÁVIT: el país ahorra más de lo que invierte, presta al mundo",
            "CC < 0 → DÉFICIT: el país invierte más de lo que ahorra, se endeuda",
            "Identidad: CC = Ahorro nacional - Inversión nacional"
        ],
        "visual": None,
        "notas_docente": "Esta es LA variable clave de macroeconomía abierta. Un déficit puede ser bueno si financia inversión productiva. Pero un déficit persistente financiando consumo es insostenible."
    },
    {
        "tipo": "formula",
        "titulo": "La identidad ahorro-inversión",
        "subtitulo": None,
        "contenido": [
            "Fórmula: CC = S - I = (S_privado - I_privado) + (T - G)",
            "Si el sector privado ahorra más de lo que invierte → superávit",
            "Si el gobierno tiene déficit fiscal (G > T) → presiona hacia déficit de CC",
            "'Déficits gemelos': déficit fiscal + déficit de cuenta corriente"
        ],
        "visual": None,
        "notas_docente": "Esta fórmula conecta macroeconomía doméstica con sector externo. Argentina históricamente tiene bajo ahorro privado + déficit fiscal = déficit de CC estructural. Es la base del 'ciclo argentino'."
    },
    # Sección: Tipo de Cambio
    {
        "tipo": "seccion",
        "titulo": "Bloque D: Tipo de Cambio",
        "subtitulo": "Competitividad y precios relativos",
        "contenido": [],
        "visual": None,
        "notas_docente": "Transición al bloque de tipo de cambio. Conectar con la cuenta corriente: el TC real afecta la competitividad y por ende el saldo comercial."
    },
    {
        "tipo": "texto",
        "titulo": "Tipo de cambio: nominal vs real",
        "subtitulo": None,
        "contenido": [
            "TC NOMINAL (E): precio de una moneda en términos de otra (pesos por dólar)",
            "TC REAL (e): TC nominal ajustado por precios relativos",
            "El TC real mide COMPETITIVIDAD: ¿son baratos o caros nuestros bienes?",
            "CUIDADO: devaluación nominal no siempre mejora competitividad"
        ],
        "visual": None,
        "notas_docente": "Esta distinción es fundamental. El TC nominal es lo que ven en las casas de cambio. El real es lo que importa para el comercio. Dar ejemplos: devaluación de 2002 vs inflación post-2010."
    },
    {
        "tipo": "formula",
        "titulo": "Indicador 6: Tipo de cambio real",
        "subtitulo": None,
        "contenido": [
            "Fórmula: e = E × (P* / P)",
            "E = TC nominal (pesos por dólar)",
            "P* = nivel de precios externo; P = nivel de precios doméstico",
            "e sube → depreciación real → más competitivos",
            "e baja → apreciación real → menos competitivos"
        ],
        "visual": None,
        "notas_docente": "Esta fórmula es la base. En la práctica se usa el ITCRM (multilateral). Enfatizar: si E sube 50% pero P sube 50%, el TCR no cambió."
    },
    # Sección: Hechos estilizados contemporáneos
    {
        "tipo": "seccion",
        "titulo": "Bloque E: Desequilibrios Globales",
        "subtitulo": "El mundo contemporáneo (1980-2024)",
        "contenido": [],
        "visual": None,
        "notas_docente": "Transición a los hechos estilizados contemporáneos. Ahora aplicamos los indicadores de BP y TC a patrones globales actuales."
    },
    {
        "tipo": "texto",
        "titulo": "¿Qué son los desequilibrios globales?",
        "subtitulo": None,
        "contenido": [
            "Algunos países tienen superávits persistentes, otros déficits persistentes",
            "No son aleatorios. Reflejan:",
            "- Diferencias en tasas de ahorro (demografía, cultura, políticas)",
            "- El rol especial del dólar como moneda de reserva",
            "- Estrategias de crecimiento (export-led vs consumption-led)"
        ],
        "visual": None,
        "notas_docente": "Los desequilibrios actuales son un tema de debate intenso. Algunos dicen que son insostenibles; otros que son un nuevo equilibrio. Conectar con la identidad S-I."
    },
    {
        "tipo": "grafico_texto",
        "titulo": "Cuenta corriente: EEUU, China, Alemania",
        "subtitulo": None,
        "contenido": [
            "EEUU: déficit persistente desde 1982 (-2% a -6% PIB)",
            "China: superávit desde 2000 (pico 10% PIB en 2007)",
            "Alemania: superávit desde 2002 (~7% PIB)",
            "EEUU consume más de lo que produce; China y Alemania al revés"
        ],
        "visual": "graficos/desequilibrios_globales.png",
        "fuente": "FMI World Economic Outlook",
        "notas_docente": "Este gráfico es fundamental. EEUU es el 'consumidor de última instancia' global. China financia el consumo americano comprando bonos del Tesoro. ¿Es sostenible?"
    },
    {
        "tipo": "texto",
        "titulo": "El 'privilegio exorbitante' del dólar",
        "subtitulo": None,
        "contenido": [
            "EEUU puede tener déficits persistentes porque emite la moneda de reserva",
            "El mundo demanda dólares para comercio y reservas",
            "EEUU paga sus importaciones con su propia moneda",
            "DILEMA DE TRIFFIN: para proveer liquidez global, EEUU debe tener déficits"
        ],
        "visual": None,
        "notas_docente": "El 'privilegio exorbitante' es un término de Valéry Giscard d'Estaing (1960s). Sigue vigente. China cuestiona este sistema, pero no hay alternativa clara."
    },
    {
        "tipo": "texto",
        "titulo": "Asia: de deudores a acreedores",
        "subtitulo": "La transformación post-crisis 1997",
        "contenido": [
            "ANTES (1990-1997): déficits de CC, endeudamiento, TC fijo",
            "CRISIS (1997-98): fuga de capitales, devaluaciones, recesión, FMI",
            "DESPUÉS (1999-hoy): superávits, acumulación de reservas, 'self-insurance'",
            "Lección: 'Nunca más depender del FMI'"
        ],
        "visual": None,
        "notas_docente": "La crisis del 97 es un caso de estudio clásico. Corea, Tailandia, Indonesia pasaron de 'milagros' a crisis en meses. La respuesta fue acumular reservas masivas."
    },
    # Sección: Caso argentino
    {
        "tipo": "seccion",
        "titulo": "Bloque F: El Caso Argentino",
        "subtitulo": "El ciclo de apreciación-crisis-devaluación",
        "contenido": [],
        "visual": None,
        "notas_docente": "Transición al caso argentino. Aplicamos todo lo aprendido a un caso cercano y recurrente."
    },
    {
        "tipo": "texto",
        "titulo": "El 'ciclo argentino'",
        "subtitulo": "¿Por qué se repite cada 10-15 años?",
        "contenido": [
            "1. APRECIACIÓN: TC real se aprecia (inflación > devaluación o TC fijo)",
            "2. DÉFICIT CRECIENTE: importaciones suben, exportaciones estancadas",
            "3. FINANCIAMIENTO: deuda o entrada de capitales financian el déficit",
            "4. SUDDEN STOP: los capitales se van, reservas caen",
            "5. CRISIS Y DEVALUACIÓN: ajuste abrupto, recesión",
            "6. RECUPERACIÓN: TC competitivo, superávit... hasta que reinicia"
        ],
        "visual": None,
        "notas_docente": "Este patrón se repitió en 1975, 1982, 1989, 2001, 2018. La convertibilidad fue el caso más extremo. ¿Por qué se repite? Política monetaria, fiscal, estructura productiva... todas contribuyen."
    },
    {
        "tipo": "grafico_texto",
        "titulo": "Tipo de cambio real Argentina (1997-2024)",
        "subtitulo": None,
        "contenido": [
            "1997-2001: apreciación sostenida (convertibilidad)",
            "2002: salto del +200% (crisis)",
            "2003-2008: estabilidad en nivel competitivo",
            "2008-2017: apreciación gradual por inflación",
            "2018-2024: volatilidad extrema"
        ],
        "visual": "graficos/tcr_argentina.png",
        "fuente": "BCRA - ITCRM",
        "notas_docente": "El gráfico muestra claramente los ciclos. Notar cómo la apreciación es gradual y la depreciación es abrupta. 'Sube por escalera, baja por ascensor'."
    },
    {
        "tipo": "grafico_texto",
        "titulo": "Cuenta corriente Argentina (1990-2024)",
        "subtitulo": None,
        "contenido": [
            "1992-2001: déficit persistente (convertibilidad)",
            "2002-2008: superávit récord (post-crisis)",
            "2010-2017: vuelta al déficit",
            "Correlación clara con TC real: peso caro → déficit"
        ],
        "visual": "graficos/cc_argentina.png",
        "fuente": "INDEC / BCRA",
        "notas_docente": "Mostrar cómo CC y TCR están correlacionados inversamente. Cuando el peso está 'caro', importamos más y exportamos menos. La convertibilidad es el caso extremo."
    },
    {
        "tipo": "grafico_texto",
        "titulo": "Reservas internacionales Argentina",
        "subtitulo": None,
        "contenido": [
            "Las reservas son el 'colchón' del país",
            "Suben en superávit / entrada de capitales",
            "Bajan en déficit / fuga",
            "Crisis 2002: mínimo US$ 10.5 bn",
            "2018: máximo US$ 66 bn (préstamo FMI)"
        ],
        "visual": "graficos/reservas_argentina.png",
        "fuente": "BCRA",
        "notas_docente": "Las reservas son el termómetro de las crisis. Cuando bajan rápido, es señal de crisis inminente. El BCRA interviene vendiendo reservas hasta que se agotan."
    },
    {
        "tipo": "texto",
        "titulo": "La Convertibilidad (1991-2001): caso de estudio",
        "subtitulo": None,
        "contenido": [
            "Régimen extremo de TC fijo: 1 peso = 1 dólar",
            "BENEFICIOS INICIALES: estabilización, credibilidad, inversión",
            "PROBLEMAS ACUMULADOS: apreciación real, déficit CC, deuda, desempleo",
            "COLAPSO: cuando el financiamiento se cortó, el ajuste fue brutal",
            "LECCIÓN: TC fijo sin flexibilidad acumula desequilibrios hasta que explota"
        ],
        "visual": None,
        "notas_docente": "La convertibilidad es un caso de manual. Funcionó para estabilizar, pero generó rigidez. Sin poder devaluar, todo el ajuste recayó en empleo y actividad. Desempleo llegó a 25% en 2002."
    },
    # Cierre
    {
        "tipo": "seccion",
        "titulo": "Cierre",
        "subtitulo": None,
        "contenido": [],
        "visual": None,
        "notas_docente": "Transición al cierre de las clases 1+2."
    },
    {
        "tipo": "texto",
        "titulo": "Resumen: 6 indicadores de inserción externa",
        "subtitulo": None,
        "contenido": [
            "1. ÍNDICE DE COMERCIO: crecimiento vs año base",
            "2. PARTICIPACIÓN REGIONAL: quién gana/pierde peso",
            "3. HHI: concentración del comercio",
            "4. COBERTURA: calidad de los datos",
            "5. CUENTA CORRIENTE (% PIB): ahorro - inversión",
            "6. TIPO DE CAMBIO REAL: competitividad"
        ],
        "visual": None,
        "notas_docente": "Este cuadro resume las herramientas. Los estudiantes deberían poder aplicar estos indicadores a cualquier país."
    },
    {
        "tipo": "texto",
        "titulo": "Resumen: hechos estilizados",
        "subtitulo": None,
        "contenido": [
            "El comercio creció 40x (1800-1913) y colapsó (1914-1945)",
            "La 'globalización' del s.XIX fue hegemonía británica",
            "Sin hegemón que garantice las reglas, el sistema se fragmenta",
            "Los desequilibrios globales reflejan el rol del dólar",
            "Argentina repite un ciclo de apreciación → déficit → crisis"
        ],
        "visual": None,
        "notas_docente": "Cerrar enfatizando que indicadores y hechos estilizados están conectados. Marco analítico: Tecnología + Reglas + Poder."
    },
    {
        "tipo": "texto",
        "titulo": "Próxima clase",
        "subtitulo": "Clase 3: Mercantilistas y Smith",
        "contenido": [
            "¿Por qué comercian los países?",
            "La visión mercantilista: comercio como guerra",
            "Adam Smith y las ventajas absolutas",
            "El debate que sigue vigente",
            "Lectura: Lugones, cap. 1"
        ],
        "visual": None,
        "notas_docente": "Anticipar que pasamos de descripción (indicadores, hechos) a explicación (teorías). Mercantilistas y Smith son el punto de partida del debate teórico."
    },
    {
        "tipo": "cierre",
        "titulo": "¿Preguntas?",
        "subtitulo": "Economía Internacional | UMET | 2026",
        "contenido": [],
        "visual": None,
        "notas_docente": "Abrir espacio para preguntas."
    }
]


def main():
    # Leer JSON existente
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Remover slides 21-24 (cierre viejo)
    data['slides'] = [s for s in data['slides'] if s['numero'] <= 20]

    # Agregar slides de clase 2
    ultimo_numero = 20
    for slide in SLIDES_CLASE2:
        ultimo_numero += 1
        slide['numero'] = ultimo_numero
        data['slides'].append(slide)

    # Actualizar metadata
    data['metadata'] = {
        "clase": "Clases 1+2",
        "titulo": "Indicadores y Hechos Estilizados del Comercio Internacional",
        "duracion": "4 horas",
        "total_slides": len(data['slides'])
    }

    # Guardar
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"JSON guardado: {OUTPUT_JSON}")
    print(f"Total slides: {len(data['slides'])}")

    # Resumen por tipo
    tipos = {}
    for s in data['slides']:
        t = s['tipo']
        tipos[t] = tipos.get(t, 0) + 1

    print("\nSlides por tipo:")
    for t, c in sorted(tipos.items()):
        print(f"  {t}: {c}")

    # Resumen por bloque
    print("\nEstructura:")
    bloque_actual = None
    for s in data['slides']:
        if s['tipo'] == 'seccion':
            bloque_actual = s['titulo']
            print(f"\n  {bloque_actual}")
        elif s['tipo'] == 'portada':
            print(f"\n  PORTADA: {s['titulo']}")
        else:
            print(f"    {s['numero']}. {s['titulo'][:50]}...")


if __name__ == "__main__":
    main()
