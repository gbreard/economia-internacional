# Spec — Notebook: Fuentes de datos para economía internacional

## Objetivo

Notebook **formativo** (sin nota) que enseña a los estudiantes a **encontrar, conectar, filtrar y cruzar fuentes de datos** para sus propios análisis. Es una guía de referencia permanente que vive dentro de Colab y que pueden consultar cuando armen el coloquio o cualquier trabajo futuro.

**No evalúa contenido económico**: evalúa que el alumno pueda, dado un tema, conseguir los datos por su cuenta.

## Público

- Alumnos que ya completaron NB1 y NB2 (saben ejecutar celdas, usar Gemini en Colab, leer gráficos)
- No saben programar — usan Gemini/ChatGPT para generar código
- Necesitan datos para el coloquio (borrador PPT 28/05, entrega final 18/06)

## Disponibilidad

- **Se abre con S6 (14/05)** — justo antes de que necesiten datos para el borrador del coloquio
- Opcionalmente se puede presentar brevemente en S5 (07/05) como adelanto
- Vive en `notebooks/` y se publica en `notebooks.html`

## Nombre tentativo

`NB_fuentes_datos.ipynb` — "Guía práctica: fuentes de datos para economía internacional"

(No lleva número de NB porque no es evaluativo ni está atado a una unidad)

---

## Principios de diseño

1. **Todo se explica dentro del notebook**: el alumno no necesita leer nada externo para entender qué hacer
2. **Cada fuente es autónoma**: se puede usar un bloque sin haber leído los anteriores
3. **Prompts modelo incluidos**: para cada fuente, un prompt de Gemini que funciona y que el alumno puede adaptar
4. **Ejercicios de práctica mínimos**: 2-3 ejercicios cortos que se resuelven en <5 min cada uno, para que prueben la mecánica
5. **Cruce de fuentes como cierre**: el notebook termina mostrando cómo combinar dos fuentes en un mismo análisis
6. **Patrón replicable**: el alumno aprende un workflow que puede repetir con cualquier fuente nueva

---

## Estructura del notebook

### Bloque 0 — Introducción y contexto (markdown)

**Contenido**:
- Para qué sirve este notebook: "es tu caja de herramientas para conseguir datos"
- Qué van a aprender: conectarse a APIs, cargar archivos, filtrar, cruzar fuentes
- Cómo usarlo: no es para leer de corrido — es para consultar cuando necesiten una fuente
- Recordatorio: el código lo genera Gemini, lo importante es **saber qué pedirle**

**Diagrama conceptual** (texto o imagen simple):
```
Tu pregunta de investigación
        ↓
¿Qué datos necesitás?
        ↓
¿Dónde están? → CATÁLOGO DE FUENTES (este notebook)
        ↓
¿Cómo se accede? → API (automático) / CSV-Excel (manual)
        ↓
Descargar → Filtrar → Visualizar → Interpretar
        ↓
¿Necesitás otra fuente? → Agregar celda nueva, repetir
        ↓
¿Querés cruzar fuentes? → Merge por año/país
```

**Regla de oro**: "Las fuentes se definen al inicio del notebook. Si necesitás una fuente nueva, creá una celda nueva y repetí el patrón."

---

### Bloque 1 — ¿Qué es una API? ¿Y un CSV? (markdown + código demo)

**Objetivo**: que entiendan la diferencia entre los dos modos de acceso a datos.

**Celda markdown — Explicación**:
- **API (Application Programming Interface)**: un "mostrador digital" donde le pedís datos a un servidor y te los devuelve en formato estructurado (JSON). No necesitás entrar a una página web ni descargar archivos — el código se conecta directo.
  - Ventajas: automático, reproducible, actualizado
  - Desventajas: no todas las fuentes tienen API, a veces hay límites de uso
  - Analogía: "es como pedir comida por delivery — le decís qué querés y te lo traen"

