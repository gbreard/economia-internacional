"""
Genera el notebook de Evaluación Unidad 4
(Prebisch, Diamand, Emmanuel, ventajas dinámicas, complejidad económica).

Output:
  notebooks/NB4_terminos_intercambio_y_complejidad.ipynb         (versión alumno)
  docente/NB4_RESUELTO_terminos_intercambio_y_complejidad.ipynb  (versión resuelta)

Estructura:
  Parte 1: 3 MC conceptuales (Prebisch-Singer, Diamand, complejidad económica)
  Parte 2: 2 MC con datos (TDI CEPAL + convergencia Maddison)
  Reflexión final

Visualizaciones: small multiples (grid de paneles) para entrenar al alumno
en lectura de varios indicadores en simultáneo.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_ALUMNO = ROOT / 'notebooks' / 'NB4_terminos_intercambio_y_complejidad.ipynb'
OUT_DOCENTE = ROOT / 'docente' / 'NB4_RESUELTO_terminos_intercambio_y_complejidad.ipynb'


def md(text):
    return {'cell_type': 'markdown', 'metadata': {}, 'source': text.splitlines(keepends=True)}


def code(text):
    return {
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': text.splitlines(keepends=True)
    }


# =============================================================================
# Portada e instrucciones
# =============================================================================

PORTADA = """# Evaluación Unidad 4 — Comercio, estructura productiva y desarrollo

**Economía Internacional — UMET 2026**

---

## Instrucciones

Esta evaluación tiene **dos partes** en un solo archivo, sobre los contenidos de las **Clases 6 y 7** (Prebisch y centro-periferia, Diamand y restricción externa, Emmanuel e intercambio desigual, List–Kaldor y ventajas dinámicas, Hausmann–Hidalgo y complejidad económica).

- **Parte 1 — Teoría**: 3 preguntas de opción múltiple sobre los conceptos centrales.

- **Parte 2 — Práctica con datos**: ejecutan código pre-armado sobre dos datasets reales (CEPAL términos del intercambio + Maddison PIB per cápita), interpretan los resultados y responden 2 preguntas adicionales.

- **Reflexión final**: una pregunta abierta de 5-10 líneas conectando ambos datos con un diagnóstico para Argentina.

### Cómo responder

- En cada pregunta de opción múltiple, escribir la **letra** elegida (a, b, c o d) y una **justificación breve** (2-3 oraciones).
- En la Parte 2, **no hace falta escribir código**: las celdas vienen con el código cargado, solo hay que ejecutarlas (Shift+Enter) y leer los resultados.
- Las visualizaciones de esta unidad están en formato **small multiples** (grilla de paneles, cada uno con un país o indicador). Esto los acostumbra a leer varios indicadores en simultáneo — una habilidad clave en economía.
- Pueden modificar el código o pedirle a una IA que les genere análisis adicionales — pero las respuestas finales y la reflexión deben ser propias.

### Dónde están los datos

**No tienen que descargar nada manualmente** — los CSV se descargan en tiempo real desde el repositorio del curso (GitHub).

Los datasets usados son:

- `cepal_terminos_intercambio_paises.csv` — índice de términos del intercambio (2018=100) para 6 países latinoamericanos + promedio AL, 1980-2024. Fuente: CEPALSTAT.
- `cepal_estructura_exportaciones_AL.csv` — composición primarios/manufacturas en exportaciones de AL, 1990-2023. Fuente: CEPALSTAT.
- `maddison_pib_pc_divergencia.csv` — PIB per cápita (USD 2011 PPA) para 9 países, 1950-2018. Fuente: Maddison Project Database 2020.

Cada CSV tiene en su header la fuente oficial y la URL de descarga original — pueden auditar los números contra el sitio oficial.

### Si una celda no anda — cómo resolverlo con IA

El notebook fue probado, pero el código puede fallar por mil razones. En lugar de trabarse, usen IA para debuggear:

- Copien el mensaje de error completo (desde `Traceback`) y péguenlo en ChatGPT/Gemini/Claude pidiendo: *"Tengo este error en un notebook de pandas, ¿qué significa y cómo lo soluciono?"*
- Adjunten también la celda que dio el error. La IA necesita ver el código para entender el contexto.
- Si la IA propone una solución, pruébenla. Si no anda, vuelvan con el nuevo error. Iteren — eso es debuggear.

En Colab, **Gemini ya puede ver los DataFrames** que cargaron — abrí el chat con el botón de estrella y pedile directamente.

**Importante**: la IA es para resolver problemas técnicos y entender conceptos. Las **respuestas a las preguntas MC y la reflexión final tienen que ser propias** — si copian texto generado por IA, va a notarse (las respuestas de IA tienen tics reconocibles) y baja la nota.

### Entrega

1. Completar **todas** las celdas de respuesta (Preguntas 1-5 + justificaciones + reflexión).
2. Ejecutar todo el notebook (**Entorno de ejecución → Ejecutar todo** en Colab).
3. Verificar que todos los gráficos aparezcan visibles.
4. Descargar como `.ipynb` (Archivo → Descargar → Descargar .ipynb).
5. Renombrar: `apellido_nombre_U4.ipynb`.
6. Subir al campus de la UMET antes del **jueves 11 de junio de 2026**.

### Puntaje

| Componente | Puntos |
|------------|--------|
| 5 preguntas MC (15 pts c/u: 10 respuesta + 5 justificación) | 75 |
| Reflexión final | 25 |
| **Total** | **100** |

**Promoción de la unidad: ≥ 70.**

**Bonus**: quienes participaron en los quizzes AhaSlides de S6 y S7 con ≥ 70% de aciertos suman fracciones de punto al total (cap final 100). Ver detalle en CLAUDE.md del curso.

