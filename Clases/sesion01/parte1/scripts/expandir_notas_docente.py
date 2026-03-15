"""
Script para expandir las notas del docente con contenido más rico:
- Explicaciones extendidas
- Ejemplos concretos
- Preguntas para estudiantes
- Conexiones con otros temas
- Datos adicionales
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"
OUTPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"

# Notas expandidas por número de slide
NOTAS_EXPANDIDAS = {
    1: """APERTURA DE CLASE (5-10 minutos)

Presentarse y presentar el curso. Esta es una materia que combina teoría económica con historia y análisis empírico.

OBJETIVO DE ESTAS DOS PRIMERAS CLASES: Que los estudiantes salgan con un "kit de herramientas" (9 indicadores) y una visión panorámica de la historia del comercio mundial.

PREGUNTA DISPARADORA para arrancar: "¿Cuánto creen que creció el comercio mundial en los últimos 200 años? ¿El doble? ¿Diez veces? ¿Cien veces?"

La respuesta (más de 400 veces en términos reales) suele sorprender y sirve para mostrar que el comercio internacional es un fenómeno que transformó radicalmente el mundo.

CONTEXTO ACTUAL: Mencionar brevemente las tensiones actuales (guerra comercial EEUU-China, nearshoring, disrupciones de pandemia) para mostrar que el tema es relevante HOY.

Si hay estudiantes que trabajan en comercio exterior, importación/exportación, o sectores exportadores, pedirles que se identifiquen - sus experiencias van a enriquecer la discusión.""",

    2: """EXPLICAR LA ESTRUCTURA (3 minutos)

La clase tiene una lógica: primero las HERRAMIENTAS (indicadores), después la APLICACIÓN (historia).

Es como aprender a leer un mapa antes de hacer un viaje. Los indicadores son el "lenguaje" que vamos a usar todo el cuatrimestre.

ACLARACIÓN IMPORTANTE: Vamos a ver 9 indicadores en total, divididos en dos bloques:
- Indicadores 1-7: sirven principalmente para análisis histórico y comparativo
- Indicadores 8-9: sirven para análisis macroeconómico contemporáneo (balanza de pagos, tipo de cambio)

Al final de estas dos clases van a poder:
1. Calcular e interpretar los 9 indicadores
2. Describir las 5 etapas históricas del comercio
3. Explicar el "ciclo argentino" de apreciación-crisis
4. Usar el marco Tecnología-Reglas-Poder para analizar cualquier período""",

    3: """TRANSICIÓN AL BLOQUE DE MEDICIÓN (1 minuto)

Enfatizar: "Sin saber medir, no podemos interpretar. Los datos no hablan solos."

ANALOGÍA: Es como ir al médico. El médico no dice "te veo mal", sino que mide: presión, temperatura, análisis de sangre. Después interpreta. Nosotros vamos a hacer lo mismo con las economías.

ADVERTENCIA: Los indicadores que vamos a ver parecen simples, pero tienen sutilezas. Vamos a ir despacio para entenderlos bien.""",

    4: """INDICADOR 1: ÍNDICE DE COMERCIO (10 minutos)

¿POR QUÉ USAMOS UN ÍNDICE?
- Problema 1: La inflación distorsiona las comparaciones. US$100 de 1913 no es lo mismo que US$100 de 2024.
- Problema 2: Las monedas cambian (el dólar de hoy no existía en 1800).
- Solución: Usar números índice que miden VARIACIÓN respecto a un año base.

¿POR QUÉ 1913 COMO AÑO BASE?
- 1913 fue el pico de la "primera globalización"
- Último año antes de la Primera Guerra Mundial
- Es un punto de referencia histórico aceptado internacionalmente
- Permite ver tanto el crecimiento previo como el colapso posterior

EJEMPLO NUMÉRICO EN PIZARRÓN:
Si comercio_1913 = 100 (por definición)
Y comercio_1932 = 74
Entonces el comercio CAYÓ 26% respecto al pico

PREGUNTA PARA ESTUDIANTES: "¿Por qué creen que el comercio no se recuperó en los años 20, después de terminada la guerra?"

CONEXIÓN: Este indicador lo vamos a usar para ver el "gran colapso" de 1914-1945, uno de los eventos más importantes de la historia económica.""",

    5: """LECTURA DEL GRÁFICO - ÍNDICE DE COMERCIO (8 minutos)

GUÍA PARA LEER EL GRÁFICO:
1. Eje Y: el índice (1913=100)
2. Eje X: años desde 1800
3. Identificar las FASES: crecimiento, pico, colapso

DATOS CLAVE PARA MENCIONAR:
- 1800: índice 2.4 → el comercio era casi inexistente comparado con 1913
- 1870: índice 25 → en 70 años se multiplicó por 10
- 1913: índice 100 → el pico, justo antes de la guerra
- 1929: índice ~95 → casi recuperado
- 1932: índice 74 → colapso por la Gran Depresión

PREGUNTA: "¿Qué pasó entre 1929 y 1932 que hizo caer el comercio tan rápido?"

RESPUESTA A DESARROLLAR: No fue solo la crisis financiera. Fue la RESPUESTA POLÍTICA a la crisis:
- Arancel Smoot-Hawley en EEUU (1930): subió aranceles a 20.000 productos
- Represalias de otros países
- Espiral proteccionista: cada país intentó "exportar su desempleo"
- Resultado: todos perdieron

ANALOGÍA CONTEMPORÁNEA: Es como si hoy EEUU, China y Europa empezaran a subir aranceles simultáneamente. Ah, esperen... algo de eso está pasando.

FUENTE: Federico-Tena World Trade Historical Database - es la mejor base de datos de comercio histórico, construida por historiadores económicos españoles.""",

    6: """INDICADOR 2: PARTICIPACIÓN REGIONAL (7 minutos)

CONCEPTO CLAVE: Este indicador mide el "peso" de cada región en el comercio mundial. Es como medir qué porcentaje de las ventas de un shopping corresponde a cada local.

FÓRMULA EXPLICADA:
s_r,t = (X_r,t / X_mundo,t) × 100

Donde:
- s = share (participación)
- r = región
- t = tiempo
- X = exportaciones

EJEMPLO EN PIZARRÓN:
Si Europa exporta $60 y el mundo exporta $100 → Europa tiene 60% de participación

¿POR QUÉ IMPORTA?
- Permite ver CAMBIOS EN EL PODER ECONÓMICO
- Un país que gana participación está creciendo más rápido que el promedio mundial
- Un país que pierde participación está quedando atrás (aunque crezca en términos absolutos)

DATO HISTÓRICO: Gran Bretaña tenía ~25% del comercio mundial en 1870. Hoy tiene ~3%. ¿Significa que comercia menos? No, comercia MUCHO más. Pero otros crecieron más rápido.

CONEXIÓN CON ACTUALIDAD: China pasó de 1% del comercio mundial en 1980 a 15% hoy. Es el cambio más rápido de la historia.""",

    7: """LECTURA DEL GRÁFICO - PARTICIPACIÓN REGIONAL (8 minutos)

PUNTOS A DESTACAR:
1. Europa DOMINABA: 60-70% de todo el comercio era europeo o con Europa
2. Las Américas eran periféricas: 10-20% (y gran parte era comercio con Europa)
3. Asia era marginal: 10-15%

LA "GLOBALIZACIÓN" DEL SIGLO XIX ERA EUROPEA:
- No era comercio "global" en el sentido actual
- Era comercio de Europa con sus colonias y ex-colonias
- El centro estaba en Londres, Liverpool, Hamburgo, Amberes
- La periferia exportaba materias primas, importaba manufacturas

PREGUNTA PARA REFLEXIÓN: "¿Por qué Latinoamérica nunca logró tener una participación mayor?"

POSIBLES RESPUESTAS A GUIAR:
- Especialización en materias primas de bajo valor agregado
- Dependencia de pocos productos (monocultivo)
- Falta de industrialización
- Términos del intercambio desfavorables (esto lo vamos a ver con el indicador 7)

CONEXIÓN: Este patrón de centro-periferia es lo que Prebisch y la CEPAL van a teorizar en los años 50. Lo veremos más adelante en el curso.""",

    8: """INDICADOR 3: CONCENTRACIÓN HHI (10 minutos)

CONTEXTO: El HHI (Herfindahl-Hirschman Index) es un indicador que viene de la economía industrial. Se usa para medir concentración de mercado en regulación antimonopolio.