- **CSV/Excel (descarga manual)**: entrás a la página de la fuente, filtrás lo que necesitás, descargás el archivo, y lo subís a Colab.
  - Ventajas: funciona con cualquier fuente, más control sobre qué descargás
  - Desventajas: manual, no se actualiza solo, puede haber errores de formato
  - Analogía: "es como ir al supermercado — vos elegís y traés"

**Celda código — Demo rápida**:
- Ejemplo mínimo de API: 3 líneas que bajan un dato del Banco Mundial y lo muestran
- Ejemplo mínimo de CSV: subir un archivo y leerlo con pandas
- Que el alumno vea la diferencia en la práctica

**Celda markdown — Cuándo usar cada uno**:
| Fuente | Tipo | Razón |
|--------|------|-------|
| Banco Mundial | API | Tiene API pública, miles de indicadores |
| BCRA | API | Tiene API pública, datos monetarios/cambiarios |
| INDEC-ICA | CSV/Excel | No tiene API pública, hay que descargar de la web |
| CEPAL | API | Tiene API pero a veces conviene bajar el CSV directamente |
| ADEFA | Excel/PDF | Solo descarga manual |

---

### Bloque 2 — Catálogo de fuentes (markdown + código por fuente)

**Estructura por fuente** (se repite para cada una):

```
--- CELDA MARKDOWN ---
## Fuente: [Nombre]
- **Qué tiene**: [indicadores disponibles, período, cobertura]
- **Tipo de acceso**: API / CSV / Excel
- **URL**: [link a la página o documentación]
- **Útil para**: [temas del coloquio donde aplica]
- **Prompt sugerido para Gemini**: "[prompt modelo]"

--- CELDA CÓDIGO (ejecutable) ---
# Ejemplo funcional que baja un indicador de esta fuente
# El alumno puede copiar esta celda y cambiar parámetros
```

#### Fuente 1: Banco Mundial (API)
- **Indicadores clave**: Trade/GDP (NE.TRD.GNFS.ZS), Current account (BN.CAB.XOKA.GD.ZS), IED (BX.KLT.DINV.WD.GD.ZS), PIB per cápita (NY.GDP.PCAP.CD), exportaciones de bienes y servicios (NE.EXP.GNFS.ZS)
- **Cobertura**: ~220 países, 1960-2024, ~1500 indicadores
- **API**: `api.worldbank.org/v2/country/{ISO}/indicator/{ID}?format=json`
- **Sin key, sin límite práctico**
- **Ejemplo**: bajar apertura comercial de Argentina 2000-2024, graficar
- **Prompt modelo**: "Escribí código Python que use la API del Banco Mundial para descargar el indicador NE.TRD.GNFS.ZS (Trade % of GDP) para Argentina, Brasil y Chile desde 2000 hasta 2024, lo ponga en un DataFrame y haga un gráfico de líneas"
- **Útil para**: todos los temas, especialmente contexto macro

#### Fuente 2: BCRA (API)
- **Indicadores clave**: ITCRM multilateral, ITCRM bilateral (con Brasil, EEUU, China, UE), tipo de cambio nominal, reservas internacionales, base monetaria
- **Cobertura**: Argentina, series diarias/mensuales desde ~2002
- **API**: `https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable/{idVariable}/{desde}/{hasta}`
- **Sin key** (pero puede tener rate limiting)
- **Variables importantes**: idVariable=4 (ITCRM multilateral), idVariable=31 (TCN), etc.
- **Ejemplo**: bajar ITCRM multilateral 2010-2025, graficar
- **Prompt modelo**: "Escribí código Python que use la API del BCRA para descargar el Índice de Tipo de Cambio Real Multilateral (variable 4) desde 2010 hasta hoy, lo convierta a DataFrame con fecha y valor, y haga un gráfico de línea"
- **Útil para**: temas 1, 6, 8 (TCR), cualquier análisis de competitividad argentina
- **Nota importante**: documentar las variables más usadas con su idVariable