### Referencia teórica

- Lugones, G. et al. — *Teorías del Comercio Internacional*, Caps. 2.2-2.3 y 5
- Prebisch, R. (1950) — *El desarrollo económico de América Latina y algunos de sus principales problemas*, CEPAL
- Diamand, M. (1972) — *La estructura productiva desequilibrada argentina*, Desarrollo Económico
- Emmanuel, A. (1969) — *L'échange inégal*
- Hausmann, R., Hwang, J. & Rodrik, D. (2007) — *What You Export Matters*, JEG
- Hidalgo, C. & Hausmann, R. (2009) — *The Building Blocks of Economic Complexity*, PNAS
- Rodrik, D. (2016) — *Premature Deindustrialization*, JEG

---
"""

# =============================================================================
# PARTE 1 — Teoría
# =============================================================================

INTRO_PARTE1 = """---

# PARTE 1: TEORÍA (3 preguntas)

Respondan con lo aprendido en las **Clases 6 y 7**. Pueden consultar Lugones caps 2.2-2.3 y 5, Prebisch (1950), Diamand (1972), y Hidalgo-Hausmann (2009).
"""

# --- Pregunta 1: Prebisch-Singer ---

P1 = """## Pregunta 1 — Los mecanismos del deterioro de los términos del intercambio (Prebisch-Singer)

Según la tesis Prebisch-Singer, los precios de las materias primas se deterioran en el largo plazo respecto de los precios de las manufacturas industriales.

**¿Cuál combinación describe MEJOR los tres mecanismos que explican ese deterioro?**

a) Inflación monetaria persistente en los países del centro + apreciación de sus monedas + barreras arancelarias en la periferia

b) Baja elasticidad-ingreso de la demanda de primarios + competencia desorganizada entre productores periféricos + sustitución tecnológica por insumos sintéticos

c) Sobreproducción agrícola por subsidios + caída de los costos de transporte + entrada de Asia al mercado mundial

d) Diferencias culturales en preferencias de consumo + ciclos climáticos + especulación financiera con commodities
"""

P1_DOC = """## Pregunta 1 — Los mecanismos del deterioro de los términos del intercambio (Prebisch-Singer)

Según la tesis Prebisch-Singer, los precios de las materias primas se deterioran en el largo plazo respecto de los precios de las manufacturas industriales.

**¿Cuál combinación describe MEJOR los tres mecanismos que explican ese deterioro?**

a) Inflación monetaria persistente en los países del centro + apreciación de sus monedas + barreras arancelarias en la periferia

b) **Baja elasticidad-ingreso de la demanda de primarios + competencia desorganizada entre productores periféricos + sustitución tecnológica por insumos sintéticos** ✅

c) Sobreproducción agrícola por subsidios + caída de los costos de transporte + entrada de Asia al mercado mundial

d) Diferencias culturales en preferencias de consumo + ciclos climáticos + especulación financiera con commodities
"""

P1_RESP = """**Mi respuesta**: [escribir letra: a, b, c o d]

**Justificación** (2-3 oraciones, mencionando explícitamente al menos **dos** de los tres mecanismos):

"""

P1_RESP_DOC = """**Mi respuesta**: **b**

**Justificación modelo**:

Los tres mecanismos del deterioro según Prebisch (1950) y Singer (1950) son: (1) **baja elasticidad-ingreso** de la demanda de primarios — cuando crece el ingreso mundial, la demanda de alimentos y materias primas crece menos que proporcionalmente, mientras la de manufacturas crece más; (2) **competencia desorganizada entre productores periféricos** — muchos países compiten entre sí en commodities tirando los precios para abajo, mientras en el centro las manufacturas tienen mayor poder de mercado y los salarios industriales más altos por sindicalización; (3) **sustitución tecnológica** — los avances técnicos en el centro reemplazan insumos naturales por sintéticos (caucho sintético, fibras artificiales, nitrógeno fijado). La opción (a) confunde con teorías monetarias, (c) son fenómenos post-1980 ajenos al argumento original, y (d) descarta el análisis estructural.

---

**Notas para el docente**:
- Si el alumno solo dice "los precios bajan" sin nombrar mecanismos: 5/15.
- Si nombra solo elasticidades: 8/15.
- Si nombra dos de los tres mecanismos correctamente: 12/15.
- Si los nombra los tres y los explica: 15/15.
- Distractor (a) es plausible si el alumno solo leyó por encima — confunde Prebisch con un argumento monetarista.

"""

# --- Pregunta 2: Diamand stop-go ---

P2 = """---

## Pregunta 2 — Diamand y la estructura productiva desequilibrada (escenario aplicado)

**Escenario**: Argentina entra en una fase expansiva. El gobierno baja los impuestos al consumo, suben los salarios y la economía crece al 5% anual durante dos años. La industria local trabaja al 90% de capacidad. Al tercer año, las reservas del Banco Central caen y aparece presión devaluatoria.

Según el diagnóstico de **Marcelo Diamand (1972)** sobre la **estructura productiva desequilibrada (EPD)** argentina, ¿cuál es la causa estructural más probable de la crisis de reservas?

a) El sector agropecuario perdió competitividad internacional porque el clima fue desfavorable

b) Como la industria local no es competitiva al tipo de cambio del agro, la expansión del ingreso aumenta las importaciones de bienes industriales más rápido que las exportaciones primarias → escasez de dólares y devaluación (ciclo *stop-go*)

c) El crédito internacional se cortó por la situación geopolítica global, generando salida de capitales especulativos

d) La población consumió más que su ingreso, generando déficit fiscal y necesidad de imprimir pesos
"""

P2_DOC = """---

## Pregunta 2 — Diamand y la estructura productiva desequilibrada (escenario aplicado)

