# Clase 5: El modelo neoclásico estándar — Dotaciones y precios relativos

## Metadata
- **Duración**: 2 horas
- **Unidad**: 2 — Teorías clásicas y neoclásicas del comercio internacional
- **Pregunta central**: ¿Qué pasa cuando abandonamos el mundo de un solo factor de Ricardo? (PPF curva, preferencias, especialización parcial)
- **Clase anterior**: Clase 4 (Ricardo — ventaja comparativa, costos de oportunidad, PPF lineal, ganancias del comercio)
- **Clase siguiente**: Clase 6 (Heckscher-Ohlin — dotaciones de factores, Stolper-Samuelson, paradoja de Leontief)

## Estado
En progreso

## Para hacer
- [ ] Generar gráfico: ppf_recta_vs_curva.png (comparación PPF Ricardo vs neoclásico)
- [ ] Generar gráfico: rendimientos_decrecientes.png (por qué la PPF se curva)
- [ ] Generar gráfico: equilibrio_autarquia.png (PPF + curva de indiferencia + tangencia)
- [ ] Generar gráfico: dos_paises_autarquia.png (dos paneles: país A vs B con distintos precios relativos)
- [ ] Generar gráfico: oferta_demanda_relativa.png (OR, OR*, DR → precio mundial)
- [ ] Generar gráfico: comercio_ppf_curva.png (PPF + línea de precios mundiales + consumo fuera PPF)
- [ ] Generar gráfico: resumen_ricardo_vs_neoclasico.png (tabla comparativa visual)
- [ ] Copiar generar_desde_md.py de clase04 → cambiar footer a "Clase 5"
- [ ] Generar HTML y verificar en navegador

## Tabla de recursos

### Gráficos (graficos/)

| Archivo | Slide | Descripción | Estado |
|---------|-------|-------------|--------|
| ppf_recta_vs_curva.png | 9 | PPF lineal (Ricardo) vs PPF cóncava (neoclásico) | Pendiente |
| rendimientos_decrecientes.png | 10 | Diagrama: por qué 2 factores + rend. decrec. = PPF curva | Pendiente |
| equilibrio_autarquia.png | 12 | PPF + curva de indiferencia + tangencia = precio relativo | Pendiente |
| dos_paises_autarquia.png | 13 | Dos paneles mostrando distintos precios relativos en autarquía | Pendiente |
| oferta_demanda_relativa.png | 15 | OR, OR*, DR → precio de equilibrio mundial | Pendiente |
| comercio_ppf_curva.png | 16 | PPF + línea de precios mundiales + punto de consumo fuera PPF | Pendiente |
| resumen_ricardo_vs_neoclasico.png | 18 | Tabla visual comparativa de los dos modelos | Pendiente |

### Imágenes (img/)

| Archivo | Slide | Descripción | Estado |
|---------|-------|-------------|--------|
| haberler_portrait.jpg | 6 | Retrato de Gottfried Haberler | Pendiente (slide cambiado a tipo texto por ahora) |

---

## Contenido

### Sección: Apertura

#### Slide 1: Portada
**Tipo**: portada
**Título**: Economía Internacional — Clase 5
**Subtítulo**: El modelo neoclásico estándar: dotaciones y precios relativos

**Notas docente**:
APERTURA (2 minutos)

'Bienvenidos. Las últimas dos clases armamos la caja de herramientas clásica: Smith nos explicó por qué el comercio es bueno (mercado más grande, más especialización, más productividad), y Ricardo nos dio EL mecanismo: la ventaja comparativa. Hoy damos un salto: ¿qué pasa cuando el mundo es más complejo que el de Ricardo?'

---

#### Slide 2: ¿Qué nos dejó Ricardo?
**Tipo**: centrado
**Título**: Repaso rápido: ¿qué sabemos hasta acá?
**Subtítulo**: Los clásicos nos dieron un motor potente... pero con limitaciones

**Contenido**:
- **Smith**: el comercio amplía el mercado → más especialización → más productividad
- **Ricardo**: ventaja comparativa por **costos relativos** (no absolutos) → ambos ganan
- **Herramienta**: PPF lineal, 1 factor (trabajo), especialización total
- **Pero**: ¿de dónde sale la diferencia de tecnología? ¿Quién gana y quién pierde *dentro* del país? ¿La especialización es siempre total?

**Notas docente**:
REPASO (3 minutos)

'Tres preguntas rápidas para ver si quedó claro lo de la clase pasada:'

1. '¿Qué es ventaja comparativa?' (Respuesta esperada: menor costo de oportunidad)
2. '¿Un país que es peor en todo puede exportar algo?' (Sí — lo que le cuesta relativamente menos)
3. '¿De dónde viene la ventaja comparativa en Ricardo?' (De diferencias de tecnología/productividad)

'Perfecto. Ahora: Ricardo usa UN solo factor — trabajo. La PPF es una recta. Los países se especializan TOTALMENTE (producen solo un bien). Y no dice nada sobre quién gana y quién pierde adentro del país. Hoy empezamos a soltar esos supuestos.'

---

#### Slide 3: Agenda
**Tipo**: agenda
**Título**: Agenda: el modelo neoclásico estándar

**Contenido**:
- ¿Qué limitaciones tiene Ricardo? Las preguntas que dejó abiertas
- Contexto histórico: la revolución marginalista y el entreguerras
- La tríada tecnología-poder-comercio en el período neoclásico
- El salto técnico: de 1 factor a 2 → la PPF se curva
- Equilibrio en autarquía: curvas de indiferencia y precios relativos
- Del equilibrio interno al comercio: especialización parcial y ganancias
- Resumen: Ricardo vs modelo neoclásico estándar

**Notas docente**:
AGENDA (2 minutos)

'La clase de hoy tiene tres partes. Primero, el contexto: ¿quiénes construyen esta nueva caja de herramientas y por qué? Segundo, la parte técnica: qué cambia cuando pasamos de 1 factor a 2 — la PPF se curva, aparecen las curvas de indiferencia, y la especialización ya no es total. Tercero: cómo funciona el comercio en este nuevo marco.'

'Es una clase más conceptual que la anterior — menos cuentas, más gráficos y más intuición.'

---

### Sección: Las limitaciones de Ricardo