#### Fuente 3: FRED — Federal Reserve Bank of St. Louis (API)
- **Indicadores clave**: tasas de interés EEUU (DFF, DGS10), CPI (CPIAUCSL), precio del oro (GOLDAMGBD228NLBM), tipo de cambio, desempleo
- **Cobertura**: principalmente EEUU, series desde ~1950
- **API**: `https://api.stlouisfed.org/fred/series/observations?series_id={ID}&api_key={KEY}&file_type=json`
- **Requiere API key** (gratis, registro en 2 minutos en fred.stlouisfed.org)
- **Ejemplo**: bajar tasa de fondos federales 2000-2025, graficar
- **Prompt modelo**: "Escribí código Python que use la API de FRED para descargar la serie DFF (Federal Funds Rate) desde 2000, necesito registrarme en fred.stlouisfed.org para obtener una API key gratuita"
- **Útil para**: contexto macro internacional, tasas, dólar
- **Nota**: explicar qué es una API key y cómo se obtiene (paso a paso con screenshots si es posible)

#### Fuente 4: UN COMTRADE (API)
- **Indicadores clave**: comercio bilateral por producto (HS 2, 4 o 6 dígitos), todos los países, exportaciones e importaciones
- **Cobertura**: ~200 países, desde 1962, desagregación por producto
- **API v2**: `https://comtradeapi.un.org/data/v1/get/{typeCode}/{freqCode}/{clCode}?reporterCode={}&partnerCode={}&period={}&cmdCode={}`
- **Requiere API key** (gratis, 100 calls/día en plan free, registro en comtradeplus.un.org)
- **Ejemplo**: bajar exportaciones de Argentina a Brasil en capítulo 87 (vehículos) 2015-2023
- **Prompt modelo**: "Escribí código Python que use la API de UN COMTRADE v2 para descargar las exportaciones de Argentina (código 032) a Brasil (código 076) del capítulo HS 87 (vehículos) anuales desde 2015 hasta 2023"
- **Útil para**: temas 1 (autos), 3 (TDF electrónica), 4 (antidumping), cálculo de GL bilateral
- **Nota**: COMTRADE es la fuente más poderosa para comercio bilateral por producto pero la API es más compleja. Incluir tabla de códigos de país y capítulos HS más relevantes

#### Fuente 5: CEPALSTAT (API)
- **Indicadores clave**: términos del intercambio, exportaciones por intensidad tecnológica, comercio intrarregional, IED en AL, PIB y empleo
- **Cobertura**: América Latina y Caribe, series desde ~1950 para algunos indicadores
- **API**: `https://statistics.cepal.org/portal/cepalstat/api/v1/indicator/{id}/data?lang=es&format=json`
- **Sin key**
- **Ejemplo**: bajar términos del intercambio de Argentina 1990-2024
- **Prompt modelo**: "Escribí código Python que use la API de CEPALSTAT para descargar el índice de términos del intercambio de Argentina desde 1990, lo ponga en un DataFrame y haga un gráfico de línea"
- **Útil para**: temas 5 (Prebisch-Singer), 6 (UE-Mercosur), 8 (TCR), U4 en general
- **Nota**: la API de CEPALSTAT puede requerir exploración previa para encontrar el ID del indicador. Incluir tabla con IDs de los indicadores más relevantes

#### Fuente 6: World Bank Pink Sheet (Excel descargable)
- **Indicadores clave**: precios mensuales de ~70 commodities (soja, maíz, trigo, petróleo, gas, litio, cobre, oro, etc.) desde 1960
- **Cobertura**: mundial, mensual
- **Acceso**: descarga directa de Excel desde URL fija del Banco Mundial
- **URL**: `https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx`
- **Ejemplo**: cargar el Excel, filtrar precio de soja 2000-2024, graficar
- **Prompt modelo**: "Escribí código Python que descargue el Pink Sheet del Banco Mundial (Excel de precios de commodities), filtre el precio mensual de la soja desde 2000, y haga un gráfico de línea"
- **Útil para**: temas 2 (litio), 5 (Prebisch-Singer), 8 (TCR), 11 (energía)
- **Nota**: el Pink Sheet se puede descargar automáticamente desde la URL (no requiere upload manual). Es un Excel con múltiples hojas — indicar cuál usar

