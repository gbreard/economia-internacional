# Clase 4: Ricardo y la ventaja comparativa

## Metadata
- **Duración**: 2 horas
- **Unidad**: 2 — Teorías clásicas y neoclásicas del comercio internacional
- **Pregunta central**: ¿Por qué comercia un país que es "peor en todo"? (costos relativos, no absolutos)
- **Clase anterior**: Clase 3 (Mercantilistas y Adam Smith — ventaja absoluta y sus límites)
- **Clase siguiente**: Clase 5 (Modelo neoclásico estándar — dotaciones de recursos y precios relativos)

## Estado
Listo

## Para hacer
- [x] Generar gráfico: corn_laws_conflicto.png (triángulo distributivo: terratenientes-industriales-trabajadores)
- [x] Generar gráfico: costo_oportunidad_tabla.png (tabla + cálculos + patrón de comercio)
- [x] Generar gráfico: ventaja_comparativa_resultado.png (antes/después: autarquía vs comercio con 48hs)
- [x] Generar gráfico: terminos_intercambio.png (recta numérica con rango 1.33-2)
- [x] Generar gráfico: ppf_pais_a.png (PPF + línea de intercambio + ganancia)
- [x] Generar gráfico: ppf_pais_b.png (PPF + línea de intercambio + ganancia)
- [x] Generar gráfico: resumen_ricardo.png (diagrama de flujo: tecnología → costos → comercio → ganancias)
- [x] Generar gráfico: rca_argentina.png (composición exportadora y RCA sectorial)
- [x] Copiar generar_desde_md.py de clase03 → cambiar footer a "Clase 4"
- [x] Generar HTML y verificar en navegador

---

## Contenido

### Sección: Apertura

#### Slide 1: Portada
**Tipo**: portada
**Título**: Economía Internacional — Clase 4
**Subtítulo**: Ricardo y la ventaja comparativa: costos relativos, no absolutos

**Notas docente**:
APERTURA (2 minutos)

'Bienvenidos. La clase pasada cerramos con un problema: ¿qué pasa cuando un país es mejor en todo? Smith no tenía respuesta. Hoy la resolvemos con Ricardo: no importa ser el mejor en absoluto, importa qué sacrificás para producir cada bien. Eso se llama ventaja comparativa.'

---

#### Slide 2: Retomamos: el problema que Smith dejó abierto
**Tipo**: centrado
**Título**: ¿Recuerdan el problema de la clase pasada?
**Subtítulo**: País A es mejor que B en tela Y en vino. ¿B no comercia?

**Contenido**:
- A: Tela = 1 hora, Vino = 2 horas
- B: Tela = 6 horas, Vino = 8 horas
- A tiene **ventaja absoluta en ambos bienes**
- Smith no puede explicar por qué B exportaría algo
- **Hoy: Ricardo resuelve este problema**

**Notas docente**:
PUENTE CON CLASE 3 (3 minutos)

'La clase pasada terminamos con esta tabla y con un signo de interrogación. A es más eficiente en todo. Según Smith, A debería producir todo y B no tendría nada que ofrecer. Pero en la realidad sí hay comercio entre países desiguales — Bangladesh exporta textiles a Alemania, por ejemplo. Hoy Ricardo nos da la respuesta.'

Retomar el gráfico de la Clase 3 (limite_smith.png) mentalmente: el panel derecho estaba VACÍO. Hoy lo llenamos.

PREGUNTA RÁPIDA: '¿Alguien se quedó pensando en esto? ¿Cómo puede ser que B exporte algo si es peor en todo?'

---

#### Slide 3: Agenda
**Tipo**: agenda
**Título**: Agenda: Ricardo y la ventaja comparativa

**Contenido**:
- ¿Quién fue Ricardo? Biografía y contexto político (Corn Laws)
- Autarquía, precios relativos y costo de oportunidad
- Ventaja comparativa: quién exporta qué (ejemplo numérico)
- Frontera de posibilidades de producción y ganancias del comercio
- De la teoría a los datos: ventaja comparativa revelada (RCA)
- Qué explica Ricardo y qué deja abierto

**Notas docente**:
AGENDA (2 minutos)

'Hoy la clase tiene cuatro bloques: primero conocemos a Ricardo — quién fue, en qué contexto político escribió. Después hacemos el ejemplo numérico con los mismos datos de la clase pasada. Tercero, graficamos la frontera de producción para VER las ganancias del comercio. Y cerramos con cómo medimos esto en datos reales.'

'Aviso: hoy SÍ hay algo de matemática, pero es simple — sumas, divisiones y gráficos de rectas. Nada que no se pueda hacer con una calculadora.'

---

### Sección: Ricardo en contexto

#### Slide 4: ¿Quién fue David Ricardo?
**Tipo**: grafico_texto
**Título**: David Ricardo (1772-1823)
**Subtítulo**: De corredor de bolsa a padre del libre comercio

**Contenido**:
- Londres, 1772. Hijo de familia **judía sefardí** de origen holandés. Trabajó en la Bolsa de Londres desde los 14 años
- A los 21 se casa fuera de la fe, rompe con su familia y se hace **rico por cuenta propia** como corredor de bolsa
- A los 27 lee *La Riqueza de las Naciones* de Smith y se vuelca a la **economía política**
- Obra principal: ***Principios de economía política y tributación*** (1817) — distribución del ingreso entre renta, ganancias y salarios
- **Parlamentario** (1819-1823): defendió el libre comercio contra las Corn Laws
- Su argumento de **ventaja comparativa** sigue siendo uno de los más citados en toda la economía — 200 años después

**Imagen**: img/ricardo_portrait.jpg
**Fuente**: Retrato por Thomas Phillips (1821), National Portrait Gallery, Londres

**Notas docente**:
¿QUIÉN FUE RICARDO? (5 minutos)

'Antes de meternos en el modelo, ubiquemos a la persona. Ricardo no era un académico de torre de marfil — era un tipo que se hizo rico en la Bolsa y después se dedicó a pensar por qué el comercio funciona como funciona.'