#### Slide 4: ¿Qué no puede explicar Ricardo?
**Tipo**: texto
**Título**: Cinco limitaciones del modelo ricardiano
**Subtítulo**: Un motor potente... pero incompleto

**Contenido**:
- **1 solo factor** (trabajo): no hay capital, ni tierra, ni trabajo calificado vs no calificado → no puede hablar de distribución del ingreso
- **PPF recta**: costo de oportunidad constante → especialización siempre total (todo o nada)
- **Tecnología diferente** entre países: ¿por qué? Ricardo no lo explica — la toma como dada
- **Sin preferencias**: los consumidores no aparecen, no hay oferta ni demanda — solo costos
- **Mundo de 2×2×1**: dos países, dos bienes, un factor. ¿Qué pasa con más factores, más bienes, más países?

**Notas docente**:
LIMITACIONES (5 minutos)

'Ricardo es genial, pero es una PRIMERA aproximación. Pensemos qué falta.'

IR PUNTO POR PUNTO:

1. UN FACTOR: 'En la realidad, producir requiere trabajo, capital, tierra, tecnología. Si solo tenés trabajo, no podés preguntar: ¿qué pasa con los salarios vs las ganancias del capital cuando abrís el comercio? Ricardo no puede responder eso — y es UNA DE LAS PREGUNTAS MÁS IMPORTANTES de la economía internacional.'

2. PPF RECTA: 'Si la PPF es recta, el costo de producir un vino más siempre es el mismo (0,5 telas). Pero en la realidad, cuanto más producís de algo, más difícil se pone. Si Argentina mete todas sus hectáreas a soja, tiene que usar tierras cada vez peores → el costo sube. Eso hace que la PPF se curve.'

3. TECNOLOGÍA: 'Ricardo asume que A y B tienen tecnologías DIFERENTES. Pero no explica POR QUÉ. ¿Es porque están en climas distintos? ¿Tienen distinta educación? ¿Distinto capital? Los neoclásicos van a decir: quizás la tecnología es la MISMA, y lo que difiere son los RECURSOS.'

4. SIN PREFERENCIAS: 'En Ricardo no hay consumidores eligiendo. El precio se determina solo por costos. Pero en la realidad, la demanda también importa para fijar precios relativos.'

5. MUNDO 2×2×1: 'Es útil para la intuición, pero necesitamos un marco más general.'

PREGUNTA: '¿Cuál de estas limitaciones les parece más grave? ¿Cuál limita más la utilidad del modelo?'

---

### Sección: Contexto histórico — La revolución marginalista

#### Slide 5: De la economía política a la economía "científica"
**Tipo**: texto
**Título**: La revolución marginalista (1870s): un cambio de paradigma
**Subtítulo**: De Smith y Ricardo a una nueva forma de pensar la economía

**Contenido**:
- **1871-1874**: tres autores publican casi al mismo tiempo ideas similares: **Jevons** (Inglaterra), **Menger** (Austria), **Walras** (Suiza)
- Cambian el **eje del análisis**: de clases sociales (renta, salarios, ganancias) a **individuos** que eligen en el margen
- Del **valor-trabajo** (el valor de un bien depende del trabajo para producirlo) al **valor-utilidad** (depende de cuánto lo valora el consumidor)
- Nueva herramienta: **equilibrio general** — todos los mercados se determinan simultáneamente
- En comercio internacional: se puede reformular la ventaja comparativa **sin depender** de la teoría del valor-trabajo

**Notas docente**:
REVOLUCIÓN MARGINALISTA (8 minutos)

'Esto es un cambio de paradigma — como pasar de Newton a Einstein, pero en economía.'

CONTEXTO: Los clásicos (Smith, Ricardo, Marx) pensaban en CLASES SOCIALES: terratenientes, capitalistas, trabajadores. El valor de un bien venía del trabajo necesario para producirlo (teoría del valor-trabajo). Los marginalistas dicen: no, el valor viene de la utilidad que le da el ÚLTIMO consumidor (utilidad marginal).

LOS TRES MARGINALISTAS:
- William Stanley Jevons (1835-1882): inglés, The Theory of Political Economy (1871). Matemático, busca hacer de la economía una ciencia exacta.
- Carl Menger (1840-1921): austríaco, Grundsätze (1871). Funda la escuela austríaca. Más filosófico, menos matemático.
- Léon Walras (1834-1910): franco-suizo, Éléments (1874). Crea el equilibrio general: un sistema de ecuaciones donde TODOS los mercados se equilibran al mismo tiempo.

¿POR QUÉ IMPORTA PARA COMERCIO?
'Porque con esta nueva caja de herramientas podés tener más de un factor, podés tener preferencias de los consumidores, podés tener equilibrio simultáneo de todos los mercados. No necesitás que el valor venga del trabajo — podés usar costos de oportunidad directamente.'

DATO PARA EL AULA: 'Los clásicos preguntaban: ¿cómo se DISTRIBUYE el ingreso entre clases? Los marginalistas preguntan: ¿cómo se ASIGNAN recursos escasos entre usos alternativos? Es un cambio de pregunta fundamental.'

---

#### Slide 6: Haberler y el puente al modelo estándar
**Tipo**: texto
**Título**: Gottfried Haberler (1900-1995): la PPF sin valor-trabajo
**Subtítulo**: El puente técnico de Ricardo al modelo neoclásico

**Contenido**:
- Economista **austríaco**, formado en Viena con Mises y Hayek. Emigra a EEUU (Harvard, 1936)
- Obra clave: *The Theory of International Trade* (1936)
- **Contribución fundamental**: reformula la frontera de posibilidades de producción usando **costos de oportunidad**, sin necesitar la teoría del valor-trabajo
- Esto permite: **múltiples factores** de producción → la PPF se curva → especialización parcial
- Haberler construye la **caja de herramientas** que después usarán Heckscher, Ohlin, Samuelson

**Notas docente**:
HABERLER (5 minutos)

'Si Ricardo es el que inventa la idea de ventaja comparativa, Haberler es el que la traduce al lenguaje moderno. Sin Haberler, no podríamos usar la PPF con más de un factor.'

BIOGRAFÍA BREVE:
- Nace en Austria en 1900. Estudia en Viena en el seminario de Ludwig von Mises (escuela austríaca).
- En 1936 publica The Theory of International Trade — un tratado que reformula toda la teoría del comercio usando costos de oportunidad en vez de valor-trabajo.
- Ese mismo año emigra a Harvard, donde será profesor hasta los 70s. Muere en 1995 a los 95 años.