FÓRMULA Y LÓGICA:
HHI = Σ(s_i)²

¿Por qué elevar al cuadrado?
- Porque queremos que las participaciones GRANDES pesen más que las chicas
- Si hay un país con 50% de participación, su contribución al HHI es 0.50² = 0.25
- Si hay 50 países con 1% cada uno, cada uno contribuye 0.01² = 0.0001

EJEMPLO EN PIZARRÓN:
Caso A: Un país tiene 100% → HHI = 1² = 1 (máxima concentración)
Caso B: Cuatro países tienen 25% cada uno → HHI = 4 × (0.25)² = 0.25
Caso C: Cien países tienen 1% cada uno → HHI = 100 × (0.01)² = 0.01 (muy disperso)

INTERPRETACIÓN:
- HHI > 0.25: concentración alta
- HHI 0.15-0.25: concentración moderada
- HHI < 0.15: mercado competitivo/disperso

APLICACIÓN AL COMERCIO: Usamos el HHI para ver si el comercio mundial está concentrado en pocos países o disperso entre muchos.

DATO: El HHI del comercio mundial cayó de ~0.15 en 1800 a ~0.05 en 2000. Esto significa que el comercio se fue DIVERSIFICANDO: más países participan.""",

    9: """LECTURA DEL GRÁFICO - HHI (5 minutos)

TENDENCIA GENERAL: El HHI baja a lo largo del período → el comercio se diversifica

¿POR QUÉ BAJA?
- Más países se industrializan y empiezan a exportar
- Las colonias se independizan y comercian más diversificado
- Nuevos productos entran al comercio (no solo textiles y materias primas)

ANOMALÍA DE LOS AÑOS 30: El HHI SUBE levemente
- Esto refleja la fragmentación en BLOQUES COMERCIALES
- Imperio británico comerciaba entre sí (preferencia imperial)
- Alemania con Europa del Este
- EEUU con América Latina
- Japón con Asia

PREGUNTA: "¿Qué creen que pasó con el HHI después de 1945?"

RESPUESTA: Siguió bajando, especialmente desde los 80s con la entrada de Asia al comercio mundial.

ADVERTENCIA: HHI bajo no significa que todos los países participen IGUAL. La distribución sigue siendo muy desigual. Solo significa que no hay UN país dominante.""",

    10: """INDICADOR 4: COBERTURA DE DATOS (5 minutos)

ESTE INDICADOR ES METODOLÓGICO - enseña pensamiento crítico sobre datos.

¿QUÉ ES LA COBERTURA?
- Porcentaje del comercio mundial que efectivamente está medido
- Si la cobertura es 80%, el 20% restante es estimación

¿POR QUÉ IMPORTA?
- Datos con baja cobertura tienen más error
- Hay que ser cauteloso al interpretar
- No todos los países reportaban datos (especialmente colonias)

EJEMPLO CONCRETO:
- Para 1850, la cobertura es ~60%: sabemos bien el comercio de Europa, poco del resto
- Para 1913, la cobertura es ~90%: casi todos los países reportan
- Para 2020, la cobertura es ~99%: datos muy confiables

REGLA PRÁCTICA: Siempre preguntar "¿De dónde vienen estos datos? ¿Qué cobertura tienen?"

APLICACIÓN: Cuando lean un paper o informe que dice "el comercio creció X% en el siglo XIX", pregunten: ¿con qué datos? ¿qué cobertura? ¿de qué países?

CONEXIÓN: Esta es una habilidad general para cualquier análisis empírico, no solo comercio internacional.""",

    11: """TRES ADVERTENCIAS - CIERRE DEL BLOQUE DE MEDICIÓN (5 minutos)

ADVERTENCIA 1: PRECIOS VS CANTIDADES
- Los datos de comercio suelen estar en VALORES (precio × cantidad)
- Si el precio sube, el valor sube aunque la cantidad sea igual
- Ejemplo: Si el precio del petróleo sube 50%, las exportaciones de petróleo "crecen" 50% en valor, aunque sean los mismos barriles
- SOLUCIÓN: Usar índices de volumen (ajustados por precios) cuando estén disponibles

ADVERTENCIA 2: COMERCIO BRUTO VS VALOR AGREGADO
- El comercio "bruto" cuenta el valor total de cada transacción
- Pero hoy, con cadenas globales de valor, el mismo insumo cruza fronteras varias veces
- Ejemplo: Un iPhone tiene componentes de 6 países. Se cuenta como exportación cada vez que cruza una frontera.
- DATO: Se estima que 1/3 del comercio mundial es "doble conteo"
- SOLUCIÓN: Usar datos de "comercio en valor agregado" cuando estén disponibles (TiVA de OCDE)

ADVERTENCIA 3: CALIDAD DE FUENTES HISTÓRICAS
- Las series largas combinan datos de distintas fuentes
- Un quiebre en la serie puede ser un cambio real O un cambio en la metodología
- REGLA: Siempre verificar si hay cambios metodológicos en las fechas de quiebre

MENSAJE FINAL: Los datos son herramientas, no verdades absolutas. Hay que usarlos con criterio.""",

    12: """INDICADOR 5: BALANZA COMERCIAL (7 minutos)

EL INDICADOR MÁS SIMPLE - pero con muchas confusiones

FÓRMULA:
BC = X - M (Exportaciones menos Importaciones)

INTERPRETACIÓN:
- BC > 0: SUPERÁVIT comercial (exporta más de lo que importa)
- BC < 0: DÉFICIT comercial (importa más de lo que exporta)
- BC = 0: Equilibrio comercial (raro en la práctica)

CONFUSIÓN COMÚN #1: "Superávit = bueno, déficit = malo"
RESPUESTA: ¡Depende del contexto!
- Un país puede tener déficit porque está INVIRTIENDO (importa maquinaria)
- Un país puede tener superávit porque está en RECESIÓN (no importa porque no consume)
- China tiene superávit, EEUU déficit, pero ambos crecieron

CONFUSIÓN COMÚN #2: "Si tenemos déficit con China, China nos está ganando"
RESPUESTA: El comercio bilateral no tiene que estar equilibrado.
- Argentina tiene superávit con China (le vendemos soja) y déficit con Brasil (les compramos autos)
- Lo que importa es la balanza TOTAL, no bilateral

DATO CURIOSO: A nivel mundial, la suma de todas las balanzas comerciales debería ser CERO (las exportaciones de uno son importaciones de otro). Pero hay una "discrepancia estadística" de ~3% por errores de medición.

PREGUNTA: "¿Argentina tiene superávit o déficit comercial habitualmente?" (Respuesta: depende del año - veremos el patrón)""",

    13: """INDICADOR 6: APERTURA COMERCIAL (8 minutos)

FÓRMULA:
Apertura = (X + M) / PIB × 100

INTERPRETACIÓN: Qué proporción del PIB se comercia con el mundo

EJEMPLOS REALES (datos aproximados):
- EEUU: ~25% (economía grande, mercado interno enorme)
- Argentina: ~30% (economía mediana, algo cerrada históricamente)
- Alemania: ~90% (economía grande pero muy orientada a exportación)
- Singapur: ~300% (¡más del 100%! - ya explico por qué)

¿CÓMO PUEDE SER MÁS DE 100%?
- Singapur, Hong Kong, Países Bajos tienen "apertura" > 100%
- Porque son HUBS DE REEXPORTACIÓN
- Importan, procesan mínimamente, y exportan
- El mismo bien se cuenta dos veces (entrada y salida)

TRAMPAS DEL INDICADOR:
1. Países GRANDES tienden a ser "cerrados" → tienen mercado interno grande
2. Países CHICOS tienden a ser "abiertos" → necesitan comerciar
3. NO confundir apertura con POLÍTICA comercial
   - Argentina es "cerrada" (30%) pero tuvo épocas de libre comercio
   - China es "abierta" (35%) pero tiene muchas barreras

PREGUNTA: "¿Por qué creen que EEUU, siendo el mayor promotor del libre comercio, tiene una apertura tan baja?"

RESPUESTA: Porque su mercado interno es TAN GRANDE que puede producir casi todo localmente. Texas comercia más con California que con México.""",

    14: """INDICADOR 7: TÉRMINOS DEL INTERCAMBIO (12 minutos)

ESTE ES CLAVE PARA ENTENDER A ARGENTINA Y LATINOAMÉRICA