**Escenario**: Argentina entra en una fase expansiva. El gobierno baja los impuestos al consumo, suben los salarios y la economía crece al 5% anual durante dos años. La industria local trabaja al 90% de capacidad. Al tercer año, las reservas del Banco Central caen y aparece presión devaluatoria.

Según el diagnóstico de **Marcelo Diamand (1972)** sobre la **estructura productiva desequilibrada (EPD)** argentina, ¿cuál es la causa estructural más probable de la crisis de reservas?

a) El sector agropecuario perdió competitividad internacional porque el clima fue desfavorable

b) **Como la industria local no es competitiva al tipo de cambio del agro, la expansión del ingreso aumenta las importaciones de bienes industriales más rápido que las exportaciones primarias → escasez de dólares y devaluación (ciclo *stop-go*)** ✅

c) El crédito internacional se cortó por la situación geopolítica global, generando salida de capitales especulativos

d) La población consumió más que su ingreso, generando déficit fiscal y necesidad de imprimir pesos
"""

P2_RESP = """**Mi respuesta**: [escribir letra: a, b, c o d]

**Justificación** (2-3 oraciones, mencionando los conceptos de **estructura productiva desequilibrada** y **tipo de cambio**):

"""

P2_RESP_DOC = """**Mi respuesta**: **b**

**Justificación modelo**:

La Argentina de Diamand tiene dos sectores productores de transables con productividades muy distintas: el agro (competitivo internacionalmente al tipo de cambio bajo del sector exportador) y la industria (que para sobrevivir necesita un tipo de cambio más alto o protección arancelaria). Esto es lo que él llama **estructura productiva desequilibrada (EPD)**. Cuando la economía crece, la demanda de bienes industriales sube y la industria tira de las **importaciones** (insumos, maquinaria, bienes finales) más rápido de lo que el agro puede aumentar sus exportaciones. El resultado mecánico es escasez de dólares → presión devaluatoria → ajuste recesivo. Es decir: el crecimiento mismo activa la restricción externa. La opción (a) culpa al clima ignorando lo estructural; (c) y (d) son problemas reales pero no explican por qué crecer genera la crisis.

---

**Notas para el docente**:
- Si solo dice "faltan dólares por crecer" sin EPD: 5/15.
- Si menciona EPD pero no el rol del TC: 8/15.
- Si articula EPD + TC + arrastre de importaciones por crecimiento: 15/15.
- Es la pregunta más argentina del notebook — el alumno debería poder citar al menos un episodio del stop-go histórico (1958-59, 1962-63, 1975-76, 1981-82, 1989, 2001, 2018).

"""

# --- Pregunta 3: ECI complejidad ---

P3 = """---

## Pregunta 3 — ¿Qué hace que un producto sea "complejo" según Hidalgo y Hausmann?

César Hidalgo y Ricardo Hausmann (2009, PNAS) construyen el **Índice de Complejidad Económica (ECI)** para medir las capacidades productivas de un país. Su pregunta de fondo es: ¿qué hace que un producto sea más "complejo" que otro?

**¿Cuál de las siguientes afirmaciones describe MEJOR la metodología de complejidad de Hidalgo-Hausmann?**

a) Un producto es complejo si su precio internacional es alto y volátil

b) Un producto es complejo si requiere mucho capital físico por unidad producida

c) Un producto es complejo si lo exportan pocos países y, además, los que lo exportan son países diversificados (que también exportan muchos otros productos) — la complejidad está en las capacidades necesarias para producirlo, no en el bien en sí

d) Un producto es complejo cuando tiene una larga cadena de valor con muchos proveedores internacionales (medida por TiVA-OECD)
"""

P3_DOC = """---

## Pregunta 3 — ¿Qué hace que un producto sea "complejo" según Hidalgo y Hausmann?

César Hidalgo y Ricardo Hausmann (2009, PNAS) construyen el **Índice de Complejidad Económica (ECI)** para medir las capacidades productivas de un país. Su pregunta de fondo es: ¿qué hace que un producto sea más "complejo" que otro?

**¿Cuál de las siguientes afirmaciones describe MEJOR la metodología de complejidad de Hidalgo-Hausmann?**

a) Un producto es complejo si su precio internacional es alto y volátil

b) Un producto es complejo si requiere mucho capital físico por unidad producida

c) **Un producto es complejo si lo exportan pocos países y, además, los que lo exportan son países diversificados (que también exportan muchos otros productos) — la complejidad está en las capacidades necesarias para producirlo, no en el bien en sí** ✅

d) Un producto es complejo cuando tiene una larga cadena de valor con muchos proveedores internacionales (medida por TiVA-OECD)
"""

P3_RESP = """**Mi respuesta**: [escribir letra: a, b, c o d]

**Justificación** (2-3 oraciones, mencionando **diversidad** y **ubicuidad** que son los dos componentes que itera el algoritmo de Hidalgo-Hausmann):

"""

P3_RESP_DOC = """**Mi respuesta**: **c**

**Justificación modelo**:

El algoritmo de Hidalgo-Hausmann (PNAS 2009) parte de dos métricas observables del comercio internacional: la **diversidad** de cada país (cuántos productos exporta con ventaja comparativa revelada) y la **ubicuidad** de cada producto (cuántos países lo exportan). Iterando estas métricas — el ECI de un país depende del ECI medio de los productos que exporta, y el PCI de un producto depende del ECI medio de los países que lo exportan — emerge una medida de capacidades. Un chip avanzado es complejo porque pocos países pueden hacerlo (baja ubicuidad) y porque esos países exportan muchas otras cosas (alta diversidad). El café es simple por lo contrario. La complejidad no está en el bien sino en las capacidades requeridas para producirlo, muchas de ellas tácitas y acumulativas. Las opciones (a) y (b) confunden complejidad con valor monetario o intensidad de capital; (d) confunde ECI con TiVA-OECD (medida CGV, otra cosa).