¿QUÉ HIZO EXACTAMENTE?
'Ricardo decía: el valor de un bien depende de las horas de trabajo para producirlo. Pero si tenés DOS factores (trabajo y capital), ¿cómo sumás horas de trabajo con unidades de capital? No se puede. Haberler dice: no necesitás medir valor en trabajo. Medí directamente cuánto del otro bien sacrificás — eso es el costo de oportunidad. Y con eso podés dibujar la PPF para cualquier cantidad de factores.'

'Con dos factores y rendimientos decrecientes, la PPF ya no es una recta: es una CURVA. Y eso cambia todo.'

CONEXIÓN CON LA CLASE: 'Haberler es el que arma la caja de herramientas que vamos a usar hoy. Después, Heckscher y Ohlin (Clase 6) le ponen el contenido: la ventaja comparativa viene de las dotaciones de factores.'

---

#### Slide 7: El entreguerras: ¿libre comercio en un mundo que se cierra?
**Tipo**: texto
**Título**: Contexto: las teorías nacen en un mundo convulsionado
**Subtítulo**: 1919-1939: proteccionismo, crisis y colapso del comercio

**Contenido**:
- **1914-1918**: la Primera Guerra Mundial destruye la primera globalización
- **1919**: Heckscher publica su artículo seminal sobre dotaciones y comercio
- **1929-1930**: crisis financiera → **Smoot-Hawley** (EEUU sube aranceles a niveles récord) → guerra comercial global
- **1933**: Ohlin publica *Interregional and International Trade* en plena Gran Depresión
- **1936**: Haberler reformula la PPF → el modelo estándar toma forma mientras el comercio mundial se desploma
- Paradoja: las teorías que justifican el libre comercio se escriben en la época de **mayor proteccionismo** del siglo XX

**Notas docente**:
ENTREGUERRAS (7 minutos)

'Esto es clave para entender el CONTEXTO de las ideas. Estas teorías no se escriben en una época de libre comercio feliz — se escriben cuando el comercio se está desplomando.'

LÍNEA DE TIEMPO PARA EL AULA:
- 1914-1918: WWI rompe la primera globalización (la que vimos en Clase 1). Los países se cierran.
- 1919: Heckscher escribe "The Effect of Foreign Trade on the Distribution of Income" — en Suecia, un país pequeño y abierto que depende del comercio. Es un artículo seminal, pero casi nadie lo lee en su momento (está en sueco).
- 1920s: intento de volver al patrón oro, pero con tensiones enormes.
- 1929: crack bursátil → Gran Depresión.
- 1930: EEUU aprueba la Smoot-Hawley Tariff Act: aranceles altísimos a más de 20.000 productos. Los socios comerciales responden con represalias → el comercio mundial cae un 65% entre 1929 y 1934.
- 1933: Ohlin publica su libro. Gana el Nobel en 1977.
- 1936: Haberler publica su tratado. Keynes publica la Teoría General el mismo año.

PREGUNTA: '¿No les parece raro que las teorías a favor del libre comercio se escriban justo cuando el mundo se está cerrando? ¿Por qué creen que pasa eso?'

(Respuesta sugerida: precisamente PORQUE el mundo se cierra, los economistas sienten urgencia de demostrar que el proteccionismo tiene costos. Las teorías son respuestas a problemas concretos — igual que Ricardo escribió por las Corn Laws.)

'Frase para recordar: las teorías del comercio son hijas de las CRISIS del comercio.'

---

#### Slide 8: La tríada tecnología-poder-comercio en el modelo neoclásico
**Tipo**: texto
**Título**: La tríada en el período neoclásico
**Subtítulo**: ¿Qué cambia en cada pilar respecto de Ricardo?

**Contenido**:
- **Tecnología**: el modelo neoclásico ASUME que es **igual** entre países. Gran cambio: si todos tienen la misma tecnología, la ventaja comparativa viene de OTRO lado → **dotaciones de recursos**
- **Poder**: la hegemonía británica se derrumba, EEUU asciende pero no lidera aún. Vacío de poder → proteccionismo, guerras comerciales, colapso del patrón oro
- **Comercio**: las reglas se quiebran. No hay orden multilateral (la OMC no existe hasta 1995, el GATT recién en 1947). Cada país pone aranceles como quiere → el comercio se desploma
- **Implicancia política del modelo**: si la ventaja viene de dotaciones "naturales" (tierra, capital, trabajo), la especialización parece **inevitable** — argumento potente para el libre comercio

**Notas docente**:
LA TRÍADA (5 minutos)

'En la Clase 1 instalamos la idea de que el comercio internacional se entiende como la interacción de tres fuerzas: tecnología, poder y reglas. Veamos cómo juegan en este período.'

TECNOLOGÍA:
'Este es el cambio conceptual más grande. Ricardo decía: los países comercian porque tienen DIFERENTE tecnología. El modelo neoclásico dice: ¿y si la tecnología es la MISMA? Entonces la ventaja comparativa tiene que venir de otra fuente: los recursos que tiene cada país. Argentina tiene mucha tierra fértil → exporta alimentos. Japón tiene mucho capital y trabajo calificado → exporta manufactura. No es porque tengan diferente tecnología — es porque tienen diferentes recursos.'

PODER:
'Entre 1919 y 1939 no hay un líder claro del sistema comercial. Gran Bretaña ya no puede sostener el libre comercio como en el siglo XIX. EEUU es la mayor economía pero es proteccionista (Smoot-Hawley). No hay reglas multilaterales. Resultado: cada uno por su cuenta, y el comercio colapsa.'

COMERCIO / REGLAS:
'No hay OMC, no hay GATT, no hay nada. Las "reglas" son bilaterales, cambiantes y frecuentemente retaliatorias. Recién en 1947, después de OTRA guerra mundial, se crea el GATT para evitar que esto pase de nuevo.'

IMPLICANCIA POLÍTICA (CLAVE):
'Si la ventaja comparativa viene de dotaciones naturales (tierra, clima, minerales), entonces la especialización parece "natural" y el libre comercio parece óptimo. Pero ojo: los estructuralistas (Prebisch, que veremos en Unidad 4) van a cuestionar esto: ¿es "natural" que Argentina exporte soja y no aviones? ¿O es resultado de la historia y el poder?'

