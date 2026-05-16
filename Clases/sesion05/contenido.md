# Clase 5: ¿Quién comercia, cómo y a qué precio?

## Metadata
- **Duración**: 4 horas
- **Pregunta central**: ¿Qué determina el IIT? ¿Dónde se produce? ¿Quién exporta? ¿A qué precio? ¿Qué se comercia realmente?
- **Unidad**: 3 — Nuevas teorías del comercio, comercio intraindustrial, dumping y firmas heterogéneas (cierra U3)

## Estado
Listo

## Para hacer
- [x] Investigar bibliografía Vernon y Melitz
- [x] Descargar papers (Vernon 1966, Melitz 2003, Grossman & Rossi-Hansberg 2008, Acemoglu & Autor 2011)
- [x] Extraer contenido de Clase 8.docx y Clase 9.docx
- [x] Definir agenda (aprobada por usuario)
- [x] Escribir contenido.md completo
- [x] Gráficos (7 PNGs)
- [x] Copiar generar_desde_md.py, cambiar footer
- [x] Generar HTML (30 slides)
- [x] Verificar en navegador
- [x] Reestructura narrativa: eliminar bloques, flujo continuo

---

## Contenido

### Sección: Apertura

#### Slide 1: Portada
**Tipo**: portada
**Título**: Economía Internacional — Clase 5
**Subtítulo**: ¿Quién comercia, cómo y a qué precio?
**Fecha**: 14 de mayo de 2026

**Notas docente**:
APERTURA (2 minutos)
"Hoy cerramos la Unidad 3. En la Clase 4 armamos el marco de Krugman: competencia monopolística, comercio intraindustrial, Grubel-Lloyd. Pero nos quedaron preguntas abiertas. Hoy las respondemos una por una, y van a ver que cada respuesta lleva naturalmente a la siguiente."

---

#### Slide 2: ¿Qué preguntas nos dejó la Clase 4?
**Tipo**: texto
**Título**: Lo que sabemos... y lo que falta
**Subtítulo**: Clase 4 nos dio el marco. Hoy lo completamos.

**Contenido**:
- **Lo que sabemos** (Clase 4 — Krugman):
  - Economías de escala + diferenciación → comercio intraindustrial entre países similares
  - El índice GL mide cuánto IIT hay ($GL = 0$ interindustrial, $GL = 1$ intraindustrial)
  - IIT horizontal (variedades) vs vertical (calidad). NGE y concentración territorial
- **Lo que falta** — las preguntas de hoy:
  - ¿Qué **determina** que el IIT sea alto o bajo entre dos países?
  - ¿**Dónde** se produce un bien a lo largo de su vida?
  - ¿Por qué solo **algunas** firmas exportan y la mayoría no?
  - Cuando una firma exporta más barato de lo que vende en casa... ¿eso es **dumping**?

**Notas docente**:
REPASO Y PREGUNTAS (3 minutos)
"Repaso rápido de la clase pasada. Krugman nos explicó POR QUÉ hay comercio entre países similares: economías de escala internas y diferenciación de productos. Medimos ese comercio con el GL. Y vimos cómo esas mismas fuerzas generan concentración territorial (NGE)."

"Pero el modelo de Krugman deja preguntas abiertas. Cuatro preguntas, exactamente, que son las que vamos a responder hoy. Y lo interesante es que la respuesta a cada una nos lleva a la siguiente. Arranquemos por la primera."

---

#### Slide 3: Agenda
**Tipo**: agenda
**Título**: Cinco bloques, una historia

**Contenido**:
- **Bloque 1 — ¿Qué determina el IIT?**: por qué es alto entre ARG-BRA y bajo entre ARG-Nigeria
- **Bloque 2 — ¿Dónde se produce?**: Vernon — el producto viaja del innovador al imitador
- **Bloque 3 — ¿Quién exporta?**: Melitz — no todas las firmas son iguales, solo las mejores exportan
- *Recreo*
- **Bloque 4 — ¿Cuándo es dumping?**: precio "demasiado bajo" + defensa comercial (AD, CVD, salvaguardia)
- **Bloque 5 — Comercio de tareas**: del comercio de bienes a la fragmentación productiva (anticipa U5)
- **Cierre**: síntesis U3, evaluación, lecturas

**Notas docente**:
AGENDA (2 minutos)
"Son 4 horas organizadas en cinco bloques. Cada bloque cierra con una pregunta abierta que dispara el siguiente — la idea es que se vea la lógica encadenada, no slides sueltos."

"Bloque 1: arrancamos con los determinantes del IIT y un caso empírico (ARG-BRA en autos). Bloque 2: eso nos lleva a preguntarnos dónde se produce cada cosa — Vernon y el ciclo del producto. Bloque 3: de ahí pasamos a quién exporta — Melitz y las firmas heterogéneas. Después del recreo, Bloque 4: a qué precio — dumping y defensa comercial. Bloque 5 — y cerramos con una idea que cambia toda la discusión: quizás no se comercian bienes, se comercian tareas."

"Si al final de la clase pueden leer una noticia sobre antidumping o sobre una empresa que decide exportar y decir 'esto se entiende con lo que vimos', la clase está lograda."

---

### Sección: Bloque 1 — ¿Qué determina el IIT?

#### Slide 4: Bloque 1 — ¿Qué determina el IIT?
**Tipo**: seccion
**Título**: Bloque 1 — ¿Qué determina el IIT?
**Subtítulo**: Krugman explica por qué hay IIT, pero no explica cuánto

**Notas docente**:
APERTURA DE BLOQUE 1 (1 minuto)
"Empezamos por la primera pregunta: el modelo de Krugman explicó por qué hay comercio intraindustrial — pero no explicó qué tan alto va a ser. ¿Por qué Argentina y Brasil tienen GL = 0,92 en autos pero solo 0,15 con China en electrónica? Hay determinantes específicos. Vamos a verlos."

---
#### Slide 5: ¿Qué determina el nivel de IIT?
**Tipo**: texto
**Título**: Determinantes del comercio intraindustrial
**Subtítulo**: ¿Por qué el IIT es alto entre algunos países y bajo entre otros?
**Layout**: dos-columnas

**Contenido**:
- **Similitud de ingreso per cápita**:
  - Consumidores con gustos parecidos demandan variedades comparables → más IIT horizontal
- **Proximidad geográfica / integración**:
  - Menores costos de transporte → más comercio de "ida y vuelta" viable
- **Tamaño de mercado / escala**:
  - Mercados grandes permiten más variedades con costos medios más bajos
- **Participación de manufacturas**:
  - IIT es alto en bienes diferenciados, bajo en commodities
- **Cadenas de valor / comercio de partes**:
  - Fragmentación productiva → IIT con rasgos verticales
- Idea fuerza: ***IIT crece con integración + escala + demanda de variedad***

**Notas docente**:
DETERMINANTES DEL IIT (8 minutos)
"Primera pregunta: ¿qué determina que el IIT sea alto o bajo? En la Clase 4 vimos que el GL varía mucho: UE ~0.64, Mercosur ~0.35, Mercosur autos ~0.75. ¿Por qué esas diferencias?"

1. Similitud de ingreso: "Países con PBI per cápita parecido tienen estructuras de demanda parecidas. Alemanes y franceses quieren autos similares pero distintos. Si comercian entre sí, es ida y vuelta de variedades: IIT horizontal alto."

2. Proximidad: "El costo de transporte mata el comercio de ida y vuelta. Si es caro mover el bien, no tiene sentido exportar e importar al mismo tiempo. Por eso el IIT es más alto entre vecinos: UE, NAFTA, Mercosur."

3. Escala: "Un mercado grande puede sostener más variedades. El mercado integrado UE (450 millones de consumidores) permite muchas más variedades que un mercado de 45 millones."

4. Manufacturas: "El IIT es un fenómeno de bienes diferenciados. En commodities (soja, petróleo, minerales), el GL tiende a 0. En manufacturas sofisticadas (autos, químicos, farmacéuticos), el GL puede superar 0.8."

5. Cadenas de valor: "La fragmentación de la producción genera comercio de partes y componentes que cruzan fronteras varias veces. Esto aumenta el IIT, muchas veces con rasgos verticales (partes de distinto nivel de complejidad)."

PREGUNTA PARA ESTUDIANTES: "Si Argentina firmara un TLC con la UE, ¿esperarían que el IIT aumente? ¿En qué sectores?"
(Respuesta: probablemente en manufactura automotriz, químicos, alimentos procesados. En commodities agrícolas, no: seguiría siendo interindustrial.)

"Veamos estos determinantes en acción con un caso concreto."

---

#### Slide 6: Argentina-Brasil: todos los determinantes en acción
**Tipo**: grafico_texto
**Título**: Argentina-Brasil: el IIT más alto de la región
**Gráfico**: graficos/arg_bra_autos_2024.png
**Fuente**: OEC / UN Comtrade, HS 87 (Vehículos), 2024

**Contenido**:
- **En el gráfico**: dos barras casi iguales — exportaciones (azul, USD 6.000 M) e importaciones (naranja, USD 5.110 M)
  - Diferencia neta: solo USD 890 M (8% del total) → **GL ≈ 0,92** (callout verde)
- **¿Por qué tan alto?** Todos los determinantes operan juntos:
  - **Proximidad** geográfica + **integración** institucional (PAM/Mercosur)
  - **Mercado ampliado** (45M + 215M = 260M consumidores)
  - **Cadenas intrafirma** (Toyota, VW, Stellantis con plantas en ambos países)
- **Tipo de IIT**: horizontal (modelos/variedades) + vertical (autopartes de distinta complejidad)

**Notas docente**:
CASO ARG-BRA (7 minutos)
"Vamos a ver los datos concretos. En el sector de vehículos (HS 87), Argentina y Brasil tienen un GL de 0,92. Es altísimo — casi todo el comercio es intraindustrial."

"¿Cómo lo leemos? De cada 100 dólares que se mueven entre ARG y BRA en autos y autopartes, 92 son ida y vuelta. Solo 8 son 'netos' (un flujo unidireccional)."