---

**Notas para el docente**:
- Si solo dice "lo exportan pocos países": 7/15.
- Si menciona diversidad + ubicuidad: 12/15.
- Si articula la iteración y por qué emergen capacidades tácitas: 15/15.
- Distractor (d) es el más sutil — separa el alumno que entendió HH del que confundió U4 (capacidades) con U5 (CGV).

"""

# =============================================================================
# PARTE 2 — Datos
# =============================================================================

INTRO_PARTE2 = """---

# PARTE 2: PRÁCTICA CON DATOS (2 preguntas)

En esta parte van a trabajar con **datos reales** de la Unidad 4:

- `cepal_terminos_intercambio_paises.csv` — índice TDI (base 2018=100) por país, 1980-2024
- `maddison_pib_pc_divergencia.csv` — PIB per cápita en USD 2011 PPA, 1950-2018

Las visualizaciones están armadas como **small multiples**: una grilla de paneles donde cada panel muestra a un país. Este formato les permite **comparar trayectorias en simultáneo** — algo central para distinguir entre tesis Prebisch-Singer (deterioro generalizado), divergencia estructural (Diamand, neoschumpeterianos) y convergencia (Tigres asiáticos).

**Solo tienen que ejecutar las celdas y observar los gráficos** — el código de visualización ya está armado.
"""

SETUP = """import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Estilo visual del curso
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['grid.linestyle'] = '--'

# Paleta del curso
AZUL_OSC = '#1F4E79'
AZUL_MED = '#2E75B6'
NARANJA = '#E8833A'
VERDE = '#27AE60'
ROJO = '#E74C3C'
GRIS = '#4B5563'

# Los datos se descargan desde el repositorio del curso (no necesitan subir nada)
DATOS = 'https://raw.githubusercontent.com/gbreard/economia-internacional/publicacion-web/notebooks/datos'
"""

# --- Bloque 1: TDI ---

BLOQUE1_INTRO = """---

## Bloque 1 — Términos de intercambio 1980-2024 (¿se cumple Prebisch-Singer?)

Prebisch (1950) y Singer (1950) plantearon que los términos del intercambio se deterioran sistemáticamente contra la periferia. Vamos a chequearlo con datos reales de CEPAL para 6 países latinoamericanos + el promedio regional, desde 1980 hasta 2024.

**Base del índice**: 2018 = 100. Un valor por encima de 100 significa que ese año los TDI eran **mejores** que en 2018; por debajo de 100, **peores**.
"""

BLOQUE1_CARGA = """# Cargar datos TDI
tdi = pd.read_csv(f'{DATOS}/cepal_terminos_intercambio_paises.csv', comment='#')
print('Países disponibles:', sorted(tdi['pais'].unique()))
print('Período:', tdi['anio'].min(), '-', tdi['anio'].max())
print('Total observaciones:', len(tdi))
tdi.head()
"""

BLOQUE1_SMALLMULT = """# Visualización SMALL MULTIPLES: un panel por país (6 países + AL)
paises_orden = ['América Latina', 'Argentina', 'Brasil', 'Chile', 'Colombia', 'México', 'Perú']
colores = {
    'América Latina': AZUL_OSC,
    'Argentina': AZUL_MED,
    'Brasil': VERDE,
    'Chile': NARANJA,
    'Colombia': '#7C3AED',
    'México': ROJO,
    'Perú': '#0EA5E9',
}

fig, axes = plt.subplots(2, 4, figsize=(15, 7), sharex=True, sharey=True, facecolor='white')
axes = axes.flatten()

for i, pais in enumerate(paises_orden):
    ax = axes[i]
    sub = tdi[tdi['pais'] == pais].sort_values('anio')
    color = colores[pais]
    ax.plot(sub['anio'], sub['tdi_idx_2018_100'], color=color, linewidth=2)
    ax.fill_between(sub['anio'], sub['tdi_idx_2018_100'], 100,
                    where=(sub['tdi_idx_2018_100'] >= 100), alpha=0.15, color=VERDE)
    ax.fill_between(sub['anio'], sub['tdi_idx_2018_100'], 100,
                    where=(sub['tdi_idx_2018_100'] < 100), alpha=0.15, color=ROJO)
    ax.axhline(100, color=GRIS, linestyle=':', linewidth=1)
    ax.set_title(pais, fontsize=11, fontweight='bold', color=color)
    ax.set_ylim(45, 140)
    ax.tick_params(labelsize=9)

# Eliminar el panel sobrante (8 paneles, solo 7 países)
axes[7].set_axis_off()

fig.suptitle('Términos del intercambio 1980-2024 (índice, 2018=100) — small multiples por país',
             fontsize=13, fontweight='bold', color=AZUL_OSC, y=1.00)
fig.supxlabel('Año', fontsize=10, color=GRIS)
fig.supylabel('Índice TDI (2018=100)', fontsize=10, color=GRIS)
fig.text(0.5, -0.02,
         'Fuente: CEPALSTAT (indicador 883). Verde = TDI por encima del nivel 2018. Rojo = por debajo.',
         ha='center', fontsize=9, style='italic', color=GRIS)

plt.tight_layout()
plt.show()
"""

BLOQUE1_TAREA = """### Tarea: medir el cambio entre 1980 y 2024