DATOS BIOGRÁFICOS QUE ENGANCHAN:
- Su padre era corredor de bolsa en la Bolsa de Ámsterdam, emigró a Londres. Ricardo trabajó con él desde los 14.
- Se enamoró de una cuáquera (Priscilla Anne Wilkinson), se casó a los 21 y su familia lo desheredó. Arrancó de cero y se hizo millonario.
- Compró una banca en el Parlamento (sí, en esa época se compraban) y desde ahí peleó por abolir las Corn Laws.
- Murió joven, a los 51, de una infección de oído. En solo 6 años de escritura cambió la economía para siempre.

CONEXIÓN CON SMITH: 'Smith era filósofo moral, profesor universitario. Ricardo era un hombre de negocios metido en política. Eso se nota en sus textos: Smith es amplio y narrativo; Ricardo es conciso, va al hueso, usa ejemplos numéricos.'

ANÉCDOTA: 'Ricardo y Malthus eran amigos íntimos pero discrepaban en casi todo. Se escribían cartas constantemente debatiendo sobre renta, comercio y población. Es una de las rivalidades intelectuales más productivas de la historia de la economía.'

PREGUNTA: '¿Les parece que importa que Ricardo haya sido rico? ¿Eso sesga su teoría a favor del libre comercio?'
(Discusión abierta — no hay respuesta única. Pero notar que Ricardo argumentaba contra los terratenientes, que eran los más ricos de su época.)

---

#### Slide 5: Las Corn Laws: el comercio como política
**Tipo**: grafico_texto
**Título**: Ricardo (1817): libre comercio en medio de un conflicto distributivo
**Subtítulo**: Las Corn Laws y el precio del pan

**Contenido**:
- **1815**: tras las Guerras Napoleónicas, se aprueban las **Corn Laws** → protegen precio del grano
- Alimentos caros → sube costo de vida → conflicto **terratenientes vs industriales vs trabajadores**
- Ricardo (Principles, 1817): la ventaja comparativa es el argumento **técnico** para una política → abrir comercio abarata bienes clave
- Ricardo entra al **Parlamento** (1819): no es solo teoría, es acción política

**Gráfico**: graficos/corn_laws_conflicto.png
**Fuente**: Elaboración propia

**Notas docente**:
RICARDO EN CONTEXTO (8 minutos)

No arrancar con la tabla. Primero el contexto político — como hicimos con Smith.

¿QUÉ FUERON LAS CORN LAWS?
"Corn" en inglés británico = granos/cereales (trigo sobre todo). Las Corn Laws son restricciones a la importación de grano para mantener precios altos. Se aprueban en 1815, justo cuando terminan las Guerras Napoleónicas y se espera que vuelva el grano barato de Europa.

¿POR QUÉ SE APRUEBAN?
Los terratenientes (landowners) tienen enorme poder en el Parlamento y temen que la competencia externa baje el precio de sus tierras. Las Corn Laws los protegen: impiden importar grano barato → el precio interno se mantiene alto → la renta de la tierra sube.

EL CONFLICTO:
- Terratenientes: ganan con protección (renta alta)
- Industriales: pierden (comida cara → presión sobre salarios → baja ganancia)
- Trabajadores/consumidores: pierden (pan caro → menor nivel de vida)

'Ricardo no escribía desde un escritorio: estaba metido en este debate. Su teoría de ventaja comparativa es el argumento técnico para decir "abramos el comercio de granos porque nos abarata el pan y reorganiza la economía".'

DATO: Las Corn Laws se derogan recién en 1846, después de una enorme campaña de la Anti-Corn Law League (1839) y agravadas por la hambruna irlandesa (1845).

DATO ADICIONAL PARA EL AULA:
Ricardo no solo escribía: era parlamentario (1819-1823). Murió en 1823 sin ver la derogación de las Corn Laws.

¿RICARDO Y MARX?
Marx nace en 1818 y Ricardo muere en 1823 — se solapan 5 años pero Marx era un niño. No hubo debate directo. Lo que sí pasa: Marx toma a Ricardo como el pico de la economía clásica y lo critica a fondo en El Capital y en Theories of Surplus Value. Marx parte de Ricardo para construir su propia teoría del valor-trabajo.

'Frase fácil: Corn Laws = protección del precio del pan. Y el comercio se vuelve un tema de vida cotidiana, no de tecnicismo.'

---

#### Slide 6: Ricardo y la distribución: ¿quién se queda con el ingreso?
**Tipo**: texto
**Título**: La gran pregunta de Ricardo: renta, salarios y ganancias
**Subtítulo**: El comercio no es neutral — cambia la distribución

**Contenido**:
- Ricardo organiza la economía por **tres ingresos**: renta (tierra), salarios (trabajo), ganancias (capital)
- Si sube el precio del grano → sube costo de vida → presión sobre salarios → **cae la ganancia industrial**
- Protección agrícola → beneficia terratenientes, perjudica a industriales y trabajadores
- **El comercio redistribuye**: importar grano barato → baja renta, sube ganancia, abarata consumo

**Notas docente**:
DISTRIBUCIÓN EN RICARDO (5 minutos)

Esta es la pieza que conecta la teoría con la política. Ricardo no solo pregunta "qué se comercia" — pregunta "qué pasa con la distribución del ingreso".

'En el mundo de Ricardo hay tres clases con tres tipos de ingreso: terratenientes que cobran renta, capitalistas que obtienen ganancias, y trabajadores que cobran salarios. Si protegés el grano, subís la renta (los terratenientes ganan) pero encarecés la comida (los trabajadores y los industriales pierden). El comercio aparece como herramienta para reorganizar eso.'

CADENA DE TRANSMISIÓN (para pizarrón):
Protección grano → precio alimentos ↑ → costo de vida ↑ → salarios presionados al alza → ganancia industrial ↓ → renta de la tierra ↑

'Entonces el argumento de Ricardo no es "libre comercio porque sí". Es: si abrís el comercio de granos, abaratás la comida, bajás presión sobre salarios, y eso permite que la economía industrial crezca. Es un argumento distributivo, no solo de eficiencia.'

CONEXIÓN CON CLASE 3: Esto es compatible con Smith (comercio genera eficiencia), pero Ricardo agrega un punto nuevo: el comercio también cambia QUIÉN gana y QUIÉN pierde dentro del país. Esta dimensión distributiva va a ser central cuando lleguemos a Stolper-Samuelson (Clase 6).

PREGUNTA: '¿Les suena este debate en Argentina? ¿Retenciones a exportaciones agropecuarias, tipo de cambio, precio de los alimentos?'
(Respuesta esperable: las retenciones son un debate similar — campo vs industria vs consumidores)