PREGUNTA: '¿Les parece que las dotaciones son realmente "naturales"? ¿O se construyen? Piensen en Corea del Sur: en 1960 era un país agrícola y pobre. Hoy exporta semiconductores. ¿Cambió su "dotación" o cambió su política?'

---

### Sección: El salto técnico — De 1 factor a 2

#### Slide 9: La PPF recta vs la PPF curva
**Tipo**: grafico_texto
**Título**: ¿Qué cambia cuando hay más de un factor?
**Subtítulo**: La frontera de posibilidades de producción se curva

**Contenido**:
- **Ricardo** (1 factor): costo de oportunidad **constante** → PPF recta → especialización **total**
- **Neoclásico** (2+ factores): costo de oportunidad **creciente** → PPF cóncava → especialización **parcial**
- Razón: al reasignar recursos, los factores no son igualmente productivos en ambos bienes
- La PPF curva refleja que cada unidad adicional del bien cuesta **más** que la anterior

**Gráfico**: graficos/ppf_recta_vs_curva.png
**Fuente**: Elaboración propia

**Notas docente**:
PPF RECTA vs CURVA (8 minutos)

'Este es el gráfico más importante de la clase. Dos paneles: a la izquierda, la PPF de Ricardo (recta); a la derecha, la PPF neoclásica (curva).'

¿POR QUÉ LA PPF DE RICARDO ES RECTA?
'Porque solo hay un factor (trabajo) y los rendimientos son constantes. Si cada vino cuesta 2 horas y cada tela 1 hora, el costo de oportunidad siempre es 0,5. No importa si estás produciendo mucho o poco vino — siempre sacrificás lo mismo.'

¿POR QUÉ LA PPF NEOCLÁSICA ES CURVA?
'Porque hay dos factores (trabajo y capital) y rendimientos decrecientes en cada uno. Pensalo así: Argentina produce trigo y manufactura. Si quiere producir más trigo, al principio puede usar la mejor tierra pampeana — alta productividad, bajo costo. Pero si quiere MÁS trigo, tiene que empezar a usar tierras de peor calidad, necesita más capital para irrigar, etc. Cada tonelada adicional cuesta más en términos de manufactura sacrificada.'

EJEMPLO EN PIZARRÓN:
'Si Argentina dedica el 50% de sus recursos a trigo y 50% a manufacturas, puede producir (50T, 40M). Si quiere pasar a 70% trigo, no obtiene 70T sino quizás 65T, porque la tierra marginal rinde menos. Y sacrifica más manufactura (baja a 25M en vez de 28M).'

CONSECUENCIA CLAVE — ESPECIALIZACIÓN PARCIAL:
'Con PPF recta (Ricardo), si te conviene producir tela, producís SOLO tela. Con PPF curva, a medida que te especializás, el costo sube. Entonces llegás a un punto donde no conviene seguir especializándose. Resultado: especialización PARCIAL — producís más de un bien que del otro, pero no dejás de producir el otro completamente.'

'Esto es mucho más realista que Ricardo: Argentina exporta soja pero también produce autos. No se especializa al 100%.'

---

#### Slide 10: ¿Por qué se curva? Rendimientos decrecientes
**Tipo**: grafico_texto
**Título**: Rendimientos decrecientes: la razón técnica de la PPF curva
**Subtítulo**: Al reasignar factores, la productividad marginal baja

**Contenido**:
- Con **1 factor**: reasignar trabajo de vino a tela tiene siempre el mismo costo
- Con **2 factores**: vino usa mucho trabajo, tela usa mucho capital. Al mover recursos de vino a tela, los primeros trabajadores se adaptan bien, pero después hay **desajuste**: sobra capital, falta trabajo especializado
- **Rendimientos decrecientes**: cada unidad adicional de un factor aporta menos producción → costo de oportunidad creciente
- Resultado: la PPF se "infla" hacia adentro → forma **cóncava**

**Gráfico**: graficos/rendimientos_decrecientes.png
**Fuente**: Elaboración propia

**Notas docente**:
RENDIMIENTOS DECRECIENTES (5 minutos)

'La razón técnica de que la PPF se curve es que los factores no son perfectamente sustituibles entre sectores.'

EJEMPLO DIDÁCTICO:
'Imaginemos que tenemos dos fábricas: una de ropa (intensiva en trabajo) y una de autos (intensiva en capital/maquinaria). Si cierro un poco la fábrica de ropa y mando trabajadores a la de autos, al principio funcionan bien — pueden operar máquinas que estaban subutilizadas. Pero si sigo mandando trabajadores, empiezan a sobrar personas y no hay suficientes máquinas para todos. La productividad marginal cae.'

'Al revés: si mando capital de autos a ropa, al principio ayuda (mejores máquinas de coser). Pero llega un punto donde tener más máquinas sin suficientes costureras no agrega nada.'

FORMALIZACIÓN SIMPLE:
'La productividad marginal de cada factor DISMINUYE a medida que se agrega más de ese factor manteniendo el otro constante. Esto es lo que los economistas llaman rendimientos decrecientes del factor.'

CONEXIÓN: 'Esto es lo que hace que la PPF sea cóncava (curvada hacia el origen). Y eso tiene una consecuencia enorme para el comercio: la especialización ya no es total.'

---

#### Slide 11: Los supuestos del modelo neoclásico estándar
**Tipo**: texto
**Título**: Los supuestos: ¿en qué mundo estamos?
**Subtítulo**: Un modelo 2 × 2 × 2

**Contenido**:
- **2 países** (A y B), **2 bienes** (tela y alimentos), **2 factores** (trabajo L y capital K)
- **Misma tecnología** en ambos países (mismas funciones de producción)
- **Rendimientos decrecientes** en cada factor
- **Competencia perfecta** en todos los mercados (bienes y factores)
- **Factores móviles** entre sectores dentro del país, pero **inmóviles** entre países
- **Mismos gustos** en ambos países (mismas curvas de indiferencia)
- **Sin costos de transporte** ni barreras al comercio
- La **única diferencia** entre países: distinta dotación relativa de factores (K/L)

**Notas docente**:
SUPUESTOS (5 minutos)