Calculen para cada país el cambio porcentual del TDI entre 1980 y el año más reciente disponible (2024).
"""

BLOQUE1_TABLA = """# Calcular variación 1980 -> 2024 por país
resumen = []
for pais in paises_orden:
    sub = tdi[tdi['pais'] == pais].sort_values('anio')
    v_ini = sub.iloc[0]['tdi_idx_2018_100']
    v_fin = sub.iloc[-1]['tdi_idx_2018_100']
    cambio_pct = (v_fin / v_ini - 1) * 100
    resumen.append({
        'país': pais,
        'TDI 1980': round(v_ini, 1),
        'TDI 2024': round(v_fin, 1),
        'cambio %': round(cambio_pct, 1),
    })

resumen_df = pd.DataFrame(resumen).sort_values('cambio %', ascending=False).reset_index(drop=True)
print('Variación de TDI 1980 → 2024 (ordenado de mayor a menor cambio):\\n')
resumen_df
"""

P4 = """---

### Pregunta 4 — ¿Qué dicen los datos TDI sobre Prebisch-Singer?

Con los gráficos *small multiples* y la tabla de cambios 1980-2024, respondan:

**¿Cuál afirmación describe MEJOR el patrón observado en los datos?**

a) Los TDI cayeron de forma generalizada en toda América Latina entre 1980 y 2024, confirmando exactamente la tesis Prebisch-Singer en su versión más fuerte

b) Los TDI subieron en todos los países entre 1980 y 2024, pero el aumento fue muy heterogéneo: los exportadores de commodities mineros (Chile, Perú) y energía (Brasil, Colombia) ganaron más del 45%, mientras que México y Argentina (con canastas más diversificadas y manufacturadas) ganaron menos del 10% — la tesis simple necesita matices, pero la idea de que la composición exportadora importa se confirma

c) Los TDI argentinos cayeron sistemáticamente, mostrando que Argentina sufre Prebisch-Singer mientras el resto de la región no

d) Los TDI no tienen ninguna relación con la composición exportadora — son ruido aleatorio que depende solo del precio del petróleo
"""

P4_DOC = """---

### Pregunta 4 — ¿Qué dicen los datos TDI sobre Prebisch-Singer?

Con los gráficos *small multiples* y la tabla de cambios 1980-2024, respondan:

**¿Cuál afirmación describe MEJOR el patrón observado en los datos?**

a) Los TDI cayeron de forma generalizada en toda América Latina entre 1980 y 2024, confirmando exactamente la tesis Prebisch-Singer en su versión más fuerte

b) **Los TDI subieron en todos los países entre 1980 y 2024, pero el aumento fue muy heterogéneo: los exportadores de commodities mineros (Chile, Perú) y energía (Brasil, Colombia) ganaron más del 45%, mientras que México y Argentina (con canastas más diversificadas y manufacturadas) ganaron menos del 10% — la tesis simple necesita matices, pero la idea de que la composición exportadora importa se confirma** ✅

c) Los TDI argentinos cayeron sistemáticamente, mostrando que Argentina sufre Prebisch-Singer mientras el resto de la región no

d) Los TDI no tienen ninguna relación con la composición exportadora — son ruido aleatorio que depende solo del precio del petróleo
"""

P4_RESP = """**Mi respuesta**: [escribir letra: a, b, c o d]

**Justificación** (2-3 oraciones, mencionando **al menos dos países específicos** con su cambio % de la tabla):

"""

P4_RESP_DOC = """**Mi respuesta**: **b**

**Justificación modelo**:

Los datos CEPAL 1980-2024 contradicen la versión simple de Prebisch-Singer: TODOS los países subieron sus TDI en el período (entre +9% y +52%). Pero la dispersión es muy grande y se ordena casi perfectamente por composición exportadora: **Chile** (+52,4 %, cobre y litio) y **Brasil** (+49,7 %, soja, hierro, petróleo) lideran las ganancias por el *super-ciclo de commodities* 2003-2014; **Argentina** (+9,2 %) y **México** (+8,8 %) — canastas más diversificadas con peso manufacturero — apenas ganan. La conclusión heterodoxa moderna (Ocampo 2022) es que la versión simple de Prebisch necesita matices — los precios de commodities tienen ciclos largos —, pero la idea central de que **la composición de la canasta determina la trayectoria de los términos del intercambio** se confirma robustamente.

---

**Notas para el docente**:
- Si nombra solo un país: 10/15.
- Si nombra dos países con su % correcto: 13/15.
- Si conecta heterogeneidad con composición exportadora: 15/15.
- Error común: confundir "TDI subieron" con "Prebisch se equivocó" (omite el componente cíclico y la heterogeneidad). Penalizar levemente esa interpretación simplista.

"""

# --- Bloque 2: Maddison convergencia ---

BLOQUE2_INTRO = """---

## Bloque 2 — Convergencia y divergencia de PIB per cápita 1950-2018 (Maddison)

Vamos a ver si los Tigres asiáticos efectivamente convergieron con el centro mientras América Latina divergía. Usamos datos del **Maddison Project Database 2020** — la fuente estándar para series largas de PIB per cápita en dólares constantes.

**Unidad**: USD 2011 PPA (dólares constantes de 2011, ajustados por paridad de poder adquisitivo).
"""

BLOQUE2_CARGA = """# Cargar datos Maddison
mad = pd.read_csv(f'{DATOS}/maddison_pib_pc_divergencia.csv', comment='#')
print('Columnas (países):', list(mad.columns))
print('Períodos:', mad['anio'].tolist())
print()
mad
"""

BLOQUE2_SMALLMULT = """# SMALL MULTIPLES: PIB per cápita por país, eje Y en escala log para ver convergencia
paises_mad = ['Argentina', 'Brasil', 'Chile', 'México', 'AL_promedio',
              'Corea_del_Sur', 'Japón', 'Alemania', 'Estados_Unidos']