FÓRMULA:
ToT = (Px / Pm) × 100

Donde:
- Px = índice de precios de lo que EXPORTAMOS
- Pm = índice de precios de lo que IMPORTAMOS

INTERPRETACIÓN:
- ToT SUBE (mejora): con las mismas exportaciones compramos MÁS importaciones
- ToT BAJA (deterioro): necesitamos exportar MÁS para comprar lo mismo

EJEMPLO NUMÉRICO EN PIZARRÓN:
Año base: Exportamos 100 toneladas de soja a $300/ton = $30.000
         Importamos 10 autos a $3.000 c/u = $30.000
         ToT = 100

Escenario A (mejora): Precio soja sube a $450
         Exportamos 100 ton × $450 = $45.000
         Podemos comprar 15 autos (en vez de 10)
         ToT = 150

Escenario B (deterioro): Precio soja cae a $200
         Exportamos 100 ton × $200 = $20.000
         Solo podemos comprar 6.7 autos
         ToT = 67

PREGUNTA: "¿Qué le pasó a Argentina en el período 2003-2012?"

RESPUESTA: ¡Mejora de ToT del 40%! El precio de la soja y otros commodities se triplicó. Argentina se "enriqueció" sin producir más.

PREGUNTA SEGUIMIENTO: "¿Y qué pasó 2012-2015?"

RESPUESTA: Deterioro del 20%. Los precios cayeron. Volvió la restricción externa.

CONEXIÓN TEÓRICA: Prebisch y Singer (economistas de CEPAL) argumentaron que los ToT de países exportadores de materias primas se deterioran a LARGO PLAZO. Es la "tesis Prebisch-Singer" que veremos más adelante.""",

    15: """ToT Y EL INGRESO REAL - PROFUNDIZACIÓN (8 minutos)

CONCEPTO CLAVE: Los ToT afectan el INGRESO REAL del país, no solo el comercio.

ANALOGÍA DEL SALARIO:
- Imaginemos que tu salario es fijo en $1000/mes
- Si el precio de lo que comprás BAJA, sos más rico (podés comprar más)
- Si el precio de lo que comprás SUBE, sos más pobre (comprás menos)
- Tu salario nominal no cambió, pero tu salario REAL sí

LO MISMO PASA CON LOS PAÍSES:
- Si el precio de lo que exportamos SUBE → nos "enriquecemos"
- Si el precio de lo que importamos SUBE → nos "empobrecemos"
- El PIB puede no cambiar, pero el poder de compra internacional sí

CASO ARGENTINA - DATOS:
- 2003-2012: ToT +40%, PIB +80%, Cuenta Corriente superavitaria
- 2012-2015: ToT -20%, PIB estancado, vuelve el déficit
- 2020-2022: ToT +30% (pandemia + guerra Ucrania), superávit récord

PREGUNTA DIFÍCIL: "¿Qué pasa si sube el precio de la soja (exportamos) pero también sube el precio del petróleo (importamos)?"

RESPUESTA: Depende de cuánto pesa cada uno. Argentina es exportador neto de alimentos pero importador neto de energía (aunque esto está cambiando con Vaca Muerta). Hay que mirar el efecto NETO en los ToT.

EJERCICIO MENTAL: "¿Qué países ganan y cuáles pierden con la suba del petróleo?" (Rusia, Arabia Saudita ganan; Japón, India pierden; Argentina... depende)""",

    16: """TRANSICIÓN AL BLOQUE HISTÓRICO (2 minutos)

RESUMEN DE LO QUE VIMOS:
Ya tenemos 7 indicadores del "kit básico":
1. Índice de comercio (nivel general)
2. Participación regional (quién gana/pierde)
3. HHI (concentración)
4. Cobertura (calidad de datos)
5. Balanza comercial (X - M)
6. Apertura ((X+M)/PIB)
7. Términos del intercambio (Px/Pm)

AHORA VAMOS A USAR ESTOS INDICADORES:
- Para leer la historia del comercio internacional
- Para entender por qué creció, colapsó, y volvió a crecer
- Para ver patrones que se repiten

METÁFORA: Ya aprendimos a leer el mapa. Ahora vamos a hacer el viaje.

Los otros 2 indicadores (Cuenta Corriente y Tipo de Cambio Real) los vemos en el bloque de Balanza de Pagos.""",

    17: """MARCO ANALÍTICO: TRES FUERZAS (10 minutos)

ESTE MARCO LO VAMOS A USAR TODO EL CUATRIMESTRE

LAS TRES FUERZAS QUE DETERMINAN EL COMERCIO:

1. TECNOLOGÍA: ¿Cuánto cuesta mover bienes e información?
   - Vela → Vapor → Contenedor → Digital
   - El costo de transporte cayó 90% en 200 años
   - El costo de comunicación cayó 99.9% (telégrafo → internet)
   - EJEMPLO: En 1800, traer té de China tardaba 6 meses. Hoy, 3 semanas por barco, 3 días por avión.

2. REGLAS: ¿Quién puede comerciar y en qué términos?
   - Monopolios coloniales → Libre comercio → Proteccionismo → OMC
   - Aranceles, cuotas, barreras no arancelarias
   - Acuerdos bilaterales, regionales, multilaterales
   - EJEMPLO: En el siglo XVI, solo la Corona española podía comerciar con América. Hoy, cualquier empresa puede (con algunas restricciones).

3. PODER: ¿Quién garantiza que se cumplan las reglas?
   - Hegemonía británica (1815-1914)
   - Hegemonía estadounidense (1945-?)
   - Sin hegemón, el sistema se fragmenta
   - EJEMPLO: La Royal Navy garantizaba que los barcos no fueran pirateados. Hoy, la Marina de EEUU patrulla el 70% de las rutas comerciales.

PREGUNTA CLAVE: "¿Qué pasa cuando UNA de estas fuerzas falla?"
RESPUESTA: El sistema comercial se contrae o colapsa. Vamos a ver ejemplos.""",

    18: """CINCO ETAPAS DEL COMERCIO INTERNACIONAL (8 minutos)

PRESENTAR EL TIMELINE:

ETAPA 1 - IBÉRICO-COLONIAL (1500-1650):
- Protagonistas: España y Portugal
- Modelo: Monopolios estatales
- Comercio: Metales preciosos, especias
- Tecnología: Navegación a vela, brújula

ETAPA 2 - PRIMERA GLOBALIZACIÓN (1800-1914):
- Protagonista: Gran Bretaña
- Modelo: Libre comercio (unilateral británico)
- Comercio: Manufacturas, materias primas, capitales
- Tecnología: Vapor, ferrocarril, telégrafo

ETAPA 3 - COLAPSO (1914-1945):
- Protagonistas: Nadie (vacío hegemónico)
- Modelo: Proteccionismo, bloques
- Comercio: Se contrae 50%
- Tecnología: Existe, pero las reglas fallan

ETAPA 4 - HEGEMONÍA EEUU (1945-2008):
- Protagonista: Estados Unidos
- Modelo: Instituciones multilaterales (GATT/OMC, FMI, BM)
- Comercio: Crece 30 veces
- Tecnología: Contenedor, aviación, internet

ETAPA 5 - SLOWBALIZATION (2008-hoy):
- Protagonistas: ¿EEUU vs China?
- Modelo: Tensiones, regionalización
- Comercio: Crece lento, se reconfigura
- Tecnología: Digital, pero con "desacople"

ACLARACIÓN: Esta periodización es una SIMPLIFICACIÓN didáctica. Las fechas son aproximadas y hay superposiciones.""",

    19: """ETAPA 1: ECONOMÍA-MUNDO IBÉRICA (10 minutos)

CONTEXTO HISTÓRICO:
- 1492: Colón llega a América
- 1498: Vasco da Gama llega a India
- España y Portugal se "reparten" el mundo (Tratado de Tordesillas, 1494)

EL MODELO DE MONOPOLIO:
- La Corona controlaba TODO el comercio
- Casa de Contratación (Sevilla): único puerto autorizado para comercio con América
- Flotas anuales: los barcos viajaban en convoy por seguridad
- Objetivo: extraer metales preciosos y controlar el comercio de especias

¿POR QUÉ MONOPOLIO Y NO LIBRE COMERCIO?
- El Estado absorbía los RIESGOS (piratas, naufragios, guerras)
- El Estado capturaba las RENTAS (impuestos del 20% sobre metales)
- No había capacidad para "regular" un mercado libre

