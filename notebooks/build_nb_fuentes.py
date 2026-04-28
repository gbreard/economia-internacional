"""Script para generar NB_fuentes_datos.ipynb"""
import json, sys, os

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

cells = []

def md(source):
    cells.append({
        'cell_type': 'markdown',
        'metadata': {},
        'source': [line + '\n' for line in source.strip().split('\n')]
    })

def code(source):
    cells.append({
        'cell_type': 'code',
        'metadata': {},
        'source': [line + '\n' for line in source.strip().split('\n')],
        'outputs': [],
        'execution_count': None
    })

# ===== BLOQUE 0: INTRODUCCIÓN =====

md(r'''# Guía práctica: fuentes de datos para economía internacional

**Economía Internacional — UMET 2026**

---

## ¿Para qué sirve este notebook?

Este notebook es tu **caja de herramientas para conseguir datos**. No evalúa contenido económico: te enseña la habilidad de conectarte a fuentes de datos reales, descargarlas, filtrarlas y combinarlas para tus propios análisis.

**Usalo como referencia**: no hace falta leerlo de corrido. Cuando necesites una fuente de datos, vení acá, buscá la fuente y copiá el patrón.

### ¿Qué vas a aprender?
1. Qué es una **API** y qué es un **CSV/Excel** (dos formas de acceder a datos)
2. Cómo conectarte a **12 fuentes de datos** del curso (con código que funciona)
3. Cómo **filtrar, procesar y graficar** datos
4. Cómo **cruzar** dos fuentes distintas en un mismo análisis

### ¿Cómo usarlo?
- El código lo genera **Gemini** (el chat de IA integrado en Colab) — vos le decís qué querés y él escribe el código
- Para cada fuente hay un **prompt modelo**: un texto que podés copiar y adaptar para pedirle a Gemini
- Los **ejercicios de práctica** al final son opcionales — son para que pruebes la mecánica antes de usarla en el coloquio

### Workflow: de la pregunta al análisis

```
Tu pregunta de investigación
        ↓
¿Qué datos necesitás? (indicador, período, países)
        ↓
¿Dónde están? → CATÁLOGO DE FUENTES (este notebook)
        ↓
¿Cómo se accede? → API (automático) o CSV/Excel (manual)
        ↓
Descargar → Filtrar → Visualizar → Interpretar
        ↓
¿Necesitás otra fuente? → Agregar celda nueva, repetir
        ↓
¿Querés cruzar fuentes? → Merge por año/país
```

> **Regla de oro**: las fuentes se definen al inicio del notebook. Si necesitás una fuente nueva, creá una celda nueva y repetí el patrón.''')

# ===== BLOQUE 1: API vs CSV =====

md(r'''---

# Bloque 1 — ¿Qué es una API? ¿Y un CSV?

Hay dos formas principales de conseguir datos para tu análisis:

## API (Application Programming Interface)

Un **"mostrador digital"** donde le pedís datos a un servidor y te los devuelve automáticamente. El código se conecta directo a la fuente — no necesitás entrar a ninguna página web.

- **Ventajas**: automático, reproducible (cualquiera puede correr tu código y obtener los mismos datos), siempre actualizado
- **Desventajas**: no todas las fuentes tienen API; a veces hay límites de uso o requieren registrarse para obtener una "llave" (API key)
- **Analogía**: es como pedir comida por delivery — le decís qué querés y te lo traen

## CSV / Excel (descarga manual)

Entrás a la página de la fuente, filtrás lo que necesitás, descargás el archivo, y lo subís a Colab.

- **Ventajas**: funciona con cualquier fuente, más control sobre qué descargás
- **Desventajas**: manual, no se actualiza solo, puede haber errores de formato
- **Analogía**: es como ir al supermercado — vos elegís y traés

## ¿Cuándo usar cada uno?

| Fuente | Tipo | ¿Por qué? |
|--------|------|-----------|
| Banco Mundial | API | Tiene API pública, miles de indicadores |
| BCRA | API + archivo | API para TC nominal; archivo descargable para ITCRM |
| INDEC | CSV/Excel | No tiene API pública, hay que descargar de la web |
| FRED (Fed EEUU) | API | Requiere API key (gratis, 2 min de registro) |
| ADEFA | Excel/PDF | Solo descarga manual |

Veamos un ejemplo rápido de cada uno:''')

code(r'''# === EJEMPLO: conectarse a una API (Banco Mundial) ===
# 3 líneas que bajan un dato y lo muestran

import pandas as pd
import requests

# Pedimos el PIB per cápita de Argentina, último año disponible
url = "https://api.worldbank.org/v2/country/ARG/indicator/NY.GDP.PCAP.CD?format=json&per_page=1&mrv=1"
resp = requests.get(url).json()
valor = resp[1][0]['value']
anio = resp[1][0]['date']
print(f"PIB per cápita de Argentina en {anio}: US$ {valor:,.0f}")
print("\n✅ Eso es una API: le pediste un dato y te lo devolvió sin descargar nada.")''')