colores_mad = {
    'Argentina': AZUL_MED,
    'Brasil': VERDE,
    'Chile': '#0EA5E9',
    'México': ROJO,
    'AL_promedio': AZUL_OSC,
    'Corea_del_Sur': NARANJA,
    'Japón': '#7C3AED',
    'Alemania': '#0F766E',
    'Estados_Unidos': GRIS,
}

fig, axes = plt.subplots(3, 3, figsize=(13, 9), sharex=True, sharey=True, facecolor='white')
axes = axes.flatten()

for i, pais in enumerate(paises_mad):
    ax = axes[i]
    color = colores_mad[pais]
    ax.plot(mad['anio'], mad[pais], color=color, linewidth=2.2, marker='o', markersize=5)
    ax.set_yscale('log')
    ax.set_title(pais.replace('_', ' '), fontsize=11, fontweight='bold', color=color)
    ax.set_ylim(700, 70000)
    ax.tick_params(labelsize=9)
    # marcar punto inicial y final
    ax.annotate(f"{mad.iloc[0][pais]:,.0f}", xy=(1950, mad.iloc[0][pais]),
                xytext=(3, -12), textcoords='offset points', fontsize=8, color=color)
    ax.annotate(f"{mad.iloc[-1][pais]:,.0f}", xy=(2018, mad.iloc[-1][pais]),
                xytext=(-30, 8), textcoords='offset points', fontsize=8, color=color, fontweight='bold')

fig.suptitle('PIB per cápita 1950-2018 (USD 2011 PPA, escala log) — small multiples por país',
             fontsize=13, fontweight='bold', color=AZUL_OSC, y=1.00)
fig.supxlabel('Año', fontsize=10, color=GRIS)
fig.supylabel('PIB pc (USD 2011 PPA, escala log)', fontsize=10, color=GRIS)
fig.text(0.5, -0.02,
         'Fuente: Maddison Project Database 2020. Escala log permite ver la pendiente como tasa de crecimiento.',
         ha='center', fontsize=9, style='italic', color=GRIS)

plt.tight_layout()
plt.show()
"""

BLOQUE2_TAREA = """### Tarea: calcular ratios de convergencia/divergencia

Vamos a calcular dos cosas que sintetizan la trayectoria:

1. **Cuántas veces creció el PIB pc** entre 1950 y 2018 (factor multiplicador).
2. **El ratio respecto a EE.UU.** en 1950 y en 2018 — si el ratio sube, hay convergencia; si baja, divergencia.
"""

BLOQUE2_CALC = """# Calcular factor de crecimiento y convergencia/divergencia vs EEUU
usa_1950 = mad[mad['anio'] == 1950]['Estados_Unidos'].iloc[0]
usa_2018 = mad[mad['anio'] == 2018]['Estados_Unidos'].iloc[0]

resumen_mad = []
for pais in paises_mad:
    v50 = mad[mad['anio'] == 1950][pais].iloc[0]
    v18 = mad[mad['anio'] == 2018][pais].iloc[0]
    factor = v18 / v50
    ratio_usa_50 = v50 / usa_1950
    ratio_usa_18 = v18 / usa_2018
    delta_ratio = ratio_usa_18 - ratio_usa_50
    resumen_mad.append({
        'país': pais.replace('_', ' '),
        'PIB pc 1950': int(v50),
        'PIB pc 2018': int(v18),
        'creció x veces': round(factor, 1),
        'ratio vs EEUU 1950': round(ratio_usa_50, 2),
        'ratio vs EEUU 2018': round(ratio_usa_18, 2),
        'Δ ratio (convergencia si >0)': round(delta_ratio, 2),
    })

resumen_mad_df = pd.DataFrame(resumen_mad).sort_values('Δ ratio (convergencia si >0)', ascending=False).reset_index(drop=True)
print('Convergencia/divergencia vs EE.UU. 1950 → 2018 (ordenado por Δ ratio):\\n')
resumen_mad_df
"""

BLOQUE2_VIS_RATIOS = """# Visualización integradora: ratio vs EEUU por país, comparado 1950 vs 2018
fig, ax = plt.subplots(figsize=(11, 5), facecolor='white')

paises_orden_ratio = sorted(paises_mad, key=lambda p: mad[mad['anio'] == 2018][p].iloc[0] / usa_2018)
nombres = [p.replace('_', ' ') for p in paises_orden_ratio]
y = np.arange(len(paises_orden_ratio))

ratios_50 = [mad[mad['anio'] == 1950][p].iloc[0] / usa_1950 for p in paises_orden_ratio]
ratios_18 = [mad[mad['anio'] == 2018][p].iloc[0] / usa_2018 for p in paises_orden_ratio]

# barras horizontales: ratio 1950 (gris) y ratio 2018 (color)
ax.barh(y - 0.18, ratios_50, height=0.35, color=GRIS, alpha=0.65, label='1950')
ax.barh(y + 0.18, ratios_18, height=0.35, color=AZUL_OSC, label='2018')

# valores numéricos
for i, (r50, r18) in enumerate(zip(ratios_50, ratios_18)):
    ax.text(r50 + 0.01, i - 0.18, f'{r50:.2f}', va='center', fontsize=8.5, color=GRIS)
    ax.text(r18 + 0.01, i + 0.18, f'{r18:.2f}', va='center', fontsize=8.5,
            color=AZUL_OSC, fontweight='bold')