#### Fuente 7: INDEC — Intercambio Comercial Argentino (CSV/Excel manual)
- **Indicadores clave**: exportaciones e importaciones por grandes rubros (MOI, MOA, Primarios, Combustibles), por destino, por producto NCM, mensual desde 1992
- **Cobertura**: Argentina, mensual
- **Acceso**: descarga manual desde indec.gob.ar → Comercio exterior
- **NO tiene API pública**
- **Ejemplo**: descargar el Excel de series de tiempo, subirlo a Colab, filtrar exportaciones por rubros 2010-2024
- **Prompt modelo**: "Tengo un archivo Excel del INDEC con exportaciones argentinas por grandes rubros. Escribí código Python que lo lea, filtre desde 2010, y haga un gráfico de barras apiladas mostrando la composición (MOI, MOA, Primarios, Combustibles) por año"
- **Útil para**: temas 5 (canasta exportadora), 8 (TCR y exportaciones), 9 (agroalimentos)
- **Nota**: incluir instrucciones paso a paso de cómo navegar indec.gob.ar para encontrar las series. Incluir screenshot o descripción del path. Explicar cómo subir archivo a Colab (botón de upload o Google Drive)

#### Fuente 8: ADEFA — Asociación de Fábricas de Automotores (Excel/PDF manual)
- **Indicadores clave**: producción nacional por terminal y modelo, ventas al mercado interno, exportaciones por destino
- **Cobertura**: Argentina, mensual/anual
- **Acceso**: descarga manual desde adefa.org.ar → Estadísticas
- **NO tiene API**
- **Ejemplo**: descargar datos de producción, subirlos a Colab, comparar producción vs exportaciones
- **Prompt modelo**: "Tengo un archivo Excel de ADEFA con producción automotriz argentina por año. Escribí código que lo lea y haga un gráfico de barras comparando producción total, ventas internas y exportaciones"
- **Útil para**: tema 1 (complejo automotriz ARG-BRA)

#### Fuente 9: CEP XXI — Centro de Estudios para la Producción (PDF + Excel)
- **Indicadores clave**: informes sectoriales con datos de empleo, producción, comercio exterior, contenido importado. Sectores: automotriz, electrónica TDF, agroalimentos, textil, software
- **Cobertura**: Argentina, datos procesados por sector
- **Acceso**: argentina.gob.ar/produccion/cep → Informes
- **NO tiene API**. Los datos vienen dentro de informes PDF o en Excel adjuntos
- **Útil para**: temas 1, 3, 9 (datos ya procesados por sector)
- **Nota**: no se conecta por código — se bajan los informes y se extraen datos manualmente. Incluir como referencia de "datos ya masticados"

#### Fuente 10: TradeMap — International Trade Centre (web + descarga)
- **Indicadores clave**: exportaciones e importaciones por producto y destino, cuotas de mercado, RCA, datos bilaterales
- **Cobertura**: ~220 países, HS 2-6 dígitos
- **Acceso**: trademap.org (registro gratis, descarga en Excel/CSV)
- **NO tiene API pública** (tiene bulk download para usuarios registrados)
- **Útil para**: análisis de socios comerciales, cálculo de RCA, diversificación de canasta

#### Fuente 11: USGS — US Geological Survey (PDF + Excel)
- **Indicadores clave**: producción mundial de minerales por país (litio, cobre, oro, plata, etc.), reservas estimadas
- **Acceso**: usgs.gov → Mineral Commodity Summaries (anual, descarga PDF/Excel)
- **Útil para**: tema 2 (litio)

#### Fuente 12: ANFAVEA — Asociación Nacional de Fabricantes de Vehículos de Brasil (Excel)
- **Indicadores clave**: producción, ventas y comercio exterior automotriz Brasil
- **Acceso**: anfavea.com.br → Estatísticas (descarga Excel)
- **Útil para**: tema 1 (comparación ARG-BRA autos)

---