code(r'''# === EJEMPLO: cargar un archivo CSV/Excel ===
# Supongamos que descargaste un Excel del INDEC y lo subiste a Colab

# Para subir un archivo a Colab:
# 1. Hacé clic en el ícono de carpeta (📁) en el panel izquierdo
# 2. Hacé clic en "Subir" (ícono de flecha hacia arriba)
# 3. Seleccioná tu archivo

# Después lo leés así:
# df = pd.read_excel("nombre_del_archivo.xlsx")
# df.head()

# O si es CSV:
# df = pd.read_csv("nombre_del_archivo.csv")
# df.head()

print("📁 Para archivos Excel/CSV: descargá de la web → subí a Colab → leé con pandas")
print("🔌 Para APIs: el código se conecta directo — no hay archivo intermedio")''')

# ===== BLOQUE 2: CATÁLOGO =====

md(r'''---

# Bloque 2 — Catálogo de fuentes

Acá están las **12 fuentes de datos** que usamos en el curso. Para cada una: qué tiene, cómo se accede, ejemplo funcional y prompt para Gemini.

---

## Fuente 1: Banco Mundial (API — sin registro)

**Qué tiene**: ~1.500 indicadores para ~220 países desde 1960. Comercio/PIB, IED, cuenta corriente, PIB per cápita, pobreza, educación, salud, emisiones...

**Cómo se accede**: API REST pública, sin necesidad de registro ni API key.

**URL de referencia**: https://data.worldbank.org/indicator

**Indicadores más útiles para el curso**:

| Código | Indicador |
|--------|-----------|
| `NE.TRD.GNFS.ZS` | Apertura comercial (Trade % of GDP) |
| `BN.CAB.XOKA.GD.ZS` | Cuenta corriente (% PIB) |
| `NE.EXP.GNFS.ZS` | Exportaciones (% PIB) |
| `NE.IMP.GNFS.ZS` | Importaciones (% PIB) |
| `NY.GDP.PCAP.CD` | PIB per cápita (US$ corrientes) |
| `BX.KLT.DINV.WD.GD.ZS` | IED neta (% PIB) |

**Prompt para Gemini**: *"Escribí código Python que use la API del Banco Mundial para descargar el indicador NE.TRD.GNFS.ZS (Trade % of GDP) para Argentina, Brasil y Chile desde 2000 hasta 2024, lo ponga en un DataFrame y haga un gráfico de líneas"*

**Útil para**: contexto macro, todos los temas del coloquio''')

code(r'''# === FUENTE 1: Banco Mundial — Ejemplo funcional ===
import pandas as pd
import requests

# Parámetros (CAMBIÁ ESTOS para tu análisis)
paises = ["ARG", "BRA", "CHL"]
indicador = "NE.TRD.GNFS.ZS"   # Apertura comercial
anio_desde = 2000
anio_hasta = 2024

# Descargar datos
datos = []
for pais in paises:
    url = f"https://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?format=json&date={anio_desde}:{anio_hasta}&per_page=100"
    resp = requests.get(url).json()
    if len(resp) > 1 and resp[1]:
        for obs in resp[1]:
            if obs['value'] is not None:
                datos.append({'pais': obs['country']['value'], 'anio': int(obs['date']), 'valor': obs['value']})

df_bm = pd.DataFrame(datos)
print(f"✅ {len(df_bm)} observaciones descargadas del Banco Mundial")
print(df_bm.pivot(index='anio', columns='pais', values='valor').tail())''')

# === FUENTE 2: BCRA ===

md(r'''---

## Fuente 2: BCRA — Banco Central de Argentina (API v4.0 + archivos)

**Qué tiene**: tipo de cambio nominal, reservas internacionales, base monetaria, tasas de interés. El **ITCRM** (Índice de Tipo de Cambio Real Multilateral) no está en la API — se descarga como archivo.

**Cómo se accede**:
- **API v4.0** (vigente desde 2026): para tipo de cambio nominal, reservas, variables monetarias
- **Archivo TXT/Excel**: para el ITCRM (multilateral y bilateral)

**API base**: `https://api.bcra.gob.ar/estadisticas/v4.0/Monetarias/{IdVariable}`

**Variables más útiles (API)**:

| IdVariable | Descripción |
|------------|-------------|
| 4 | Tipo de cambio minorista (vendedor, promedio) |
| 5 | Tipo de cambio mayorista de referencia |
| 1 | Reservas internacionales (millones USD) |

**ITCRM (no está en API)**: se descarga directo de:
- Multilateral: `https://www.bcra.gob.ar/archivos/PublicacionesEstadisticas/itcrm.txt`
- Bilateral EEUU: `https://www.bcra.gob.ar/archivos/PublicacionesEstadisticas/ITCRM_EEUU.txt`
- Bilateral Brasil: `https://www.bcra.gob.ar/archivos/PublicacionesEstadisticas/ITCRM_brasil.txt`

**Documentación oficial**: https://www.bcra.gob.ar/en/central-bank-api-catalog/

**Útil para**: temas 1, 6, 8 del coloquio (tipo de cambio, competitividad)''')