"¿Por qué tan alto? Porque operan TODOS los determinantes que vimos: proximidad geográfica (compartimos frontera), integración institucional (el PAM/Mercosur con coeficiente flex), mercado ampliado (45M + 215M = 260M de consumidores potenciales), y cadenas intrafirma (Toyota, VW, Fiat/Stellantis tienen plantas en ambos países y dividen producción de modelos)."

DATO ADICIONAL: "El coeficiente flex del PAM garantiza equilibrio: por cada dólar que importo del otro, tengo que exportar una proporción. Esto fuerza el 'ida y vuelta' y eleva artificialmente el GL. Sin ese régimen, probablemente el comercio sería más asimétrico."

PREGUNTA PARA ESTUDIANTES: "Si se eliminara el PAM y se abriera el mercado sin restricciones, ¿qué pasaría con el GL? ¿Subiría o bajaría?"
(Respuesta: probablemente bajaría, porque sin el flex, Brasil podría dominar por escala. El IIT alto es parcialmente un resultado del diseño institucional.)

TRANSICIÓN: "Fíjense en un detalle del caso: Toyota tiene la planta de Hilux en Zárate y la de Corolla en San Pablo. ¿Por qué produce una cosa acá y otra allá? ¿Por qué la producción se MUEVE geográficamente? Esta es nuestra segunda pregunta, y la respondió un economista en 1966."

---

### Sección: Bloque 2 — ¿Dónde se produce el bien?

#### Slide 7: Bloque 2 — ¿Dónde se produce a lo largo de su vida?
**Tipo**: seccion
**Título**: Bloque 2 — ¿Dónde se produce a lo largo de su vida?
**Subtítulo**: Toyota fabrica Hilux en Zárate Y Corolla en San Pablo: ¿por qué se mueve la producción?

**Notas docente**:
APERTURA DE BLOQUE 2 (1 minuto)
"Cerramos el primero: el IIT alto entre Argentina y Brasil en autos se explica por todos los determinantes operando juntos. Pero les dejé un detalle pendiente: Toyota tiene la planta de Hilux en Zárate y la de Corolla en San Pablo. ¿Por qué produce una cosa acá y otra allá? ¿Por qué la producción se MUEVE geográficamente? La respuesta la dio Raymond Vernon en 1966."

---
#### Slide 8: Raymond Vernon — El economista de las multinacionales
**Tipo**: texto
**Título**: Raymond Vernon (1913-1999)
**Subtítulo**: Harvard Business School — Comercio, inversión y multinacionales

**Contenido**:
- **Quién fue**: economista estadounidense, profesor en Harvard Business School
  - Asesor del Plan Marshall (posguerra) y del Departamento de Estado
- **Paper clave**: *"International Investment and International Trade in the Product Cycle"* (1966, QJE)
- **Observación central**: las multinacionales no solo comercian bienes, también **mueven la producción**
  - Rompió con la tradición: el patrón de comercio **cambia** con el tiempo, no es estático
- **Cita**: *"La localización de la producción no es un dato fijo: es una función del ciclo de vida del producto"*

**Notas docente**:
BIOGRAFÍA VERNON (4 minutos)
"Raymond Vernon fue un caso particular: no era un teórico puro, sino alguien con mucha experiencia práctica. Trabajó en el gobierno de EEUU durante la posguerra (Plan Marshall), donde vio de primera mano cómo las empresas estadounidenses se expandían al exterior."

"Su gran contribución fue conectar comercio internacional con inversión extranjera directa. Los modelos previos (Ricardo, H-O, Krugman) trataban el comercio como si los factores de producción fueran inmóviles. Vernon dijo: las empresas no solo exportan, también MUDAN su producción."

"El paper es de 1966 y reflejaba la realidad de su época: EEUU era el gran innovador, Europa y Japón eran imitadores/adoptantes. Hoy la realidad es más compleja, pero la lógica del ciclo del producto sigue siendo útil."

ANÉCDOTA: Vernon dirigió el famoso 'New York Metropolitan Region Study' en los años 50, que estudió por qué ciertas industrias se iban de Manhattan a los suburbios. Esa misma lógica de relocalización la aplicó después al comercio internacional.

---

#### Slide 9: El ciclo del producto — Tres fases
**Tipo**: grafico_texto
**Título**: El producto viaja: innovación → maduración → estandarización
**Gráfico**: graficos/vernon_ciclo_producto.png
**Fuente**: Basado en Vernon (1966), adaptación propia

**Contenido**:
- **En el gráfico**: tres fases de izquierda a derecha siguiendo el eje del **tiempo**
  - Cada caja indica dónde se produce (abajo) y qué caracteriza la fase (adentro)
- **Fase 1 — Producto nuevo** (azul, EEUU):
  - Requiere I+D, mano de obra calificada, cercanía al mercado. Se exporta a países ricos
- **Fase 2 — Producto maduro** (naranja, Europa/Japón):
  - La demanda crece afuera. Las firmas invierten allá (IED). El innovador empieza a importar
- **Fase 3 — Estandarizado** (rojo, países en desarrollo):
  - Producción migra a países de bajos costos. El bien se vuelve commodity. El innovador importa lo que inventó

**Notas docente**:
EL CICLO DEL PRODUCTO (10 minutos)
"Esta es la idea central de Vernon. Un producto pasa por tres fases, y en cada fase la producción se mueve geográficamente."

Fase 1 — Producto nuevo (innovación): "Pensemos en los semiconductores en los años 60, los PCs en los 80, los smartphones en los 2000. Al principio, solo se producen en EEUU (o el país innovador). ¿Por qué? Porque necesitás cercanía a centros de I+D, trabajadores calificados, clientes sofisticados que te den feedback, y la incertidumbre es alta — necesitás flexibilidad, no escala. Las exportaciones van a otros países ricos que demandan el producto."

Fase 2 — Producto maduro: "La demanda crece en Europa y Japón. El producto se estandariza parcialmente. Los costos de producción empiezan a importar más que la innovación. Las empresas americanas (o quienes sean los innovadores) empiezan a instalar plantas en esos mercados: IED horizontal. Es más barato producir cerca del cliente que exportar. EEUU empieza a importar desde sus propias filiales."

Fase 3 — Estandarizado: "El producto ya no tiene secreto tecnológico. La producción migra a donde los costos son más bajos: primero Japón, después los Tigres Asiáticos, después China. El innovador ahora importa el producto que él mismo inventó. El bien se convirtió en commodity."

"¿Ven la lógica? La ventaja comparativa NO es estática. Lo que hoy es innovación de punta, mañana es commodity. La localización de la producción sigue al producto a lo largo de su vida."

EJEMPLO EN PIZARRÓN: "Textiles: Inglaterra los inventó (revolución industrial) → se estandarizaron → migraron a Asia → hoy Bangladesh es el mayor exportador del mundo. El ciclo tomó 200 años."

"Electrónica de consumo: inventada en EEUU → producida en Japón (años 70-80) → Corea/Taiwán (90s) → China (2000s). El ciclo se acortó a 30-40 años."

---

#### Slide 10: Vernon hoy — ¿Sigue vigente?
**Tipo**: texto
**Título**: Crítica y actualización del modelo de Vernon
**Subtítulo**: Útil pero incompleto
**Layout**: dos-columnas

**Contenido**:
- **Lo que sigue vigente**:
  - La producción se mueve geográficamente con el tiempo
  - La conexión entre comercio e IED
- **Lo que cambió**:
  - Ya no hay un único país innovador (China, Corea, India innovan)
  - Los ciclos se acortaron dramáticamente (de décadas a años)
  - Las CGV fragmentan la producción: un producto puede estar en las 3 fases *simultáneamente*
  - La innovación puede ocurrir en países de "bajos costos" (apps en India, drones en China)
- **Lugones**: *"El esquema no se corresponde con la realidad actual"* — pero valora la ruptura con el enfoque estático
- **La pregunta que queda**: Vernon pensó en **productos** que viajan. Pero ¿quién decide mover la producción? Las **firmas**. Y no todas son iguales...

**Notas docente**:
CRÍTICA Y ACTUALIZACIÓN (5 minutos)
"Vernon escribió en 1966. En ese momento, EEUU era el innovador dominante y el modelo reflejaba bien la realidad. Hoy hay varias cosas que cambiaron."

"Primero: ya no hay un único polo innovador. China diseña y produce tecnología de punta (Huawei, BYD, DJI). India desarrolla software. Corea domina semiconductores. El modelo asumía un flujo unidireccional: de EEUU al mundo. Hoy es multidireccional."

"Segundo: los ciclos se acortaron brutalmente. El iPhone pasó de innovación a commodity en 15 años. Los textiles tardaron 200. Esto comprime las tres fases."

"Tercero: las cadenas globales de valor (que vamos a ver en la Unidad 5) fragmentaron la producción. Un iPhone tiene diseño en California, componentes de Japón/Corea/Taiwán, ensamblaje en China. No es que 'todo el producto' migra: partes están en fase 1, partes en fase 3, simultáneamente."

PREGUNTA PARA ESTUDIANTES: "¿Pueden pensar en un producto que HOY esté en fase 1 de Vernon (innovación, concentrado en un país)?"
(Respuestas posibles: chips de IA/GPU (Nvidia, EEUU/Taiwán), vehículos eléctricos de alta gama, terapias génicas)

TRANSICIÓN: "Vernon nos mostró que la producción se mueve. Pero él pensó en productos — el 'producto' viaja del innovador al imitador. La decisión de mover la producción la toman las FIRMAS. Y acá viene algo que rompe todo lo que asumimos hasta ahora: resulta que las firmas dentro de un mismo sector son MUY distintas entre sí. Tan distintas que la mayoría ni siquiera exporta."

---

#### Slide 11: Un dato que rompe la intuición
**Tipo**: centrado
**Título**: Si el comercio es tan beneficioso... ¿por qué tan pocas firmas exportan?

**Contenido**:
- **El dato**: en EEUU, solo el **18%** de las empresas manufactureras exporta (2002)
- **Las exportadoras son muy diferentes** del resto:
  - **2 veces más grandes** que las no exportadoras
  - Producen **11% más de valor añadido** por trabajador
  - Pagan **mejores salarios**