### Bloque 3 — Workflow: cómo armar tu propio notebook de datos (markdown)

**Objetivo**: enseñar el patrón de trabajo que van a repetir en el coloquio.

**Celda markdown — El workflow en 6 pasos**:

```
PASO 1: Definí tu pregunta
  → "¿La apreciación cambiaria reprimariza las exportaciones argentinas?"

PASO 2: Identificá qué datos necesitás
  → ITCRM (para medir apreciación) + Exportaciones por rubro (para medir composición)

PASO 3: Buscá en el catálogo (Bloque 2) dónde están esos datos
  → ITCRM: BCRA API (variable 4)
  → Exportaciones por rubro: INDEC-ICA (Excel manual)

PASO 4: Creá una celda por fuente al INICIO del notebook
  → Celda 1: conexión BCRA → DataFrame df_tcr
  → Celda 2: carga INDEC → DataFrame df_expo

PASO 5: Filtrá y procesá cada fuente por separado
  → df_tcr: promediar por año, filtrar 2000-2024
  → df_expo: calcular % de cada rubro sobre el total

PASO 6: Cruzá las fuentes si necesitás (merge por año)
  → df_merged = df_tcr.merge(df_expo, on='año')
  → Gráfico: ITCRM vs % MOI en exportaciones
```

**Celda markdown — Reglas prácticas**:
- Las fuentes **siempre van al inicio** del notebook (como los imports van al inicio de un programa)
- **Un DataFrame por fuente**: `df_bcra`, `df_indec`, `df_comtrade`
- Si necesitás una fuente nueva, **creá una celda nueva arriba** (no la metas entre el análisis)
- Nombrá las variables de forma descriptiva: `df_tcr_mensual`, `df_expo_rubros`, `df_precios_soja`
- **Guardá siempre la fecha de descarga**: "Datos descargados el 15/05/2026" — los datos cambian

---

### Bloque 4 — Operaciones básicas con datos (markdown + código)

**Objetivo**: enseñar las 5 operaciones que van a necesitar siempre.

Cada operación tiene:
- Celda markdown con explicación breve
- Celda código con ejemplo ejecutable
- Prompt modelo para Gemini

#### 4.1 — Filtrar por período
- "Quedate solo con los datos de 2010 a 2024"
- `df = df[df['year'].between(2010, 2024)]`
- **Prompt**: "Filtrá el DataFrame para quedarme solo con los años entre 2010 y 2024"

#### 4.2 — Filtrar por país/categoría
- "Quedate solo con Argentina y Brasil"
- `df = df[df['country'].isin(['ARG', 'BRA'])]`
- **Prompt**: "Filtrá para quedarme solo con los datos de Argentina y Brasil"

#### 4.3 — Calcular proporciones
- "¿Qué porcentaje de las exportaciones son MOI?"
- `df['pct_moi'] = df['moi'] / df['total'] * 100`
- **Prompt**: "Agregá una columna que calcule el porcentaje de MOI sobre el total de exportaciones"

#### 4.4 — Agrupar y resumir
- "Dame el promedio por año" o "Dame el total por país"
- `df.groupby('year')['value'].mean()`
- **Prompt**: "Agrupá por año y calculá el promedio del indicador"

#### 4.5 — Hacer un gráfico
- Gráfico de líneas (series temporales), barras (comparación), barras apiladas (composición)
- Incluir la paleta del curso: `#1F4E79, #2E75B6, #0EA5E9, #E8833A, #27AE60, #E74C3C`
- **Prompt**: "Hacé un gráfico de líneas con año en el eje X y el valor en el eje Y, con título y fuente"

---

### Bloque 5 — Cruce de fuentes (markdown + código)

**Objetivo**: mostrar que se pueden combinar datos de fuentes distintas para un análisis más rico.

**Celda markdown — ¿Qué es cruzar fuentes?**:
- "Cruzar" = combinar dos tablas usando una columna en común (generalmente año o país)
- Ejemplo: ITCRM del BCRA (por año) + composición exportadora del INDEC (por año) → una tabla con las dos variables para cada año
- En pandas: `df_merged = df1.merge(df2, on='year')`