code(r'''# === FUENTE 2a: BCRA API v4.0 — Tipo de cambio nominal ===
import pandas as pd
import requests

# Descargar tipo de cambio minorista (variable 4)
url = "https://api.bcra.gob.ar/estadisticas/v4.0/Monetarias/4?desde=2024-01-01&hasta=2025-12-31&limit=3000"
resp = requests.get(url, verify=False)  # verify=False porque el cert BCRA a veces falla en Colab
data = resp.json()

# Parsear resultados
registros = []
for item in data['results']:
    for det in item['detalle']:
        registros.append({'fecha': det['fecha'], 'tc_nominal': det['valor']})

df_tc = pd.DataFrame(registros)
df_tc['fecha'] = pd.to_datetime(df_tc['fecha'])
df_tc = df_tc.sort_values('fecha')

print(f"✅ {len(df_tc)} observaciones de tipo de cambio nominal (BCRA)")
print(df_tc.tail())''')

code(r'''# === FUENTE 2b: BCRA — ITCRM (archivo, no API) ===
import pandas as pd
import requests
import re

# Descargar el archivo de texto del ITCRM multilateral
url = "https://www.bcra.gob.ar/archivos/PublicacionesEstadisticas/itcrm.txt"
resp = requests.get(url, verify=False)
texto = resp.text

# Parsear: el formato es [Date.UTC(año,mes,dia),valor]
patron = r"Date\.UTC\((\d+),(\d+),(\d+)\),([\d.]+)"
matches = re.findall(patron, texto)

registros = []
for anio, mes, dia, valor in matches:
    # Ojo: en JavaScript los meses van de 0-11, en Python de 1-12
    fecha = f"{anio}-{int(mes)+1:02d}-{int(dia):02d}"
    registros.append({'fecha': fecha, 'itcrm': float(valor)})

df_itcrm = pd.DataFrame(registros)
df_itcrm['fecha'] = pd.to_datetime(df_itcrm['fecha'])

# Filtrar desde 2000
df_itcrm = df_itcrm[df_itcrm['fecha'] >= '2000-01-01']

print(f"✅ {len(df_itcrm)} observaciones del ITCRM multilateral (BCRA)")
print(f"Período: {df_itcrm['fecha'].min().date()} a {df_itcrm['fecha'].max().date()}")
print(df_itcrm.tail())''')

# === FUENTE 3: FRED ===

md(r'''---

## Fuente 3: FRED — Federal Reserve Bank of St. Louis (API — requiere registro)

**Qué tiene**: ~800.000 series de datos macro, principalmente EEUU: tasas de interés, inflación (CPI), desempleo, tipo de cambio del dólar, precio del oro.

**Cómo se accede**: API REST. **Requiere API key gratuita**.

### ⚠️ Cómo obtener tu API key (2 minutos):
1. Entrá a https://fred.stlouisfed.org/
2. Hacé clic en "My Account" → "Create Account" (es gratis)
3. Una vez logueado, andá a https://fredaccount.stlouisfed.org/apikeys
4. Hacé clic en "Request API Key" → completá el formulario breve
5. Copiá la key (es un código alfanumérico largo)

**Series más útiles**:

| Serie ID | Descripción |
|----------|-------------|
| `DFF` | Federal Funds Rate (tasa de la Fed) |
| `CPIAUCSL` | CPI EEUU (índice de precios al consumidor) |
| `GOLDAMGBD228NLBM` | Precio del oro (USD/oz) |

**Útil para**: contexto internacional, tasas de interés, precio del dólar

> ⚠️ Nunca compartas tu API key públicamente.''')

code(r'''# === FUENTE 3: FRED — Ejemplo funcional ===
# ⚠️ Necesitás tu propia API key (ver instrucciones arriba)
import pandas as pd
import requests

FRED_API_KEY = "TU_API_KEY_ACA"  # ← Reemplazá con tu key

if FRED_API_KEY == "TU_API_KEY_ACA":
    print("⚠️ Necesitás reemplazar TU_API_KEY_ACA con tu key de FRED")
    print("   Registrate gratis en https://fred.stlouisfed.org/")
else:
    serie = "DFF"  # Federal Funds Rate
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={serie}&api_key={FRED_API_KEY}&file_type=json&observation_start=2000-01-01"
    resp = requests.get(url).json()

    df_fred = pd.DataFrame(resp['observations'])
    df_fred['date'] = pd.to_datetime(df_fred['date'])
    df_fred['value'] = pd.to_numeric(df_fred['value'], errors='coerce')

    print(f"✅ {len(df_fred)} observaciones de {serie} (FRED)")
    print(df_fred.tail())''')