ax.set_yticks(y)
ax.set_yticklabels(nombres, fontsize=10)
ax.axvline(1.0, color=ROJO, linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(1.02, len(paises_mad) - 0.5, 'paridad con EE.UU.', color=ROJO, fontsize=9, style='italic')
ax.set_xlabel('PIB per cápita relativo a EE.UU. (EE.UU. = 1.00)', fontsize=10.5, color=GRIS)
ax.set_xlim(0, 1.25)
ax.set_title('¿Quién convergió y quién divergió con EE.UU. entre 1950 y 2018?',
             fontsize=13, fontweight='bold', color=AZUL_OSC, pad=10)
ax.legend(loc='lower right', fontsize=10, edgecolor=GRIS)

fig.text(0.5, -0.03,
         'Fuente: Maddison Project Database 2020. Si la barra azul (2018) > barra gris (1950) → convergencia; si es menor → divergencia.',
         ha='center', fontsize=9, style='italic', color=GRIS)
plt.tight_layout()
plt.show()
"""

P5 = """---

### Pregunta 5 — Convergencia y divergencia: ¿qué muestra Maddison?

Con los small multiples y el gráfico de ratios respecto a EE.UU., respondan:

**¿Cuál afirmación describe MEJOR el patrón observado en los datos Maddison 1950-2018?**

a) Todos los países convergieron a EE.UU. — la economía mundial avanza hacia la igualación de niveles de ingreso, como predice el modelo neoclásico de Solow

b) Corea del Sur convergió de forma espectacular (su PIB pc pasó de 6% a 69% del de EE.UU. y creció más de 40 veces), mientras Argentina divergió (de 51% a 34% de EE.UU., creciendo solo 2.4 veces). El resto de AL tuvo una trayectoria intermedia — la convergencia es posible pero NO automática

c) Argentina convergió levemente con EE.UU. gracias a su industrialización por sustitución de importaciones (ISI)

d) Corea creció mucho pero sin acortar la distancia con EE.UU., porque EE.UU. también creció a la misma velocidad
"""

P5_DOC = """---

### Pregunta 5 — Convergencia y divergencia: ¿qué muestra Maddison?

Con los small multiples y el gráfico de ratios respecto a EE.UU., respondan:

**¿Cuál afirmación describe MEJOR el patrón observado en los datos Maddison 1950-2018?**

a) Todos los países convergieron a EE.UU. — la economía mundial avanza hacia la igualación de niveles de ingreso, como predice el modelo neoclásico de Solow

b) **Corea del Sur convergió de forma espectacular (su PIB pc pasó de 6% a 69% del de EE.UU. y creció más de 40 veces), mientras Argentina divergió (de 51% a 34% de EE.UU., creciendo solo 2.4 veces). El resto de AL tuvo una trayectoria intermedia — la convergencia es posible pero NO automática** ✅

c) Argentina convergió levemente con EE.UU. gracias a su industrialización por sustitución de importaciones (ISI)

d) Corea creció mucho pero sin acortar la distancia con EE.UU., porque EE.UU. también creció a la misma velocidad
"""

P5_RESP = """**Mi respuesta**: [escribir letra: a, b, c o d]

**Justificación** (2-3 oraciones, mencionando **valores concretos** de la tabla de ratios para al menos dos países, e identificando qué teoría heterodoxa explica mejor estas trayectorias):

"""

P5_RESP_DOC = """**Mi respuesta**: **b**

**Justificación modelo**:

Maddison muestra dos patrones opuestos: **Corea del Sur** pasa de PIB pc relativo a EE.UU. de 0,06 (1950) a 0,69 (2018) y multiplica su PIB pc por 44,6 — convergencia espectacular; **Argentina** retrocede de 0,51 a 0,34 (Δ = −0,17) y solo crece x2,4 — divergencia clara. La opción (a) es falsa empíricamente (no toda AL converge); (c) es factualmente incorrecta (Argentina divergió, no convergió); (d) ignora los datos. La teoría que explica mejor estas trayectorias divergentes NO es el modelo neoclásico de convergencia incondicional sino el enfoque **neoschumpeteriano + ventajas dinámicas (Kaldor/List)**: Corea construyó capacidades tecnológicas acumulativas con política industrial activa (HCI plan + metas exportadoras + tipo de cambio competitivo), Argentina no las sostuvo y entró en un proceso de regresión estructural (consistente con el ECI argentino cayendo de 0,2 a −0,4 según Atlas of Economic Complexity).

---

**Notas para el docente**:
- Si solo dice "Corea creció mucho": 7/15.
- Si cita ratios de la tabla: 12/15.
- Si nombra teoría heterodoxa que lo explica (neoschumpeterianos, Hidalgo-Hausmann, Kaldor): 15/15.
- Conexión bonus: alumno que cita el ECI cae argentino del cierre de S7 → buena señal de integración U4 completa.

"""

# =============================================================================
# Reflexión final
# =============================================================================

REFLEXION = """---

## Reflexión final

Respondan brevemente (5-10 líneas), integrando lo que vieron en las dos partes:

**Si combinamos los datos del Bloque 1 (TDI 1980-2024) con los del Bloque 2 (PIB pc 1950-2018), ¿qué diagnóstico ofrece la teoría heterodoxa (Prebisch + Diamand + neoschumpeterianos) sobre la trayectoria argentina y las opciones de política económica hacia adelante?**

Pueden articular su respuesta con estas preguntas guía:

- ¿Por qué, a pesar de que los TDI argentinos subieron 9% entre 1980 y 2024, Argentina divergió fuertemente con EE.UU. (de 51% a 34%) en el período largo?
- ¿Qué teoría que vimos explica mejor por qué Corea convergió y Argentina no, si Argentina partía de un nivel mucho más alto en 1950?
- ¿Qué tipo de política industrial sería compatible con un diagnóstico heterodoxo del problema argentino? (No tienen que dar una receta cerrada — basta con identificar **una** dimensión: tipo de cambio, política tecnológica, composición exportadora, restricción externa, complejidad económica, etc.)

**Mi respuesta**:

"""

# =============================================================================
# Versión docente — respuestas + criterios
# =============================================================================

REFL_DOCENTE = """---