**Celda código — Ejemplo completo ejecutable**:
1. Bajar ITCRM del BCRA (API) → `df_tcr`
2. Bajar exportaciones de Argentina del Banco Mundial (API) → `df_expo`
3. Merge por año → `df_merged`
4. Gráfico de doble eje: ITCRM (línea azul, eje izquierdo) + exportaciones/PIB (línea naranja, eje derecho)
5. Interpretación: "¿se mueven juntos? ¿hay relación?"

**Celda markdown — Nota metodológica**:
- Cruzar fuentes requiere que las dos tablas tengan al menos una columna en común
- Cuidado con: diferentes frecuencias (mensual vs anual → agregar primero), diferentes nombres de país (ARG vs Argentina vs 032)
- El merge puede perder filas si un año está en una fuente pero no en la otra (explicar `how='inner'` vs `how='outer'`)

---

### Bloque 6 — Ejercicios de práctica (2-3 ejercicios cortos)

**No evaluativos** — son para que prueben la mecánica antes de usarla en el coloquio.

#### Ejercicio 1: "Conectate a una API" (~5 min)
- **Consigna**: "Usando la API del Banco Mundial, bajá el PIB per cápita (NY.GDP.PCAP.CD) de Argentina, Chile y Uruguay desde 2000. Hacé un gráfico de líneas."
- **Pista**: copiá la celda del Banco Mundial del catálogo y cambiá el indicador y los países
- Celda vacía para código
- Celda vacía para interpretación: "¿Cuál creció más? ¿Hay algún quiebre visible?"

#### Ejercicio 2: "Cargá un archivo descargado" (~5 min)
- **Consigna**: "Descargá el Pink Sheet del Banco Mundial. Encontrá el precio mensual del petróleo crudo (Brent) desde 2000. Hacé un gráfico."
- **Pista**: el Pink Sheet se puede descargar automáticamente con la URL del catálogo
- Celda vacía para código
- Celda vacía para interpretación: "¿Qué pasó en 2008? ¿Y en 2020? ¿Podés identificar los shocks?"

#### Ejercicio 3: "Cruzá dos fuentes" (~10 min)
- **Consigna**: "Combiná el ITCRM del BCRA con las exportaciones/PIB del Banco Mundial para Argentina, ambos por año desde 2005. Hacé un gráfico de doble eje. ¿Se mueven juntos?"
- **Pista**: primero bajá cada fuente por separado, después hacé merge por año
- Celda vacía para código
- Celda vacía para interpretación: "¿Cuándo el TCR sube, las exportaciones/PIB suben también? ¿Siempre?"

---

### Bloque 7 — Cierre y tips para el coloquio (markdown)

**Contenido**:
- Resumen del workflow: pregunta → datos → fuente → descargar → filtrar → graficar → interpretar → cruzar si es necesario
- "Este notebook es tu referencia. Cada vez que necesites una fuente, volvé acá."
- Tips para el coloquio:
  - Arrancá por los datos ANTES de armar slides — los datos te van a decir qué historia contar
  - Mínimo 2 gráficos propios con datos reales (requisito de la consigna)
  - Citá siempre la fuente: "Fuente: BCRA, ITCRM multilateral" al pie del gráfico
  - Si un dato no te cierra, verificá con otra fuente (triangulación)
- Tabla resumen: fuente → tipo de acceso → qué tema del coloquio cubre

---

## Decisiones de diseño pendientes

### 1. ¿Incluir las API keys como secretos de Colab?
- FRED y COMTRADE requieren API key
- Opción A: el alumno se registra y pone su propia key
- Opción B: el docente provee una key compartida (riesgo de rate limiting)
- **Propuesta**: Opción A para FRED (registro simple), evaluar si COMTRADE vale la pena dado que la API free tiene 100 calls/día