'Todo modelo simplifica la realidad. La gracia es saber QUÉ se simplifica y POR QUÉ.'

RECORRER LOS SUPUESTOS:

MISMA TECNOLOGÍA: 'Este es el supuesto más fuerte y el más diferente respecto de Ricardo. Si la tecnología es igual, ¿por qué comercian? Porque tienen DISTINTA PROPORCIÓN de factores. Argentina: mucha tierra, poco capital. Japón: mucho capital, poca tierra. Eso solo alcanza para generar precios distintos y comercio.'

RENDIMIENTOS DECRECIENTES: 'Ya lo vimos — es lo que curva la PPF.'

COMPETENCIA PERFECTA: 'Nadie tiene poder de mercado. Los precios reflejan costos. Esto lo vamos a relajar en Clase 7 con Krugman (competencia imperfecta).'

FACTORES INMÓVILES ENTRE PAÍSES: 'Los trabajadores no emigran, el capital no se mueve libremente entre países. Esto es clave: si los factores se movieran, no necesitaríamos comercio de bienes — directamente se moverían los factores.'

MISMOS GUSTOS: 'Simplificación útil. Si los gustos fueran distintos, habría otra fuente de diferencia de precios. Acá queremos aislar el efecto de las DOTACIONES.'

PREGUNTA RETÓRICA: '¿Les parecen realistas estos supuestos? Obviamente no del todo. Pero recordemos: el modelo no busca describir la realidad perfectamente — busca aislar UN mecanismo. El mecanismo que queremos ver es: dotaciones diferentes → precios diferentes → comercio.'

'Y después, cuando veamos H-O (Clase 6), vamos a ponerle nombre a este mecanismo y derivar predicciones concretas.'

---

### Sección: Equilibrio en autarquía

#### Slide 12: Preferencias y equilibrio: la curva de indiferencia
**Tipo**: grafico_texto
**Título**: Lo que faltaba en Ricardo: las preferencias de los consumidores
**Subtítulo**: Curvas de indiferencia + PPF = equilibrio en autarquía

**Contenido**:
- **Curva de indiferencia**: todas las combinaciones de bienes que dan la **misma utilidad** al consumidor
- Más alejada del origen = **mayor bienestar**
- **Equilibrio en autarquía**: el punto donde la PPF es **tangente** a la curva de indiferencia más alta posible
- En ese punto de tangencia, la **pendiente** de la PPF = pendiente de la curva de indiferencia = **precio relativo** de equilibrio
- Cada país maximiza bienestar dado lo que puede producir

**Gráfico**: graficos/equilibrio_autarquia.png
**Fuente**: Elaboración propia

**Notas docente**:
CURVAS DE INDIFERENCIA (8 minutos)

'En Ricardo no había preferencias: los precios se determinaban solo por costos. Acá las preferencias IMPORTAN. Necesitamos una herramienta para representarlas: la curva de indiferencia.'

EXPLICACIÓN DIDÁCTICA:
'Imaginemos que les da lo mismo consumir (10 telas, 5 alimentos) que (8 telas, 7 alimentos). Los dos puntos están en la misma curva de indiferencia. Pero (10 telas, 7 alimentos) está en una curva MÁS ALTA — es mejor.'

'El país quiere llegar a la curva más alta posible. Pero en autarquía, solo puede consumir lo que produce. Entonces el punto óptimo es donde la PPF TOCA la curva de indiferencia más alta posible — el punto de tangencia.'

EN EL GRÁFICO:
'Miren el punto E. Es donde la PPF toca la curva U₁. No puede llegar a U₂ porque la PPF no alcanza. La pendiente en E es el precio relativo de tela en términos de alimentos.'

PREGUNTA: '¿Por qué en Ricardo no necesitábamos esto?'
(Respuesta: porque con PPF recta y un solo factor, la producción = consumo estaba determinada solo por costos. Con PPF curva, hay MÚLTIPLES puntos posibles en la frontera — las preferencias eligen cuál.)

DATO CONCEPTUAL:
'Estamos usando "curvas de indiferencia sociales" — una simplificación fuerte. Asumimos que el país se comporta como UN consumidor. En realidad, dentro del país hay distintos consumidores con distintos gustos. Pero para la intuición del modelo, alcanza.'

---

#### Slide 13: Dos países, dos equilibrios de autarquía
**Tipo**: grafico_texto
**Título**: Distintas dotaciones → distintos precios en autarquía
**Subtítulo**: La fuente del comercio ya no es la tecnología — son los recursos

**Contenido**:
- **País A**: abundante en capital → PPF sesgada hacia tela (intensiva en K) → precio relativo de tela **bajo** en autarquía
- **País B**: abundante en trabajo → PPF sesgada hacia alimentos (intensivos en L) → precio relativo de tela **alto** en autarquía
- **Misma tecnología, mismos gustos** → la diferencia de precios viene SOLO de las dotaciones
- Si los precios relativos difieren en autarquía → **hay incentivos para comerciar** (igual que en Ricardo, pero por otra razón)

**Gráfico**: graficos/dos_paises_autarquia.png
**Fuente**: Elaboración propia

**Notas docente**:
DOS PAÍSES (8 minutos)

'Este es el slide clave conceptual de la clase. Veamos dos paneles lado a lado.'

PANEL IZQUIERDO — PAÍS A (abundante en capital):
'A tiene mucho capital relativo al trabajo. Como la tela es intensiva en capital, a A le resulta relativamente fácil producir tela → su PPF está "estirada" hacia el eje de tela. En equilibrio de autarquía, la tela es relativamente barata (pendiente plana = precio relativo bajo).'

PANEL DERECHO — PAÍS B (abundante en trabajo):
'B tiene mucho trabajo relativo al capital. Como los alimentos son intensivos en trabajo, a B le sale relativamente fácil producir alimentos → su PPF está "estirada" hacia alimentos. En autarquía, la tela es relativamente cara (pendiente empinada = precio relativo alto).'

RESULTADO:
'Los precios relativos de la tela difieren entre A y B. ¡Y la tecnología es la misma! ¡Y los gustos son los mismos! La ÚNICA diferencia son las dotaciones de factores.'

CONEXIÓN CON RICARDO:
'En Ricardo, los precios diferían porque la TECNOLOGÍA era distinta (A necesitaba 1 hora para tela, B necesitaba 6). Acá la tecnología es igual — lo que difiere es con cuánto de cada factor cuenta cada país. Es una fuente DIFERENTE de ventaja comparativa.'