- Este patrón se repite en **todos los países** estudiados (Europa, América Latina, Asia)
- ***Si el comercio es tan beneficioso... ¿por qué el 82% no participa?***

**Notas docente**:
EL HECHO ESTILIZADO (5 minutos)
"Arranquemos con un dato que rompe la intuición. En EEUU, en un año típico, solo el 18% de las empresas manufactureras reporta alguna exportación. 82 de cada 100 no exporta nada."

Tabla 8.3 de Krugman (para mencionar en clase):
- Imprenta: 5% exporta
- Muebles: 7%
- Ropa: 8%
- Productos metálicos: 14%
- Petróleo/carbón: 18%
- Equipos de transporte: 28%
- Química: 36%
- Informática y electrónica: 38%

"Y no es que las exportadoras sean iguales a las demás. Son MUY distintas: el doble de grandes, 11% más productivas, pagan mejores salarios. La exportación no es algo que haga 'cualquier' empresa: es algo que hacen las mejores."

"Este patrón se repite en todos lados. Bernard, Jensen, Redding y Schott (2007) documentaron esto para EEUU. Mayer y Ottaviano (2008) lo confirmaron para Europa. En Argentina, los estudios muestran lo mismo: un puñado de firmas concentra la mayor parte de las exportaciones."

PREGUNTA PARA ESTUDIANTES: "¿Por qué creen que la mayoría de las empresas no exporta? ¿Qué les impide hacerlo?"
(Respuestas esperadas: costos, burocracia, no conocen el mercado, no tienen escala, etc. Conducir hacia la idea de costos fijos de exportación.)

"Hasta 2003, la teoría del comercio no podía explicar este dato. Ni Ricardo, ni H-O, ni Krugman. En todos esos modelos, las firmas dentro de un sector eran idénticas. ¿Quién lo resolvió?"

---

### Sección: Bloque 3 — ¿Quién exporta y quién no?

#### Slide 12: Bloque 3 — ¿Quién exporta y quién no?
**Tipo**: seccion
**Título**: Bloque 3 — ¿Quién exporta y quién no?
**Subtítulo**: Si solo el 18% de las firmas exporta, ¿qué tienen de especial las que sí?

**Notas docente**:
APERTURA DE BLOQUE 3 (1 minuto)
"Vernon nos mostró que la producción se mueve. Pero él pensó en productos. Las decisiones reales las toman las firmas. Y acá viene algo que rompe todo lo que asumimos hasta ahora: las firmas dentro de un mismo sector no son iguales. La mayoría ni siquiera exporta. Si el comercio es tan beneficioso como dicen Ricardo, H-O y Krugman... ¿por qué solo el 18% participa? Esta pregunta la respondió Marc Melitz en 2003."

---
#### Slide 13: Marc Melitz — El teórico de las firmas que exportan
**Tipo**: texto
**Título**: Marc Melitz (1968-)
**Subtítulo**: Harvard — Firmas heterogéneas y comercio internacional

**Contenido**:
- **Quién es**: economista franco-estadounidense, nacido en París
  - PhD en Michigan, profesor en Harvard desde 2010
- **Paper clave**: *"The Impact of Trade on Intra-Industry Reallocations and Aggregate Industry Productivity"* (2003, Econometrica)
  - Uno de los papers más citados en economía internacional del siglo XXI
- **Dato**: **coautor del manual de Krugman** desde la 9na edición (el que usan en este curso)
- **Contribución central**: no todas las firmas son iguales → la apertura **selecciona**
  - Las mejores crecen, las peores salen

**Notas docente**:
BIOGRAFÍA MELITZ (3 minutos)
"Marc Melitz es probablemente el economista de comercio internacional más influyente de los últimos 20 años. Su paper de 2003 cambió el campo: por primera vez, las firmas individuales pasaron a ser el centro del análisis."

"Dato interesante: Melitz es coautor del manual que ustedes usan. Si se fijan en la tapa, dice 'Krugman, Obstfeld & Melitz'. La 9na edición incorporó todo un capítulo nuevo (Cap 8) basado en su modelo."

"¿Por qué fue tan influyente? Porque conectó con datos microeconómicos que se estaban haciendo disponibles. Hasta los 2000, los economistas de comercio trabajaban con datos de países y sectores. Cuando empezaron a tener datos de firmas individuales (censos industriales, registros aduaneros), descubrieron que la heterogeneidad entre firmas era enorme. Melitz dio el marco teórico para entender esos datos."

"Veamos cómo lo explica."

---

#### Slide 14: Firmas distintas, destinos distintos
**Tipo**: grafico_texto
**Título**: El mecanismo de selección de Melitz
**Gráfico**: graficos/melitz_seleccion.png
**Fuente**: Basado en Melitz (2003) y Krugman Cap 8

**Contenido**:
- **En el gráfico**: la curva muestra la distribución de firmas por coste marginal ($c_i$)
  - Eje X: coste marginal (más a la derecha = menos productiva). Dos líneas verticales marcan los **umbrales**
- **Tres zonas de color** — tres destinos para firmas del mismo sector:
  - **Verde** (izquierda, $c_i < c^* - t$): firmas que **exportan** — las más productivas
  - **Naranja** (medio, entre los dos umbrales): firmas que **venden localmente** — sobreviven pero no exportan
  - **Rojo** (derecha, $c_i > c^*$): firmas que **cierran** — no cubren costos fijos
- **Clave**: exportar tiene un coste adicional $t$ → solo las firmas con $c_i + t < c^*$ pueden exportar rentablemente

**Notas docente**:
MECANISMO DE SELECCIÓN (8 minutos)
"El modelo de Melitz tiene una idea muy simple pero muy poderosa. Imaginemos un sector con muchas firmas. Cada firma tiene un coste marginal distinto. Algunas son muy eficientes (coste bajo), otras son ineficientes (coste alto)."

"Hay un umbral de supervivencia: si tu coste es demasiado alto, no podés cubrir los costos fijos (alquiler, máquinas, etc.) y tenés que cerrar. Ese umbral se llama c*."

"Ahora metamos el comercio. Para exportar, hay un coste adicional 't' por unidad: transporte, aduanas, adaptación del producto, etc. Entonces exportar es rentable solo si tu coste marginal más el coste de comercio (c_i + t) sigue estando por debajo de c*."

"Resultado: tres grupos de firmas."
1. "Las de coste muy alto (c_i > c*): cierran. No pueden competir ni siquiera en el mercado local."
2. "Las de coste intermedio (c* - t < c_i < c*): sobreviven y venden localmente, pero exportar les sale muy caro."
3. "Las de coste bajo (c_i < c* - t): pueden vender local Y exportar. Son las más productivas, las más grandes, las que pagan mejores salarios."

"¿Ven cómo esto explica el dato del slide anterior? Solo el 18% exporta porque exportar tiene costos fijos y variables adicionales que solo las mejores firmas pueden absorber."

EJEMPLO: "Toyota Argentina produce y vende localmente la Hilux. La exporta a Brasil y a otros mercados. Tiene escala, tecnología y logística para absorber el costo de exportar. Una PyME autopartista que hace un componente específico probablemente solo venda al mercado interno, o como mucho a una terminal local."

---

#### Slide 15: ¿Qué pasa cuando se abre el comercio?
**Tipo**: grafico_texto
**Título**: Apertura = selección: las mejores crecen, las peores salen
**Gráfico**: graficos/melitz_apertura.png
**Fuente**: Basado en Krugman Cap 8, Figura 8.7

**Contenido**:
- **En el gráfico**: dos paneles — *antes* de la apertura (izquierda) y *después* (derecha)
  - Notar cómo el umbral $c^*$ se mueve a la izquierda → se vuelve **más exigente**
- **Antes**: todas las firmas que sobreviven venden localmente. Solo hay una zona (azul)
- **Después** — aparecen tres zonas (como en el slide anterior):
  - Las más productivas **ganan cuota y exportan** (verde, "Exportan — crecen")
  - Las intermedias venden solo local con márgenes más bajos (naranja)
  - Más firmas **salen del mercado** — el umbral subió (rojo expandido, "Salen — más")
- **Efecto neto**: sube la **productividad promedio** de la industria (reasignación hacia las mejores)

**Notas docente**:
EFECTOS DE LA APERTURA (7 minutos)
"¿Qué pasa cuando se abre el comercio? El mercado se agranda. Eso suena bien — más clientes potenciales. Pero también significa más competencia: entran firmas extranjeras que también son productivas."

"El resultado es una selección darwiniana dentro del sector:"
- "Las firmas más productivas (costes bajos) ganan: acceden a nuevos mercados, exportan, aumentan ventas, crecen."
- "Las firmas intermedias se aprietan: enfrentan más competencia, bajan márgenes."
- "Las firmas menos productivas no sobreviven: el umbral sube y quedan fuera."

"Este efecto de 'reasignación' tiene una consecuencia muy importante: sube la productividad promedio de la industria. No porque cada firma sea más productiva, sino porque cambió la composición — más peso de las buenas, menos de las malas."

"Daniel Trefler, de la Universidad de Toronto, estudió exactamente esto con el TLC Canadá-EEUU de 1989. Encontró que la productividad en las industrias más afectadas subió entre 14 y 15%. Pero también hubo un costo de ajuste: empresas que cerraron, trabajadores desplazados. El título del paper es elocuente: 'Pain, Then Gain'."

CONFUSIÓN COMÚN: "Ojo: esto no quiere decir que la apertura sea buena para todos. Las firmas que cierran pierden, los trabajadores desplazados pierden (al menos en el corto plazo). Melitz no dice 'abramos y todo se arregla'. Dice que hay ganadores y perdedores DENTRO del sector, y que el efecto neto sobre productividad es positivo. Pero el ajuste es doloroso."

CONEXIÓN CON STOLPER-SAMUELSON (Clase 3): "En H-O, los perdedores eran factores de producción (trabajo vs capital). En Melitz, los perdedores son firmas específicas (las menos productivas). Es un conflicto intra-sectorial, no inter-sectorial."

---