DATO: Entre 1500 y 1650, llegaron a España ~180 toneladas de ORO y ~17.000 toneladas de PLATA. Esto generó la "revolución de los precios" en Europa (inflación).

CONSECUENCIAS:
- España se volvió DEPENDIENTE de la plata americana
- No desarrolló industria propia (compraba todo con plata)
- Cuando la plata se agotó, España decayó

PREGUNTA: "¿Ven algún paralelo con países que hoy dependen de un solo recurso?" (Venezuela, petróleo; Argentina, soja)""",

    20: """EL GALEÓN DE MANILA - PRIMERA CADENA GLOBAL (8 minutos)

HISTORIA FASCINANTE:

LA RUTA (1565-1815, 250 años):
1. Manila (Filipinas): Se cargaban productos asiáticos
2. Cruce del Pacífico: 4-6 meses de viaje
3. Acapulco (México): Descarga y venta
4. Por tierra a Veracruz
5. Flota del Atlántico a Sevilla

¿QUÉ SE COMERCIABA?
- DE ASIA: Seda china, porcelana, especias, marfil
- DE AMÉRICA: Plata, y solo plata

LOS NÚMEROS:
- 1-2 galeones por año (únicos autorizados)
- Cada viaje movía ~2 millones de pesos en plata
- La seda china se vendía en México a 10 veces su precio en Manila

¿POR QUÉ IMPORTA?
- Primera conexión REGULAR entre tres continentes
- La plata americana financiaba el comercio asiático
- China tenía DÉFICIT de plata → la necesitaba para su sistema monetario
- Este fue el primer "desequilibrio comercial" global

CONEXIÓN ACTUAL: Hoy China tiene SUPERÁVIT con EEUU. En el siglo XVI era al revés: China tenía "déficit" (recibía plata a cambio de bienes).

ANÉCDOTA: Los comerciantes de Manila eran tan ricos que el virrey de México se quejaba de que "toda la plata de América termina en China".""",

    21: """ETAPA 2: PRIMERA GLOBALIZACIÓN (12 minutos)

¿POR QUÉ "PRIMERA" GLOBALIZACIÓN?
- Porque hubo una antes de la actual
- Y porque colapsó (1914-1945)
- Lección: la globalización NO es irreversible

LOS CUATRO PILARES DEL SISTEMA BRITÁNICO:

1. TECNOLOGÍA - Revolución del transporte:
   - Barco a vapor (1820s): reduce tiempo de viaje 50%
   - Ferrocarril: conecta interiores (trigo de Kansas, carne de Pampa)
   - Canal de Suez (1869): acorta ruta Europa-Asia de 6 meses a 6 semanas
   - DATO: El costo del flete marítimo cayó 60% entre 1840 y 1910

2. REGLAS - Libre comercio unilateral:
   - Gran Bretaña abolió las Corn Laws (1846): aranceles al trigo
   - Tratado Cobden-Chevalier (1860): libre comercio con Francia
   - GB no exigía reciprocidad: "comercien con nosotros aunque ustedes tengan aranceles"
   - ¿Por qué? Porque GB era tan competitiva que le convenía el libre comercio

3. DINERO - Patrón oro:
   - La libra esterlina era convertible a oro
   - Tipo de cambio fijo entre países
   - Facilitaba el comercio y la inversión internacional

4. PODER - Pax Britannica:
   - Royal Navy: supremacía naval absoluta
   - GB controlaba puntos estratégicos: Gibraltar, Suez, Singapur, Hong Kong
   - Garantizaba que las rutas comerciales fueran seguras

DATO: En 1870, Gran Bretaña producía 50% de los textiles del mundo y tenía 25% del comercio mundial.""",

    22: """EL TELÉGRAFO: PRIMERA REVOLUCIÓN DE LA INFORMACIÓN (8 minutos)

IMPACTO REVOLUCIONARIO:

ANTES DEL TELÉGRAFO (pre-1850):
- Un comerciante en Londres no sabía el precio del algodón en Nueva York hasta que llegaba el barco (4-6 semanas)
- Enviaba mercadería sin saber si habría demanda
- Los precios variaban enormemente entre mercados
- Alto riesgo, altas ganancias (o pérdidas)

DESPUÉS DEL TELÉGRAFO (post-1870):
- Precios se conocían en MINUTOS
- Arbitraje inmediato: si el precio es mayor en un lugar, alguien compra donde es barato y vende donde es caro
- Los precios se "convergen" entre mercados
- Contratos a distancia: se podía cerrar un negocio sin verse

DATOS DE LA RED:
- 1851: Primer cable submarino (Dover-Calais)
- 1866: Primer cable transatlántico exitoso
- 1870: Londres conectada con Bombay
- 1900: 300.000 km de cables submarinos en el mundo

ANALOGÍA: El telégrafo fue la "internet" del siglo XIX. Cambió la velocidad de los negocios de la misma manera.

PREGUNTA: "¿Qué tecnología actual está teniendo un impacto similar?"

POSIBLES RESPUESTAS:
- Internet (ya pasó)
- Smartphones (habilitan comercio electrónico en países pobres)
- Blockchain? (aún no claro)
- IA? (potencial para automatizar logística)""",

    23: """ETAPA 3: EL COLAPSO 1914-1945 (15 minutos)

ESTE ES UNO DE LOS EVENTOS MÁS IMPORTANTES DE LA HISTORIA ECONÓMICA

CRONOLOGÍA DEL DESASTRE:

1914-1918: PRIMERA GUERRA MUNDIAL
- Rutas comerciales bloqueadas
- Los países beligerantes imponen aranceles
- El patrón oro se suspende
- DATO: El comercio mundial cayó 30% durante la guerra

1919-1929: FALSA RECUPERACIÓN
- Intento de volver al patrón oro (pero con tipos de cambio mal calibrados)
- Alemania devastada por reparaciones de guerra
- EEUU se vuelve acreedor mundial pero no asume liderazgo
- El comercio se recupera PARCIALMENTE pero no al nivel de 1913

1929-1933: LA GRAN DEPRESIÓN
- Crack de Wall Street (octubre 1929)
- Contracción crediticia global
- RESPUESTA FATAL: Proteccionismo
- Arancel Smoot-Hawley (EEUU, 1930): aranceles a 20.000 productos
- REPRESALIAS de otros países
- Espiral descendente

1930-1939: FRAGMENTACIÓN EN BLOQUES
- Preferencia imperial británica
- Bloque del marco (Alemania + Europa del Este)
- Bloque del yen (Japón + Asia)
- Cada bloque comerciaba internamente
- El comercio mundial en 1938 era MENOR que en 1913

LECCIÓN CLAVE: "El comercio no colapsó solo por la guerra o la crisis. Colapsó por la RESPUESTA POLÍTICA a la crisis."

PREGUNTA: "¿Qué deberían haber hecho en vez de subir aranceles?"

RESPUESTA: Coordinación internacional, no competencia. Pero no había instituciones ni hegemón que coordinara.""",

    24: """EL PODER DETRÁS DEL COMERCIO (10 minutos)

TESIS CENTRAL: El libre comercio del siglo XIX no fue "natural" ni "automático". Fue SOSTENIDO por el poder británico.

LA HEGEMONÍA BRITÁNICA PROVEÍA:

1. SEGURIDAD DE RUTAS:
   - Royal Navy era la marina más grande del mundo
   - Controlaba puntos estratégicos
   - Combatía piratería
   - DATO: GB gastaba 3% del PIB en defensa naval

2. REGLAS DEL JUEGO:
   - GB impuso el libre comercio como "norma"
   - Pero no a todos: con India y colonias era comercio FORZADO
   - El liberalismo era selectivo

3. MONEDA DE RESERVA:
   - La libra esterlina era la moneda del comercio
   - Londres era el centro financiero mundial
   - GB proveía liquidez al sistema

¿POR QUÉ COLAPSÓ?
- Las guerras mundiales AGOTARON a Gran Bretaña
- GB pasó de acreedor a deudor
- EEUU era el nuevo poder económico, pero no quería el rol
- Entre 1918 y 1945 hubo un "vacío hegemónico"
- Sin nadie que garantice las reglas, cada país se protegió