---

### Sección: El modelo ricardiano

#### Slide 7: Autarquía y precios relativos
**Tipo**: texto
**Título**: Autarquía: el punto de partida
**Subtítulo**: Cada país solo, con sus propios precios

**Contenido**:
- **Autarquía** = economía cerrada: todo lo que consume se produce internamente
- En autarquía, cada país tiene un **precio relativo interno** (determinado por su tecnología)
- **Precio relativo** = cuánto de un bien "cuesta" en términos del otro
- **Costo de oportunidad** = cuántas unidades del otro bien sacrifico para producir 1 unidad de este
- Si los precios relativos son **distintos** entre países → hay incentivo a comerciar

**Notas docente**:
AUTARQUÍA Y PRECIOS RELATIVOS (5 minutos)

'Antes de hablar de comercio, pensemos en un mundo sin comercio. Cada país produce y consume solo. En ese mundo aparecen precios internos: cuánto "cuesta" el vino en términos de tela, o viceversa.'

DEFINICIÓN CLARA:
Autarquía = sin comercio exterior. Todo lo que consumís lo producís vos. Es el "antes" contra el que comparamos el "después" (con comercio).

COSTO DE OPORTUNIDAD — LA DEFINICIÓN CLAVE:
'Costo de oportunidad = lo que dejás de producir cuando elegís producir algo. Si dedicás horas a hacer vino, esas horas no las usás para tela. Entonces el "costo" del vino no es solo el trabajo directo — es la tela que sacrificaste.'

SUPUESTOS DEL MODELO RICARDIANO (simplificados):
- 2 países, 2 bienes, 1 factor (trabajo)
- Productividad distinta por bien y por país
- Competencia perfecta, rendimientos constantes
- Sin costos de transporte

'Estos supuestos son simplificaciones para VER el mecanismo. Después, en clases futuras, los relajamos.'

PREGUNTA: 'Si un país produce solo para sí mismo, ¿qué determina el precio de cada bien?'
(Respuesta: la tecnología — cuánto trabajo necesita cada bien)

---

#### Slide 8: Costos de oportunidad: el cálculo clave
**Tipo**: grafico_texto
**Título**: Costos de oportunidad: ¿qué sacrifica cada país?
**Subtítulo**: Los mismos números de la clase pasada, distinta lectura

**Contenido**:
- **País A**: 1 Tela cuesta 0,5 Vinos. 1 Vino cuesta 2 Telas
- **País B**: 1 Tela cuesta 0,75 Vinos. 1 Vino cuesta 1,33 Telas
- A sacrifica **menos** para producir Tela → **ventaja comparativa en Tela**
- B sacrifica **menos** para producir Vino → **ventaja comparativa en Vino**
- A exporta Tela, B exporta Vino — **B tiene algo para exportar**

**Gráfico**: graficos/costo_oportunidad_tabla.png
**Fuente**: Elaboración propia

**Notas docente**:
COSTOS DE OPORTUNIDAD — EL NÚCLEO (10 minutos)

Este es el slide más importante de la clase. Tomarse el tiempo para hacerlo bien.

TABLA DE HORAS (la misma de la Clase 3):
         Tela    Vino
País A:   1 h     2 h
País B:   6 h     8 h

A es más eficiente en AMBOS bienes (ventaja absoluta).

CÁLCULO PASO A PASO:

'Para calcular el costo de oportunidad, la pregunta es: ¿cuánto del otro bien sacrifico?'

COSTO DE 1 TELA (en Vinos sacrificados):
- A: Producir 1 tela = 1 hora. Esa hora podría hacer 1/2 = 0,5 vinos. → Costo = 0,5V
- B: Producir 1 tela = 6 horas. Esas horas podrían hacer 6/8 = 0,75 vinos. → Costo = 0,75V
- A sacrifica MENOS vino → A tiene ventaja comparativa en Tela ✓

COSTO DE 1 VINO (en Telas sacrificadas):
- A: Producir 1 vino = 2 horas. Esas horas podrían hacer 2/1 = 2 telas. → Costo = 2T
- B: Producir 1 vino = 8 horas. Esas horas podrían hacer 8/6 = 1,33 telas. → Costo = 1,33T
- B sacrifica MENOS tela → B tiene ventaja comparativa en Vino ✓

'Miren lo que pasa: A es mejor en todo EN ABSOLUTO, pero B es relativamente MENOS malo en Vino. La desventaja de B es 6:1 en tela pero solo 4:1 en vino. Esa diferencia relativa es la ventaja comparativa.'

FRASE PARA QUE RECUERDEN: 'No importa ser el mejor en absoluto. Importa en qué sos relativamente menos malo — ahí está tu ventaja.'

EJEMPLO COTIDIANO: '¿Messi debería cortar el pasto de su casa? Probablemente lo haga más rápido que un jardinero, pero su costo de oportunidad es enorme — esas horas las puede usar jugando al fútbol. Le conviene "especializarse" en fútbol y "importar" el servicio de jardinería.'

CONFUSIÓN COMÚN: Los alumnos mezclan "eficiente" con "ventaja comparativa". Insistir: la ventaja comparativa es sobre costos RELATIVOS, no absolutos.

---

#### Slide 9: El precio mundial: ¿de dónde sale y qué rango tiene?
**Tipo**: grafico_texto
**Título**: El precio mundial: ¿de dónde sale?
**Subtítulo**: Cuando dos países se abren al comercio, aparece un precio internacional

**Contenido**:
- En autarquía cada país tiene su **precio interno** (= su costo de oportunidad): A valúa 1V = 2T, B valúa 1V = 1,33T
- Al abrirse al comercio aparece un **precio mundial**: un precio relativo al que ambos intercambian
- Ese precio se forma por **oferta y demanda internacionales** — no lo fija ningún país solo
- Para que ambos ganen, el precio debe caer **entre** los precios internos: **1,33 < P < 2**
- Usamos P = 1,6 como ejemplo → ambos están mejor que en autarquía

**Gráfico**: graficos/terminos_intercambio.png
**Fuente**: Elaboración propia

**Notas docente**:
EL PRECIO MUNDIAL — CONCEPTO CLAVE (10 minutos)

