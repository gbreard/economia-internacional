# Evaluación — Unidad 1: Introducción, hechos estilizados e indicadores

## Instrucciones generales
- Esta evaluación cubre los contenidos de las **Clases 1 y 2**
- Las 5 preguntas son de **opción múltiple** (una sola respuesta correcta)
- Las preguntas 4 y 5 requieren **descargar datos y procesarlos** antes de responder
  - Se proporcionan los links directos de descarga y los pasos a seguir
  - No es posible responder correctamente sin haber procesado los datos

---

## Pregunta 1 — El marco Tecnología-Reglas-Poder

En clase vimos que el comercio internacional florece cuando se alinean tres factores: Tecnología (T), Reglas (R) y Poder (P).

**¿Cuál de las siguientes afirmaciones explica mejor por qué el comercio mundial colapsó entre 1914 y 1945?**

a) La tecnología de transporte retrocedió: los barcos a vapor dejaron de funcionar y el telégrafo fue destruido por las guerras.

b) Las reglas colapsaron (fin del patrón oro, aranceles como Smoot-Hawley) y el poder hegemónico se fragmentó (Gran Bretaña no podía sostener el sistema y EEUU no quería asumir el rol), aunque la tecnología seguía disponible.

c) El colapso se debió exclusivamente a las dos guerras mundiales, que interrumpieron físicamente las rutas comerciales.

d) Los países en desarrollo dejaron de exportar materias primas porque descubrieron que el comercio los perjudicaba.

**Respuesta correcta**: b)

**Justificación**: La tecnología no retrocedió (los barcos seguían funcionando). Lo que falló fueron las reglas (colapso del patrón oro en 1931, espiral proteccionista con Smoot-Hawley en 1930) y el poder (vacío hegemónico: Gran Bretaña debilitada, EEUU aislacionista). Las guerras fueron parte del problema, pero el comercio ya había caído antes de 1939 por la Gran Depresión y el proteccionismo. Es el ejemplo más claro de que la tecnología sola no alcanza: se necesita T+R+P alineados.

---

## Pregunta 2 — Convergencia, divergencia y comercio

En la Clase 1 vimos las trayectorias de PIB per cápita de distintas regiones entre 1820 y 2018 (datos de Maddison). Asia Oriental convergió hacia los niveles europeos, pero América Latina no lo hizo a pesar de haber crecido.

**¿Cuál de las siguientes afirmaciones es la interpretación más correcta de la evidencia?**

a) América Latina no creció entre 1820 y 2018, por eso no convergió.

b) Asia Oriental convergió gracias a que adoptó el libre comercio puro, sin ninguna intervención del Estado.

c) Lo que importa no es solo SI un país se integra al comercio mundial, sino CÓMO lo hace: Asia Oriental combinó apertura con política industrial, tipo de cambio competitivo e inversión en educación; América Latina creció pero sin cerrar la brecha con los países ricos.

d) La divergencia de América Latina se explica porque nunca participó del comercio internacional.

**Respuesta correcta**: c)

**Justificación**: América Latina SÍ creció (de ~$1.500 a ~$14.000 en PIB per cápita), por lo que (a) es falsa. Asia Oriental no adoptó libre comercio puro: Japón, Corea y China tuvieron política industrial activa, por lo que (b) es falsa. América Latina participó activamente del comercio (Argentina fue top 10 exportador en 1900), por lo que (d) es falsa. La clave es que exportar commodities sin diversificarse no produce el mismo resultado que una inserción estratégica con upgrading tecnológico.

---

## Pregunta 3 — Indicadores de sostenibilidad y el patrón pre-crisis argentino

En la Clase 2 estudiamos que la cuenta corriente (CC) y el tipo de cambio real (TCR) son los indicadores que mejor anticipan las crisis externas. También vimos la identidad ahorro-inversión: CC = (S_privado - I_privado) + (T - G).

**¿Cuál de las siguientes situaciones describe correctamente el patrón previo a las crisis argentinas de 2001 y 2018?**

a) Superávit de cuenta corriente persistente, tipo de cambio real depreciado (peso barato) y acumulación de reservas.