TEORÍA DE LA ESTABILIDAD HEGEMÓNICA (Kindleberger):
- Un sistema comercial abierto necesita un "hegemón"
- El hegemón provee bienes públicos: seguridad, reglas, liquidez
- Cuando el hegemón declina y no hay sucesor, el sistema colapsa

PREGUNTA: "¿Quién es el hegemón hoy? ¿Está en declinación?"

CONEXIÓN: Esto es muy relevante para entender las tensiones actuales EEUU-China.""",

    25: """TRANSICIÓN AL BLOQUE DE BALANZA DE PAGOS (2 minutos)

RECAPITULACIÓN:
- Vimos la historia del comercio (1500-1945)
- Vimos 7 indicadores de comercio
- Ahora agregamos 2 indicadores más: Cuenta Corriente y Tipo de Cambio Real

¿POR QUÉ NECESITAMOS ESTOS INDICADORES?
- La balanza comercial (X - M) solo mide bienes
- Pero hay más: servicios, rentas, transferencias
- Y todo esto se relaciona con el tipo de cambio

ESTOS INDICADORES SON CLAVE PARA:
- Analizar la situación ACTUAL de un país
- Entender las crisis (Argentina 2001, Asia 1997)
- Ver los desequilibrios globales (EEUU vs China)

El bloque de historia continúa después (Etapas 4 y 5: hegemonía EEUU y slowbalization), pero primero completamos las herramientas.""",

    26: """¿QUÉ ES LA BALANZA DE PAGOS? (10 minutos)

DEFINICIÓN: Registro sistemático de TODAS las transacciones de un país con el resto del mundo.

ANALOGÍA: Es como el "estado de cuenta" de un país. Registra todo lo que entra y sale.

LAS TRES CUENTAS:

1. CUENTA CORRIENTE (la más importante):
   - Bienes: exportaciones e importaciones físicas
   - Servicios: turismo, fletes, software, consultoría
   - Rentas: intereses, dividendos, remesas
   - Transferencias: donaciones, ayuda

2. CUENTA DE CAPITAL (menor):
   - Transferencias de capital (condonación de deuda)
   - Activos no financieros (patentes, marcas)
   - En la práctica, es pequeña

3. CUENTA FINANCIERA:
   - Inversión Extranjera Directa (fábricas, empresas)
   - Inversión de cartera (bonos, acciones)
   - Otra inversión (préstamos bancarios)
   - Reservas internacionales

EL PRINCIPIO CONTABLE FUNDAMENTAL:
CC + CK + CF = 0 (con signo inverso)

Si tenés DÉFICIT de cuenta corriente, necesitás SUPERÁVIT de cuenta financiera (alguien te financia).

EJEMPLO NUMÉRICO:
Argentina importa más de lo que exporta (déficit CC = -$10.000 millones)
¿De dónde sale la plata?
- Entran dólares de inversores (superávit CF = +$10.000 millones)
- O el BCRA vende reservas

PREGUNTA: "¿Qué pasa si tenés déficit de CC y nadie quiere financiarte?"
RESPUESTA: Crisis de balanza de pagos.""",

    27: """INDICADOR 8: CUENTA CORRIENTE (12 minutos)

FÓRMULA COMPLETA:
CC = (X - M) + Rentas + Transferencias

Expresada como % del PIB:
CC/PIB × 100

INTERPRETACIÓN:
- CC > 0: SUPERÁVIT → El país produce más de lo que consume
  → Ahorra más de lo que invierte
  → PRESTA al resto del mundo

- CC < 0: DÉFICIT → El país consume más de lo que produce
  → Invierte más de lo que ahorra
  → Se ENDEUDA con el resto del mundo

¿DÉFICIT ES MALO?
¡DEPENDE!

DÉFICIT "BUENO":
- Si financia INVERSIÓN productiva
- Ejemplo: Chile en los 90s tenía déficit pero invertía en minería
- La inversión genera retorno futuro para pagar la deuda

DÉFICIT "MALO":
- Si financia CONSUMO
- Ejemplo: Argentina en los 90s tenía déficit y no invertía
- La deuda crece sin capacidad de pago

LA IDENTIDAD FUNDAMENTAL:
CC = S - I (Ahorro nacional menos Inversión nacional)

Si CC < 0 → S < I → El país invierte más de lo que ahorra → Necesita ahorro externo

DATOS PARA COMPARAR:
- EEUU: -3% del PIB (déficit persistente)
- Alemania: +7% del PIB (superávit persistente)
- China: +2% del PIB (superávit moderado, antes era +10%)
- Argentina: oscila entre +5% y -5% dependiendo del ciclo

PREGUNTA: "¿Por qué EEUU puede tener déficit persistente sin entrar en crisis?"
(Lo vemos en el bloque de desequilibrios globales)""",

    28: """LA IDENTIDAD AHORRO-INVERSIÓN (10 minutos)

ESTA FÓRMULA CONECTA MACROECONOMÍA DOMÉSTICA CON SECTOR EXTERNO

FÓRMULA DESAGREGADA:
CC = (S_privado - I_privado) + (T - G)

Donde:
- S_privado = ahorro del sector privado
- I_privado = inversión del sector privado
- T = impuestos (ingresos del gobierno)
- G = gasto del gobierno

INTERPRETACIÓN:
- Si sector privado ahorra más de lo que invierte → contribuye al superávit
- Si gobierno tiene déficit fiscal (G > T) → presiona hacia déficit de CC

LOS "DÉFICITS GEMELOS":
Cuando hay déficit fiscal Y déficit de cuenta corriente simultáneamente.
- El gobierno gasta más de lo que recauda
- Parte de ese gasto se filtra a importaciones
- Resultado: déficit de CC

CASO ARGENTINA:
- Tasa de ahorro privado: ~15% del PIB (baja para estándares internacionales)
- Inversión: ~18% del PIB
- Sector privado ya genera déficit de 3%
- Si además hay déficit fiscal de 3%
- → Déficit de CC de 6%

PREGUNTA: "¿Por qué creen que Argentina tiene baja tasa de ahorro?"

POSIBLES RESPUESTAS:
- Inflación erosiona el ahorro
- Tasas de interés reales negativas
- Desconfianza en el sistema financiero
- Ahorro se va al dólar o al exterior

CONEXIÓN: Esta es la base del "ciclo argentino" que veremos más adelante.""",

    29: """TRANSICIÓN AL BLOQUE DE TIPO DE CAMBIO (2 minutos)

CONEXIÓN CC ↔ TC:

La cuenta corriente y el tipo de cambio están RELACIONADOS:
- Si el tipo de cambio está "caro" (moneda apreciada) → importaciones baratas, exportaciones caras → déficit CC
- Si el tipo de cambio está "barato" (moneda depreciada) → importaciones caras, exportaciones baratas → superávit CC

Pero ojo: la relación no es automática ni inmediata. Hay otros factores.

PREGUNTA DISPARADORA: "¿Qué prefieren: un dólar barato (digamos, $500) o un dólar caro (digamos, $2000)?"

Esta pregunta genera debate porque:
- Dólar barato → viajes baratos, importaciones baratas, bienestar inmediato
- Dólar caro → exportaciones competitivas, empleo industrial, pero inflación

No hay respuesta "correcta" universal. Depende del contexto y las prioridades.""",

    30: """TIPO DE CAMBIO: NOMINAL VS REAL (12 minutos)

TIPO DE CAMBIO NOMINAL (E):
- Es el que ven en las casas de cambio o en los diarios
- Pesos por dólar (en Argentina)
- Ejemplo: E = 1000 $/US$

TIPO DE CAMBIO REAL (e):
- Es el TC nominal AJUSTADO por precios relativos
- Mide COMPETITIVIDAD: ¿son baratos o caros nuestros bienes en el mundo?

EJEMPLO PARA ENTENDER LA DIFERENCIA:

Situación A (enero 2024):
- TC nominal: 800 $/US$
- Big Mac en Argentina: $4.000 (= US$ 5.00)
- Big Mac en EEUU: US$ 5.50

Situación B (julio 2024, con inflación argentina):
- TC nominal: 900 $/US$
- Big Mac en Argentina: $5.400 (= US$ 6.00)
- Big Mac en EEUU: US$ 5.50

¿Qué pasó?
- El dólar subió 12.5% (de 800 a 900)
- Pero la Big Mac subió 35% (de 4000 a 5400)
- En dólares, Argentina se encareció (de US$5.00 a US$6.00)
- El tipo de cambio REAL se apreció (aunque el nominal subió)

