# Datos para Sesion 5 — Dumping y Comercio de Tareas

Datos oficiales descargados de fuentes publicas para uso en clase y trabajos
de los alumnos. Cada CSV incluye en su header las URLs y fechas de extraccion.

## Bloque 4 — Dumping (datos WTO Anti-Dumping Statistics)

| Archivo | Contenido | Anio |
|---------|-----------|------|
| `wto_antidumping_iniciaciones_anual.csv` | Serie anual de iniciaciones AD globales | 1995-2023 |
| `wto_antidumping_top_aplicadores_y_afectados.csv` | Top 10 paises que aplican y top 10 afectados | acumulado |
| `wto_antidumping_argentina_origen.csv` | Origen de medidas iniciadas por Argentina | acumulado |

**Fuente principal**: WTO Anti-Dumping Statistics
URL: https://www.wto.org/english/tratop_e/adp_e/adp_stattab_e.htm

**Datos complementarios Argentina**: CNCE (Comision Nacional de Comercio Exterior)
URL: https://www.argentina.gob.ar/produccion/comercio/cnce

## Bloque 5 — Comercio de tareas (datos OECD TiVA + Linden et al.)

| Archivo | Contenido |
|---------|-----------|
| `oecd_tiva_valor_agregado_extranjero_electronica.csv` | % FVA en exports de electronica por pais (2020) |
| `oecd_tiva_participacion_cgv_paises.csv` | Backward + forward GVC participation por pais (2020) |
| `iphone_descomposicion_valor_linden2018.csv` | Descomposicion del valor agregado de un iPhone X |

**Fuente OECD**: Trade in Value Added (TiVA) database, 2023 edition
URL: https://www.oecd.org/sti/ind/measuring-trade-in-value-added.htm

**Fuente iPhone**: Linden, Kraemer & Dedrick (2018) — UC Irvine

## Como usar estos datos

```python
import pandas as pd

# Cargar serie temporal AD
df = pd.read_csv('wto_antidumping_iniciaciones_anual.csv', comment='#')
df.plot(x='year', y='initiations')

# Cargar OECD TiVA
gvc = pd.read_csv('oecd_tiva_participacion_cgv_paises.csv', comment='#')
gvc.plot.bar(x='country', y=['backward_pct', 'forward_pct'], stacked=True)
```

El argumento `comment='#'` ignora las lineas de cita al inicio del CSV.

## Para tu evaluacion U3 (notebook integrado)

Estos datasets estan disponibles para que puedas:
- Hacer tus propios graficos comparativos
- Calcular indices (intensidad AD = medidas/comercio total)
- Cruzar con datos de Comtrade o WB para analizar patrones
- Comparar la posicion de Argentina con la region

Si querias profundizar en defensa comercial argentina especifica, revisa los
informes anuales de la CNCE (link arriba) — tienen las medidas vigentes
detalladas con producto, origen, fecha de inicio y vigencia.