'Hasta ahora calculamos costos de oportunidad y sabemos quién exporta qué. Pero falta una pieza: ¿a qué precio intercambian? Acá es donde aparece el concepto de precio mundial.'

¿QUÉ ES EL PRECIO MUNDIAL?
'Cuando dos países se abren al comercio, los precios internos ya no rigen solos. Aparece un ÚNICO precio relativo al que ambos comercian — el precio mundial o precio internacional. No es el precio de A ni el de B: es un precio nuevo que emerge del encuentro entre lo que uno quiere vender y lo que el otro quiere comprar.'

¿CÓMO SE CONSTRUYE?
'En un modelo simple de 2 países, el precio mundial se determina por la oferta y demanda recíprocas:
- A quiere comprar vino (porque le sale caro producirlo) → demanda de vino
- B quiere vender vino (porque es su ventaja comparativa) → oferta de vino
- El precio se ajusta hasta que la cantidad que A quiere comprar coincide con la que B quiere vender.'

'Ricardo no formalizó esto completamente — fue John Stuart Mill (1848) quien introdujo la "demanda recíproca" para determinar el precio exacto. Pero Ricardo sí estableció los LÍMITES:'

EL RANGO (esto es lo que Ricardo sí resuelve):
Precio relativo del Vino en Telas (P_V/P_T):
- Precio interno de A: 1V = 2T (el "techo" — si el precio mundial fuera mayor, A preferiría producirlo)
- Precio interno de B: 1V = 1,33T (el "piso" — si el precio mundial fuera menor, B no querría venderlo)
- Rango: 1,33 < P < 2

¿POR QUÉ DENTRO DEL RANGO AMBOS GANAN?
'Si el precio mundial es P = 1,6 telas por vino:'
- Para A: en autarquía, 1V le cuesta 2T. Con comercio, compra 1V por 1,6T → ahorra 0,4T por cada vino. Le conviene comprar afuera.
- Para B: en autarquía, producir 1V le cuesta 1,33T. Con comercio, vende 1V por 1,6T → gana 0,27T extra por cada vino. Le conviene vender afuera.

'Los dos están mejor que solos. Ese es el poder del precio mundial intermedio.'

¿QUÉ PASA FUERA DEL RANGO?
- Si P < 1,33: A querría comprar vino pero B no querría venderlo (le sale más caro que producirlo)
- Si P > 2: B querría vender vino pero A prefiere producirlo (le sale más barato adentro)

ANALOGÍA: 'Piensen en Mercado Libre: el vendedor tiene un precio mínimo (su costo), el comprador tiene un precio máximo (lo que está dispuesto a pagar). Si hay un precio en el medio, se hace la transacción y ambos ganan. El rango de Ricardo es exactamente eso.'

PREGUNTA: '¿Quién se beneficia más: el que está cerca de su precio interno o el que está lejos?'
(Respuesta: el que está más lejos de su precio interno gana más. Si P = 1,6, A ahorra 0,4T por vino — B solo gana 0,27T. El precio más cercano a B favorece a A.)

CONEXIÓN: 'Recuerden el indicador de Términos de Intercambio de la Clase 2 (TdI = P_expo/P_impo). Acá estamos viendo la versión teórica del mismo concepto: el precio relativo al que un país comercia determina cuánto gana.'

---

#### Slide 10: Ventaja comparativa en acción: ahora sí, con números
**Tipo**: grafico_texto
**Título**: Ventaja comparativa en acción: autarquía vs comercio
**Subtítulo**: Con precio mundial P = 1,6, ambos terminan con más (dotación: 48 horas)

**Contenido**:
- **Autarquía** (24 hs cada bien): A produce 24T + 12V, B produce 4T + 3V
- **Con comercio**: A se especializa en Tela (48T), B en Vino (6V)
- A compra 12V al precio mundial 1,6 T/V → paga 19,2T → le quedan **28,8T + 12V** (gana +4,8T)
- B vende 3V al precio mundial 1,6 T/V → recibe 4,8T → le quedan **4,8T + 3V** (gana +0,8T)
- **Mismo vino, más tela**: ambos ganan — el precio mundial intermedio lo hace posible

**Gráfico**: graficos/ventaja_comparativa_resultado.png
**Fuente**: Elaboración propia

**Notas docente**:
VENTAJA COMPARATIVA EN ACCIÓN (8 minutos)

'Ahora que sabemos de dónde sale el precio mundial y por qué P = 1,6 está en el rango, veamos qué pasa con la producción y el consumo.'

CON 48 HORAS, en autarquía repartiendo 50/50:
- A: 24h tela → 24 telas, 24h vino → 12 vinos
- B: 24h tela → 4 telas, 24h vino → 3 vinos
- Total mundial: 28 telas + 15 vinos

CON ESPECIALIZACIÓN TOTAL:
- A: 48h en tela → 48 telas, 0 vinos
- B: 48h en vino → 0 telas, 6 vinos
- Total mundial: 48 telas + 6 vinos

'Ojo: la producción total de tela sube (28 → 48) pero la de vino baja (15 → 6). La especialización total no siempre aumenta todo — redistribuye. Lo importante es que con INTERCAMBIO al precio mundial, ambos pueden terminar mejor que en autarquía.'

EL INTERCAMBIO CONCRETO (al precio mundial P = 1,6):
- A tiene 48T y quiere vino. Compra 12V a 1,6T cada uno → paga 19,2T → queda con 28,8T + 12V
- Comparación: en autarquía tenía 24T + 12V → ganó +4,8 telas manteniendo el mismo vino
- B tiene 6V y quiere tela. Vende 3V a 1,6T cada uno → recibe 4,8T → queda con 4,8T + 3V
- Comparación: en autarquía tenía 4T + 3V → ganó +0,8 telas manteniendo el mismo vino

'Las ganancias son desiguales (+4,8T vs +0,8T) porque el precio mundial P = 1,6 está más cerca del precio de B que del de A. Si el precio fuera 1,9 (más cerca de A), B ganaría más y A menos. Pero dentro del rango, AMBOS ganan algo.'

PREGUNTA: '¿Por qué B se especializa en vino si A produce vino más barato en absoluto?'
(Respuesta: porque el costo de oportunidad de B en vino es menor — 1,33T vs 2T. No importa quién es más rápido, importa quién sacrifica menos.)

---