#### Slide 16: De Ricardo a Melitz — Tres capas de realismo
**Tipo**: grafico_texto
**Título**: Cómo evolucionó la teoría del comercio
**Gráfico**: graficos/evolucion_teorias.png
**Fuente**: Basado en Bernard, Jensen, Redding & Schott (2007), JEP

**Contenido**:
- **En el gráfico**: tres columnas (azul → naranja → verde) con cuatro filas comparativas
  - Leer de izquierda a derecha: cada teoría **agrega una capa** de realismo
- **Teoría clásica** (Ricardo/H-O):
  - Fuente de comercio: diferencias entre países. Firmas: idénticas dentro del sector
- **Nueva teoría** (Krugman 1980):
  - Fuente de comercio: economías de escala + diferenciación. Firmas: idénticas (simétricas)
- **Firmas heterogéneas** (Melitz 2003):
  - Fuente de comercio: diferencias de productividad entre firmas. Firmas: heterogéneas (distintos costes)
- Las teorías **no se reemplazan**: el comercio real combina los tres mecanismos simultáneamente

**Notas docente**:
EVOLUCIÓN TEÓRICA (5 minutos)
"Vamos a hacer un mapa de cómo evolucionó la teoría del comercio. Esto viene de un paper muy bueno de Bernard, Jensen, Redding y Schott (2007) en el Journal of Economic Perspectives."

"Ricardo y H-O (siglo XIX - primera mitad del XX): el comercio se explica por diferencias entre países (tecnología o dotaciones). Genera comercio interindustrial. Las firmas dentro de cada sector son todas iguales."

"Krugman (1980): agrega economías de escala y diferenciación. Explica el comercio entre países similares. Genera comercio intraindustrial. Pero las firmas siguen siendo iguales (simétricas)."

"Melitz (2003): las firmas son distintas. Tienen costes diferentes. Solo las más productivas exportan. Explica por qué tan pocas firmas participan del comercio internacional. Y genera predicciones sobre productividad y ajuste que los otros modelos no pueden hacer."

"Lo importante: no es que una teoría reemplace a la otra. Las tres conviven. Argentina exporta soja por ventaja comparativa (Ricardo/H-O), intercambia autos con Brasil por escala y variedades (Krugman), y dentro del sector automotriz solo las firmas más productivas exportan (Melitz). Los tres mecanismos operan simultáneamente."

TRANSICIÓN: "Ahora bien. Melitz nos mostró que las firmas exportadoras son distintas de las que no exportan. Son más productivas, más grandes. Y cuando exportan, enfrentan un costo del comercio t, así que fijan un precio de exportación distinto al doméstico. ¿Ven adónde lleva esto? Si el precio de exportación es menor al precio interno... técnicamente eso es dumping. ¿Pero es realmente dumping? ¿O es simplemente cómo funciona la competencia monopolística? Esta es nuestra cuarta pregunta."

---

### Sección: Bloque 4 — ¿Cuándo el precio bajo es dumping?

#### Slide 17: Bloque 4 — ¿Cuándo el precio bajo es dumping?
**Tipo**: seccion
**Título**: Bloque 4 — ¿Cuándo el precio bajo es dumping?
**Subtítulo**: Si el precio externo < interno, ¿es trampa, subsidio o competencia legítima?

**Notas docente**:
APERTURA DE BLOQUE 4 (1 minuto)
"Melitz nos mostró que las firmas exportadoras son distintas: más productivas, fijan precios distintos en el mercado externo. Pero entonces aparece una pregunta política sensible: si una empresa china exporta a la mitad de precio que vende en su país, ¿es dumping desleal o simplemente competencia? Argentina aplica antidumping desde hace décadas — ¿está siempre justificado? Acá necesitamos distinguir tres cosas que se confunden todo el tiempo: dumping, subsidios y competencia legítima."

---
#### Slide 18: Dumping: cuando el precio de exportación es "demasiado bajo"
**Tipo**: texto
**Título**: Dumping = precio de exportación < "valor normal"
**Subtítulo**: No todo precio bajo es dumping
**Layout**: dos-columnas

**Contenido**:
- **Definición**: una firma vende en el exterior a un precio inferior al "valor normal"
- **¿Qué es "valor normal"?**
  - Precio en el mercado interno del exportador
  - Precio a terceros mercados (referencia alternativa)
  - Costo de producción + margen razonable
- **No confundir** dumping con:
  - Menores costos / mayor productividad
  - Tipo de cambio depreciado
  - Rebajas puntuales o liquidación de stock
  - Diferencias de calidad
- Frase clave: ***Precio bajo puede ser competitividad. Dumping es discriminación de precios entre mercados, sostenida por segmentación y poder de mercado***

**Notas docente**:
DEFINICIÓN (7 minutos)
"Dijimos que Melitz muestra que las firmas exportadoras cobran distinto en el mercado de exportación y en el mercado doméstico. Ahora: ¿cuándo esa diferencia de precios se convierte en dumping?"

"Dumping es cuando una firma vende en el exterior a un precio inferior a lo que se considera un 'valor normal'. La comparación puede hacerse contra el precio que cobra en su mercado interno, contra el precio a terceros mercados, o contra un costo construido (costo + margen razonable)."

"Pero ojo: no todo precio bajo es dumping. Esto es clave y los alumnos suelen confundirlo."

"Cuatro cosas que NO son dumping:"
1. "Menores costos / mayor productividad: si una empresa china produce más barato porque tiene escala enorme, tecnología mejor o energía más barata, eso no es dumping. Es competitividad."
2. "Tipo de cambio: un país con moneda depreciada tiene exportaciones más baratas en dólares. Eso tampoco es dumping."
3. "Rebajas puntuales: liquidar stock por recesión no es lo mismo que discriminar precios sostenidamente."
4. "Diferencias de calidad: si el producto importado es más barato porque es de menor calidad, no estás comparando lo mismo."

"La pregunta correcta no es '¿es barato?' sino '¿cobra distinto en distintos mercados?' Esa es la esencia del dumping: discriminación internacional de precios."

EJEMPLO: "Si una firma vende a 100 en su mercado y exporta a 70, solo puede sostener eso si los mercados están segmentados: si no, alguien compra a 70 y revende a 100. Cuando ese arbitraje no es viable, aparece el espacio para la discriminación de precios."

---

#### Slide 19: Las tres condiciones del dumping
**Tipo**: texto
**Título**: La tríada del dumping
**Subtítulo**: Tres condiciones necesarias — todas conectan con lo que ya vimos
**Layout**: dos-columnas

**Contenido**:
- **1. Poder de mercado**:
  - La firma puede fijar precios (competencia imperfecta)
  - En competencia perfecta, $P = CMg$ y no hay margen para discriminar
- **2. Mercados segmentados**:
  - No hay arbitraje fácil entre mercados
  - Fuentes: costos de transporte, regulaciones sanitarias/técnicas, aranceles, distribución exclusiva
- **3. Elasticidades distintas**:
  - La demanda responde diferente en cada mercado
  - La firma cobra más donde la demanda es inelástica (mercado interno) y menos donde es elástica (exportación)
- Si falta alguna de las tres → **no hay dumping sostenible**

**Notas docente**:
CONDICIONES (5 minutos)
"Para que exista dumping hacen falta tres cosas simultáneamente. Y fíjense que las tres conectan con conceptos que ya vimos."

1. Poder de mercado: "Si el mercado fuera perfectamente competitivo, el precio lo pone el mercado y punto. Nadie puede decidir 'acá cobro 100 y allá 70'. Tiene que haber competencia imperfecta — la firma tiene algún poder para fijar precios. ¿Dónde vimos esto? En Krugman, Clase 4: las firmas producen variedades diferenciadas y tienen poder de mercado."

2. Mercados segmentados: "Esta es la condición clave. Si los mercados no están separados, aparece el arbitraje: alguien compra donde es barato y revende donde es caro, y los precios se igualan. La segmentación puede venir de costos de transporte, regulaciones, aranceles o canales de distribución exclusivos. ¿Dónde vimos esto? En Melitz: el costo del comercio t es exactamente lo que segmenta los mercados."

3. Elasticidades distintas: "La firma cobra más donde puede (mercado interno, clientes cautivos, menos opciones) y menos donde tiene que competir más duro (mercado de exportación con muchos competidores). Técnicamente, el precio es menor donde la demanda es más elástica."

"¿Ven cómo el dumping NO es un tema separado? Es la consecuencia lógica de la competencia monopolística con costos del comercio. Lo mismo que Krugman y Melitz modelizaron."

---

#### Slide 20: El dumping en el modelo de Krugman-Melitz
**Tipo**: texto
**Título**: El dumping como resultado "natural"
**Subtítulo**: Krugman Cap 8: cuando el dumping surge del modelo

**Contenido**:
- **En el modelo de Melitz**, una firma exportadora fija:
  - Precio doméstico: $P^D_1 = c_1 + \text{margen}$
  - Precio de exportación: $P^X_1 = (c_1 + t)$ — menor al doméstico
  - Como $P^X < P^D$ → esto **es** dumping por definición
- **Pero**: surge **naturalmente** de la estructura de mercado
  - La empresa no se comporta distinto de sus competidoras locales en el destino
  - Es el resultado lógico de competencia monopolística + costes del comercio
- **Implicancia**: buena parte del dumping es un artefacto del modelo, no conducta predatoria
- ***¿Tiene sentido penalizar una conducta que surge naturalmente del modelo?***

**Notas docente**:
MODELO KRUGMAN (5 minutos)
"Este es un punto muy importante que viene de Krugman Cap 8. Volvamos al modelo de Melitz. Una empresa exporta al mercado extranjero. Tiene un coste marginal c_1 y un coste del comercio t. En su mercado nacional, fija un precio P_D basado en su coste marginal y su margen. En el mercado de exportación, fija P_X = P_D - t. ¿Por qué? Porque el coste del comercio hace que la competencia sea más dura allá, y la firma acepta un margen menor para ganar cuota."

"¿Eso es dumping? Sí, por definición: P_X < P_D. Pero no hay intención predatoria, no hay subsidio, no hay conducta anticompetitiva. Es simplemente cómo funciona la competencia monopolística con costes del comercio."