MENSAJE CLAVE:
"DEVALUACIÓN NOMINAL NO ES LO MISMO QUE DEPRECIACIÓN REAL"

Si después de devaluar hay inflación que "se come" la devaluación, la competitividad no mejora.

PREGUNTA: "¿Qué pasó en Argentina después de la devaluación de 2002?"
RESPUESTA: El TC real se depreció MUCHO porque la inflación tardó en ajustar. Eso hizo las exportaciones muy competitivas.""",

    31: """INDICADOR 9: TIPO DE CAMBIO REAL (12 minutos)

FÓRMULA:
e = E × (P* / P)

Donde:
- e = tipo de cambio real
- E = tipo de cambio nominal (pesos por dólar)
- P* = nivel de precios externo (ej: EEUU)
- P = nivel de precios doméstico (Argentina)

INTERPRETACIÓN:
- Si e SUBE → depreciación real → somos MÁS competitivos
- Si e BAJA → apreciación real → somos MENOS competitivos

EJEMPLO NUMÉRICO EN PIZARRÓN:

Período 1:
E = 100, P* = 100, P = 100
e = 100 × (100/100) = 100 (índice base)

Período 2 (devaluación sin inflación):
E = 150, P* = 100, P = 100
e = 150 × (100/100) = 150 (depreciación real del 50%)

Período 3 (inflación que compensa):
E = 150, P* = 100, P = 150
e = 150 × (100/150) = 100 (volvió al nivel inicial)

EN LA PRÁCTICA:
- Argentina usa el ITCRM (Índice de Tipo de Cambio Real Multilateral)
- "Multilateral" porque considera múltiples socios comerciales, no solo EEUU
- Lo calcula el BCRA mensualmente

REGLA SIMPLE:
"Si la inflación acumulada supera la devaluación acumulada, el peso se está apreciando en términos reales."

DATO HISTÓRICO:
- Durante la convertibilidad (1991-2001), el TC nominal estaba fijo en 1:1
- Pero Argentina tenía inflación y EEUU casi no
- → Apreciación real sostenida
- → Pérdida de competitividad
- → Déficit de CC
- → Crisis""",

    32: """TRANSICIÓN A DESEQUILIBRIOS GLOBALES (3 minutos)

AHORA TENEMOS LAS 9 HERRAMIENTAS:
1-7: Indicadores de comercio
8: Cuenta corriente
9: Tipo de cambio real

VAMOS A APLICARLAS A:
1. Los desequilibrios globales (EEUU, China, Alemania)
2. El caso argentino

PREGUNTA DISPARADORA:
"¿Por qué hay países que tienen superávit de cuenta corriente SIEMPRE (Alemania, China) y países que tienen déficit SIEMPRE (EEUU, Reino Unido)?"

¿No deberían los mercados equilibrar esto?
¿No debería el tipo de cambio ajustar?

Spoiler: No es tan simple. Hay factores estructurales.""",

    33: """¿QUÉ SON LOS DESEQUILIBRIOS GLOBALES? (10 minutos)

DEFINICIÓN: Persistencia de superávits y déficits de cuenta corriente en los mismos países durante décadas.

LOS PROTAGONISTAS:

EEUU - El gran deudor:
- Déficit desde 1982 (más de 40 años)
- Oscila entre -2% y -6% del PIB
- Acumula deuda externa equivalente a 70% del PIB
- ¿Por qué no entra en crisis? (lo vemos)

CHINA - El gran acreedor:
- Superávit desde 1994
- Pico de 10% del PIB en 2007
- Hoy ~2% (el gobierno rebalanceó hacia consumo interno)
- Acumula reservas: US$ 3 trillones

ALEMANIA - El otro gran acreedor:
- Superávit desde 2002
- ~7% del PIB, muy alto para una economía grande
- Financia al resto de Europa (y a EEUU)

CAUSAS ESTRUCTURALES:

1. DEMOGRAFÍA:
- Países con población envejecida (Alemania, Japón) ahorran más
- Países con población joven (EEUU) ahorran menos

2. MODELO DE CRECIMIENTO:
- China y Alemania: "export-led growth" (crecen exportando)
- EEUU: "consumption-led growth" (crecen consumiendo)

3. EL ROL DEL DÓLAR:
- EEUU puede tener déficits porque el mundo QUIERE dólares
- Es el "privilegio exorbitante" de emitir la moneda de reserva""",

    34: """GRÁFICO: CUENTA CORRIENTE EEUU, CHINA, ALEMANIA (10 minutos)

LECTURA DEL GRÁFICO:

EJE Y: Cuenta corriente como % del PIB
EJE X: Años (1980-2024)

IDENTIFICAR:

EEUU (línea negra o azul oscuro):
- Casi siempre debajo de cero
- Pico de déficit: -6% en 2006 (antes de la crisis)
- Se reduce post-2008 pero sigue negativo
- Años recientes: -3% a -4%

CHINA (línea roja):
- Casi cero hasta 2000
- Despega 2001 (entrada a OMC)
- Pico: +10% en 2007 (¡enorme!)
- Cae post-2008: rebalanceo hacia consumo
- Hoy: +2%

ALEMANIA (línea verde o amarilla):
- Déficit en los 90s (reunificación costosa)
- Superávit desde 2002 (reformas Hartz)
- Se mantiene en +6% a +8%
- Muy alto para una economía de su tamaño

PREGUNTAS PARA DISCUSIÓN:

1. "¿Por qué China redujo su superávit después de 2007?"
RESPUESTA: Política deliberada de aumentar consumo interno + críticas internacionales + demanda externa más débil post-crisis.

2. "¿Por qué Alemania no reduce su superávit?"
RESPUESTA: Estructura productiva orientada a exportación + demografía + moderación salarial + ahorro alto.

3. "¿Es sostenible el déficit de EEUU?"
RESPUESTA: Probablemente sí mientras el dólar sea moneda de reserva. Pero hay límites.""",

    35: """EL PRIVILEGIO EXORBITANTE DEL DÓLAR (10 minutos)

TÉRMINO: Acuñado por Valéry Giscard d'Estaing (Ministro de Finanzas francés) en los años 60.

¿QUÉ ES?

EEUU puede tener déficits persistentes porque EMITE LA MONEDA DE RESERVA MUNDIAL.

¿CÓMO FUNCIONA?
1. El mundo necesita dólares para:
   - Comercio internacional (80% se factura en dólares)
   - Reservas de bancos centrales (60% son en dólares)
   - Deuda internacional (50% denominada en dólares)

2. Para conseguir dólares, el mundo tiene que:
   - Exportar a EEUU, o
   - Comprar bonos del Tesoro de EEUU

3. Resultado:
   - EEUU puede importar más de lo que exporta
   - Paga sus importaciones con su propia moneda
   - El mundo financia el déficit americano

DILEMA DE TRIFFIN (1960):
- Para proveer liquidez global, EEUU debe tener déficits
- Pero déficits persistentes erosionan la confianza en el dólar
- Es una contradicción interna del sistema

DATOS:
- Deuda externa neta de EEUU: ~US$ 18 trillones
- Pero el dólar no colapsa porque no hay alternativa clara
- El euro representa 20% de reservas, el yuan solo 3%

PREGUNTA: "¿China podría reemplazar al dólar?"

RESPUESTA: No en el corto plazo. El yuan no es libremente convertible. China tiene controles de capital. No quiere asumir el rol (implicaría tener déficits).""",

    36: """ASIA: DE DEUDORES A ACREEDORES (10 minutos)

LA CRISIS ASIÁTICA DE 1997 CAMBIÓ TODO

ANTES DE LA CRISIS (1990-1997):
- "Milagros asiáticos": Corea, Tailandia, Indonesia, Malasia
- Crecían 7-10% anual
- PERO: déficits de cuenta corriente del 5-8% del PIB
- Financiados con deuda externa de corto plazo
- Tipos de cambio fijos (anclados al dólar)

LA CRISIS (1997-1998):
- Comienza en Tailandia (julio 1997): el baht colapsa
- Contagio a Indonesia, Corea, Malasia, Filipinas
- Fuga de capitales masiva
- Devaluaciones del 50-80%
- Recesiones del 5-15%
- FMI interviene con condiciones duras