### Sección: Frontera de posibilidades y ganancias del comercio

#### Slide 11: La Frontera de Posibilidades de Producción (PPF)
**Tipo**: formula
**Título**: Frontera de Posibilidades de Producción (PPF)
**Subtítulo**: Todo lo que un país puede producir con sus recursos

**Contenido**:
- **PPF** = combinaciones máximas de producción dados los recursos
- Con 48 horas de trabajo, la restricción es: $a_{LT} \times T + a_{LV} \times V = L$
- **País A** (Tela=1h, Vino=2h): $T + 2V = 48$ → máx T = 48, máx V = 24
- **País B** (Tela=6h, Vino=8h): $6T + 8V = 48$ → máx T = 8, máx V = 6
- La **pendiente** de la PPF = costo de oportunidad = precio relativo en autarquía

**Notas docente**:
PPF — LA HERRAMIENTA GRÁFICA (5 minutos)

'La PPF es simplemente la línea que muestra todas las combinaciones posibles de producción. En el modelo ricardiano (1 factor, rendimientos constantes), es una recta.'

CONSTRUIR EN PIZARRÓN (o señalar en el slide):
País A: si pone todo en Tela: 48/1 = 48 telas. Si pone todo en Vino: 48/2 = 24 vinos. La PPF es la recta que une (T=48, V=0) con (T=0, V=24).

País B: todo en Tela: 48/6 = 8 telas. Todo en Vino: 48/8 = 6 vinos. PPF une (T=8, V=0) con (T=0, V=6).

PENDIENTE:
- A: por cada vino adicional, sacrifica 2 telas (pendiente = -2)
- B: por cada vino adicional, sacrifica 4/3 ≈ 1,33 telas (pendiente = -4/3)

'La pendiente de la PPF ES el costo de oportunidad. Para A, el vino es "caro" (cuesta 2 telas); para B, el vino es relativamente "barato" (cuesta 1,33 telas). Por eso B exporta vino.'

LA CLAVE: en autarquía, solo podés consumir lo que producís → estás limitado a la PPF. Con comercio, podés consumir FUERA de la PPF. Eso lo vemos en los próximos slides.

---

#### Slide 12: PPF País A: la ganancia del comercio
**Tipo**: grafico_texto
**Título**: País A: consumir más allá de lo que puede producir
**Subtítulo**: La línea de intercambio "sale" de la PPF

**Contenido**:
- **PPF de A**: recta de (T=48, V=0) a (T=0, V=24). Pendiente: -2
- A se especializa en Tela (produce 48T) y compra Vino a precio mundial (1,6T por V)
- **Línea de intercambio**: T = 48 - 1,6V → más plana que la PPF
- Ejemplo: para consumir V=10 → autarquía: T=28 | comercio: T=32 → **ganancia = +4 telas**
- La línea de intercambio está **por encima** de la PPF → nuevas combinaciones posibles

**Gráfico**: graficos/ppf_pais_a.png
**Fuente**: Elaboración propia

**Notas docente**:
PPF PAÍS A — GANANCIAS DEL COMERCIO (8 minutos)

'Este gráfico es donde se "VE" la ganancia del comercio. La PPF es lo máximo que A puede producir solo. La línea de intercambio muestra lo que puede CONSUMIR con comercio.'

GUÍA PARA LEER EL GRÁFICO:
- Eje horizontal: Vino (V)
- Eje vertical: Tela (T)
- PPF (línea sólida): combinaciones de producción en autarquía
- Línea de intercambio (línea punteada): combinaciones de consumo con comercio
- Zona sombreada entre ambas: la GANANCIA del comercio

CÓMO SE CONSTRUYE LA LÍNEA DE INTERCAMBIO:
1. A se especializa 100% en Tela → produce (T=48, V=0)
2. Desde ese punto, puede "comprar" vino a precio 1,6T por V
3. Si quiere 1V, da 1,6T → queda (T=46,4, V=1)
4. Si quiere 10V, da 16T → queda (T=32, V=10)
5. Ecuación: T = 48 - 1,6V

COMPARACIÓN PUNTO A PUNTO:
- En autarquía (PPF): T = 48 - 2V. Para V=10: T = 28
- Con comercio: T = 48 - 1,6V. Para V=10: T = 32
- Ganancia: +4 telas manteniendo los mismos 10 vinos

'Cada punto donde la línea de intercambio está por encima de la PPF es una combinación de consumo que era IMPOSIBLE en autarquía. Eso es la ganancia del comercio.'

PREGUNTA: '¿Por qué la línea de intercambio es más plana que la PPF?'
(Respuesta: porque el precio mundial del vino es 1,6T, menor que el costo de oportunidad interno de A que es 2T. Comprar vino afuera es más barato que producirlo.)

---

#### Slide 13: PPF País B: el país "peor en todo" también gana
**Tipo**: grafico_texto
**Título**: País B también gana: comercio como nueva frontera
**Subtítulo**: Incluso siendo menos productivo en todo, B consume más con comercio

**Contenido**:
- **PPF de B**: recta de (T=8, V=0) a (T=0, V=6). Pendiente: -4/3
- B se especializa en Vino (produce 6V) y vende a precio mundial (1,6T por V)
- **Línea de intercambio**: T = 9,6 - 1,6V → intercepto T más alto que PPF (9,6 > 8)
- Ejemplo: para consumir V=3 → autarquía: T=4 | comercio: T=4,8 → **ganancia = +0,8 telas**
- **B puede consumir combinaciones imposibles en autarquía**

**Gráfico**: graficos/ppf_pais_b.png
**Fuente**: Elaboración propia

**Notas docente**:
PPF PAÍS B — EL "PEOR EN TODO" TAMBIÉN GANA (8 minutos)

Este slide es el que "mata" la intuición equivocada. Si Ricardo tiene razón, B gana del comercio a pesar de ser menos productivo en todo.

GUÍA PARA LEER EL GRÁFICO:
- PPF de B: recta de (T=8, V=0) a (T=0, V=6)
- Línea de intercambio: parte de (T=0, V=6) — B se especializa en vino — y sube a (T=9,6, V=0)
- En autarquía, si B no produce vino, máximo de tela = 8
- Con comercio, si B vende TODO su vino, obtiene 6 × 1,6 = 9,6 telas
- 9,6 > 8 → la línea de intercambio está POR ENCIMA de la PPF