# === FUENTE 4: Pink Sheet ===

md(r'''---

## Fuente 4: World Bank Pink Sheet — Precios de commodities (Excel descargable)

**Qué tiene**: precios mensuales de ~70 commodities desde 1960. Soja, maíz, trigo, petróleo, gas, litio, cobre, oro, aluminio...

**Cómo se accede**: Excel descargable desde URL fija (no requiere registro). El código puede bajarlo automáticamente.

**Hoja del Excel**: "Monthly Prices" (precios mensuales en USD)

**Prompt para Gemini**: *"Descargá el Pink Sheet del Banco Mundial, filtrá el precio mensual de la soja desde 2000, y hacé un gráfico de línea"*

**Útil para**: temas 2 (litio), 5 (Prebisch-Singer, TDI), 8 (precios de exportación), 11 (energía)''')

code(r'''# === FUENTE 4: Pink Sheet — Precios de commodities ===
import pandas as pd

# Descargar directo (no hace falta bajar a mano)
url = "https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx"
df_pink = pd.read_excel(url, sheet_name="Monthly Prices", header=4)

# Veamos qué columnas tiene
print("Columnas disponibles (primeras 20):")
for i, col in enumerate(df_pink.columns[:20]):
    print(f"  {i}: {col}")

print(f"\n✅ {len(df_pink)} filas descargadas del Pink Sheet")
print('\nPara filtrar un commodity específico, pedile a Gemini:')
print('"Filtrá la columna de soja (Soybeans) desde el año 2000 y hacé un gráfico"')''')

# === FUENTE 5: COMTRADE ===

md(r'''---

## Fuente 5: UN COMTRADE — Comercio bilateral por producto (API — requiere registro)

**Qué tiene**: comercio bilateral por producto para ~200 países desde 1962. Exportaciones e importaciones desagregadas por capítulo HS.

**Cómo se accede**: API REST. **Requiere registro gratuito** (100 consultas/día en plan free).

### ⚠️ Cómo obtener tu API key:
1. Entrá a https://comtradeplus.un.org/
2. Creá una cuenta (botón "Register", es gratis)
3. Una vez logueado, andá a tu perfil → API Subscription → copiá tu key

**Códigos de país y producto**: consultá en https://comtradeplus.un.org/TradeFlow

Algunos códigos frecuentes: ARG=032, BRA=076, CHN=156, USA=842, DEU=276

**Capítulos HS relevantes**: 87 (vehículos), 27 (combustibles), 12 (oleaginosas/soja), 15 (aceites), 84 (maquinaria), 85 (electrónica), 28 (químicos inorgánicos/litio)

**Útil para**: temas 1 (autos), 3 (TDF electrónica), 4 (antidumping), cálculo de GL bilateral

> ⚠️ La API free tiene límite de 100 consultas por día. Guardá los resultados.''')

code(r'''# === FUENTE 5: UN COMTRADE — Ejemplo funcional ===
# ⚠️ Necesitás tu propia API key (ver instrucciones arriba)
import pandas as pd
import requests

COMTRADE_API_KEY = "TU_API_KEY_ACA"  # ← Reemplazá con tu key

if COMTRADE_API_KEY == "TU_API_KEY_ACA":
    print("⚠️ Necesitás reemplazar TU_API_KEY_ACA con tu key de UN COMTRADE")
    print("   Registrate gratis en https://comtradeplus.un.org/")
else:
    # Exportaciones de Argentina a Brasil, vehículos (HS 87), 2020-2023
    url = "https://comtradeapi.un.org/data/v1/get/C/A/HS"
    params = {
        'reporterCode': '032',      # Argentina
        'partnerCode': '076',       # Brasil
        'period': '2020,2021,2022,2023',
        'cmdCode': '87',            # Vehículos
        'flowCode': 'X',            # Exportaciones
        'subscription-key': COMTRADE_API_KEY
    }
    resp = requests.get(url, params=params)
    data = resp.json()

    if 'data' in data:
        df_comtrade = pd.DataFrame(data['data'])
        cols = ['period', 'reporterDesc', 'partnerDesc', 'cmdDesc', 'primaryValue']
        print(df_comtrade[cols].head(10))
        print(f"\n✅ {len(df_comtrade)} registros de COMTRADE")
    else:
        print(f"Respuesta: {data}")''')

# === FUENTE 6: INDEC ===