EJEMPLO REAL:
'Pensemos: ¿por qué Australia exporta minerales y trigo, y Japón exporta autos y electrónica? No es porque tengan distinta tecnología para cultivar trigo — es porque Australia tiene ENORMES extensiones de tierra y minerales, y Japón tiene mucho capital y trabajo calificado.'

PREGUNTA: '¿La diferencia de dotaciones les parece más realista que la diferencia de tecnología como explicación del comercio?'

---

#### Slide 14: De la autarquía al precio relativo
**Tipo**: formula
**Título**: ¿Cómo se determina el precio relativo en autarquía?
**Subtítulo**: El precio es donde la oferta (PPF) se encuentra con la demanda (preferencias)

**Contenido**:
- En el punto de tangencia: $TMT = TMS = P_T / P_A$
- **TMT** (Tasa Marginal de Transformación): pendiente de la PPF = cuántos alimentos sacrifico por 1 tela más (lado de la **producción**)
- **TMS** (Tasa Marginal de Sustitución): pendiente de la curva de indiferencia = cuántos alimentos estoy **dispuesto** a ceder por 1 tela más (lado del **consumo**)
- **Precio relativo**: cuando TMT = TMS, el mercado está en equilibrio
- Cada país tiene su propio precio de autarquía → si difieren → base para el comercio

**Notas docente**:
FORMALIZACIÓN (5 minutos)

'No se asusten con la notación. Es intuitiva.'

EXPLICAR EN LENGUAJE SIMPLE:
'La pendiente de la PPF les dice cuánto CUESTA producir una tela más (en términos de alimentos). La pendiente de la curva de indiferencia les dice cuánto VALORAN una tela más (en términos de alimentos). Cuando lo que cuesta = lo que vale, estamos en equilibrio. Eso define el precio relativo.'

EN PIZARRÓN:
- Dibujar PPF cóncava
- Dibujar una curva de indiferencia tangente
- Marcar el punto de tangencia: E
- Trazar la recta tangente: su pendiente es P_T/P_A
- 'Esa pendiente es el precio relativo de la tela en autarquía.'

'Si en A la pendiente es plana (tela barata) y en B la pendiente es empinada (tela cara), hay incentivos para que A exporte tela y B importe tela.'

'Esto es EXACTAMENTE lo mismo que en Ricardo — precios relativos distintos → base para comerciar — pero con otro mecanismo detrás.'

CONFUSIÓN COMÚN: 'TMT no es lo mismo que TMS. TMT es producción (lo que podés hacer). TMS es preferencias (lo que querés). Solo en equilibrio coinciden.'

---

### Sección: Del equilibrio interno al comercio

#### Slide 15: Oferta y demanda relativa mundiales
**Tipo**: grafico_texto
**Título**: ¿Cómo se determina el precio mundial?
**Subtítulo**: Oferta relativa (OR), demanda relativa (DR) y equilibrio

**Contenido**:
- **Oferta relativa (OR)**: cuánta tela vs alimentos produce el mundo a cada precio relativo. Pendiente positiva: si sube el precio de la tela, se produce más tela
- Cada país tiene su propia OR (según dotaciones) → OR y OR*
- **Demanda relativa (DR)**: cuánta tela vs alimentos quiere consumir el mundo. Pendiente negativa: si sube el precio de la tela, se consume menos tela
- DR mundial es **única** (mismos gustos en ambos países)
- **Precio de equilibrio mundial**: donde OR mundial cruza DR → punto **intermedio** entre precios de autarquía

**Gráfico**: graficos/oferta_demanda_relativa.png
**Fuente**: Elaboración propia a partir de Lugones (2008), Gráfico G.1.6

**Notas docente**:
OFERTA Y DEMANDA RELATIVA (8 minutos)

'Este gráfico es la versión neoclásica del "rango de precios" que vimos con Ricardo (el rango 1,33-2). Pero ahora tenemos un mecanismo completo para determinar DÓNDE exactamente cae el precio mundial.'

EXPLICAR EL GRÁFICO:
- Eje X: cantidad relativa de tela vs alimentos (Q_T / Q_A)
- Eje Y: precio relativo de tela (P_T / P_A)

'La curva OR sube: si la tela se encarece, los productores producen más tela relativo a alimentos. La curva DR baja: si la tela se encarece, los consumidores compran menos tela.'

DOS CURVAS OR:
'OR es la oferta relativa de A (abundante en capital → produce mucha tela → OR está más a la derecha). OR* es la de B (abundante en trabajo → produce más alimentos → OR* está más a la izquierda). Cuando se abren al comercio, las dos ofertas se suman y la OR mundial queda en algún punto intermedio.'

RESULTADO:
'El precio mundial queda entre el precio de autarquía de A y el de B. Exactamente como en Ricardo, pero ahora con un mecanismo explícito de oferta y demanda.'

CONEXIÓN CON LUGONES:
'Esto corresponde al Gráfico G.1.6 de Lugones (pág. 27). La curva DR es la demanda relativa mundial, OR y OR* son las ofertas relativas de cada país.'

CONEXIÓN CON RICARDO:
'En Ricardo, el precio mundial "caía en algún punto" del rango sin que supiéramos exactamente dónde (salvo intuición). Acá OR y DR lo determinan. Mill (siglo XIX) fue el primero en plantear la "demanda recíproca" para cerrar este punto — el modelo estándar lo formaliza.'

---

#### Slide 16: Comercio con PPF curva: especialización parcial
**Tipo**: grafico_texto
**Título**: Ganancias del comercio: consumir fuera de la PPF
**Subtítulo**: Con comercio, el país puede consumir combinaciones que no podía producir

**Contenido**:
- **Autarquía**: producción = consumo en el punto E (tangencia PPF + CI)
- **Con comercio**: nuevo precio relativo mundial (distinto al de autarquía) → el país **ajusta producción** hacia el bien donde tiene ventaja
- Produce en Q (sobre la PPF), pero consume en C (sobre la **línea de precios mundiales**, fuera de la PPF)
- La diferencia entre Q y C es lo que **exporta e importa**
- Resultado: el país alcanza una curva de indiferencia **más alta** → **mayor bienestar**