CÓMO SE CONSTRUYE:
B produce 6V. Vende vino a 1,6T por V.
T = (6 - V) × 1,6 = 9,6 - 1,6V

EJEMPLO:
- Para V=3: Autarquía T = 8 - (4/3)×3 = 4. Comercio T = 9,6 - 4,8 = 4,8. Ganancia: +0,8T
- Para V=0: Autarquía T = 8. Comercio T = 9,6. Ganancia: +1,6T

'El país "peor en todo" gana. No importa que A sea más productivo: lo que importa es que el precio mundial le permite a B obtener tela más barata que produciéndola. B vende vino (donde su desventaja es menor) y compra tela (donde su desventaja es mayor).'

FRASE CLAVE: 'Esto es exactamente lo que pasa con Bangladesh y la ropa, o con muchos países en desarrollo que exportan productos donde su desventaja es menor. No necesitan ser los mejores — necesitan tener un costo de oportunidad menor en al menos un bien.'

PREGUNTA: '¿Qué pasaría si el precio mundial fuera exactamente 1,33 o exactamente 2?'
(Respuesta: toda la ganancia iría a uno solo — el otro queda indiferente entre comercio y autarquía)

---

#### Slide 14: Resumen del modelo ricardiano
**Tipo**: grafico_texto
**Título**: Ricardo en un slide: el mecanismo completo
**Subtítulo**: De la autarquía a las ganancias del comercio

**Contenido**:
- **Paso 1**: En autarquía, cada país tiene precios relativos internos (por su tecnología)
- **Paso 2**: Diferencias tecnológicas → costos de oportunidad distintos → ventaja comparativa
- **Paso 3**: Cada país se especializa donde su costo de oportunidad es menor
- **Paso 4**: Comercian a un precio mundial intermedio → ambos consumen fuera de su PPF
- **Resultado**: ganancias del comercio para AMBOS países, incluso si uno es "mejor en todo"

**Gráfico**: graficos/resumen_ricardo.png
**Fuente**: Elaboración propia

**Notas docente**:
RESUMEN RICARDO (5 minutos)

'Esto es Ricardo: el comercio nace de diferencias relativas, no absolutas. Esas diferencias generan precios relativos distintos en autarquía, aparece un precio mundial intermedio, y eso expande el conjunto de consumo.'

DIAGRAMA (el gráfico muestra este flujo):
Tecnología distinta → Costos de oportunidad distintos → Precios relativos en autarquía distintos → Especialización (ventaja comparativa) → Comercio a precio mundial intermedio → Ganancias del comercio (consumo fuera de la PPF)

'Con esto tenemos el motor clásico del comercio. Después, otras teorías cambian la FUENTE de la ventaja comparativa (factores, escala, tecnología dinámica), pero el corazón del mecanismo queda.'

CONEXIÓN CON SMITH: 'Smith decía "cada uno produce lo que hace más barato". Ricardo refina: "cada uno produce donde su costo de oportunidad es menor". Smith requiere ventaja absoluta; Ricardo muestra que basta con ventaja comparativa.'

CONEXIÓN CON CLASE 3: 'Ahora el panel derecho del gráfico de la clase pasada se llena: B exporta vino (ventaja comparativa) y ambos ganan.'

---

### Sección: De la teoría a los datos

#### Slide 15: Ventaja comparativa revelada (RCA)
**Tipo**: formula
**Título**: ¿Cómo "vemos" la ventaja comparativa en datos?
**Subtítulo**: Índice de Balassa (1965): Ventaja Comparativa Revelada (RCA)

**Contenido**:
- Ricardo habla de ventajas comparativas → pero ¿cómo las medimos?
- **Béla Balassa** (1965): propone "revelar" la ventaja a partir de lo que efectivamente se exporta
- $RCA_{i,k} = \frac{X_{i,k} / X_{i}}{X_{w,k} / X_{w}}$ → participación del producto en exportaciones del país vs del mundo
- **RCA > 1**: el país exporta ese bien más que el promedio mundial → **especialización**
- **RCA < 1**: el país está menos especializado que el mundo en ese bien

**Notas docente**:
RCA / BALASSA (7 minutos)

'Ricardo nos dio el mecanismo teórico. Pero para ir a datos necesitamos una herramienta. Balassa la propone en 1965.'

¿QUIÉN FUE BALASSA?
Béla Balassa (1928-1991): economista húngaro-estadounidense. Publicó "Trade Liberalisation and 'Revealed' Comparative Advantage" (1965, The Manchester School). La idea: si no podemos observar directamente los costos de oportunidad de cada país, podemos INFERIR la ventaja comparativa a partir de lo que realmente exportan.

LA FÓRMULA EXPLICADA:
- Numerador: ¿qué porcentaje de las exportaciones del país es ese producto?
- Denominador: ¿qué porcentaje de las exportaciones MUNDIALES es ese producto?
- Si el país exporta un producto MÁS que el promedio mundial → RCA > 1 → está especializado

EJEMPLO SENCILLO:
Si las exportaciones de soja son el 15% de las exportaciones de Argentina, pero solo el 3% de las exportaciones mundiales → RCA = 15/3 = 5 → Argentina tiene fuerte ventaja comparativa revelada en soja.

ADVERTENCIA IMPORTANTE:
'RCA es un indicador DESCRIPTIVO, no causal. Mezcla tecnología + política comercial + tipo de cambio + subsidios + historia. Que un país tenga RCA > 1 no significa que "debería" exportar eso — puede ser resultado de distorsiones.'

PREGUNTA: '¿Si Argentina tiene RCA alto en soja, es porque tiene ventaja comparativa genuina o porque hay tipo de cambio favorable, subsidios, o simplemente abundancia de tierra?'
(Respuesta: probablemente todas juntas — RCA no distingue causas)

---

#### Slide 16: RCA en la práctica: Argentina, ¿especialización ricardiana?
**Tipo**: grafico_texto
**Título**: Argentina: ¿qué revela su patrón exportador?
**Subtítulo**: Composición de exportaciones y especialización sectorial

**Contenido**:
- Argentina muestra fuerte RCA en **productos primarios y agroindustriales** (soja, maíz, carne, aceites)
- RCA bajo en **manufacturas de origen industrial** (maquinaria, electrónica, automotriz complejo)
- Pregunta ricardiana: ¿es tecnología (costo de oportunidad) o es dotación de recursos + historia + política?
- El RCA **cambia en el tiempo**: refleja transformaciones productivas, precios y política comercial