"Esto es lo que hace que el antidumping sea tan polémico entre los economistas. Krugman dice literalmente: 'el dumping surge de forma natural' en estos modelos. Y si es natural, ¿tiene sentido penalizarlo?"

"Sin embargo, el sistema legal trata el dumping como práctica 'desleal'. Y las demandas antidumping se multiplican: China ha sido el principal objetivo. El debate sigue abierto."

"Entonces la pregunta pasa a ser: si parte del dumping es 'natural', ¿cuándo SÍ hay que preocuparse? Cuando el mecanismo es otro."

---

#### Slide 21: Cuatro formas de dumping — No todas son iguales
**Tipo**: texto
**Título**: Mismo síntoma, causas distintas
**Subtítulo**: El mecanismo importa para la respuesta de política
**Layout**: dos-columnas

**Contenido**:
- **1. Predatorio** (empresa):
  - Entra muy barato → expulsa competidores → luego sube precio
  - El más nocivo, pero el más difícil de probar
- **2. Persistente / discriminación** (empresa):
  - Precios distintos de forma estable por segmentación + elasticidades
  - "Natural" en competencia monopolística
- **3. Cíclico / exceso de capacidad** (industria):
  - Exporta barato para sostener producción en períodos de recesión. Temporal
- **4. Apoyo estatal** (Estado + empresa):
  - Precio bajo por subsidios, crédito dirigido, energía subsidiada, TC administrado
  - Caso China. Jurídicamente: muchas veces es "subsidio" → herramienta distinta (CVD)
- ***Mismo síntoma (precio bajo), causas distintas → respuestas de política distintas***

**Notas docente**:
TIPOLOGÍAS (8 minutos)
"Acabamos de ver que el dumping 'persistente' surge naturalmente del modelo. Pero hay otras formas que sí son problemáticas."

1. Predatorio: "Es el que más preocupa: la firma entra a un mercado con precios por debajo de costo, acepta pérdidas, destruye a la competencia local, y cuando queda sola, sube precios. Es la pesadilla del productor local. Pero ojo: es el más difícil de probar. Necesitás demostrar que la empresa pierde hoy con la intención de ganar mañana."

2. Persistente: "Es el más común y el más 'natural'. Es lo que acabamos de ver con la fórmula de Krugman: la firma cobra distinto en distintos mercados porque las condiciones son distintas. Puede hacerlo de forma sostenida."

3. Cíclico: "Cuando hay recesión o exceso de capacidad, las firmas exportan barato para no parar las máquinas. Es temporal: cuando la demanda interna se recupera, los precios vuelven."

4. Apoyo estatal: "Este es el caso más polémico. Cuando hablamos de China, muchas veces lo que está en juego no es solo la decisión de una empresa, sino un ecosistema de apoyo estatal: crédito subsidiado, energía barata, compras públicas, tipo de cambio administrado. En el debate público se le llama 'dumping', pero en términos de reglas OMC, muchas veces es un caso de subsidios. Y la herramienta es distinta: no antidumping (AD) sino derechos compensatorios (CVD)."

"En la práctica, los casos se mezclan. Una empresa china puede tener ventajas de escala legítimas (no dumping) + subsidios estatales (subsidio, no dumping) + discriminación de precios (dumping propiamente dicho). Separar es clave para elegir bien la herramienta."

---

#### Slide 22: Efectos del dumping — ¿Quién gana y quién pierde?
**Tipo**: texto
**Título**: Efectos económicos: corto plazo vs largo plazo
**Subtítulo**: El dilema de política

**Contenido**:
- **Corto plazo**:
  - Consumidores del país importador: **ganan** (precio baja, más variedad)
  - Productores locales: **pierden** (caen ventas y márgenes)
- **Largo plazo (riesgos)**:
  - Salida de productores → pérdida de **capacidad productiva** (difícil de recuperar)
  - Empleo: caída directa + **efectos en cadena** (proveedores, servicios, logística)
  - Si hay predación: menor competencia futura → posible **suba de precios**
- **El dilema**: proteger productores/empleo vs sostener precios bajos para consumidores
- La respuesta depende del **mecanismo** (predatorio vs persistente vs cíclico)

**Notas docente**:
EFECTOS (5 minutos)
"Acá aparece el dilema distributivo — que ya conocemos de Stolper-Samuelson y de Melitz. El dumping tiene ganadores y perdedores, y depende del horizonte temporal."

"Corto plazo: el consumidor está feliz. Paga menos. En un contexto de inflación o caída del ingreso real, esto pesa mucho políticamente. Pero el productor local que hace el mismo bien entra en una competencia brutal: baja precios, pierde mercado, cae rentabilidad."

"Largo plazo: si el shock dura, podés perder capacidad productiva. Y esa pérdida no se recupera fácil: se destruyen redes de proveedores, conocimiento, maquinaria, crédito. El empleo no es solo el de la fábrica: hay transporte, insumos, mantenimiento, logística. Es un efecto en cadena."

"Si el mecanismo es predatorio, además, hay un riesgo de concentración futura: la firma que destruyó la competencia puede después subir precios. Pero si es persistente o cíclico, ese riesgo es menor."

"Entonces: ¿qué puede hacer el Estado?"

---

#### Slide 23: Tres instrumentos, tres diagnósticos
**Tipo**: texto
**Título**: ¿Qué puede hacer el Estado?
**Subtítulo**: El instrumento depende del diagnóstico
**Layout**: dos-columnas

**Contenido**:
- **Antidumping (AD)**:
  - Se aplica cuando se prueba: dumping + daño + nexo causal
  - Instrumento: arancel adicional que compensa el margen de dumping
- **Derechos compensatorios (CVD)**:
  - Se aplica cuando el problema es **subsidio** del país exportador
  - Instrumento: arancel que neutraliza el beneficio del subsidio
- **Salvaguardias**:
  - Ante aumento **súbito** de importaciones que causa daño serio
  - No requiere probar dumping ni subsidio. Instrumento: restricción/recargo temporal
- Clave: ***mecanismo distinto → herramienta distinta***

**Notas docente**:
INSTRUMENTOS (6 minutos)
"Tres herramientas de defensa comercial. Cada una responde a un diagnóstico distinto."

AD: "Antidumping se aplica cuando se prueba un triángulo: (1) hay dumping (precio de exportación < valor normal), (2) hay daño a la industria local, y (3) hay nexo causal entre el dumping y el daño. Si se cumplen las tres, se impone un derecho antidumping — un arancel extra que sube el precio del importado."

CVD: "Si el problema no es discriminación de precios sino subsidio estatal, se usan derechos compensatorios. La lógica es: el Estado del exportador está dando una ventaja artificial a sus empresas, y yo la neutralizo con un arancel equivalente. Muchos de los casos vinculados a China encajan mejor acá."

Salvaguardias: "Se aplican ante un shock de importaciones, aunque no haya dumping ni subsidio comprobado. Aumentan las importaciones de golpe, causan daño serio, y el Estado impone una restricción temporal para dar tiempo de ajuste. Son como un 'paréntesis'. Ejemplo: crisis global, desvío de comercio, caída de demanda en otros mercados."

"Ojo: antidumping no se aplica porque 'me molesta la importación'. Se aplica si se prueba el triángulo. Sin daño y sin nexo causal, no hay caso."

---

#### Slide 24: Del síntoma al instrumento
**Tipo**: grafico_texto
**Título**: ¿Qué instrumento usar?
**Gráfico**: graficos/dumping_arbol.png
**Fuente**: Elaboración propia

**Contenido**:
- **En el gráfico**: árbol de decisión que empieza por el **síntoma** (caja azul oscura, arriba)
  - Las flechas Sí/No conducen a distintas ramas y desenlaces
- **Rama izquierda** (hay dumping):
  - ¿Precio exportación < valor normal? → Sí → ¿Hay daño + nexo causal?
  - Sí: **Antidumping** (caja verde) / No: no corresponde
- **Rama derecha** (no hay dumping pero hay problema):
  - ¿La causa es subsidio estatal? → Sí: **CVD** (caja naranja)
  - ¿Aumento súbito + daño serio? → Sí: **Salvaguardia** (caja celeste)
- Idea fuerza: ***primero diagnóstico, después instrumento***

**Notas docente**:
ÁRBOL DE DECISIÓN (5 minutos)
"Vamos a armar la lógica de decisión paso a paso."

Paso 1 — ¿Hay dumping?: "Primero: ¿el precio de exportación es menor al valor normal? Recordar las tres formas de medir el valor normal (precio interno, precio a terceros, costo construido)."

Paso 2 — ¿Hay daño + causalidad?: "Si hay dumping, no alcanza: necesitás probar que la industria local está sufriendo Y que ese sufrimiento es causado por las importaciones con dumping. Si la industria cayó pero por una recesión interna o por un cambio tecnológico, no hay caso."

Paso 3 — ¿Subsidio?: "Si no hay dumping per se, pero los precios son inexplicablemente bajos, puede haber subsidios. Ahí el instrumento es CVD."

Paso 4 — ¿Shock de importaciones?: "Si no hay dumping ni subsidio, pero hay un aumento súbito de importaciones que causa daño serio, la salvaguardia es el último recurso."

"El instrumento depende del diagnóstico, no del enojo. Y ojo: en la práctica, las herramientas se usan muchas veces de forma proteccionista — las demandas antidumping se volvieron la barrera comercial favorita de los países ricos. Esto lo vamos a profundizar en la Unidad 6."

---

#### Slide 25: Caso aplicado — ¿Corresponde defensa comercial?
**Tipo**: texto
**Título**: Mini caso: Sector X del país A (datos estilizados)
**Subtítulo**: Diagnóstico con el árbol de decisión

**Contenido**:
- Importaciones: **+60%** (en volumen, 2023-2024)
- Precio importado: **-25%**
- Participación importada en mercado interno: **15% → 35%**
- Producción local: **-20%**
- Utilización de capacidad: **75% → 55%**
- Empleo sectorial: **-10%**
- Rentabilidad: cae fuerte, pasa a **negativa**
- **Preguntas**: (1) ¿Hay daño? (2) ¿Hay indicios de nexo causal? (3) ¿Qué información falta para elegir AD, CVD o salvaguardia?