## Reflexión final — Notas para el docente

**Esperado del alumno**: integrar Prebisch (TDI heterogéneos según composición exportadora) + Diamand (estructura productiva desequilibrada explica por qué crecer genera crisis externa) + neoschumpeterianos / Hausmann-Hidalgo (capacidades tecnológicas determinan trayectoria de largo plazo, mucho más que precios de commodities).

**Puntos altos de la reflexión**:
- Identificar que el "boom de commodities" 2000-2014 ayudó pero no resolvió el problema estructural argentino.
- Argentina partía de un nivel ALTO en 1950 (51% de EE.UU.) y igual divergió: muestra que no es un problema de "punto de partida" sino de **acumulación de capacidades** a lo largo del tiempo (path dependence, ECI).
- Corea hizo ISI con metas exportadoras y disciplina sobre el capital privado; Argentina hizo ISI sin esas dos cosas.
- Política industrial moderna (Rodrik 2016): apuntar a sectores intensivos en conocimiento, no replicar el modelo coreano de los 70s (la ventana de manufactura intensiva en mano de obra se cerró por la competencia china).

**Puntos bajos / errores comunes**:
- Confundir TDI subieron con "Prebisch se equivocó". El alumno debe ver que es heterogéneo por país y que el ascenso post-2003 viene de un boom específico de commodities, no un cambio estructural.
- Decir "Argentina necesita devaluar para crecer" sin entender el stop-go.
- Reducir todo a "más Estado" o "menos Estado" sin nombrar el problema estructural.

### Rúbrica reflexión (25 puntos)

| Criterio | Puntos |
|----------|--------|
| Integra los dos bloques de datos (no responde solo con uno) | 5 |
| Cita al menos dos autores/conceptos heterodoxos de U4 | 10 |
| Identifica al menos una dimensión de política coherente con el diagnóstico | 5 |
| Coherencia argumentativa + escritura clara | 5 |

### Respuestas MC

| # | Tema | Resp | Notas |
|---|------|------|-------|
| 1 | Prebisch-Singer mecanismos | **b** | Distractores plausibles. El (a) confunde con teorías monetarias. El (c) es post-2000 y no Prebisch. El (d) es ruido. |
| 2 | Diamand stop-go | **b** | Único que menciona EPD + tipo de cambio + importaciones. Los demás son problemas, pero no el problema estructural. |
| 3 | Complejidad económica | **c** | (d) confunde con TiVA-OECD (CGV), no con ECI. (a) es valor monetario. (b) es intensidad de capital. |
| 4 | TDI heterogéneo | **b** | El (a) afirma generalizado falso. El (c) es falso (Argentina subió). El (d) descarta análisis económico. |
| 5 | Convergencia Maddison | **b** | (a) falso (Argentina divergió). (c) factualmente incorrecto (Argentina divergió). (d) factualmente incorrecto. |
"""

# =============================================================================
# Ensamblar notebooks
# =============================================================================


def build_notebook(docente: bool = False):
    # En la versión docente: preguntas marcadas con ✅ + respuestas y justificaciones modelo escritas.
    # En la versión alumno: opciones neutras (sin marcar correcta) + celdas de respuesta vacías.
    p1, p1r = (P1_DOC, P1_RESP_DOC) if docente else (P1, P1_RESP)
    p2, p2r = (P2_DOC, P2_RESP_DOC) if docente else (P2, P2_RESP)
    p3, p3r = (P3_DOC, P3_RESP_DOC) if docente else (P3, P3_RESP)
    p4, p4r = (P4_DOC, P4_RESP_DOC) if docente else (P4, P4_RESP)
    p5, p5r = (P5_DOC, P5_RESP_DOC) if docente else (P5, P5_RESP)

    cells = [
        md(PORTADA),
        md(INTRO_PARTE1),
        md(p1),
        md(p1r),
        md(p2),
        md(p2r),
        md(p3),
        md(p3r),
        md(INTRO_PARTE2),
        code(SETUP),
        md(BLOQUE1_INTRO),
        code(BLOQUE1_CARGA),
        code(BLOQUE1_SMALLMULT),
        md(BLOQUE1_TAREA),
        code(BLOQUE1_TABLA),
        md(p4),
        md(p4r),
        md(BLOQUE2_INTRO),
        code(BLOQUE2_CARGA),
        code(BLOQUE2_SMALLMULT),
        md(BLOQUE2_TAREA),
        code(BLOQUE2_CALC),
        code(BLOQUE2_VIS_RATIOS),
        md(p5),
        md(p5r),
        md(REFLEXION),
    ]

    if docente:
        cells.append(md(REFL_DOCENTE))

    nb = {
        'cells': cells,
        'metadata': {
            'kernelspec': {
                'display_name': 'Python 3',
                'language': 'python',
                'name': 'python3'
            },
            'language_info': {
                'name': 'python',
                'version': '3.x'
            }
        },
        'nbformat': 4,
        'nbformat_minor': 5,
    }
    return nb


def main():
    nb_alumno = build_notebook(docente=False)
    nb_docente = build_notebook(docente=True)

    OUT_ALUMNO.parent.mkdir(parents=True, exist_ok=True)
    OUT_DOCENTE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_ALUMNO, 'w', encoding='utf-8') as f:
        json.dump(nb_alumno, f, indent=1, ensure_ascii=False)
    with open(OUT_DOCENTE, 'w', encoding='utf-8') as f:
        json.dump(nb_docente, f, indent=1, ensure_ascii=False)

    print(f'NB alumno:  {OUT_ALUMNO}  ({len(nb_alumno["cells"])} celdas)')
    print(f'NB docente: {OUT_DOCENTE}  ({len(nb_docente["cells"])} celdas)')


if __name__ == '__main__':
    main()