### 2. ¿Verificar disponibilidad de las APIs antes de publicar?
- Las APIs del BCRA y CEPALSTAT pueden tener downtime o cambios de endpoint
- **Propuesta**: verificar cada endpoint al momento de armar el notebook. Incluir un bloque de "fallback" para cada fuente con API: "Si la API no responde, podés descargar los datos manualmente desde [URL]"

### 3. ¿Qué fuentes incluir como código ejecutable vs solo referencia?
- **Con código ejecutable** (celda que funciona al correr): Banco Mundial, BCRA, FRED, Pink Sheet, CEPALSTAT, COMTRADE
- **Solo referencia** (markdown con instrucciones de descarga): INDEC-ICA, ADEFA, CEP XXI, TradeMap, USGS, ANFAVEA
- Criterio: si se puede automatizar la descarga, incluir código. Si requiere navegación web manual, dar instrucciones paso a paso

### 4. ¿Incluir imágenes/screenshots de las páginas de descarga?
- Para INDEC y ADEFA, un screenshot del portal ayudaría mucho
- **Propuesta**: sí, incluir capturas de pantalla embebidas en celdas markdown para las fuentes manuales. Guardar en `notebooks/img/` o embeber como base64

### 5. ¿Cuántos ejercicios de práctica?
- **Propuesta**: 3 ejercicios (API simple, CSV/Excel, cruce). Suficiente para probar las tres mecánicas sin que se haga largo. No evaluativos.

### 6. ¿Tabla de códigos de país y producto?
- COMTRADE usa códigos numéricos (032=Argentina, 076=Brasil), el Banco Mundial usa ISO3 (ARG, BRA)
- **Propuesta**: incluir una tabla de referencia con los 10-15 países más usados en el curso y sus códigos en cada sistema. Idem para capítulos HS relevantes (87=vehículos, 27=combustibles, 12=oleaginosas, etc.)

### 7. ¿Extensión esperada del notebook?
- Estimación: ~35-40 celdas
  - Bloque 0: 1-2 celdas
  - Bloque 1: 3 celdas (explicación + 2 demos)
  - Bloque 2: ~24 celdas (12 fuentes × 2 celdas: markdown + código o instrucciones)
  - Bloque 3: 1-2 celdas (workflow)
  - Bloque 4: 10 celdas (5 operaciones × 2: explicación + código)
  - Bloque 5: 3-4 celdas (explicación + ejemplo + nota)
  - Bloque 6: 6-9 celdas (3 ejercicios × 2-3 celdas)
  - Bloque 7: 1-2 celdas (cierre)
- Total estimado: ~50 celdas
- Tiempo de lectura/exploración: ~30-45 min si lo recorren completo

---

## Conexión con otros materiales

| Material | Relación |
|----------|----------|
| NB1 | Los alumnos ya usaron la API del Banco Mundial ahí — pueden volver a ese patrón |
| NB2 | Ya calcularon RCA con datos del Banco Mundial — este notebook amplía las fuentes |
| Coloquio | Referencia directa: cada tema tiene fuentes sugeridas en el feedback que remiten a este catálogo |
| Evaluaciones U4+ | Si las evaluaciones incluyen búsqueda de datos, este notebook es el prerequisito |
| notebooks.html | Agregar card nueva sin número de NB, con tag "Guía de referencia" |
| asistente-ia.html | Complementario: NotebookLM para bibliografía, este notebook para datos |

---

## Resumen ejecutivo

- **Qué es**: notebook formativo de referencia para aprender a trabajar con fuentes de datos
- **Para quién**: alumnos que ya hicieron NB1-NB2 y necesitan datos para el coloquio
- **Cuándo se abre**: S6 (14/05), antes del borrador del coloquio (28/05)
- **Qué enseña**: API vs CSV, 12 fuentes del curso, workflow de datos, operaciones básicas, cruce de fuentes
- **Qué NO enseña**: programación, estadística, interpretación económica (eso lo aprenden en clase)
- **Evaluación**: ninguna — es una herramienta de consulta
- **Extensión**: ~50 celdas, 30-45 min de exploración