**Notas docente**:
CASO APLICADO (8 minutos)
"Vamos a ejercitar con un mini caso. Datos estilizados — no es un país real, pero los números son realistas."

Pregunta 1 — ¿Hay daño?: "Producción -20%, capacidad 75%→55%, empleo -10%, rentabilidad negativa. Sí, hay daño. Y no es un indicador suelto: es un paquete consistente de deterioro productivo, laboral y financiero."

Pregunta 2 — ¿Nexo causal?: "Importaciones +60%, precio importado -25%, participación 15%→35%. La hipótesis causal empieza a ser fuerte: el deterioro de la industria local coincide con el aumento masivo de importaciones baratas."

"PERO: esto todavía no 'prueba' causalidad al 100%. Hay que preguntar: ¿hubo recesión? ¿cayó la demanda total? ¿subieron los costos internos? ¿cambió el tipo de cambio? Si la caída de la industria se explica por un factor interno, el nexo causal se debilita."

Pregunta 3 — ¿Qué falta?: "Para AD: necesitás comparar el precio de exportación con el valor normal del exportador y calcular el margen de dumping. Para CVD: necesitás evidencia de subsidios (crédito preferencial, energía subsidiada, beneficios fiscales). Para salvaguardia: el +60% de importaciones y el salto de 15% a 35% de share ya son indicios fuertes."

DINÁMICA: Pedir a los alumnos que digan qué instrumento elegirían y por qué. No hay respuesta única — depende de qué información adicional se consiga.

TRANSICIÓN: "Bien. Hasta acá respondimos cuatro preguntas: qué determina el IIT, dónde se produce, quién exporta, a qué precio. Nos queda una última, y es quizás la más importante para entender el mundo de hoy. Melitz nos mostró que las firmas deciden SI exportar. Pero hay una decisión más fundamental: las firmas también deciden QUÉ HACER adentro y qué mandar afuera. No mudan la fábrica entera — mudan TAREAS. Y eso cambia toda la discusión."

---

#### Slide 26: Antidumping en el mundo — 4 décadas de explosión
**Tipo**: grafico_texto
**Título**: El antidumping en cifras: ~250 medidas/año, picos en crisis
**Subtítulo**: WTO Anti-Dumping Statistics — 1995-2023

**Imagen**: graficos/dumping_mundial_serie_y_ranking.png

**Contenido**:
- **Volumen total**: ~250 iniciaciones/año en promedio mundial
- **Picos**: crisis asiática (2001), post-China en OMC (2013), COVID (2020 — record de 348)
- **Top 5 aplicadores**: India, EEUU, UE, Brasil, **Argentina** (5° mundial — sorprende para una economía chica)
- **Top 5 afectados**: China (1714, lejos), Corea, Taiwán, EEUU, Japón
- **Patrón**: el antidumping no es un fenómeno "raro" — es el instrumento de defensa comercial **más usado** del sistema multilateral
- Datos completos en `notebooks/datos/wto_antidumping_*.csv` (para analizar en notebook)