md(r'''---

## Fuente 6: INDEC — Intercambio Comercial Argentino (descarga manual)

**Qué tiene**: exportaciones e importaciones de Argentina por grandes rubros (MOI, MOA, Primarios, Combustibles), por destino, por producto. Mensual desde 1992.

**Cómo se accede**: **descarga manual** desde la web del INDEC. No tiene API pública.

### Paso a paso para descargar:
1. Entrá a https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-2-40
2. Buscá "Series de tiempo" o "Cuadros estadísticos"
3. Descargá el Excel de "Exportaciones por grandes rubros"
4. Subí el archivo a Colab (ícono de carpeta 📁 → botón de subir)

**Prompt para Gemini**: *"Tengo un archivo Excel del INDEC con exportaciones argentinas por grandes rubros. Escribí código que lo lea, filtre desde 2010, y haga un gráfico de barras apiladas con la composición (MOI, MOA, Primarios, Combustibles) por año"*

**Útil para**: temas 5 (canasta exportadora), 8 (TCR y exportaciones), 9 (agroalimentos)

> 💡 **Tip**: guardá el Excel en Google Drive y montá Drive en Colab. Así no tenés que subirlo cada vez.''')

code(r'''# === FUENTE 6: INDEC — Ejemplo de carga de Excel ===

# PASO 1: Subir el archivo a Colab
# (hacé clic en 📁 en el panel izquierdo → botón de subir)

# PASO 2: Leerlo con pandas
# import pandas as pd
# df_indec = pd.read_excel("nombre_del_archivo.xlsx")

# ALTERNATIVA: montar Google Drive
# from google.colab import drive
# drive.mount('/content/drive')
# df_indec = pd.read_excel("/content/drive/MyDrive/datos/indec_exportaciones.xlsx")

# PASO 3: Explorar
# print(df_indec.columns)  # ver qué columnas tiene
# print(df_indec.head())   # ver las primeras filas
# print(df_indec.shape)    # ver cuántas filas y columnas

print("📥 Para el INDEC: descargá el Excel → subilo a Colab → leelo con pd.read_excel()")
print("📂 Si lo guardás en Google Drive, montá Drive y leelo desde ahí")''')

# === FUENTES 7-12 ===

md(r'''---

## Fuentes adicionales (descarga manual — referencia)

Las siguientes fuentes **no tienen API**. Instrucciones para descargar y cargar:

### Fuente 7: ADEFA — Asociación de Fábricas de Automotores
- **Qué tiene**: producción nacional, ventas, exportaciones por terminal y modelo
- **Dónde**: https://adefa.org.ar → Estadísticas
- **Formato**: Excel | **Útil para**: tema 1 (autos)

### Fuente 8: ANFAVEA — Industria automotriz Brasil
- **Qué tiene**: producción, ventas y exportaciones de Brasil
- **Dónde**: https://anfavea.com.br → Estatísticas
- **Formato**: Excel | **Útil para**: tema 1 (comparación ARG-BRA)

### Fuente 9: CEP XXI — Centro de Estudios para la Producción
- **Qué tiene**: informes sectoriales con datos de empleo, producción, comercio exterior
- **Dónde**: https://www.argentina.gob.ar/produccion/cep → Informes
- **Formato**: PDF + Excel | **Útil para**: temas 1, 3, 9

### Fuente 10: Secretaría de Minería
- **Qué tiene**: producción, exportaciones e IED en litio, oro, cobre
- **Dónde**: https://www.argentina.gob.ar/economia/mineria
- **Formato**: Excel/PDF | **Útil para**: tema 2 (litio)

### Fuente 11: TradeMap — International Trade Centre
- **Qué tiene**: exportaciones/importaciones por producto y destino, RCA, cuotas de mercado
- **Dónde**: https://trademap.org (registro gratis)
- **Formato**: Excel descargable | **Útil para**: análisis de socios comerciales

### Fuente 12: USGS — US Geological Survey
- **Qué tiene**: producción mundial de minerales por país, reservas estimadas
- **Dónde**: https://www.usgs.gov → Mineral Commodity Summaries
- **Formato**: PDF + Excel | **Útil para**: tema 2 (litio, contexto mundial)

> 💡 **Para todas**: descargá → subí a Colab → `pd.read_excel()` o `pd.read_csv()` → filtrá y graficá.''')

# ===== BLOQUE 3: WORKFLOW =====

