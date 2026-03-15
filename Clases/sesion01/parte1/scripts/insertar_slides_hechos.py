import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('../datos/slides_clase1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

nuevos = [
    {
        "numero": 7,
        "tipo": "texto",
        "titulo": "Convergencia, divergencia y comercio",
        "subtitulo": "¿Qué explica el crecimiento? ¿Tecnología o comercio?",
        "contenido": [
            "PIB per cápita = proxy de desarrollo. ¿Por qué unos países crecen y otros no?",
            "Dos grandes explicaciones: cambio tecnológico (producir más/mejor) y apertura comercial (acceso a mercados, especialización)",
            "¿El comercio causa crecimiento o el crecimiento genera comercio?",
            "La evidencia: no hay respuesta única. Importa CÓMO te insertás, no solo SI te insertás"
        ],
        "visual": None,
        "notas_docente": "CONVERGENCIA Y COMERCIO (10 minutos)\n\nEL DEBATE CENTRAL:\nEn economía del desarrollo hay una pregunta permanente: ¿qué explica que unos países sean ricos y otros pobres?\n\nDOS CANDIDATOS PRINCIPALES:\n\n1. TECNOLOGÍA / PRODUCTIVIDAD:\n- Solow: el crecimiento viene de la acumulación de capital y el progreso técnico\n- Los neoschumpeterianos: innovación, capacidades tecnológicas\n- Implicancia: lo importante es PRODUCIR MEJOR\n\n2. COMERCIO / APERTURA:\n- Ricardo, H-O: especializarse según ventajas comparativas genera ganancias\n- Apertura como motor: acceso a mercados grandes, competencia, transferencia tecnológica\n- Implicancia: lo importante es ABRIRSE AL MUNDO\n\nPERO LA REALIDAD ES MÁS COMPLEJA:\n- Hay países abiertos que crecieron mucho (Corea del Sur, China post-2001)\n- Hay países abiertos que NO crecieron (muchos de África Subsahariana)\n- Hay países que crecieron con protección (EEUU siglo XIX, Japón posguerra)\n\nLa clave no es SI te abrís, sino CÓMO te insertás:\n- ¿Exportás commodities o manufacturas?\n- ¿Tenés política industrial o te dejás llevar por el mercado?\n- ¿Absorbés tecnología del comercio o solo exportás materias primas?\n\nPREGUNTA: \"Argentina fue muy abierta en 1900 y era rica. ¿Por qué eso no alcanzó para seguir creciendo?\"\n(Respuesta: porque la inserción como exportador primario tenía límites - Prebisch, Unidad 4)\n\nCONEXIÓN: Este debate cruza TODO el curso. Las teorías clásicas (Unidades 2-3) dicen que el comercio siempre es bueno. Los estructuralistas (Unidad 4) dicen que depende. Los datos que vamos a ver ahora muestran que los dos tienen parte de razón."
    },
    {
        "numero": 8,
        "tipo": "grafico_texto",
        "titulo": "La Gran Divergencia",
        "subtitulo": "Reino Unido vs. China: 1000 años de historia",
        "contenido": [
            "Año 1000: China y Europa tenían un PIB per cápita similar (~$1.100)",
            "Hasta 1800: diferencias pequeñas. China era una economía avanzada",
            "Revolución Industrial: UK se dispara. Comercio + tecnología + imperio",
            "Desde 1980: China converge aceleradamente (de $1.000 a $13.000 en 40 años)"
        ],
        "visual": "graficos/gran_divergencia_uk_china.png",
        "fuente": "Maddison Project Database 2020",
        "notas_docente": "LA GRAN DIVERGENCIA (10 minutos)\n\nLECTURA DEL GRÁFICO:\n- Eje Y: PIB per cápita en dólares de 2011 (PPP)\n- Eje X: desde el año 1000\n- Las franjas de color corresponden a las 5 etapas que ya vimos\n\nDATOS CLAVE:\n- Año 1000: UK ~$1.150, China ~$1.225. China ERA MÁS RICA\n- Año 1820: UK ~$2.100, China ~$1.000. Empieza la divergencia\n- Año 1913: UK ~$7.000, China ~$1.000. Brecha máxima: 7 a 1\n- Año 1950: UK ~$10.000, China ~$600. China toca fondo (guerras, revolución)\n- Año 2018: UK ~$38.000, China ~$13.000. Ratio 3 a 1 y cerrándose\n\n¿QUÉ EXPLICA LA DIVERGENCIA?\n- Revolución Industrial: tecnología aplicada a la producción\n- Pero también: COMERCIO imperial, acceso a materias primas baratas\n- Y PODER: la Royal Navy abrió mercados (guerras del opio)\n\n¿QUÉ EXPLICA LA CONVERGENCIA CHINA?\n- Apertura comercial post-1978 (Deng Xiaoping)\n- Pero CON política industrial, tipo de cambio competitivo, inversión en tecnología\n- No fue \"abrirse y ya\". Fue una inserción estratégica\n\nPREGUNTA: \"¿China convergió por abrirse al comercio o por su política industrial?\"\nRESPUESTA: Por las dos cosas. Se abrió pero con estrategia. Ese es el punto.\n\nCONEXIÓN: Kenneth Pomeranz (\"The Great Divergence\", 2000) argumenta que hasta 1750 no había diferencias significativas. La divergencia fue rápida y estuvo ligada al carbón y a las colonias americanas."
    },
    {
        "numero": 9,
        "tipo": "grafico_texto",
        "titulo": "Trayectorias regionales",
        "subtitulo": "Misma economía mundial, destinos muy distintos",
        "contenido": [
            "Europa Occidental: de $2.300 a $40.000 (x17 en 200 años)",
            "Asia Oriental: estancada hasta 1950, después convergencia acelerada",
            "América Latina: creció pero NO convergió. Siempre ~35% de Europa",
            "África Subsahariana: divergencia persistente. Hoy ~9% de Europa"
        ],
        "visual": "graficos/trayectorias_regionales.png",
        "fuente": "Maddison Project Database 2020",
        "notas_docente": "TRAYECTORIAS REGIONALES (12 minutos)\n\nLECTURA DEL GRÁFICO:\n- 4 regiones, mismo período (1820-2018)\n- Las franjas coinciden con las etapas del comercio\n- Notar: todos crecieron, pero a ritmos MUY distintos\n\nEUROPA OCCIDENTAL (línea azul oscuro):\n- Crecimiento sostenido, se acelera con posguerra\n- De $2.300 (1820) a $40.000 (2018): se multiplicó por 17\n\nASIA ORIENTAL (línea roja):\n- Estancada hasta 1950 (guerras, colonialismo, revolución)\n- Despegue post-1960: Japón, Corea, Taiwán\n- Aceleración post-1980: China\n- De $1.100 (1820) a $16.300 (2018): se multiplicó por 15\n- Es LA historia de convergencia exitosa del siglo XX\n\nAMÉRICA LATINA (línea celeste):\n- Creció, pero siempre MENOS que Europa\n- En 1820 era ~40% de Europa. En 2018 sigue en ~35%\n- NO CONVERGIÓ. Creció pero no acortó la brecha\n- Argentina es un caso extremo: era 80% de Europa en 1900, hoy es ~35%\n\nÁFRICA SUBSAHARIANA (línea naranja):\n- Casi plana hasta 1950\n- En 1820 era ~35% de Europa. En 2018 es ~9%\n- DIVERGENCIA persistente\n\nPREGUNTAS PARA DISCUSIÓN:\n1. \"¿Por qué Asia Oriental convergió y América Latina no?\"\n   (Política industrial, educación, tipo de cambio competitivo, rol del Estado)\n2. \"¿El comercio ayudó o perjudicó a África?\"\n   (Debate: inserción primaria sin industrialización)\n3. \"¿Argentina es un caso de éxito o fracaso de la inserción comercial?\"\n   (Ambos: éxito en 1880-1930, fracaso en no diversificar después)\n\nCONEXIÓN: Este gráfico es el resumen visual de TODO el curso. Vamos a dedicar unidades enteras a explicar por qué las trayectorias son tan distintas."
    }
]

slides = data['slides']
for i, s in enumerate(nuevos):
    slides.insert(6 + i, s)

for i, s in enumerate(slides):
    s['numero'] = i + 1

data['metadata']['total_slides'] = len(slides)

with open('../datos/slides_clase1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"JSON actualizado: {len(slides)} slides")
for s in slides:
    print(f"  Slide {s['numero']}: {s['titulo']}")