b) Déficit de cuenta corriente persistente, tipo de cambio real apreciado (peso caro) y pérdida gradual de reservas, financiado con endeudamiento externo.

c) Equilibrio de cuenta corriente, tipo de cambio real estable y reservas internacionales constantes.

d) Déficit de cuenta corriente financiado exclusivamente con inversión extranjera directa productiva, lo que lo hacía sostenible.

**Respuesta correcta**: b)

**Justificación**: Tanto en la Convertibilidad (1991-2001) como en 2016-2018, Argentina mostró: TCR apreciado (peso caro por inflación mayor que devaluación), déficit de CC persistente (entre -3% y -5% del PIB, zona de riesgo) y financiamiento con deuda. Cuando el mercado duda de la sostenibilidad, se produce fuga de capitales, caída de reservas y devaluación brusca. Este es el "ciclo argentino": estabilización → apreciación → crisis → recuperación.

---

## Pregunta 4 — Apertura comercial: ¿quién se abrió y quién se cerró?

### Instrucciones para descargar y procesar los datos

1. Entrar al portal de datos del Banco Mundial:
   **https://data.worldbank.org/indicator/NE.TRD.GNFS.ZS**
   (esto abre el indicador "Trade (% of GDP)", que es la apertura comercial)

2. **Seleccionar los países**: debajo del gráfico principal hay un mapa o una lista de países. Buscar y seleccionar **Argentina**, **China** y **Alemania** (Germany). También pueden usar la barra de búsqueda de países que aparece sobre el gráfico. Si hay países preseleccionados que no necesitan, pueden deseleccionarlos.

3. Hacer clic en **"Download"** (botón arriba a la derecha del gráfico) → elegir **CSV** o **Excel**. Se descarga una tabla con los valores anuales de cada país.

4. En Excel o Google Sheets, para cada país calcular el **promedio** de los valores en dos sub-períodos:
   - **Período 1**: 2000 a 2007 (8 años)
   - **Período 2**: 2015 a 2022 (8 años)
   - Pueden usar la función PROMEDIO() sobre las celdas correspondientes

5. Calcular la **diferencia** entre ambos promedios (Período 2 menos Período 1) para cada país

### Pregunta

**Calculen los promedios y las diferencias. ¿Cuál de las siguientes afirmaciones describe correctamente lo que muestran los datos?**

a) Argentina tuvo la mayor caída en apertura (~15 pp), lo que refleja que las políticas proteccionistas y los controles cambiarios redujeron drásticamente su comercio exterior.

b) China tuvo la mayor caída en apertura (~15 pp), pero esto no significa que se haya "cerrado" al comercio: su PIB creció más rápido que su comercio, es decir, su mercado interno se expandió enormemente mientras seguía comerciando más en términos absolutos.

c) Alemania tuvo la mayor caída en apertura (~10 pp), como consecuencia de la crisis de deuda europea que redujo el comercio intra-UE.

d) Los tres países aumentaron su apertura comercial entre ambos períodos, confirmando que la globalización siguió avanzando de forma pareja para todos.

**Respuesta correcta**: b)

**Justificación (datos procesados del Banco Mundial)**:

| País | Promedio 2000-2007 | Promedio 2015-2022 | Cambio |
|------|--------------------|--------------------|--------|
| Argentina | 36% | 29% | −7 pp |
| China | 52% | 36% | **−15 pp** |
| Alemania | 64% | 79% | +15 pp |

China tuvo la mayor caída (~15 pp). La opción (b) es correcta tanto en el dato como en la explicación: China no se "cerró" al comercio — sus exportaciones en dólares siguieron subiendo — pero su PIB (el denominador de la fórmula de apertura) creció tanto que el ratio bajó. Es un caso clásico de cómo el indicador de apertura "tiene trampas", como vimos en clase. Argentina cayó menos (~7 pp), no 15 pp como dice (a). Alemania AUMENTÓ su apertura (+15 pp), no cayó como dice (c). Y la opción (d) es falsa porque dos de los tres países bajaron.

---