**Fuente**: WTO Anti-Dumping Statistics (https://www.wto.org/english/tratop_e/adp_e/adp_stattab_e.htm)

**Notas docente**:
ANTIDUMPING EN EL MUNDO (5 minutos)
"Hasta acá el dumping era teoría. Veamos qué pasa en la práctica."

LECTURA DEL GRÁFICO:
"Panel izquierdo: serie histórica de iniciaciones AD por año desde 1995 (creación de la OMC). Vemos un volumen base de ~200-250/año, con picos en momentos de crisis: 2001 (post-burbuja Asia, dumping de acero), 2013 (después del shock chino post-OMC), 2020 (COVID, todos protegieron sus industrias). El máximo histórico fue 2020 con 348 iniciaciones."

"Panel derecho: top 10 aplicadores acumulado 1995-2023. India lidera con 1124 medidas. Argentina aparece quinta — eso es destacable: somos una economía chica pero usamos AD intensamente."

DATO PARA ANCLAR:
"China es el blanco principal del mundo: 1714 medidas iniciadas contra exportadores chinos, casi 4 veces más que el segundo (Corea). Esto NO es casualidad: es el reflejo de la integración china al sistema multilateral en 2001 + su escala industrial + el patrón de subsidios estatales."

PARA EL NOTEBOOK DEL ALUMNO:
"En `notebooks/datos/` están los CSVs de WTO. Pueden por ejemplo cruzar con datos de comercio bilateral para calcular 'intensidad AD' = medidas/comercio. Es buen ejercicio para Eval U3."

PREGUNTA PARA ESTUDIANTES: "¿Por qué creen que países muy chicos como Argentina están entre los top aplicadores? ¿Y por qué China no aparece en el top de aplicadores hasta hace pocos años?"
(Pista: AD es defensa de industria nacional. Países chicos lo usan como instrumento principal porque no tienen otros. China hasta hace poco era exportador, no industria a defender — ahora cambió.)

---

#### Slide 27: Argentina y el antidumping
**Tipo**: grafico_texto
**Título**: Argentina aplica casi 1 medida cada 3 semanas (acumulado 1995-2023)
**Subtítulo**: 462 medidas iniciadas — China es el origen del 50%

**Imagen**: graficos/dumping_argentina.png

**Contenido**:
- **462 medidas iniciadas** desde 1995 — quinta posición mundial
- **China concentra el 50%** de las medidas argentinas (229 casos)
- **Brasil** segundo lugar pero lejos (51, 11%) — paradoja: socio Mercosur que también nos demanda con AD
- Otros principales: Corea, Taiwán, India, Indonesia (~15 países representan el 90%)
- **Sectores típicos** (informes CNCE): acero, productos químicos, plásticos, textiles, bicicletas, electrodomésticos
- Las medidas vigentes detalladas en informe anual de la **CNCE** (las veremos en S10/Política Comercial)

**Fuente**: WTO Anti-Dumping Statistics + CNCE (Comisión Nacional de Comercio Exterior, Argentina)

**Notas docente**:
ARGENTINA Y EL ANTIDUMPING (5 minutos)
"Argentina es uno de los grandes usuarios del AD a nivel mundial. Para una economía de su tamaño, es desproporcionadamente activa."

LECTURA DEL GRÁFICO:
"China concentra la mitad de las medidas argentinas. Esto es coherente con el patrón mundial: China es el blanco favorito post-2001."

"Brasil es el segundo origen — y eso es interesante porque es nuestro socio principal del Mercosur. La excepción al librecambio interno se da cuando un sector argentino siente daño concreto (caso típico: línea blanca, calzado, textiles). El Mercosur permite medidas AD intra-bloque solo en condiciones excepcionales."

SECTORES MÁS ACTIVOS:
"Los informes de la CNCE muestran que los sectores con más medidas son acero (productos planos/largos), químicos básicos, plásticos y textiles. Son sectores con escala importante, sensibles a la competencia importada y con asociaciones empresariales activas en pedir defensa."

NOTA SOBRE FUENTES:
"Los datos completos de WTO están en `notebooks/datos/wto_antidumping_argentina_origen.csv`. Para datos detallados de medidas vigentes hoy (con productos, fechas, países, márgenes específicos), la CNCE publica informes anuales. Vamos a verlos con detalle en la Sesión 10 — Política Comercial."

PREGUNTA PARA ESTUDIANTES: "¿Por qué creen que un país aplica AD a un socio del bloque (Brasil)? ¿No es contradictorio con la integración?"
(Respuesta sugerida: la integración no elimina el AD, lo regula. El Mercosur permite AD intra-bloque en casos excepcionales. La paradoja es que la integración profunda exige asimetrías productivas que pueden requerir defensa puntual.)

DATO ADICIONAL: "El sesgo anti-China es global, pero no por casualidad: China subsidia con créditos blandos, energía barata y régimen tributario especial — todo legítimo desde su perspectiva, pero distorsionante desde la perspectiva del importador. Es una de las grandes tensiones del sistema multilateral hoy."

---

### Sección: Bloque 5 — Comercio de tareas

#### Slide 28: Bloque 5 — ¿Y si no se mueven los bienes, sino las tareas?
**Tipo**: seccion
**Título**: Bloque 5 — ¿Y si no se mueven los bienes, sino las tareas?
**Subtítulo**: Las firmas no mueven la fábrica entera — fragmentan la producción

**Notas docente**:
APERTURA DE BLOQUE 5 (1 minuto)
"Hasta acá respondimos cuatro preguntas: qué determina el IIT, dónde se produce, quién exporta, a qué precio. Pero hay una última pregunta — quizás la más importante para entender el mundo de hoy. Las firmas no exportan o no exportan — eso es Melitz. Tampoco mudan la fábrica entera — eso es solo una caricatura. Lo que las firmas hacen REALMENTE es decidir qué TAREAS hacer adentro y cuáles mandar al exterior. Esa es la fragmentación del proceso productivo, y es lo que abre la discusión de cadenas globales de valor que vamos a profundizar en la Unidad 5."

---
#### Slide 29: Del comercio de bienes al comercio de tareas
**Tipo**: texto
**Título**: Trading Tasks — El comercio de tareas
**Subtítulo**: Grossman & Rossi-Hansberg (2008), AER

**Contenido**:
- **De Melitz a Grossman & Rossi-Hansberg**:
  - Melitz: la firma decide **si** exportar → basado en productividad vs costes del comercio
  - G&RH: la firma decide **qué tareas** hacer internamente y cuáles enviar al exterior (offshoring)
- **Cambio de perspectiva**: no se comercian bienes finales, se comercian **tareas**
  - Diseño, ensamblaje, logística, atención al cliente, contabilidad...
- **¿Qué tareas se offshoreean?**
  - Las **rutinarias y codificables** → más fáciles de enviar al exterior
  - Las que requieren **interacción, creatividad o presencia física** → tienden a quedarse
  - Determinantes: costos de comunicación/coordinación + naturaleza de la tarea

**Notas docente**:
TRADING TASKS (7 minutos)
"Grossman y Rossi-Hansberg publicaron en 2008 un paper titulado 'Trading Tasks: A Simple Theory of Offshoring'. La idea central es potente: cuando pensamos en comercio internacional, no deberíamos pensar en bienes que cruzan fronteras. Deberíamos pensar en TAREAS."

"Un iPhone no se 'produce en China'. Se DISEÑA en California (tarea creativa, fase 1 de Vernon), los CHIPS se fabrican en Taiwán (tarea intensiva en capital y tecnología), se ENSAMBLA en China (tarea rutinaria, intensiva en trabajo), se DISTRIBUYE globalmente (logística), y el SOFTWARE se actualiza desde Cupertino. Son tareas distintas, en lugares distintos, dentro del mismo producto."

"¿Ven cómo esto conecta con Vernon? Vernon pensaba en EL PRODUCTO que se mueve geográficamente. Grossman y Rossi-Hansberg dicen: no, se mueven LAS TAREAS dentro del producto. El producto no viaja entero — se fragmenta."

"Grossman y Rossi-Hansberg formalizan esto: una firma puede 'offshoreear' las tareas donde los costos de hacerlo afuera (salarios más bajos) superan los costos de coordinación a distancia. Las tareas rutinarias y codificables son las más fáciles de offshoreear. Las que requieren interacción cara a cara, creatividad o presencia física son más difíciles."

"Esto tiene implicancias enormes para el mercado de trabajo. No es que 'la industria se va': se van CIERTAS TAREAS. Los trabajadores que hacían esas tareas pierden, pero los que hacen tareas complementarias (coordinación, diseño, gestión) pueden ganar. Es una redistribución dentro del proceso productivo."

---

#### Slide 30: ¿Quién hace cada tarea?
**Tipo**: grafico_texto
**Título**: El enfoque de tareas — Una nueva forma de pensar
**Gráfico**: graficos/comercio_tareas.png
**Fuente**: Basado en Grossman & Rossi-Hansberg (2008) y Acemoglu & Autor (2011)

**Contenido**:
- **En el gráfico**: tres niveles de arriba a abajo
  - **Arriba**: el bien final (caja azul oscura)
  - **Medio**: se descompone en 5 tareas (diseño, componentes, ensamblaje, logística, marketing)
  - **Abajo**: para cada tarea, tres opciones → **trabajador local** / **trabajador extranjero** / **máquina-IA**
- **¿Qué determina la asignación?**
  - **Costos relativos** + costos de coordinación + naturaleza de la tarea
- **Acemoglu & Autor** (2011): este enfoque unifica comercio + cambio tecnológico + mercado de trabajo
  - Anticipos para Unidades 5 y 7: CGV, outsourcing, automatización, IA
- ***La tarea es la unidad de análisis del siglo XXI***

**Notas docente**:
ENFOQUE DE TAREAS (6 minutos)
"Acá viene el cierre conceptual que me parece más potente. Acemoglu y Autor, en un trabajo de 2011, proponen que la TAREA es la unidad de análisis fundamental. No el bien, no el sector, no el país: la tarea."

"Para cada tarea involucrada en producir un bien, hay tres opciones:"
1. "Un trabajador local la hace (empleo doméstico)"
2. "Un trabajador extranjero la hace (offshoring / comercio de tareas)"
3. "Una máquina la hace (automatización)"

"¿Qué determina quién la hace? Los costos relativos. Si un trabajador en Vietnam hace la misma tarea por un décimo del costo y los costos de coordinación a distancia son bajos → offshoring. Si un robot la hace mejor y más barato → automatización. Si requiere presencia física, creatividad o interacción → se queda local."

"Esto unifica tres debates que suelen ir por separado: comercio internacional (quién produce qué), cambio tecnológico (qué se automatiza) y mercado de trabajo (qué empleos desaparecen y cuáles aparecen). Es el mismo problema: la asignación de tareas."

"En la Unidad 5 vamos a ver las cadenas globales de valor (CGV) como la manifestación concreta de esto: cómo las empresas fragmentan la producción en tareas y las distribuyen geográficamente. Y en la Unidad 7 vamos a ver cómo la automatización y la IA están cambiando la asignación de tareas. Todo parte de esta misma lógica."

PREGUNTA PARA ESTUDIANTES: "Piensen en una empresa argentina que conozcan. ¿Qué tareas hace internamente? ¿Cuáles terceriza? ¿Cuáles podrían irse al exterior?"

---

### Sección: Cierre

#### Slide 31: Unidad 3 completa — ¿Qué aprendimos?
**Tipo**: texto
**Título**: De los países a las firmas, de los bienes a las tareas
**Subtítulo**: El recorrido de la Unidad 3

**Contenido**:
- **Clase 4** (Krugman): economías de escala + diferenciación → IIT. GL, IIT H/V, NGE
- **Clase 5** — cuatro preguntas encadenadas:
  - **¿Qué lo determina?** → similitud, proximidad, escala, integración. Caso ARG-BRA
  - **¿Dónde se produce?** → Vernon: el producto viaja del innovador al imitador
  - **¿Quién exporta?** → Melitz: solo las mejores firmas, selección darwiniana
  - **¿A qué precio?** → Dumping como resultado natural de la competencia monopolística
  - **¿Qué se comercia?** → No bienes: tareas (Grossman & Rossi-Hansberg, Acemoglu & Autor)
- **Hilo conductor**: de un mundo de **países y sectores** (Ricardo, H-O) a un mundo de **firmas y tareas**

**Notas docente**:
RESUMEN (5 minutos)
"Hagamos el cierre de la Unidad 3. Fíjense cómo cada pieza encajó con la siguiente."

"Arrancamos preguntándonos qué determina el IIT. De ahí fuimos a dónde se produce — Vernon nos dijo que la producción se mueve con el ciclo del producto. Pero ¿quién toma la decisión? Las firmas, y no son iguales — Melitz nos mostró que solo las mejores exportan. Y cuando exportan, cobran distinto — lo que nos llevó al dumping, que resulta ser un fenómeno natural de la competencia monopolística. Y al final, el cambio de paradigma: no se comercian bienes, se comercian tareas."

"El gran mensaje de la Unidad 3: el nivel de análisis cambió radicalmente respecto de Ricardo y H-O. De países y sectores pasamos a firmas y tareas."

---

#### Slide 32: Evaluación Unidad 3
**Tipo**: texto
**Título**: Evaluación Unidad 3
**Subtítulo**: Se abre hoy, deadline miércoles 28 de mayo (2 semanas)

**Contenido**:
- **5 preguntas multiple choice + reflexión final**, integradas en un notebook Jupyter
- **Parte 1**: 3 preguntas conceptuales (Krugman, Melitz, dumping)
- **Parte 2**: 2 preguntas con procesamiento de datos reales (WTO antidumping + comercio bilateral ARG-BRA → cálculo GL por sector)
- **Reflexión final**: diagnóstico teórico del caso argentino (5-10 líneas)
- Archivo: `notebooks/Eval_U3_Krugman_Melitz_Dumping.ipynb`
- Datos en `notebooks/datos/`: WTO Anti-Dumping + UN Comtrade ARG-BRA bilateral por capítulo HS
- **Bonus quiz AhaSlides de hoy**: hasta +1 punto si participaron + acertaron ≥ 70%

**Notas docente**:
EVALUACIÓN U3 (3 minutos)
"La evaluación de la Unidad 3 ya está disponible. Es un notebook Jupyter que combina cinco preguntas multiple choice más una reflexión final. La pueden bajar del campus o de GitHub Pages."

ESTRUCTURA:
"Parte 1 — tres preguntas conceptuales sobre lo que vimos: el mecanismo de Krugman, el modelo de Melitz, y cómo distinguir dumping de competencia legítima. Estas se contestan con lo que aprendieron en clase y con la bibliografía (Lugones cap 2.1, Krugman caps 7-8, Bernard et al. 2007)."

"Parte 2 — dos preguntas con datos. Acá tienen que ejecutar el código que viene cargado en el notebook. Primer bloque: los CSV de WTO antidumping que vimos hoy en los slides 26-27 (origen de medidas argentinas). Segundo bloque: comercio bilateral Argentina-Brasil por capítulo HS, donde van a calcular el **índice Grubel-Lloyd** para 10 sectores y ver qué bienes tienen IIT alto (manufacturas industriales — Krugman) vs IIT bajo (commodities — Ricardo/H-O). El notebook hace los cálculos por ustedes — la tarea de ustedes es **interpretar** los resultados y elegir la opción correcta con justificación."

"Reflexión final — 5 a 10 líneas conectando ambos bloques de datos con el caso argentino. Pueden articular usando los conceptos que más les hayan llegado."

CONDICIONES Y PUNTAJE:
"Escala 0-100. Para promocionar la unidad necesitan ≥ 70. Cada pregunta MC vale 15 puntos (75 en total) y la reflexión vale 25 puntos."

"Y recuerden lo del quiz AhaSlides de inicio de clase: si participaron hoy y acertaron al menos 4 de las 5 preguntas (70%+), suman +1 punto al puntaje de esta evaluación (cap final en 100)."

DEADLINE:
"Tienen hasta el **miércoles 28 de mayo** para entregar. Suben el notebook completo (.ipynb) al campus UMET. Es importante que ejecuten todas las celdas antes de descargar, para que los gráficos queden visibles."

CONEXIÓN CON PARCIAL 1:
"El Parcial 1 es el promedio de las evaluaciones de U1 + U2 + U3. Con esta evaluación cierran ese parcial."

PREGUNTAS DEL AULA:
- "¿Se puede consultar con compañeros?" — Sí, pueden discutir entre ustedes, pero las respuestas finales son individuales. Justificaciones idénticas se consideran copia.
- "¿Se puede usar IA?" — Sí para entender conceptos o generar código adicional, pero las respuestas MC y la reflexión deben ser propias. La nota cae fuerte si la reflexión es genérica/templete de ChatGPT.
- "¿Y si no se ejecutan los datos?" — La parte 1 es teórica, no requiere datos. La parte 2 sí los necesita pero el notebook trae los CSVs cargados — no hay que descargar nada nuevo.

---

#### Slide 33: Material complementario
**Tipo**: texto
**Título**: Material complementario
**Subtítulo**: Para profundizar

**Contenido**:
- 🎬 **DW Documental** — "Made in China: el ascenso de un gigante industrial" (42 min, español) — ciclo del producto en acción
- 📺 **MRU (Marginal Revolution University)** — "Why Do Some Firms Export?" (8 min, inglés) — modelo de Melitz simplificado
- 📺 **Khan Academy** — "Dumping and Anti-dumping Duties" (12 min, inglés) — definición y ejemplos
- 🎬 **Netflix** — "American Factory" (110 min) — firma china Fuyao en EEUU, choque de culturas productivas, IED y offshoring
- 📺 **TED-Ed** — "What is the Product Life Cycle?" (5 min, inglés) — ciclo del producto animado
- 🎬 **DW Documental** — "Juego sin límites: La mentira del libre comercio" (42 min, español) — dumping, subsidios y defensa comercial

**Notas docente**:
MATERIAL COMPLEMENTARIO (2 minutos)
"Les dejo material para profundizar. 'American Factory' en Netflix es excelente: una fábrica de vidrio automotor de China (Fuyao) que abre en Ohio, EEUU. Muestra IED, diferencias culturales, conflictos laborales. Es el caso real de lo que teóricamente vimos hoy."

"El documental de DW sobre libre comercio toca dumping y subsidios agrícolas con ejemplos concretos. Y el video de MRU sobre 'Why Do Some Firms Export?' es un resumen de 8 minutos del modelo de Melitz, muy claro."

---

#### Slide 34: Lecturas — Unidad 3
**Tipo**: texto
**Título**: Lecturas — Unidad 3
**Subtítulo**: Obligatorias y complementarias

**Contenido**:
- **Obligatorias**:
  - Lugones, G. et al. — *Teorías del Comercio Internacional*, Cap. 2.1 (pp. 31-40): rendimientos crecientes y competencia imperfecta
  - Krugman, Obstfeld & Melitz (9a ed.) — Caps. 7 y 8: economías de escala, competencia monopolística, firmas heterogéneas, dumping
  - Lucángeli, J. (2007) — "La especialización intraindustrial en el MERCOSUR", CEPAL
  - Bernard, Jensen, Redding & Schott (2007) — "Firms in International Trade", JEP
- **Complementarias**:
  - Steinberg, F. (2004) — *La nueva teoría del comercio internacional y la política comercial estratégica*
  - Durán Lima & Álvarez (2008) — "Indicadores de comercio exterior y política comercial", CEPAL

**Notas docente**:
LECTURAS (2 minutos)
"Las lecturas obligatorias de la Unidad 3. Lugones cubre la base teórica de rendimientos crecientes. Krugman caps 7 y 8 son el corazón: economías de escala externas, competencia monopolística, firmas heterogéneas y dumping. Lucángeli aplica el GL al Mercosur. Y Bernard et al es el paper que documenta las diferencias entre firmas exportadoras y no exportadoras — es accesible, no tiene matemática pesada."

"Las complementarias: Steinberg conecta con política comercial estratégica, que es un tema de la Unidad 6. Durán Lima tiene la metodología detallada para calcular indicadores de comercio, incluyendo el GL."

---

#### Slide 35: Guía de lectura — Unidad 3
**Tipo**: texto
**Título**: Guía de lectura — Unidad 3
**Subtítulo**: Preguntas orientadoras para la bibliografía

**Contenido**:
- ¿Por qué el modelo de Krugman predice comercio entre países **similares** y no solo entre diferentes?
- ¿Qué mide el índice de Grubel-Lloyd y cómo se interpreta un GL cercano a 0 vs cercano a 1?
- ¿Cuál es la diferencia entre IIT **horizontal** (variedades) e IIT **vertical** (calidad)?
- Según Melitz, ¿por qué solo una **minoría** de firmas exporta? ¿Qué las distingue?
- ¿Qué predice el modelo de Melitz sobre los efectos de la **apertura** en la productividad de la industria?
- ¿Cuál es la diferencia entre **dumping**, **subsidio** y **competencia legítima por costos**?
- ¿Qué tres condiciones necesita el dumping para existir?
- ¿Cómo conecta el enfoque de **comercio de tareas** (Grossman & Rossi-Hansberg) con las cadenas globales de valor?

**Notas docente**:
GUÍA DE LECTURA (1 minuto)
"Esta guía orienta la lectura de la bibliografía. Las preguntas cubren los temas principales de ambas clases: desde Krugman y el GL hasta Melitz, dumping y comercio de tareas."

---

#### Slide 36: Próxima clase
**Tipo**: texto
**Título**: Próxima clase: Unidad 4 — Prebisch y el estructuralismo
**Subtítulo**: Clase 6, jueves 21 de mayo

**Contenido**:
- Cambiamos de perspectiva: de las "nuevas teorías" al enfoque **estructuralista latinoamericano**
- **Prebisch**: la tesis del deterioro de los términos de intercambio
- **Centro-periferia**: ¿por qué el comercio puede ser **desigual**?
- **CEPAL** e industrialización por sustitución de importaciones (ISI)
- Pregunta guía: ***¿Quién gana y quién pierde con el comercio internacional?***
- Lecturas: Lugones caps 2.2-2.3, Prebisch (1950), Diamand (1972)

**Notas docente**:
PRÓXIMA CLASE (2 minutos)
"La próxima clase empezamos la Unidad 4. Cambiamos radicalmente de perspectiva. Hasta acá, las teorías que vimos (Ricardo, H-O, Krugman, Melitz) son mayormente de tradición anglosajona. En la Unidad 4 entramos al estructuralismo latinoamericano: Prebisch, CEPAL, Diamand."

"La pregunta central cambia: ya no es '¿por qué comerciamos?' sino '¿quién gana y quién pierde?' Prebisch observó que los países exportadores de materias primas tendían a perder en los términos de intercambio frente a los exportadores de manufacturas. Eso generó toda una escuela de pensamiento sobre desarrollo, industrialización y política económica que sigue siendo central en América Latina."

"Traigan leído al menos el texto de Prebisch. Es corto y potente."

---

#### Slide 37: Preguntas
**Tipo**: cierre
**Título**: ¿Preguntas?
**Subtítulo**: Economía Internacional | Clase 5

**Notas docente**:
CIERRE (5 minutos)
Abrir espacio para preguntas. Temas que suelen generar consultas:
- ¿Melitz dice que la apertura siempre es buena? (No: dice que hay ganadores y perdedores, y que el ajuste es doloroso. El efecto neto sobre productividad es positivo, pero eso no significa que todos ganen.)
- ¿Todo dumping es malo? (No: el dumping "persistente" es natural en competencia monopolística. El predatorio sí es nocivo. La clave es distinguir mecanismos.)
- ¿El enfoque de tareas reemplaza a los modelos anteriores? (No: agrega una capa. Ricardo sigue explicando el comercio de commodities, Krugman el IIT, Melitz la selección de firmas. El enfoque de tareas explica la fragmentación de la producción.)

---

## Recursos

### Gráficos necesarios
| Archivo | Descripción | Estado |
|---------|-------------|--------|
| arg_bra_autos_2024.png | Barras X ARG→BRA y M ARG←BRA con callout GL≈0.92 | ✓ Existe |
| vernon_ciclo_producto.png | 3 fases del ciclo del producto, con flujos geográficos | ✓ Existe |
| melitz_seleccion.png | Distribución de productividad + umbrales (cerrar/local/exportar) | ✓ Existe |
| melitz_apertura.png | Efecto de apertura: ganadores y perdedores, cambio de umbral | ✓ Existe |
| evolucion_teorias.png | Tabla: Ricardo → Krugman → Melitz (basado en Bernard et al 2007) | ✓ Existe |
| dumping_arbol.png | Árbol de decisión: síntoma → diagnóstico → instrumento | ✓ Existe |
| comercio_tareas.png | Framework: tarea → trabajador local / extranjero / máquina | ✓ Existe |

### Imágenes
No se requieren imágenes externas para esta sesión. Las biografías de Vernon y Melitz son slides tipo texto.

---

## Notas de investigación

### Papers descargados para esta sesión
- Vernon (1966) "International Investment and International Trade in the Product Cycle", QJE → `bibliografia/unidad3/Vernon_1966_Product_Cycle_QJE.pdf`
- Melitz (2003) "The Impact of Trade on Intra-Industry Reallocations", Econometrica → `bibliografia/unidad3/Melitz_2003_Heterogeneous_Firms_Econometrica.pdf`
- Grossman & Rossi-Hansberg (2008) "Trading Tasks: A Simple Theory of Offshoring", AER → `bibliografia/unidad3/Grossman_Rossi-Hansberg_2008_Trading_Tasks_AER.pdf`
- Acemoglu & Autor (2011) "Skills, Tasks and Technologies", Handbook of Labor Economics → `bibliografia/unidad3/Acemoglu_Autor_2011_Skills_Tasks_Technologies.pdf`
- Bernard, Jensen, Redding & Schott (2007) "Firms in International Trade", JEP → ya existía en `bibliografia/unidad3/`

### Fuentes principales
- **Clase 8.docx**: IIT determinantes, GL numérico, caso ARG-BRA (Clase 6 del plan original)
- **Clase 9.docx**: Dumping completo — definición, tipologías, instrumentos, caso aplicado (Clase 9 del plan original)
- **Krugman Cap 8** (pp. 157-193): competencia monopolística, Melitz (pp. 173-180), dumping (pp. 180-182)
- **Lugones** (pp. 55, 58-59): Vernon y ciclo del producto
- **Bernard et al 2007 JEP**: Table 1 — evolución de teorías del comercio

### Conexiones con el usuario
- El usuario enfatizó la importancia del enfoque de tareas como puente a Acemoglu & Autor
- Opción C elegida: mención breve en S5 + profundización en U5
- El hilo Melitz → Grossman-Rossi-Hansberg → Acemoglu-Autor es central para el curso
- REESTRUCTURA: usuario pidió eliminar bloques, todo conectado narrativamente. Hilo: "¿Quién comercia, cómo y a qué precio?"