**Gráfico**: graficos/rca_argentina.png
**Fuente**: Elaboración propia a partir de datos WITS / Banco Mundial

**Notas docente**:
RCA ARGENTINA — DEBATE (8 minutos)

Este slide es para DISCUTIR, no para "dar la respuesta".

DATOS DE REFERENCIA (Argentina, circa 2019):
- Productos primarios: RCA alto (soja, cereales, carne)
- Manufacturas de origen agropecuario (MOA): RCA alto (aceites, harinas, biodiesel)
- Manufacturas de origen industrial (MOI): RCA generalmente < 1 (con excepciones: tubos de acero, algunos autos)
- Energía: variable (pasó de exportador neto a importador neto y está volviendo con Vaca Muerta)

DEBATE "A LO RICARDO":
'Si miramos esto con los lentes de Ricardo: Argentina se especializa en lo que le cuesta relativamente menos — alimentos y materias primas — y "desertificó" industrias donde su costo relativo era mayor. ¿Les parece que eso es solo tecnología/costos de oportunidad, o hay más?'

DEBATE "A LO SMITH":
'Smith diría: ¿el tamaño del mercado argentino permite la especialización industrial profunda? ¿El comercio amplió mercados para Argentina o la encasilló en primarios?'

PREGUNTA PROVOCADORA:
'¿Este patrón de especialización es "natural" (ventaja comparativa genuina) o es "construido" (resultado de historia + política + tipo de cambio)?'
(No resolver — esto se retoma en la Unidad 4 con Prebisch y los estructuralistas)

'Un adelanto: Prebisch (Clase 11) va a decir que esta especialización es PARTE DEL PROBLEMA, no la solución. Los estructuralistas ven en este patrón una trampa, no una ventaja.'

CONEXIÓN CON CLASE 2: 'Recuerden los indicadores: la composición exportadora de Argentina que medimos en la Clase 2 con el índice de comercio. Ahora le ponemos el marco teórico.'

---

### Sección: Cierre

#### Slide 17: ¿Qué explica Ricardo y qué deja abierto?
**Tipo**: texto
**Título**: Ricardo: motor potente, preguntas abiertas
**Subtítulo**: Cada pregunta abre una clase futura

**Contenido**:
- **Explica**: por qué hay comercio incluso entre países muy desiguales. Mecanismo: costos relativos → especialización → ganancias mutuas
- **¿De dónde sale la ventaja comparativa si no es solo tecnología?** → Heckscher-Ohlin (Clase 6)
- **¿Quién gana y quién pierde dentro del país?** → Stolper-Samuelson (Clase 6), política comercial (Clase 17)
- **¿Por qué hay comercio entre países parecidos y dentro del mismo sector?** → Comercio intraindustrial (Clases 7-8)
- **¿Qué pasa con costos de transporte, empresas dominantes, cadenas globales?** → Firmas heterogéneas, CGV (Clase 10)

**Notas docente**:
LIMITACIONES / TEASER (5 minutos)

'Ricardo nos dio un motor potente. Pero deja preguntas abiertas — y cada una abre una puerta a lo que viene.'

REPASAR CADA PREGUNTA:

1. FUENTE DE LA VENTAJA: Ricardo dice "tecnología" (productividad). ¿Pero y si la ventaja viene de tener más capital, más tierra, más trabajo calificado? → Heckscher-Ohlin.

2. DISTRIBUCIÓN: Ricardo habla de ganancias para "el país", pero ¿quién gana y quién pierde adentro? Si Argentina se abre al comercio, el sector agropecuario gana pero la industria puede perder. → Stolper-Samuelson, política comercial.

3. COMERCIO ENTRE SIMILARES: Alemania y Francia comercian mucho entre sí, y exportan e importan los MISMOS tipos de bienes (autos, maquinaria). Ricardo no explica eso — su modelo predice especialización INTER-industrial. → Comercio intraindustrial, Krugman.

4. MUNDO REAL: En Ricardo no hay costos de transporte, no hay empresas con poder de mercado, no hay cadenas globales de valor. → Firmas heterogéneas (Melitz), CGV.

'No es que Ricardo esté "equivocado" — es que es una primera aproximación. Como todo modelo, ilumina algo y oscurece otro. Las próximas clases van completando el panorama.'

---

#### Slide 18: Resumen de la clase
**Tipo**: texto
**Título**: Lo que vimos hoy

**Contenido**:
- **Contexto**: Ricardo escribe en el debate por las Corn Laws — el comercio redistribuye
- **Ventaja comparativa**: lo que importa es el costo de oportunidad (relativo), no la eficiencia absoluta
- **Modelo**: precios relativos en autarquía → especialización → comercio a precio intermedio → ganancias mutuas
- **PPF**: la línea de intercambio está por encima de la PPF → ambos consumen más
- **RCA (Balassa)**: herramienta para "ver" la ventaja comparativa en datos reales

**Notas docente**:
RESUMEN (3 minutos)

Recapitular los 4 bloques:
1. Contexto político: Ricardo no escribía en abstracto — las Corn Laws, el precio del pan, renta vs ganancias
2. Modelo: costos de oportunidad como clave; la ventaja comparativa; el rango de precios
3. PPF: la herramienta gráfica que muestra las ganancias del comercio
4. RCA: el puente a los datos — cómo medimos especialización

'Hoy resolvimos el problema de la clase pasada: B SÍ tiene algo para exportar. No importa ser el mejor en absoluto — importa qué sacrificás. Eso es Ricardo, y es uno de los argumentos más poderosos de toda la economía.'

---

#### Slide 19: Bibliografía y lecturas
**Tipo**: texto
**Título**: Lecturas para esta clase
**Subtítulo**: Bibliografía del curso

**Contenido**:
- **Lugones, G. et al.** — Teorías del Comercio Internacional: sección sobre Ricardo, ventaja comparativa y costos de oportunidad
- **Krugman, Obstfeld & Melitz** — Economía Internacional: capítulo 3 (modelo ricardiano, PPF, ganancias del comercio)
- Para contexto histórico: notas de Clase 3 (Smith) + debate Corn Laws
- **Balassa, B. (1965)** — "Trade Liberalisation and 'Revealed' Comparative Advantage" (The Manchester School)