**Gráfico**: graficos/comercio_ppf_curva.png
**Fuente**: Elaboración propia

**Notas docente**:
GANANCIAS DEL COMERCIO (10 minutos)

'Este es el gráfico que cierra la historia. Compárenlo con el de Ricardo (PPF lineal + recta de intercambio). La idea es la misma, pero con una diferencia crucial.'

PASO A PASO EN EL GRÁFICO:
1. 'Punto E: equilibrio de autarquía. La producción = el consumo. El país está sobre la PPF y sobre la curva de indiferencia U₁.'
2. 'Se abre el comercio: el precio relativo mundial es diferente al de autarquía. Supongamos que la tela es más cara en el mundo que internamente.'
3. 'El país ajusta: produce MÁS tela y MENOS alimentos — se mueve a lo largo de la PPF hasta el punto Q.'
4. 'Pero no tiene que CONSUMIR lo que produce. Puede vender tela al precio mundial e importar alimentos. Consume en el punto C, que está FUERA de la PPF.'
5. 'C está sobre una curva de indiferencia más alta (U₂ > U₁). El bienestar subió.'

DIFERENCIA CLAVE CON RICARDO:
'En Ricardo, la especialización era TOTAL: el país producía SOLO tela. Acá, el punto Q sigue teniendo algo de ambos bienes — la especialización es PARCIAL. Esto es más realista.'

'La exportación es la distancia horizontal entre Q y C (tela). La importación es la distancia vertical entre Q y C (alimentos).'

EJEMPLO:
'Argentina: en autarquía, produce soja y autos. Con comercio, produce MÁS soja y MENOS autos (pero sigue produciendo algunos). Exporta soja, importa autos. Puede consumir más de ambos que en autarquía.'

PREGUNTA: '¿Por qué la especialización no es total como en Ricardo?'
(Respuesta: porque la PPF es curva — a medida que te especializás, el costo sube. Llegás a un punto donde el costo marginal iguala el precio mundial y no conviene seguir.)

---

#### Slide 17: ¿Qué determina en qué se especializa cada país?
**Tipo**: texto
**Título**: El anticipo de Heckscher-Ohlin
**Subtítulo**: La dotación de factores como fuente de ventaja comparativa

**Contenido**:
- En el modelo estándar, la **forma** de la PPF depende de las **dotaciones de factores** (cuánto K y L tiene el país)
- País abundante en capital → PPF sesgada a tela → tela barata → **exporta tela**
- País abundante en trabajo → PPF sesgada a alimentos → alimentos baratos → **exporta alimentos**
- Predicción: cada país exporta el bien que usa intensivamente su **factor abundante**
- Esto es la intuición central del modelo **Heckscher-Ohlin** → Clase 6

**Notas docente**:
ANTICIPO H-O (5 minutos)

'Todo lo que vimos hoy funciona como marco general. Pero hay una pregunta que dejamos en el aire: ¿QUÉ determina la forma de la PPF? ¿Por qué A tiene la PPF sesgada hacia tela y B hacia alimentos?'

'La respuesta: las dotaciones de factores. Si A tiene mucho capital y poco trabajo, le resulta fácil producir bienes que usan mucho capital (tela, manufactura, maquinaria). Si B tiene mucho trabajo y poco capital, le sale fácil producir bienes que usan mucho trabajo (alimentos, textiles básicos).'

'Esto es exactamente la tesis de Heckscher-Ohlin, que vamos a formalizar en la Clase 6.'

TEASER PARA CLASE 6:
'Pero H-O no solo predice QUÉ se comercia. También predice QUIÉN GANA Y QUIÉN PIERDE dentro del país. Si Argentina abre el comercio y exporta más soja, ¿qué pasa con los salarios? ¿Y con la renta de la tierra? La Clase 6 responde eso con Stolper-Samuelson.'

'También vamos a ver la paradoja de Leontief: cuando probaron empíricamente el modelo H-O en EEUU, ¡les dio al revés! EEUU, el país más abundante en capital del mundo, exportaba bienes intensivos en trabajo. ¿Cómo se explica?'

CONEXIÓN CON LA TRÍADA:
'Recuerden: el modelo dice que la especialización viene de las dotaciones. Pero Corea del Sur pasó de exportar pelucas en 1960 a semiconductores hoy. ¿Cambió su dotación "natural"? No — cambió su POLÍTICA. Esto nos va a llevar a los enfoques estructuralistas (Unidad 4): la ventaja comparativa se puede CONSTRUIR.'

---

### Sección: Cierre

#### Slide 18: Ricardo vs modelo neoclásico estándar
**Tipo**: grafico_texto
**Título**: Tabla comparativa: ¿qué cambia?
**Subtítulo**: Dos modelos, un mismo objetivo: explicar el comercio

**Contenido**:
- **Factores**: Ricardo = 1 (trabajo) → Neoclásico = 2+ (trabajo + capital)
- **PPF**: Ricardo = recta → Neoclásico = curva (cóncava)
- **Costo de oportunidad**: Ricardo = constante → Neoclásico = creciente
- **Especialización**: Ricardo = total → Neoclásico = parcial
- **Fuente de ventaja comparativa**: Ricardo = tecnología → Neoclásico = dotaciones
- **Preferencias**: Ricardo = no importan → Neoclásico = curvas de indiferencia
- **En común**: precios relativos diferentes → comercio → ganancias para ambos

**Gráfico**: graficos/resumen_ricardo_vs_neoclasico.png
**Fuente**: Elaboración propia

**Notas docente**:
TABLA COMPARATIVA (5 minutos)

'Este slide resume toda la clase. Dos columnas: Ricardo a la izquierda, modelo estándar a la derecha.'

RECORRER FILA POR FILA:
- Factores: '1 vs 2+. Con más factores podemos hablar de distribución del ingreso.'
- PPF: 'Recta vs curva. La curva es más realista.'
- Costo de oportunidad: 'Constante vs creciente. Eso cambia todo sobre la especialización.'
- Especialización: 'Total vs parcial. Argentina no deja de producir manufactura por exportar soja.'
- Fuente: 'Tecnología vs dotaciones. Cambio conceptual enorme.'
- Preferencias: 'Antes no importaban, ahora sí. La demanda ayuda a determinar el precio.'