md(r'''---

# Bloque 3 — Cómo armar tu propio notebook de datos

Cuando arranques tu análisis para el coloquio, seguí este patrón:

### Paso 1: Definí tu pregunta
> "¿La apreciación cambiaria reprimariza las exportaciones argentinas?"

### Paso 2: Identificá qué datos necesitás
> ITCRM (para medir apreciación) + Exportaciones por rubro (para medir composición)

### Paso 3: Buscá en el catálogo dónde están
> ITCRM → BCRA (archivo TXT) | Exportaciones → INDEC (Excel manual)

### Paso 4: Creá una celda por fuente AL INICIO del notebook
```python
# --- FUENTE 1: BCRA - ITCRM ---
df_tcr = ...  # código de descarga

# --- FUENTE 2: INDEC - Exportaciones ---
df_expo = ...  # código de carga
```

### Paso 5: Filtrá y procesá cada fuente por separado
```python
df_tcr = df_tcr[df_tcr['fecha'] >= '2000-01-01']
df_expo['pct_moi'] = df_expo['moi'] / df_expo['total'] * 100
```

### Paso 6: Cruzá las fuentes si necesitás
```python
df_merged = df_tcr.merge(df_expo, on='anio')
```

### Reglas prácticas

- **Un DataFrame por fuente**: `df_bcra`, `df_indec`, `df_comtrade`
- **Nombres descriptivos**: `df_tcr_mensual`, `df_expo_rubros`, `df_precios_soja`
- **Fuentes al inicio**: si agregás una fuente nueva, poné la celda arriba
- **Anotá la fecha de descarga**: "Datos descargados el 15/05/2026"
- **Guardá versiones**: si modificás datos, guardá el original y trabajá sobre una copia''')

# ===== BLOQUE 4: OPERACIONES BÁSICAS =====

md(r'''---

# Bloque 4 — Operaciones básicas con datos

Las 5 operaciones que vas a necesitar siempre.''')

md(r'''### 4.1 — Filtrar por período
Quedarte solo con un rango de años.

**Prompt**: *"Filtrá el DataFrame para quedarme solo con los años entre 2010 y 2024"*''')

code(r'''# 4.1 — Filtrar por período
import pandas as pd

df_ejemplo = pd.DataFrame({'anio': range(2000, 2025), 'valor': range(25)})
df_filtrado = df_ejemplo[df_ejemplo['anio'].between(2010, 2024)]
print(f"Original: {len(df_ejemplo)} filas → Filtrado: {len(df_filtrado)} filas")
print(df_filtrado.head())''')

md(r'''### 4.2 — Filtrar por país o categoría
**Prompt**: *"Filtrá para quedarme solo con Argentina y Brasil"*''')

code(r'''# 4.2 — Filtrar por país
import pandas as pd

df_paises = pd.DataFrame({
    'pais': ['ARG', 'BRA', 'CHL', 'ARG', 'BRA', 'CHL'],
    'anio': [2020, 2020, 2020, 2021, 2021, 2021],
    'expo': [65, 210, 70, 77, 280, 85]
})

df_ab = df_paises[df_paises['pais'].isin(['ARG', 'BRA'])]
print(df_ab)''')

md(r'''### 4.3 — Calcular proporciones
**Prompt**: *"Agregá una columna que calcule el porcentaje de MOI sobre el total"*''')

code(r'''# 4.3 — Calcular proporciones
import pandas as pd

df_rubros = pd.DataFrame({
    'anio': [2020, 2021, 2022],
    'moi': [15, 18, 16], 'moa': [25, 30, 28],
    'primarios': [20, 22, 24], 'combustibles': [5, 8, 10]
})

df_rubros['total'] = df_rubros[['moi', 'moa', 'primarios', 'combustibles']].sum(axis=1)
df_rubros['pct_moi'] = (df_rubros['moi'] / df_rubros['total'] * 100).round(1)
print(df_rubros[['anio', 'total', 'moi', 'pct_moi']])''')

md(r'''### 4.4 — Agrupar y resumir
**Prompt**: *"Agrupá por año y calculá el promedio del indicador"*''')

code(r'''# 4.4 — Agrupar y resumir
import pandas as pd

df_mensual = pd.DataFrame({
    'anio': [2020]*12 + [2021]*12,
    'mes': list(range(1,13))*2,
    'valor': [100+i*2 for i in range(24)]
})

df_anual = df_mensual.groupby('anio')['valor'].mean().reset_index()
df_anual.columns = ['anio', 'promedio']
print(df_anual)''')

md(r'''### 4.5 — Hacer un gráfico
Los tres tipos más comunes: líneas (series temporales), barras (comparación), barras apiladas (composición).

**Prompt**: *"Hacé un gráfico de líneas con año en X y valor en Y, con título y fuente al pie"*''')

code(r'''# 4.5 — Gráficos básicos
import matplotlib.pyplot as plt

# Paleta del curso
colores = ['#1F4E79', '#E8833A', '#27AE60', '#2E75B6', '#E74C3C', '#0EA5E9']

anios = [2018, 2019, 2020, 2021, 2022, 2023]
arg = [65, 55, 45, 78, 88, 67]
bra = [210, 220, 190, 280, 335, 340]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(anios, arg, marker='o', color=colores[0], label='Argentina')
ax.plot(anios, bra, marker='s', color=colores[1], label='Brasil')
ax.set_title('Exportaciones de bienes (miles de millones USD)', fontsize=13, fontweight='bold')
ax.set_xlabel('Año')
ax.set_ylabel('Miles de millones USD')
ax.legend()
ax.grid(True, alpha=0.3)

# Fuente al pie (siempre incluir — es requisito del coloquio)
fig.text(0.5, -0.02, 'Fuente: Banco Mundial', ha='center', fontsize=8, color='gray')
plt.tight_layout()
plt.show()''')