**Notas docente**:
BIBLIOGRAFÍA (2 minutos)

'Para repasar, lean la sección de Ricardo en Lugones y el capítulo 3 de Krugman-Obstfeld-Melitz. La formalización con PPF está bien explicada ahí. Balassa es opcional: lo mencionamos para que sepan de dónde viene el indicador RCA.'

Krugman-Obstfeld-Melitz Cap. 3 es especialmente bueno para los gráficos de PPF y ganancias del comercio — tiene el mismo tipo de ejemplo que hicimos en clase.

---

#### Slide 20: Material complementario
**Tipo**: texto
**Título**: Material complementario
**Subtítulo**: Videos y documentales recomendados

**Contenido**:
- **"Conociendo al capital: David Ricardo"** (Canal Encuentro, 26 min, en español) — Documental argentino sobre Ricardo y su contribución a la economía política. Ideal para repasar lo que vimos hoy
- **"Capitalism" Ep.3: Ricardo and Malthus** (Ilan Ziv, 2014, 52 min) — Documental en profundidad con entrevistas a Piketty, Varoufakis y Chomsky. Cómo Ricardo y Malthus reestructuran la sociedad a imagen del mercado
- **"The Deceptive Promise of Free Trade"** (DW Documentary, 2018, YouTube, 43 min) — Crítica al libre comercio actual: la brecha entre la teoría ricardiana y la realidad de las negociaciones comerciales
- **Khan Academy: Ventaja comparativa** (khanacademy.org, en español, 10-15 min) — Ejercicios numéricos paso a paso para reforzar costos de oportunidad y PPF

**Notas docente**:
MATERIAL COMPLEMENTARIO (2 minutos)

Presentar brevemente los videos. El de Canal Encuentro es el más accesible: está en español, es corto y va directo a Ricardo.

Links para compartir con los alumnos:
- Conociendo al capital: buscar "Conociendo al capital David Ricardo Canal Encuentro" en YouTube, o en encuentro.gob.ar
- Capitalism Ep.3: disponible en OVID.tv y bibliotecas universitarias (buscar "Capitalism Ilan Ziv Episode 3 Ricardo")
- DW Documentary: https://www.youtube.com/watch?v=DnW9ZQtI1_E
- Khan Academy: https://es.khanacademy.org/economics-finance-domain/microeconomics/basic-economic-concepts-gen-micro/comparative-advantage-and-the-gains-from-trade

'Si ven un solo video, vean el de Canal Encuentro — 26 minutos, en español, y les cuenta quién fue Ricardo con más detalle del que pudimos ver hoy. El de DW es para los que quieran pensar críticamente: ¿funciona el libre comercio como prometía Ricardo?'

---

#### Slide 21: Preguntas
**Tipo**: cierre
**Título**: ¿Preguntas?
**Subtítulo**: Economía Internacional | Clase 4

**Notas docente**:
CIERRE (3 minutos)

Abrir espacio para preguntas.

Recapitular la idea central:
'Hoy resolvimos el problema que Smith dejó abierto: incluso si un país es peor en todo, tiene ventaja comparativa en algo. El mecanismo es elegante: costos de oportunidad, especialización, precio intermedio. La próxima clase preguntamos: ¿y si la ventaja no viene de la tecnología sino de los FACTORES de producción? Ahí entramos al modelo neoclásico.'

'Nos vemos la próxima con dotaciones de recursos, curvas de transformación y precios relativos.'

---

## Recursos

### Gráficos necesarios (carpeta graficos/)
| Archivo | Descripción | Slide | Estado |
|---------|-------------|-------|--------|
| corn_laws_conflicto.png | Triángulo distributivo terratenientes-industriales-trabajadores | 5 | ✓ Listo |
| costo_oportunidad_tabla.png | Tabla horas + cálculo costos de oportunidad + patrón | 8 | ✓ Listo |
| terminos_intercambio.png | Recta numérica con rango 1.33-2 y ejemplo 1.6 | 9 | ✓ Listo |
| ventaja_comparativa_resultado.png | Antes/después: autarquía vs comercio con 48hs | 10 | ✓ Listo |
| ppf_pais_a.png | PPF + línea de intercambio + zona de ganancia | 12 | ✓ Listo |
| ppf_pais_b.png | PPF + línea de intercambio + zona de ganancia | 13 | ✓ Listo |
| resumen_ricardo.png | Diagrama de flujo: tecnología → costos → comercio → ganancias | 14 | ✓ Listo |
| rca_argentina.png | Composición exportadora Argentina y RCA sectorial | 16 | ✓ Listo |

### Imágenes (carpeta img/)
| Archivo | Descripción | Slide | Estado |
|---------|-------------|-------|--------|
| ricardo_portrait.jpg | Retrato de David Ricardo por Thomas Phillips (1821) | 4 | ✓ Listo |

---

## Notas de investigación

### Datos para gráficos
- Costos de oportunidad: A: Tela=1h, Vino=2h; B: Tela=6h, Vino=8h (mismos que Clase 3 slide 12)
- PPF con 48 horas: A: MaxT=48, MaxV=24; B: MaxT=8, MaxV=6
- Precio mundial ejemplo: P_V/P_T = 1,6
- RCA Argentina: datos hardcodeados de WITS/Banco Mundial circa 2019

### Conexiones con otras clases
- Clase 3: limite_smith.png (panel vacío que hoy llenamos), números A:1,2 B:6,8
- Clase 2: indicadores (TdI, composición exportadora)
- Clase 5: modelo neoclásico (curvas de transformación, precios relativos)
- Clase 6: Heckscher-Ohlin (fuente de ventaja comparativa = factores)
- Clase 11: Prebisch (la especialización como trampa, no como solución)
- Clase 17: política comercial (aranceles, protección — debate Corn Laws actualizado)

### Contexto histórico para notas docente
- Corn Laws (1815-1846): protección agrícola → precio del pan
- Anti-Corn Law League (1839): movimiento pro libre comercio
- Ricardo parlamentario (1819-1823): acción política directa
- Ricardo y Marx: no contemporáneos intelectuales, Marx lo critica a posteriori
- Balassa (1965): formaliza RCA como indicador empírico