LO QUE NO CAMBIA:
'El mecanismo básico es el MISMO: precios relativos diferentes en autarquía → incentivos al comercio → especialización → ganancias. Eso es herencia de Ricardo. Lo que cambia es el motor detrás de las diferencias de precios.'

---

#### Slide 19: Lo que viene: Heckscher-Ohlin y la distribución
**Tipo**: texto
**Título**: Después del recreo: ¿quién gana y quién pierde?
**Subtítulo**: Heckscher-Ohlin, Stolper-Samuelson y la paradoja de Leontief

**Contenido**:
- Hasta acá armamos la **caja de herramientas** (PPF curva, preferencias, oferta/demanda relativa)
- Después del recreo: le ponemos **contenido** con el modelo H-O
- **Tres preguntas** que vamos a responder:
  - ¿Qué predice H-O sobre el patrón de comercio?
  - ¿Quién gana y quién pierde **dentro** del país? → Stolper-Samuelson
  - ¿Los datos confirman el modelo? → Paradoja de Leontief

**Notas docente**:
ANTICIPO (3 minutos)

'Hicimos el trabajo pesado de armar las herramientas. Después del recreo es más divertido: vamos a usarlas para responder preguntas concretas.'

'H-O dice: cada país exporta bienes que usan intensivamente el factor que tiene en abundancia. Argentina tiene tierra → exporta agro. Japón tiene capital → exporta manufactura. Suena lógico. Pero Stolper-Samuelson agrega un giro oscuro: el comercio beneficia al dueño del factor abundante y PERJUDICA al dueño del factor escaso. Si Argentina abre el comercio, los terratenientes ganan y los trabajadores industriales pierden.'

'Y después viene Leontief con los datos y dice: ¡en EEUU no se cumple! La mayor potencia industrial del mundo exporta bienes intensivos en trabajo. ¿Cómo puede ser?'

'Eso vemos después del recreo. No se vayan lejos.'

---

#### Slide 20: Material complementario
**Tipo**: texto
**Título**: Material complementario
**Subtítulo**: Para profundizar los temas de esta clase

**Contenido**:
- 🎬 *Juego sin límites: La mentira del libre comercio* (DW Documental, 42 min, español) — Cómo funciona realmente el comercio internacional: entre la teoría del libre comercio y la práctica proteccionista
- 🎬 *1929: The Great Crash* (BBC, 60 min, inglés) — El crack del '29, Smoot-Hawley y el colapso del comercio mundial en los años '30
- 📺 *Crash Course Economics #2: Specialization and Trade* (YouTube, 11 min, inglés con subs) — Ventaja comparativa, costo de oportunidad y PPF explicados con animaciones
- 🎥 *Ferris Bueller's Day Off* — La escena de Ben Stein (2 min, YouTube) — "Anyone? Anyone?" La explicación más famosa (y aburrida) de Smoot-Hawley en el cine
- 📺 *Marginal Revolution University: Comparative Advantage* (YouTube, 8 min, inglés) — Costo de oportunidad y especialización: por qué comerciar siempre conviene

**Notas docente**:
MATERIAL COMPLEMENTARIO (2 minutos)

'Les recomiendo especialmente dos cosas: el documental de DW en español sobre libre comercio — les va a mostrar la distancia entre la teoría que vemos acá y la realidad. Y la escena de Ferris Bueller — son 2 minutos que resumen Smoot-Hawley mejor que cualquier libro.'

'El documental de la BBC sobre 1929 es excelente para entender el contexto histórico del entreguerras que vimos hoy: cómo el proteccionismo destruyó el comercio mundial.'

'Los videos de Crash Course y MRU son buenos para repasar los conceptos de ventaja comparativa y PPF si les quedó algo flojo de la clase anterior.'

---

#### Slide 21: Lecturas y bibliografía
**Tipo**: texto
**Título**: Lecturas para esta clase
**Subtítulo**: Bibliografía del curso

**Contenido**:
- **Lectura principal**: Lugones, G. et al. *Teorías del Comercio Internacional* — Sección 1.2: "Los neoclásicos (Heckscher-Ohlin): diferencias en la dotación de factores" (pp. 25-30)
- **Complementaria**: Krugman, P., Obstfeld, M. & Melitz, M. *Economía Internacional* — Cap. 6: "El modelo estándar de comercio"
- **Complementaria**: Krugman et al. — Cap. 5: "Recursos y comercio: el modelo Heckscher-Ohlin" (anticipar para Clase 6)

**Notas docente**:
LECTURAS (2 minutos)

'La lectura de Lugones (pp. 25-30) es corta y cubre tanto lo de hoy como lo de la Clase 6. Si pueden leerla antes de la próxima clase, mejor — van a llegar con la intuición de H-O más asentada.'

'El Krugman capítulo 6 es más formal — tiene los gráficos de oferta y demanda relativa que vimos hoy. El capítulo 5 es H-O propiamente dicho, para la Clase 6.'

'Recuerden: no tienen que memorizar las demostraciones. Lo importante es la intuición: dotaciones → precios → comercio → ganancias... y también perdedores.'

---

#### Slide 22: Preguntas
**Tipo**: cierre
**Título**: ¿Preguntas?
**Subtítulo**: Clase 5 — El modelo neoclásico estándar

**Notas docente**:
CIERRE (5 minutos)

Si quedan dudas, hacer un repaso rápido de 30 segundos:
'Hoy hicimos tres cosas: primero, ubicamos históricamente la revolución marginalista y el entreguerras. Segundo, vimos el salto técnico de Ricardo al modelo estándar: más factores, PPF curva, preferencias, especialización parcial. Tercero, vimos cómo se determina el precio mundial con oferta y demanda relativa. La próxima clase le ponemos contenido a este marco con H-O.'

PREGUNTAS FRECUENTES QUE PUEDEN SURGIR:
- '¿La curva de indiferencia es real?' → No — es una abstracción. Representa preferencias agregadas. En la realidad no existe "un" consumidor representativo.
- '¿Por qué asumir misma tecnología?' → Para aislar el efecto de las dotaciones. Si los países tienen diferente tecnología, hay DOS fuentes de diferencia de precios y no sabés cuál importa más.
- '¿Argentina tiene especialización parcial?' → Sí — exporta agro pero también produce y exporta algo de manufactura (autos a Brasil). No es 100% soja.