# ===== BLOQUE 5: CRUCE DE FUENTES =====

md(r'''---

# Bloque 5 — Cruzar fuentes

"Cruzar" fuentes = **combinar dos tablas** usando una columna en común (año, país).

```python
df_combinado = df_fuente1.merge(df_fuente2, on='anio')
```

### Cuidados:
- Las tablas necesitan **al menos una columna en común**
- Si una es **mensual** y la otra **anual**, primero agregá la mensual a anual
- Cuidado con **nombres de país** distintos: "ARG" vs "Argentina" vs "032"
- El merge puede **perder filas** si un año falta en una de las tablas

Ejemplo completo:''')

code(r'''# === CRUCE: ITCRM (BCRA) + Exportaciones/PIB (Banco Mundial) ===
import pandas as pd
import requests
import re
import matplotlib.pyplot as plt

# --- FUENTE 1: BCRA - ITCRM ---
url_itcrm = "https://www.bcra.gob.ar/archivos/PublicacionesEstadisticas/itcrm.txt"
resp = requests.get(url_itcrm, verify=False)
matches = re.findall(r"Date\.UTC\((\d+),(\d+),(\d+)\),([\d.]+)", resp.text)

registros_tcr = []
for anio, mes, dia, valor in matches:
    registros_tcr.append({'fecha': f"{anio}-{int(mes)+1:02d}-{int(dia):02d}", 'itcrm': float(valor)})

df_tcr = pd.DataFrame(registros_tcr)
df_tcr['fecha'] = pd.to_datetime(df_tcr['fecha'])
df_tcr['anio'] = df_tcr['fecha'].dt.year
df_tcr_anual = df_tcr.groupby('anio')['itcrm'].mean().reset_index()

# --- FUENTE 2: Banco Mundial - Exportaciones % PIB ---
url_bm = "https://api.worldbank.org/v2/country/ARG/indicator/NE.EXP.GNFS.ZS?format=json&date=2000:2024&per_page=100"
resp_bm = requests.get(url_bm).json()

registros_bm = []
for obs in resp_bm[1]:
    if obs['value'] is not None:
        registros_bm.append({'anio': int(obs['date']), 'expo_pib': obs['value']})
df_expo = pd.DataFrame(registros_bm)

# --- CRUCE ---
df_merged = df_tcr_anual.merge(df_expo, on='anio')
df_merged = df_merged[(df_merged['anio'] >= 2000) & (df_merged['anio'] <= 2024)].sort_values('anio')

print(f"✅ Cruce exitoso: {len(df_merged)} años con datos de ambas fuentes")
print(df_merged.head(10))

# --- GRÁFICO DE DOBLE EJE ---
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(df_merged['anio'], df_merged['itcrm'], color='#1F4E79', marker='o', linewidth=2, label='ITCRM')
ax1.set_xlabel('Año')
ax1.set_ylabel('ITCRM (base dic-2001=100)', color='#1F4E79')
ax1.tick_params(axis='y', labelcolor='#1F4E79')

ax2 = ax1.twinx()
ax2.plot(df_merged['anio'], df_merged['expo_pib'], color='#E8833A', marker='s', linewidth=2, label='Expo/PIB')
ax2.set_ylabel('Exportaciones (% PIB)', color='#E8833A')
ax2.tick_params(axis='y', labelcolor='#E8833A')

plt.title('Argentina: ITCRM vs Exportaciones/PIB (2000-2024)', fontsize=13, fontweight='bold')
fig.text(0.5, -0.02, 'Fuentes: BCRA (ITCRM) + Banco Mundial (Expo/PIB)', ha='center', fontsize=8, color='gray')
fig.tight_layout()
plt.show()

print("\n💡 Este gráfico cruza dos fuentes distintas.")
print("   Cuando el ITCRM sube (peso más competitivo), ¿suben las exportaciones?")''')

# ===== BLOQUE 6: EJERCICIOS =====

md(r'''---

# Bloque 6 — Ejercicios de práctica

Estos ejercicios **no se evalúan**. Son para que pruebes la mecánica antes de usarla en el coloquio.

---

### Ejercicio 1: Conectate a una API (~5 min)

**Consigna**: usando la API del Banco Mundial, descargá el PIB per cápita (`NY.GDP.PCAP.CD`) de Argentina, Chile y Uruguay desde 2000. Hacé un gráfico de líneas.

**Pista**: copiá la celda del Banco Mundial del Bloque 2 y cambiá el indicador y los países.

**Interpretá**: ¿Cuál creció más? ¿Hay algún quiebre visible? ¿A qué puede deberse?''')