## Pregunta 5 — Cuenta corriente: Argentina vs. Corea del Sur

### Instrucciones para descargar y procesar los datos

1. Entrar al portal de datos del Banco Mundial:
   **https://data.worldbank.org/indicator/BN.CAB.XOKA.GD.ZS**
   (esto abre el indicador "Current account balance (% of GDP)")

2. **Seleccionar los países**: buscar y seleccionar **Argentina** y **Korea, Rep.** (Corea del Sur). Si hay otros países preseleccionados, deseleccionarlos para que el gráfico quede limpio.

3. Hacer clic en **"Download"** → elegir **CSV** o **Excel**

4. En Excel o Google Sheets, para cada país revisar los **24 años del período 2000-2023** y contar en cuántos la cuenta corriente fue **positiva** (superávit: valor mayor a cero)

### Pregunta

**Cuenten los años con superávit para cada país. ¿Cuál de las siguientes afirmaciones describe correctamente lo que muestran los datos Y su explicación?**

a) Corea tuvo superávit en los 24 años y Argentina en unos 10: ambos tuvieron superávits post-crisis, pero la diferencia se explica porque Corea exporta tecnología y Argentina commodities — cuando los precios de los commodities caen, Argentina vuelve al déficit.

b) Corea tuvo superávit en los 24 años y Argentina en unos 10: Corea mantuvo una estrategia deliberada de tipo de cambio competitivo y acumulación de reservas tras la crisis de 1997 ("nunca más depender del capital externo"); Argentina tuvo superávits post-2002 pero volvió al ciclo de apreciación cambiaria y déficit a partir de 2010.

c) Ambos países tuvieron superávit en más de 20 de los 24 años, confirmando que las crisis de 1997 (Corea) y 2001 (Argentina) generaron un cambio estructural permanente en ambas economías.

d) Corea tuvo superávit en los 24 años y Argentina en unos 10: esto se explica porque Corea recibió mucha más inversión extranjera directa que Argentina, lo que le permitió financiar sus importaciones sin generar déficit.

**Respuesta correcta**: b)

**Justificación (datos procesados del Banco Mundial)**:

| País | Años con CC > 0 (de 24) | Detalle |
|------|--------------------------|---------|
| Corea del Sur | **24 de 24** | Superávit TODOS los años, incluso +0.2% en 2008 (crisis global) |
| Argentina | **10 de 24** | Superávit 2002-2009 (8 años) y 2020-2021 (2 años); déficit el resto |

Las opciones (a), (b) y (d) coinciden en el dato numérico (Corea 24, Argentina ~10), pero difieren en la explicación:

- **(a)** tiene el dato correcto pero la explicación es incompleta: no es solo un problema de commodities. Brasil también exporta commodities y no tiene el mismo patrón de crisis. El problema argentino es el ciclo cambiario (apreciación → déficit → crisis), no la composición de exportaciones.
- **(b)** tiene el dato correcto Y la explicación correcta: Corea cambió de estrategia tras 1997 (TC competitivo, acumulación de reservas, superávit permanente). Argentina mejoró post-2002 pero volvió al patrón de apreciación cambiaria y déficit externo a partir de 2010, con crisis en 2018.
- **(c)** tiene el dato incorrecto: Argentina NO tuvo superávit en 20+ años.
- **(d)** tiene el dato correcto pero la explicación es incorrecta: la IED no explica el superávit de cuenta corriente de Corea (de hecho, la IED entra por la cuenta financiera, no la corriente). Lo que explica el superávit coreano es la competitividad exportadora y el tipo de cambio.

---

## Rúbrica

| Pregunta | Puntaje |
|----------|---------|
| 1 — Marco T-R-P (conceptual) | 20 puntos |
| 2 — Convergencia/divergencia (conceptual) | 20 puntos |
| 3 — Indicadores de sostenibilidad (conceptual) | 20 puntos |
| 4 — Apertura comercial (procesamiento de datos) | 20 puntos |
| 5 — Cuenta corriente (procesamiento de datos) | 20 puntos |
| **Total** | **100 puntos** |