DESPUÉS DE LA CRISIS (1999-hoy):
- Conclusión de los países: "Nunca más depender del FMI"
- Política de ACUMULACIÓN DE RESERVAS
- Tipos de cambio más flexibles
- Superávits de cuenta corriente
- "Self-insurance" contra crisis futuras

DATOS DE RESERVAS:
- China: US$ 3 trillones
- Japón: US$ 1.2 trillones
- Corea: US$ 400.000 millones
- India: US$ 600.000 millones

CONSECUENCIA GLOBAL:
Asia pasa de DEMANDAR capital a PROVEER capital.
Financia los déficits de EEUU y Europa.
Es un cambio estructural en la economía mundial.

PREGUNTA: "¿Qué costos tiene acumular tantas reservas?"
RESPUESTA: Costo de oportunidad (podrían invertir en infraestructura, educación). Pero el "seguro" contra crisis vale la pena para ellos.""",

    37: """TRANSICIÓN AL CASO ARGENTINO (3 minutos)

AHORA APLICAMOS TODO AL CASO QUE CONOCEMOS

Argentina es un "laboratorio" de crisis de balanza de pagos:
- 1975: Rodrigazo
- 1982: Crisis de deuda
- 1989: Hiperinflación
- 2001: Fin de la convertibilidad
- 2018: Crisis y vuelta al FMI
- 2023-24: Nuevo episodio

PREGUNTA CENTRAL: "¿Por qué Argentina repite el mismo patrón cada 10-15 años?"

HIPÓTESIS QUE VAMOS A EXPLORAR:
1. Es un problema de TIPO DE CAMBIO (se aprecia hasta que explota)
2. Es un problema de AHORRO (bajo ahorro + déficit fiscal)
3. Es un problema de ESTRUCTURA PRODUCTIVA (dependencia de commodities)
4. Es un problema de INSTITUCIONES (políticas inconsistentes)

Spoiler: Probablemente sea una combinación de todos.""",

    38: """EL CICLO ARGENTINO (15 minutos)

ESTE PATRÓN SE REPITE SISTEMÁTICAMENTE

FASE 1 - APRECIACIÓN:
- El tipo de cambio se atrasa (por inflación > devaluación, o TC fijo)
- Todo parece bien: el dólar está "barato", viajes al exterior, importaciones fáciles
- La gente se siente "rica"

FASE 2 - DÉFICIT CRECIENTE:
- Importaciones suben (están baratas)
- Exportaciones estancadas o caen (no somos competitivos)
- Déficit de cuenta corriente crece
- Pero "alguien" financia: deuda o entrada de capitales

FASE 3 - FINANCIAMIENTO:
- Mientras haya financiamiento, el ciclo continúa
- Puede ser: inversión extranjera, endeudamiento público, préstamos del FMI
- El nivel de reservas parece estable (pero la deuda crece)

FASE 4 - SUDDEN STOP:
- Los inversores se ponen nerviosos
- Los capitales empiezan a salir ("fuga")
- Las reservas caen rápido
- El BCRA defiende el tipo de cambio vendiendo reservas

FASE 5 - CRISIS Y DEVALUACIÓN:
- Las reservas se agotan (o el FMI no da más plata)
- Devaluación abrupta
- Inflación
- Recesión
- Default (a veces)

FASE 6 - RECUPERACIÓN:
- Con el tipo de cambio competitivo, las exportaciones repuntan
- La recesión reduce importaciones
- Superávit de cuenta corriente
- La economía se recupera
- ...hasta que vuelve a empezar

EJERCICIO: Identificar en qué fase estaba Argentina en 1999, 2008, 2017, 2023.""",

    39: """GRÁFICO: TIPO DE CAMBIO REAL ARGENTINA (12 minutos)

LECTURA DEL GRÁFICO - ITCRM (Índice de Tipo de Cambio Real Multilateral):

EJE Y: Índice (diciembre 2001 = 100 es una referencia común, o promedio histórico)
EJE X: Años

IDENTIFICAR LOS CICLOS:

1997-2001 - APRECIACIÓN EN CONVERTIBILIDAD:
- TC nominal fijo (1 peso = 1 dólar)
- Inflación argentina > inflación EEUU
- Resultado: apreciación real sostenida
- El ITCRM cayó ~30%
- Argentina se volvió "cara" en dólares

2002 - EL SALTO:
- Devaluación del 200% (de 1 a 3 pesos por dólar)
- Inflación del 40% (pero menos que la devaluación)
- Resultado: depreciación real del 150%
- Argentina se volvió "barata" en dólares

2003-2008 - ESTABILIDAD COMPETITIVA:
- TC real se mantuvo competitivo
- Superávit comercial y de cuenta corriente
- Acumulación de reservas
- Crecimiento económico alto

2008-2017 - APRECIACIÓN GRADUAL:
- Inflación creciente (20-40% anual)
- Tipo de cambio nominal subía menos
- Apreciación real gradual
- Vuelve el déficit de CC

2018 - CRISIS:
- Corrida cambiaria
- Devaluación del 100%
- Vuelta al FMI
- Pero inflación alta redujo el efecto real

2020-2024 - VOLATILIDAD:
- Múltiples tipos de cambio
- Brecha cambiaria
- Difícil medir el TC real "verdadero"

FRASE PARA RECORDAR: 'El tipo de cambio en Argentina sube por escalera y baja por ascensor.'""",

    40: """GRÁFICO: CUENTA CORRIENTE ARGENTINA (10 minutos)

LECTURA DEL GRÁFICO:

EJE Y: Cuenta corriente como % del PIB
EJE X: Años (1990-2024)

CORRELACIÓN CON EL TIPO DE CAMBIO:

1992-2001 - DÉFICIT PERSISTENTE:
- Promedio: -3% a -4% del PIB
- Máximo déficit: -5% en 1998
- Coincide con: apreciación real (convertibilidad)
- Financiamiento: deuda externa, privatizaciones, inversión extranjera

2002-2008 - SUPERÁVIT RÉCORD:
- Promedio: +2% a +3% del PIB
- Máximo superávit: +4% en 2002
- Coincide con: depreciación real (post-crisis)
- Resultado: acumulación de reservas, desendeudamiento

2010-2017 - VUELTA AL DÉFICIT:
- Gradual deterioro
- Déficit creciente hasta -5% en 2017
- Coincide con: apreciación real gradual
- Financiamiento: reservas, deuda, FMI

2020-2022 - SUPERÁVIT EXCEPCIONAL:
- Pandemia redujo importaciones
- Boom de commodities (ToT favorables)
- Superávit de +1% a +2%
- Pero con múltiples TC y cepo

MENSAJE: La cuenta corriente de Argentina es PROCÍCLICA con el tipo de cambio real.
- Peso caro → déficit
- Peso barato → superávit

PREGUNTA: "¿Por qué el mercado no ajusta automáticamente? Si hay déficit, debería haber presión para devaluar..."

RESPUESTA: Porque el gobierno interviene (controles de cambio, cepo, uso de reservas). El ajuste se retrasa hasta que es forzado por una crisis.""",

    41: """GRÁFICO: RESERVAS INTERNACIONALES ARGENTINA (10 minutos)

LECTURA DEL GRÁFICO:

EJE Y: Reservas en miles de millones de dólares
EJE X: Años

LAS RESERVAS SON EL "TERMÓMETRO" DE LAS CRISIS:

PUNTO MÍNIMO 2002: ~US$ 10.500 millones
- Crisis de convertibilidad
- Default de deuda
- Corrida bancaria
- El país casi se queda sin reservas

ACUMULACIÓN 2003-2011: Suben a US$ 52.000 millones
- Superávit comercial
- Precios de commodities altos
- BCRA compraba dólares del superávit
- "Blindaje" contra crisis

CAÍDA 2011-2015: Bajan a US$ 25.000 millones
- Déficit de CC creciente
- Fuga de capitales
- BCRA vendía para sostener el TC
- Controles de cambio ("cepo")

PRÉSTAMO FMI 2018: Suben a US$ 66.000 millones
- Préstamo récord del FMI (US$ 57.000 millones)
- Pero se usaron para financiar fuga
- No sirvieron para estabilizar

CAÍDA POSTERIOR: Bajan a ~US$ 23.000 millones
- Agotamiento del préstamo
- Nuevo cepo
- Reservas netas negativas (si descontamos encajes y swaps)

LECCIÓN: Las reservas no son infinitas. Cuando se agotan, el ajuste es forzoso y doloroso.