code(r'''# Ejercicio 1 — Tu código acá
# Prompt sugerido para Gemini:
# "Escribí código que use la API del Banco Mundial para descargar
#  NY.GDP.PCAP.CD para ARG, CHL y URY desde 2000 a 2024,
#  lo ponga en un DataFrame y haga un gráfico de líneas"

''')

md(r'''**Tu interpretación**: *(escribí acá)*

''')

md(r'''---

### Ejercicio 2: Cargá un archivo descargado (~5 min)

**Consigna**: usá la celda del Pink Sheet (Bloque 2, Fuente 4) para descargar los precios de commodities. Encontrá el precio del petróleo Brent desde 2000. Hacé un gráfico.

**Pista**: el Pink Sheet tiene muchas columnas — pedile a Gemini que te muestre los nombres.

**Interpretá**: ¿Qué pasó en 2008? ¿Y en 2020? ¿Podés identificar los shocks?''')

code(r'''# Ejercicio 2 — Tu código acá
# Prompt sugerido para Gemini:
# "Descargá el Pink Sheet con pd.read_excel(), mostrá las columnas,
#  filtrá el Brent desde 2000, y hacé un gráfico de línea"

''')

md(r'''**Tu interpretación**: *(escribí acá)*

''')

md(r'''---

### Ejercicio 3: Cruzá dos fuentes (~10 min)

**Consigna**: combiná el ITCRM del BCRA con la apertura comercial (`NE.TRD.GNFS.ZS`) del Banco Mundial para Argentina, por año desde 2005. Hacé un gráfico de doble eje.

**Pista**: el ejemplo del Bloque 5 es casi lo mismo — adaptalo cambiando el indicador.

**Interpretá**: ¿Cuando el TCR sube, la apertura comercial sube también? ¿Siempre? ¿Qué otros factores influyen?''')

code(r'''# Ejercicio 3 — Tu código acá
# Prompt sugerido para Gemini:
# "Combiná el ITCRM del BCRA (promedio anual) con Trade/GDP del
#  Banco Mundial para Argentina desde 2005. Merge por año y
#  graficá con doble eje Y"

''')

md(r'''**Tu interpretación**: *(escribí acá)*

''')

# ===== BLOQUE 7: CIERRE =====

md(r'''---

# Bloque 7 — Cierre y tips para el coloquio

### Resumen del workflow
```
Pregunta → ¿Qué datos? → ¿Dónde están? → Descargar → Filtrar → Graficar → Interpretar → Cruzar
```

### Este notebook es tu referencia
Cada vez que necesites una fuente de datos, volvé acá. Copiá la celda, cambiá los parámetros, listo.

### Tips para el coloquio

1. **Arrancá por los datos ANTES de armar slides** — los datos te dicen qué historia contar
2. **Mínimo 2 gráficos propios** con datos reales (es requisito de la consigna)
3. **Citá siempre la fuente** al pie del gráfico: "Fuente: BCRA, ITCRM multilateral"
4. Si un dato no cierra, **verificá con otra fuente** (triangulación)
5. **Guardá tu notebook**: es evidencia de tu trabajo con datos

### Tabla resumen de fuentes

| Fuente | Acceso | Temas del coloquio |
|--------|--------|-------------------|
| Banco Mundial | API (libre) | Todos |
| BCRA | API v4 + archivo TXT | 1, 6, 8 |
| FRED | API (key gratis) | Contexto internacional |
| Pink Sheet | Excel (URL fija) | 2, 5, 8, 11 |
| UN COMTRADE | API (key gratis, 100/día) | 1, 3, 4 |
| INDEC-ICA | Descarga manual | 5, 8, 9 |
| ADEFA | Descarga manual | 1 |
| ANFAVEA | Descarga manual | 1 |
| CEP XXI | PDF + Excel | 1, 3, 9 |
| Sec. Minería | Excel/PDF | 2 |
| TradeMap | Web (registro gratis) | Todos |
| USGS | PDF + Excel | 2 |

---

*Economía Internacional — UMET 2026*
*Guía de referencia para el trabajo con datos del curso.*''')

# ===== BUILD NOTEBOOK =====

notebook = {
    'nbformat': 4,
    'nbformat_minor': 5,
    'metadata': {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'name': 'python',
            'version': '3.10.0'
        },
        'colab': {
            'provenance': [],
            'toc_visible': True
        }
    },
    'cells': cells
}

output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, 'NB_fuentes_datos.ipynb')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f'Notebook saved: {output_path}')
print(f'Total cells: {len(cells)}')
md_cells = sum(1 for c in cells if c['cell_type'] == 'markdown')
code_cells = sum(1 for c in cells if c['cell_type'] == 'code')
print(f'Markdown: {md_cells}, Code: {code_cells}')