PREGUNTA: "¿Cuántas reservas debería tener Argentina para estar 'segura'?"

REGLA PRÁCTICA: 3-4 meses de importaciones como mínimo. Pero depende de la deuda en dólares y la confianza.""",

    42: """LA CONVERTIBILIDAD COMO CASO DE ESTUDIO (15 minutos)

LA CONVERTIBILIDAD (1991-2001) ES UN EXPERIMENTO DE LIBRO DE TEXTO

EL DISEÑO:
- TC fijo extremo: 1 peso = 1 dólar por ley
- Base monetaria respaldada por reservas
- Prohibido emitir sin respaldo
- Objetivo: terminar con la inflación

BENEFICIOS INICIALES (1991-1994):
- Inflación: de 5000% (1989) a 4% (1994)
- Credibilidad: inversión extranjera, crédito
- Crecimiento: promedio 6% anual
- "El milagro argentino"

PROBLEMAS ACUMULADOS (1995-2001):
- Sin posibilidad de devaluar, toda la competitividad se perdía
- Inflación argentina > inflación EEUU → apreciación real
- Exportaciones estancadas, importaciones crecientes
- Déficit de CC creciente (-4% a -5% del PIB)
- Desempleo: de 6% a 18%
- Deuda externa: se triplicó

¿POR QUÉ NO AJUSTABA?
- En teoría, con TC fijo, el ajuste viene por DEFLACIÓN (caen los precios)
- Pero los precios y salarios son "rígidos a la baja"
- El ajuste vino por CANTIDAD: desempleo, recesión

EL COLAPSO (2001-2002):
- Fuga de capitales acelerada
- "Corralito" bancario
- Default de deuda (US$ 100.000 millones)
- Devaluación 200%
- Caída del PIB: -11%
- Desempleo: 25%

LECCIÓN: "Un tipo de cambio fijo sin flexibilidad acumula desequilibrios hasta que explota. El ajuste postergado es ajuste magnificado."

PREGUNTA CONTRAFACTUAL: "¿Qué hubiera pasado si Argentina hubiera salido de la convertibilidad en 1997, antes de la crisis?"

RESPUESTA: Imposible saberlo, pero probablemente hubiera sido menos traumático.""",

    43: """TRANSICIÓN AL CIERRE (1 minuto)

ESTAMOS LLEGANDO AL FINAL DE LAS CLASES 1+2

En estas 4 horas vimos:
- 9 indicadores para analizar el sector externo
- Historia del comercio (1500-1945) - faltan etapas 4 y 5
- Desequilibrios globales contemporáneos
- El caso argentino en profundidad

AHORA: Resumen y próximos pasos""",

    44: """RESUMEN: 9 INDICADORES (5 minutos)

REPASAR RÁPIDAMENTE CADA UNO:

BLOQUE HISTÓRICO-COMERCIAL:
1. ÍNDICE DE COMERCIO: Mide el nivel general (año base = 100)
2. PARTICIPACIÓN REGIONAL: Quién gana/pierde peso en el comercio mundial
3. HHI: Concentración (si pocos países dominan o está disperso)
4. COBERTURA: Calidad de los datos
5. BALANZA COMERCIAL: X - M (superávit o déficit)
6. APERTURA: (X+M)/PIB (qué tan integrado está un país)
7. TÉRMINOS DEL INTERCAMBIO: Px/Pm (precio de lo que exportamos vs importamos)

BLOQUE MACROECONÓMICO:
8. CUENTA CORRIENTE: CC/PIB (ahorro menos inversión)
9. TIPO DE CAMBIO REAL: E × P*/P (competitividad)

MENSAJE: Con estos 9 indicadores pueden analizar la inserción externa de CUALQUIER país. Úsenlos como checklist:
- ¿Cómo está el comercio?
- ¿Quién gana/pierde participación?
- ¿Hay déficit o superávit?
- ¿El TC está caro o barato?
- ¿Mejoran o empeoran los ToT?""",

    45: """RESUMEN: HECHOS ESTILIZADOS (5 minutos)

LAS GRANDES LECCIONES:

1. EL COMERCIO NO CRECE LINEALMENTE
- Creció 40 veces (1800-1913)
- Colapsó (1914-1945)
- Volvió a crecer (1945-2008)
- Ahora está en tensión

2. LA GLOBALIZACIÓN REQUIERE HEGEMONÍA
- Siglo XIX: Gran Bretaña
- Siglo XX-XXI: Estados Unidos
- ¿Futuro?: ¿EEUU vs China? ¿Fragmentación?

3. SIN REGLAS ESTABLES, EL SISTEMA SE FRAGMENTA
- 1930s: bloques comerciales, proteccionismo
- ¿2020s?: ¿nearshoring, decoupling?

4. LOS DESEQUILIBRIOS GLOBALES REFLEJAN ASIMETRÍAS ESTRUCTURALES
- EEUU: déficit por rol del dólar
- China/Alemania: superávit por modelo exportador
- No se ajustan automáticamente

5. ARGENTINA REPITE UN CICLO
- Apreciación → déficit → crisis → devaluación → recuperación → ...
- ¿Es evitable? Requiere políticas consistentes y sostenibles

MARCO PARA RECORDAR: TECNOLOGÍA + REGLAS + PODER""",

    46: """PRÓXIMA CLASE (3 minutos)

CLASE 3: TEORÍAS DEL COMERCIO - MERCANTILISTAS Y SMITH

¿QUÉ VAMOS A VER?
- ¿Por qué comercian los países?
- Los MERCANTILISTAS: comercio como guerra, acumulación de oro
- ADAM SMITH: ventajas absolutas, crítica al mercantilismo
- El debate que sigue vigente (¿Trump es mercantilista?)

CONEXIÓN CON LO QUE VIMOS:
- Pasamos de DESCRIPCIÓN (indicadores, hechos) a EXPLICACIÓN (teorías)
- Los indicadores nos dicen QUÉ pasa
- Las teorías intentan explicar POR QUÉ

LECTURA SUGERIDA:
- Lugones, capítulo 1 (o lo que indique el programa)
- Alternativa: Adam Smith, "La Riqueza de las Naciones", Libro IV (fragmentos)

PREGUNTA PARA PENSAR:
"Si el comercio beneficia a todos, ¿por qué los países ponen aranceles?"

Esta pregunta conecta mercantilistas (proteccionismo) con Smith (libre comercio).""",

    47: """CIERRE - PREGUNTAS (5-10 minutos)

ABRIR ESPACIO PARA PREGUNTAS

PREGUNTAS FRECUENTES:

P: "¿Cómo consigo los datos para calcular estos indicadores?"
R: INDEC, BCRA, FMI WEO, Banco Mundial WDI, UNCTAD. Les paso links.

P: "¿Cómo es el parcial/final?"
R: Según el programa. Típicamente: análisis de caso aplicando indicadores.

P: "¿Hay algún libro de texto?"
R: Krugman-Obstfeld es el estándar. Lugones para perspectiva latinoamericana.

P: "¿Qué va a pasar con el dólar en Argentina?"
R: No soy futurólogo, pero ahora tienen herramientas para analizar la situación.

SI NO HAY PREGUNTAS:

Recapitular los 3 puntos más importantes:
1. El comercio internacional no es automático ni natural - requiere condiciones
2. Argentina tiene un patrón recurrente que pueden analizar con estos indicadores
3. Las teorías que veremos intentan explicar por qué los países comercian (y por qué a veces no)

DESPEDIDA:
"Nos vemos la próxima clase. Traigan preguntas sobre los mercantilistas y Smith."
"""
}


def main():
    # Leer JSON existente
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Actualizar notas_docente
    actualizados = 0
    for slide in data['slides']:
        numero = slide['numero']
        if numero in NOTAS_EXPANDIDAS:
            slide['notas_docente'] = NOTAS_EXPANDIDAS[numero]
            actualizados += 1

    # Guardar
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Notas docente expandidas: {actualizados} de {len(data['slides'])} slides")

    # Mostrar longitud promedio de notas
    longitudes = [len(s.get('notas_docente', '')) for s in data['slides']]
    promedio = sum(longitudes) / len(longitudes)
    print(f"Longitud promedio de notas: {promedio:.0f} caracteres")
    print(f"Nota más larga: {max(longitudes)} caracteres")
    print(f"Nota más corta: {min(longitudes)} caracteres")


if __name__ == "__main__":
    main()
