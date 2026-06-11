# -*- coding: utf-8 -*-
"""
Genera el notebook MODELO del Trabajo Final (coloquio).

Tema del ejemplo: capacidades tecnologicas e insercion exportadora
(enfoque neoschumpeteriano, Unidad 4).

El notebook es la VARA DE REFERENCIA que se entrega a los alumnos: muestra como
debe verse un TP donde el PROCESAMIENTO de los datos esta adentro del notebook,
no solo un grafico pegado.

Para iterar el contenido: editar los bloques de texto de abajo y volver a correr
    python generar_modelo_tp.py
"""

import json
import os
import io
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Imagen de respaldo de la fórmula del ECI (PNG embebido en base64)
# Se genera con matplotlib (mathtext) para que la ecuación se vea SIEMPRE,
# aunque el visor no renderice LaTeX.
# ---------------------------------------------------------------------------

def formula_eci_datauri():
    AZUL, GRIS = "#1F4E79", "#4B5563"
    fig = plt.figure(figsize=(8.2, 5.2), dpi=150)
    fig.patch.set_facecolor("white")

    def eq(y, texto, fs=18):
        fig.text(0.06, y, texto, fontsize=fs, color=AZUL, va="center")

    def lbl(y, texto):
        fig.text(0.06, y, texto, fontsize=9.5, color=GRIS, va="center")

    fig.text(0.06, 0.95, "Cálculo del ECI — método de reflexiones (Hidalgo & Hausmann, 2009)",
             fontsize=11, color=GRIS, va="center", style="italic")
    eq(0.84, r"$k_{c,0}=\sum_p M_{cp}$")
    lbl(0.75, "Diversidad: cuántos productos exporta el país c con ventaja (RCA >= 1)")
    eq(0.65, r"$k_{p,0}=\sum_c M_{cp}$")
    lbl(0.56, "Ubicuidad: cuántos países exportan el producto p con ventaja")
    eq(0.45, r"$k_{c,N}=\frac{1}{k_{c,0}}\sum_p M_{cp}\,k_{p,N-1}$")
    eq(0.34, r"$k_{p,N}=\frac{1}{k_{p,0}}\sum_c M_{cp}\,k_{c,N-1}$")
    lbl(0.25, "Reflexiones: diversidad y ubicuidad se corrigen mutuamente, iterando")
    eq(0.13, r"$ECI=\frac{\vec{K}-\langle \vec{K}\rangle}{\sigma_K}$")
    lbl(0.04, "Autovector estandarizado (media 0, desvío 1):  + = sobre el promedio,  - = debajo")

    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")

# ---------------------------------------------------------------------------
# Helpers para construir celdas
# ---------------------------------------------------------------------------

import re

def _reflow(text):
    """Une los saltos de línea 'blandos' dentro de un mismo párrafo, para que el
    markdown no se vea 'cortado' en visores que tratan cada \\n como un <br> (Colab).
    Preserva la estructura: encabezados, listas, tablas, citas, bloques de código,
    fórmulas e imágenes."""
    out, buf, in_code = [], "", False

    def flush():
        nonlocal buf
        if buf:
            out.append(buf)
            buf = ""

    def is_struct(s):
        return (s.startswith("#") or s.startswith("|") or s.startswith("$$")
                or s.startswith("- ") or s.startswith("* ") or s.startswith("+ ")
                or s.startswith("> ") or s.startswith("---") or s.startswith("![")
                or bool(re.match(r"\d+\.\s", s)))

    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            flush(); out.append(line.rstrip()); in_code = not in_code; continue
        if in_code:
            out.append(line); continue
        if s == "":
            flush(); out.append("")
        elif s.startswith(">") and buf.strip().startswith(">"):
            buf = buf.rstrip() + " " + s[1:].strip()
        elif is_struct(s):
            flush(); buf = line.rstrip()
        else:
            buf = (buf.rstrip() + " " + s) if buf else line.rstrip()
    flush()

    res = []
    for x in out:
        if x == "" and (not res or res[-1] == ""):
            continue
        res.append(x)
    return "\n".join(res)

def md(texto):
    return {"cell_type": "markdown", "metadata": {}, "source": _reflow(texto)}

def code(texto):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": texto}

cells = []

# ---------------------------------------------------------------------------
# Portada
# ---------------------------------------------------------------------------
cells.append(md(
"""# Trabajo Final — Modelo de referencia

## ¿Las capacidades tecnológicas explican qué exporta un país?

**Economía Internacional — UMET** · Notebook modelo para el coloquio

> **Para qué sirve este notebook.** Es un **ejemplo** de cómo debe verse tu trabajo final.
> No alcanza con pegar un gráfico bonito: el **procesamiento de los datos** tiene que estar
> *adentro* del notebook, junto con la **pregunta**, la **hipótesis**, la **construcción del
> gráfico** y la **interpretación** con un marco teórico de la materia.
>
> Tu entrega debe seguir esta misma lógica, con **tu** tema y **un** modelo del curso.

---

### La estructura de un buen TP (la que vas a replicar)

1. **Pregunta teórica** — una sola, clara y *testeable* con datos.
2. **Hipótesis** — qué creés que vas a encontrar, y por qué.
3. **Datos** — de dónde salen, qué miden, qué limitaciones tienen.
4. **El gráfico** — el dato procesado que muestra el *hecho estilizado* y permite responder.
5. **Interpretación con el marco teórico** — acá aplicás el modelo del curso.
6. **Conclusión propia** — la respuesta a tu pregunta, con balance crítico.

> 💡 **Un solo modelo, una sola pregunta, un gráfico que cuente la historia.** Después podés
> sumar uno o dos gráficos que la refuercen o la matizen, pero no encadenes cinco teorías."""
))

# ---------------------------------------------------------------------------
# Bloque 1 — Pregunta e hipotesis
# ---------------------------------------------------------------------------
cells.append(md(
"""---
## Bloque 1 — Pregunta e hipótesis

**Pregunta de investigación**

> ¿El esfuerzo tecnológico de un país explica qué tan sofisticada es su canasta exportadora?
> Y en ese mapa, ¿dónde se ubica Argentina?

Es una pregunta **analítica** (no descriptiva): no pregunta "cuánto exporta Argentina", sino
si existe una **relación** entre dos variables y qué dice esa relación sobre el desarrollo.

**Hipótesis**

> A mayor inversión en I+D (investigación y desarrollo), mayor es la participación de bienes
> sofisticados en las exportaciones. **Argentina, que invierte poco en I+D, debería mostrar una
> canasta poco sofisticada** — una inserción primarizada coherente con la "trampa de capacidades"
> que describe el enfoque neoschumpeteriano.

**El contraste que hace interesante la hipótesis**

Si el comercio se explicara solo por la **dotación de factores** (Heckscher-Ohlin), el esfuerzo
tecnológico *no debería* predecir lo que un país exporta. La apuesta neoschumpeteriana es que
**sí lo predice**: las ventajas comparativas no se heredan, se *construyen*. El gráfico va a
poner esa apuesta a prueba."""
))

# ---------------------------------------------------------------------------
# Bloque 2 — Marco teorico
# ---------------------------------------------------------------------------
cells.append(md(
"""---
## Bloque 2 — Marco teórico y conceptual

### Marco teórico — el enfoque neoschumpeteriano

El punto de partida es un **quiebre con Ricardo y Heckscher-Ohlin**. Para los neoschumpeterianos
las ventajas comparativas **no vienen dadas por la dotación de factores**: se construyen acumulando
**capacidades tecnológicas**. El motor del comercio y del crecimiento es la innovación y el
aprendizaje, no solo los precios relativos.

Tres ideas que usamos en este trabajo:

1. **No da lo mismo qué se exporta.** Hausmann, Hwang y Rodrik (2007), *"What You Export Matters"*,
   muestran que los bienes no son equivalentes: algunos cargan más aprendizaje y más derrames
   tecnológicos. Los países que exportan canastas más **sofisticadas** crecen más rápido.

2. **Las capacidades son activos acumulados → *path dependence*.** Hidalgo y Hausmann (2009)
   formalizan la **complejidad económica**: una economía compleja es la que reúne muchas
   capacidades productivas. Saltar a productos nuevos es difícil porque requiere capacidades que
   todavía no se tienen. La estructura de hoy condiciona la de mañana.

3. **La brecha tecnológica explica la divergencia** (Cimoli y Porcile). El país que no invierte en
   capacidades queda encerrado en exportaciones de bajo contenido tecnológico y **diverge**. Acá se
   enlaza con Prebisch y la CEPAL: sin **cambio estructural** hacia sectores intensivos en
   conocimiento, la inserción primarizada reproduce la restricción externa.

**En una frase:** *cómo te insertás en el mundo depende de las capacidades que construiste;
exportar bienes sin contenido tecnológico limita el desarrollo.*"""
))

# ---------------------------------------------------------------------------
# Bloque 3 — Datos
# ---------------------------------------------------------------------------
cells.append(md(
"""### Marco conceptual — qué medimos y con qué

El marco teórico habla de "capacidades" y "sofisticación", que no se observan directamente. El marco
conceptual los **operacionaliza**: define cada concepto y elige una variable medible (un *proxy*).

| Concepto | Qué es | Cómo lo medimos (proxy) |
|----------|--------|-------------------------|
| **Esfuerzo tecnológico** | recursos que un país dedica a generar conocimiento | Gasto en **I+D (% del PIB)** |
| **Sofisticación exportadora** | cuánto conocimiento incorpora lo que se exporta | **% de exportaciones de alta tecnología** (proxy); EXPY sería el ideal |
| **Complejidad económica** | diversidad de capacidades productivas de la economía | **ECI** (Hidalgo-Hausmann) |
| **Capacidades tecnológicas** | activos de conocimiento acumulados | no se miden directas: se **infieren** de las anteriores |

> ⚠️ **Concepto clave a no confundir:** *exportar* alta tecnología (un valor que sale del país) no es
> lo mismo que *dominar* la tecnología (una capacidad). Un país que solo **ensambla** puede exportar
> "alta tecnología" sin tener las capacidades. Por eso cruzamos dos medidas (alta tec y ECI)."""
))

cells.append(md(
"""### El Índice de Complejidad Económica (ECI)

Una de las medidas de la tabla merece su propia definición, porque la vamos a usar como segunda
mirada en el Bloque 5. El **ECI** de Hidalgo y Hausmann (2009) estima el **conocimiento productivo**
acumulado en una economía, *infiriéndolo* de lo que el país logra exportar. La intuición: un país es
complejo si exporta **muchos** productos (alta **diversidad**) que **pocos** países saben hacer (baja
**ubicuidad**). Exportar un producto que casi cualquiera puede ensamblar aporta poca complejidad;
exportar bienes que requieren capacidades raras, mucha."""
))

cells.append(md(
r"""#### ¿Cómo se calcula? (el "método de reflexiones")

Se parte de una matriz país–producto $M_{cp}$, que vale **1 si el país $c$ exporta el producto $p$
con ventaja comparativa revelada** (RCA ≥ 1, el mismo índice de Balassa de la Unidad 2) y 0 si no.

A partir de ahí se definen dos medidas:

$$\text{Diversidad: } k_{c,0}=\sum_{p} M_{cp} \qquad\qquad \text{Ubicuidad: } k_{p,0}=\sum_{c} M_{cp}$$

- **Diversidad** ($k_{c,0}$): cuántos productos exporta el país $c$ con ventaja.
- **Ubicuidad** ($k_{p,0}$): cuántos países exportan el producto $p$ con ventaja.

La clave es que estas dos se **corrigen mutuamente de forma iterativa** (las "reflexiones"): la
complejidad de un país depende de la de sus productos, y la de un producto, de la de los países que
lo hacen.

$$k_{c,N}=\frac{1}{k_{c,0}}\sum_{p} M_{cp}\,k_{p,N-1} \qquad k_{p,N}=\frac{1}{k_{p,0}}\sum_{c} M_{cp}\,k_{c,N-1}$$

Formalmente, el ECI es el **autovector** asociado al segundo mayor autovalor de la matriz que conecta
países por sus productos, $\tilde{M}_{cc'}=\sum_{p}\dfrac{M_{cp}\,M_{c'p}}{k_{c,0}\,k_{p,0}}$, y luego
se **estandariza** (media 0, desvío 1):

$$ECI=\frac{\vec{K}-\langle \vec{K}\rangle}{\text{desv. est.}(\vec{K})}$$

Por eso los valores están **centrados en 0**: un ECI **positivo** indica complejidad por encima del
promedio mundial; **negativo**, por debajo. Argentina, con ECI ≈ −0,4, está por debajo del promedio:
exporta pocos productos y los que exporta (commodities) los exportan muchos países.

> 📖 **Fuente del método:** Hidalgo, C. & Hausmann, R. (2009), *The Building Blocks of Economic
> Complexity*, PNAS (en la bibliografía de la Unidad 4)."""
))

_uri_formula = formula_eci_datauri()
cells.append(md(
"**¿Tu visor no renderiza las fórmulas de arriba?** Acá están las mismas ecuaciones como "
"**imagen** y como **texto plano**, para que se vean en cualquier programa:\n\n"
f"![Fórmula del ECI]({_uri_formula})\n\n"
"```\n"
"Diversidad del país c:      k_c = Σ_p M_cp     (productos que exporta con ventaja, RCA>=1)\n"
"Ubicuidad del producto p:   k_p = Σ_c M_cp     (países que lo exportan con ventaja)\n"
"\n"
"Reflexiones (se iteran, corrigiéndose una a la otra):\n"
"   k_c(N) = (1/k_c) · Σ_p M_cp · k_p(N-1)\n"
"   k_p(N) = (1/k_p) · Σ_c M_cp · k_c(N-1)\n"
"\n"
"ECI = ( K − promedio(K) ) / desvío(K)      ->  estandarizado: media 0, desvío 1\n"
"```"
))

cells.append(md(
"""### Relación marco → hipótesis

El puente entre la teoría y lo que vamos a medir:

1. **La teoría dice:** las capacidades se construyen con esfuerzo tecnológico → quien invierte más en
   I+D acumula más capacidades → exporta bienes más sofisticados.
2. **Predicción testeable:** entonces, entre países, debería haber una **relación positiva** entre
   I+D (% del PIB) y sofisticación exportadora (alta tec % / ECI).
3. **Hipótesis:** esa relación existe, y **Argentina —con baja I+D— debería ubicarse en la zona de
   baja sofisticación.**
4. **El test:** el gráfico del Bloque 4 pone esa predicción a prueba con datos reales.

> Y el contraste que lo hace interesante: **si valiera Heckscher-Ohlin puro**, lo que un país exporta
> dependería solo de su dotación de factores y la I+D **no** debería predecir nada. La apuesta
> neoschumpeteriana es que **sí** predice."""
))

cells.append(md(
"""---
## Bloque 3 — Los datos

Para poner la hipótesis a prueba necesitamos dos variables comparables entre países:

| Variable | Indicador (Banco Mundial) | Qué mide |
|----------|---------------------------|----------|
| **Esfuerzo tecnológico** | `GB.XPD.RSDV.GD.ZS` | Gasto en I+D como % del PIB |
| **Sofisticación exportadora** (proxy) | `TX.VAL.TECH.MF.ZS` | Exportaciones de alta tecnología como % de las exportaciones manufactureras |

Los bajamos **en vivo** de la API del Banco Mundial (la misma que usaste en el Notebook 1).
Elegimos 15 países que cubren todo el espectro de desarrollo, para que el contraste se vea.

> ⚠️ **Honestidad metodológica (esto súmalo siempre a tu TP).** "Exportaciones de alta tecnología"
> es un **proxy** imperfecto de sofisticación: cuenta el *valor exportado* de bienes clasificados
> como alta tecnología, sin importar si el país los *diseña* o solo los *ensambla*. Más abajo
> vamos a ver por qué esto importa."""
))

cells.append(code(
"""# --- Configuración e importación de librerías ---
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paleta del curso
AZUL      = "#1F4E79"
AZUL_MED  = "#2E75B6"
CELESTE   = "#0EA5E9"
NARANJA   = "#E8833A"
VERDE     = "#27AE60"
ROJO      = "#E74C3C"
GRIS      = "#4B5563"

# Países a comparar (código ISO-3 -> nombre en español)
PAISES = {
    "ARG": "Argentina", "KOR": "Corea del Sur", "ISR": "Israel",
    "DEU": "Alemania",  "JPN": "Japón",         "USA": "EE.UU.",
    "CHN": "China",     "MEX": "México",         "BRA": "Brasil",
    "CHL": "Chile",     "MYS": "Malasia",        "TUR": "Turquía",
    "ZAF": "Sudáfrica", "COL": "Colombia",       "ESP": "España",
}
print("Vamos a comparar", len(PAISES), "países.")"""
))

cells.append(code(
'''# --- Función para bajar un indicador del Banco Mundial ---
import time

def bajar_indicador_bm(codigo, paises, desde=2010, hasta=2022, reintentos=3):
    """Devuelve {iso: (año, valor)} con el ÚLTIMO dato disponible de cada país."""
    lista = ";".join(paises)
    url = (f"https://api.worldbank.org/v2/country/{lista}/indicator/{codigo}"
           f"?format=json&date={desde}:{hasta}&per_page=5000")
    # La API a veces corta una respuesta; reintentamos un par de veces.
    for intento in range(reintentos):
        try:
            respuesta = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=60)
            datos = respuesta.json()[1]    # [0] son metadatos; [1] son los datos
            break
        except Exception:
            if intento == reintentos - 1:
                raise
            time.sleep(2)

    ultimo = {}
    for d in datos:
        iso, valor = d["countryiso3code"], d["value"]
        if valor is None:                   # algunos años no tienen dato
            continue
        anio = int(d["date"])
        if iso not in ultimo or anio > ultimo[iso][0]:
            ultimo[iso] = (anio, valor)
    return ultimo

I_MAS_D  = "GB.XPD.RSDV.GD.ZS"   # Gasto en I+D (% del PIB)
ALTA_TEC = "TX.VAL.TECH.MF.ZS"   # Exportaciones de alta tecnología (% de exp. manufactureras)

datos_id  = bajar_indicador_bm(I_MAS_D,  PAISES.keys())
datos_tec = bajar_indicador_bm(ALTA_TEC, PAISES.keys())
print("Datos descargados correctamente.")'''
))

cells.append(code(
"""# --- Armamos la tabla de trabajo ---
filas = []
for iso, nombre in PAISES.items():
    if iso in datos_id and iso in datos_tec:
        filas.append({
            "País": nombre,
            "iso": iso,
            "I+D (% PIB)": round(datos_id[iso][1], 2),
            "año I+D": datos_id[iso][0],
            "Alta tec (% manuf)": round(datos_tec[iso][1], 1),
            "año alta tec": datos_tec[iso][0],
        })

df = pd.DataFrame(filas).sort_values("I+D (% PIB)", ascending=False).reset_index(drop=True)
df"""
))

cells.append(md(
"""**Cómo leer la tabla.** Arriba están los países que más invierten en I+D (Israel, Corea, EE.UU.,
Japón, Alemania) y abajo los que menos (Argentina, Chile, Colombia, México). Fijate ya en una
anomalía: **Malasia y México** tienen mucha "alta tecnología" exportada con **poca** I+D. Volvemos
sobre eso después del gráfico — es la parte más interesante."""
))

# ---------------------------------------------------------------------------
# Grafico 1
# ---------------------------------------------------------------------------
cells.append(md(
"""---
## Bloque 4 — El gráfico: el hecho estilizado

Ahora **construimos** el gráfico que responde la pregunta. Es un diagrama de dispersión: cada país
es un punto, el eje X es el esfuerzo tecnológico (I+D) y el eje Y la sofisticación exportadora.
Marcamos a **Argentina** en rojo y a los dos *outliers* en naranja."""
))

cells.append(code(
'''# --- Gráfico 1: I+D vs sofisticación exportadora ---
fig, ax = plt.subplots(figsize=(10, 7))

OUTLIERS = ("MYS", "MEX")   # plataformas de ensamblaje (lo explicamos abajo)

for _, r in df.iterrows():
    es_arg     = r["iso"] == "ARG"
    es_outlier = r["iso"] in OUTLIERS
    color = ROJO if es_arg else (NARANJA if es_outlier else AZUL_MED)
    ax.scatter(r["I+D (% PIB)"], r["Alta tec (% manuf)"],
               s=160 if es_arg else 90, color=color,
               edgecolor="white", linewidth=1.2, zorder=3)
    ax.annotate(r["País"], (r["I+D (% PIB)"], r["Alta tec (% manuf)"]),
                xytext=(7, 4), textcoords="offset points",
                fontsize=9, color=(ROJO if es_arg else AZUL),
                fontweight=("bold" if es_arg or es_outlier else "normal"))

# Recta de tendencia y correlación (sobre TODOS los países)
x = df["I+D (% PIB)"].values
y = df["Alta tec (% manuf)"].values
pendiente, ordenada = np.polyfit(x, y, 1)       # ajuste lineal y = pendiente*x + ordenada
xs = np.linspace(x.min(), x.max(), 50)
ax.plot(xs, pendiente * xs + ordenada, color=GRIS, linestyle="--", linewidth=1.5, zorder=2)
r_todos = np.corrcoef(x, y)[0, 1]               # coeficiente de correlación de Pearson
ax.text(0.97, 0.97,
        f"Recta de tendencia (todos los países)\\nCorrelación r = {r_todos:.2f}",
        transform=ax.transAxes, fontsize=10, color=AZUL, va="top", ha="right",
        bbox=dict(boxstyle="round", facecolor="white", edgecolor=AZUL_MED, alpha=0.9))

ax.set_xlabel("Gasto en I+D (% del PIB)  →  esfuerzo tecnológico", fontsize=11, color=GRIS)
ax.set_ylabel("Exportaciones de alta tecnología (% de exp. manufactureras)", fontsize=11, color=GRIS)
ax.set_title("Esfuerzo tecnológico y sofisticación exportadora",
             fontsize=14, color=AZUL, fontweight="bold", pad=14)
ax.grid(True, alpha=0.3)
ax.figure.text(0.99, 0.01,
               "Fuente: Banco Mundial (I+D y alta tecnología, último dato disponible). Elaboración propia.",
               ha="right", fontsize=8, color=GRIS)
plt.tight_layout()
plt.show()'''
))

cells.append(md(
"""### Lectura del gráfico

**1. La nube es positiva.** El bloque de arriba a la derecha (Israel, Corea, EE.UU., Japón,
Alemania, China) invierte mucho en I+D *y* exporta alta tecnología. El de abajo a la izquierda
(Argentina, Chile, Colombia, Sudáfrica, Brasil) casi no invierte *y* casi no exporta tecnología.
La relación que predice el enfoque neoschumpeteriano **aparece**.

**2. Argentina queda firme abajo a la izquierda.** Con I+D ≈ 0,5% del PIB y ~5% de alta tecnología,
Argentina está entre los países de menor esfuerzo tecnológico y menor sofisticación exportadora.
**La hipótesis se sostiene.**

**3. Los dos *outliers* son el corazón del argumento, no un error.** Malasia (¡~58%!) y México
exportan mucha "alta tecnología" con muy poca I+D. ¿Por qué? Porque **ensamblan** electrónica y
manufacturas importadas (plataformas de maquila). Es la distinción clave de Hausmann:
**exportar alta tecnología ≠ dominar la tecnología.** El dato cuenta el *valor* que sale del país,
no las *capacidades* que hay detrás.

> 🔗 **Conexión con el curso.** Este es exactamente el debate de Tierra del Fuego: ¿aprendizaje
> tecnológico genuino o ensamblaje protegido? El gráfico muestra que el indicador "alta tecnología"
> puede confundir una cosa con la otra."""
))

# ---------------------------------------------------------------------------
# Analisis de correlacion
# ---------------------------------------------------------------------------
cells.append(md(
"""### Análisis de los datos: ¿cuánto pesan los *outliers*?

La recta de tendencia y la correlación (r) resumen en un número la fuerza de la relación. Pero
**el número solo cuenta la mitad de la historia** si no entendés tus datos. Vamos a medir cuánto
distorsionan Malasia y México la correlación."""
))

cells.append(code(
'''# --- ¿Cuánto pesan los outliers de ensamblaje en la correlación? ---
def correlacion(datos, x, y):
    return np.corrcoef(datos[x], datos[y])[0, 1]

x, y = "I+D (% PIB)", "Alta tec (% manuf)"
r_todos = correlacion(df, x, y)
r_sin   = correlacion(df[~df["iso"].isin(OUTLIERS)], x, y)   # sin Malasia ni México

print("Correlación entre I+D y exportaciones de alta tecnología")
print(f"  con TODOS los países:                  r = {r_todos:+.2f}")
print(f"  SIN Malasia y México (ensamblaje):     r = {r_sin:+.2f}")'''
))

cells.append(md(
"""**Qué nos dice esto.** Con todos los países la correlación es apenas **moderada (r ≈ 0,4)**: a
primera vista, la relación entre I+D y alta tecnología parece floja. Pero al sacar a las dos
plataformas de ensamblaje, la correlación **salta a fuerte (r ≈ 0,9)**. Es decir: la relación que
predice la teoría neoschumpeteriana *sí está ahí*, y es robusta; lo que la "ensuciaba" eran dos
casos que el indicador clasifica mal (exportan alta tecnología sin dominarla).

> 🎯 **Lección metodológica para tu TP.** No reportes una correlación sin mirar el gráfico. Un solo
> número puede esconder *outliers* que cambian por completo la lectura. Identificarlos y
> **explicarlos con la teoría** (acá: ensamblaje ≠ capacidades) es exactamente el tipo de análisis
> que se valora — no esconderlos."""
))

# ---------------------------------------------------------------------------
# Grafico 2 — ECI
# ---------------------------------------------------------------------------
cells.append(md(
"""---
## Bloque 5 — Segunda mirada: la complejidad económica (ECI)

Ya **definimos el ECI en el marco conceptual** (Bloque 2): mide el conocimiento productivo de una
economía a partir de la diversidad y la ubicuidad de lo que exporta. Acá lo **aplicamos a nuestros
15 países**. Como penaliza el ensamblaje (exportar un producto que muchos países hacen aporta poca
complejidad), es la medida que corrige la confusión "exportar alta tecnología ≠ dominarla" que vimos
en el gráfico 1."""
))

cells.append(md(
"""### ¿De dónde salen estos valores? (trazabilidad)

El ECI **no tiene una API abierta**, así que los valores se cargan a mano. Cuando esto pasa, hay que
**citar exactamente de dónde se copió el dato** para que cualquiera pueda verificarlo:

- **Productor del dato:** Atlas of Economic Complexity, Harvard Growth Lab — ECI **2023**, clasificación
  HS. 🔗 https://atlas.hks.harvard.edu/rankings
- **Transcripto de:** la tabla publicada en 🔗 https://en.wikipedia.org/wiki/Economic_Complexity_Index
  (que cita al Atlas), **consultada el 10/06/2026**.

> ⚠️ El valor **absoluto** del ECI se estandariza por edición y clasificación, así que puede variar
> levemente entre fuentes y años. Lo **robusto** es la **posición relativa** entre países (quién está
> arriba y quién abajo), no el segundo decimal."""
))

cells.append(code(
"""# --- Índice de Complejidad Económica (ECI) ---
# Productor: Atlas of Economic Complexity, Harvard Growth Lab. Año 2023, clasificación HS.
#   https://atlas.hks.harvard.edu/rankings
# Sin API abierta -> valores TRANSCRIPTOS de la tabla publicada en (cita al Atlas):
#   https://en.wikipedia.org/wiki/Economic_Complexity_Index  (consultada 10/06/2026)
# Verificá los valores en el link. Lo robusto es la posición relativa, no el 2do decimal.
ECI_2023 = {
    "JPN": 2.43, "KOR": 2.23, "DEU": 2.01, "USA": 1.51, "CHN": 1.47,
    "MEX": 1.41, "ISR": 1.36, "MYS": 1.03, "ESP": 0.61, "TUR": 0.46,
    "COL": -0.14, "ZAF": -0.28, "ARG": -0.41, "CHL": -0.44, "BRA": -0.52,
}
df["ECI"] = df["iso"].map(ECI_2023)
df[["País", "I+D (% PIB)", "Alta tec (% manuf)", "ECI"]]"""
))

cells.append(code(
'''# --- Gráfico 2: I+D vs complejidad económica (ECI) ---
fig, ax = plt.subplots(figsize=(10, 7))

for _, r in df.iterrows():
    es_arg     = r["iso"] == "ARG"
    es_outlier = r["iso"] in OUTLIERS
    color = ROJO if es_arg else (NARANJA if es_outlier else AZUL_MED)
    ax.scatter(r["I+D (% PIB)"], r["ECI"],
               s=160 if es_arg else 90, color=color,
               edgecolor="white", linewidth=1.2, zorder=3)
    ax.annotate(r["País"], (r["I+D (% PIB)"], r["ECI"]),
                xytext=(7, 4), textcoords="offset points",
                fontsize=9, color=(ROJO if es_arg else AZUL),
                fontweight=("bold" if es_arg or es_outlier else "normal"))

# Recta de tendencia y correlación (sobre TODOS los países)
xe = df["I+D (% PIB)"].values
ye = df["ECI"].values
pend_e, ord_e = np.polyfit(xe, ye, 1)
xs_e = np.linspace(xe.min(), xe.max(), 50)
ax.plot(xs_e, pend_e * xs_e + ord_e, color=GRIS, linestyle="--", linewidth=1.5, zorder=2)
r_eci = np.corrcoef(xe, ye)[0, 1]
ax.text(0.03, 0.97,
        f"Recta de tendencia (todos los países)\\nCorrelación r = {r_eci:.2f}",
        transform=ax.transAxes, fontsize=10, color=AZUL, va="top",
        bbox=dict(boxstyle="round", facecolor="white", edgecolor=AZUL_MED, alpha=0.9))

ax.axhline(0, color=GRIS, linewidth=0.8, alpha=0.5)   # ECI = 0 separa complejas de simples
ax.set_xlabel("Gasto en I+D (% del PIB)  →  esfuerzo tecnológico", fontsize=11, color=GRIS)
ax.set_ylabel("Índice de Complejidad Económica (ECI)", fontsize=11, color=GRIS)
ax.set_title("Esfuerzo tecnológico y complejidad de la canasta exportadora",
             fontsize=14, color=AZUL, fontweight="bold", pad=14)
ax.grid(True, alpha=0.3)
ax.figure.text(0.99, 0.01,
               "Fuentes: Banco Mundial (I+D) y Atlas of Economic Complexity, Harvard (ECI 2023). Elaboración propia.",
               ha="right", fontsize=8, color=GRIS)
plt.tight_layout()
plt.show()'''
))

cells.append(md(
"""### Lectura del gráfico 2

**Malasia se ordena.** Pasa de ~58% de "alta tecnología" a un ECI moderado (≈1,0): la complejidad
**sí le descuenta** el ensamblaje de electrónica. Confirma la crítica de Hausmann.

**México sigue siendo un *outlier*** (poca I+D, pero ECI alto ≈1,4): su canasta es **diversificada**
(autos, electrónica, maquinaria) y eso puntúa alto en complejidad aunque casi no invierta en I+D.
¿Por qué? Porque buena parte de esa diversidad la trajo la **IED** (empresas transnacionales) dentro
del bloque del T-MEC. Abre una discusión honesta: **ningún indicador es perfecto**, y la complejidad
de la canasta puede venir "prestada" por las ETN sin reflejar capacidades nacionales propias.

**Argentina queda abajo a la izquierda con las dos medidas.** Sea con "alta tecnología" o con
complejidad económica, Argentina aparece como un país de bajo esfuerzo tecnológico y baja
sofisticación. **La conclusión es robusta:** no depende del indicador que elijas.

**Y la correlación lo confirma.** Con el ECI, la relación con la I+D es **fuerte ya con todos los
países (r ≈ 0,7)** — más alta que el r ≈ 0,4 del gráfico 1. ¿Por qué? Porque el ECI no se deja
engañar por el ensamblaje: es una **mejor medida** de capacidades. Cuando un indicador bien elegido
da una señal más limpia *sin necesidad de descartar casos*, es una señal de que estás midiendo mejor
lo que la teoría dice que importa."""
))

# ---------------------------------------------------------------------------
# Conclusion
# ---------------------------------------------------------------------------
cells.append(md(
"""---
## Bloque 6 — Contraste de la hipótesis

> ⚠️ **Ojo con un error muy común:** *contrastar la hipótesis* y *concluir* **no son lo mismo**.
> Acá (Bloque 6) hacemos una sola cosa: poner la hipótesis a prueba contra los datos y preguntarnos
> honestamente si se **confirma** o se **refuta**. La conclusión y las propuestas van **después**
> (Bloque 7).

**Recordemos la hipótesis:** *a mayor I+D, mayor sofisticación exportadora; Argentina, con baja I+D,
debería tener una canasta poco sofisticada.*

**Evidencia a favor.**
- Argentina queda abajo a la izquierda en **los dos** gráficos (alta tecnología y ECI): baja I+D y
  baja sofisticación, tal como predice la hipótesis.
- La relación es positiva en ambos casos. Con el ECI —la mejor medida— es **fuerte (r ≈ 0,70)** y
  robusta; y al aislar el ruido del ensamblaje, la relación I+D–alta tecnología trepa a **r ≈ 0,88**.

**El contraste crítico: ¿cómo podría refutarse?** (hay que tomárselo en serio, no esquivarlo)
1. *Correlación débil:* con **todos** los países, la relación I+D–alta tecnología es apenas **0,41**.
   Un escéptico diría que la evidencia es floja.
2. *Contraejemplos:* Malasia y México exportan mucha alta tecnología **sin** I+D. ¿No es un golpe
   directo a "I+D → sofisticación"?
3. *Explicación rival (Heckscher-Ohlin):* tal vez Argentina exporta primarios por su **dotación de
   factores** (tierra), no por falta de capacidades. Si fuera así, la I+D sería irrelevante.
4. *Asociación ≠ causalidad:* quizás una tercera variable (el ingreso) explique a la vez la I+D y la
   sofisticación.

**¿Resiste la hipótesis? (respuesta razonada a cada objeción)**
1. El 0,41 era un **artefacto del proxy**: "alta tecnología exportada" mezcla diseñar con ensamblar.
   Con la medida correcta (ECI) la relación ya es fuerte *sin descartar nada*. La debilidad no era de
   la hipótesis, era del indicador.
2. Los contraejemplos **no la refutan: la confirman en su versión fina**. Al medir capacidades reales
   (ECI), Malasia se ordena y México queda explicado por la IED. Exportar ≠ dominar: la teoría
   *predice* y *explica* el outlier, en vez de tropezar con él.
3. H-O explica la *dirección* (primarios), pero no por qué Argentina **no logró diversificarse** hacia
   bienes complejos en décadas. Eso —la trayectoria, el *path dependence*— es justo lo que el enfoque
   de capacidades agrega y H-O no.
4. Es cierto: el gráfico muestra **asociación, no causalidad**. Por eso la hipótesis queda confirmada
   en su forma asociativa, **no** en la causal fuerte. Hay que decirlo.

> 🎯 **Veredicto.** La hipótesis **no se refuta**: sobrevive al contraste crítico, sobre todo con el
> ECI. Argentina aparece de forma consistente como un caso de baja capacidad tecnológica y baja
> sofisticación exportadora. Lo que *no* podemos afirmar con estos datos es la **causalidad**: que
> más I+D *causaría* más sofisticación. Eso lo sostiene la teoría, no este gráfico."""
))

cells.append(md(
"""---
## Limitaciones y honestidad metodológica

- **Proxies, no medidas perfectas.** "Alta tecnología exportada" mide valor, no capacidades; el ECI
  no distingue del todo capacidades propias de las que aportan las ETN (caso México).
- **Asociación ≠ causalidad.** El gráfico no prueba que la I+D *cause* la sofisticación; muestra que
  van juntas. La causalidad la argumenta la teoría.
- **Años mezclados.** I+D y alta tecnología son del último dato disponible (≈2022); el ECI es 2023.
  Para un trabajo así la diferencia es menor, pero **hay que declararla**.
- **Muestra de 15 países.** Elegidos para cubrir el espectro; con otra muestra la nube podría verse
  algo distinta."""
))

cells.append(md(
"""---
## Bloque 7 — Conclusión: discusión de política (abierta)

> Acá cambia el registro. El Bloque 6 era **análisis** (¿la hipótesis se sostiene?); este es **tu
> voz**: qué proponés, qué discutís, qué creés que habría que hacer. No hay una única respuesta
> "correcta" — se valora que **tomes posición y la fundamentes**.

*(Ejemplo de una conclusión posible — la tuya puede ir por otro lado.)*

Si el lugar de un país en el mundo depende de las capacidades que construye, entonces la posición de
Argentina —baja I+D, canasta poco compleja— **no es un destino natural, sino el resultado de una
trayectoria** que se puede cambiar. Pero cambiarla no es automático ni llega "por precios" o por
abrir la economía: exige una política deliberada de **cambio estructural** —I+D, formación,
financiamiento a la innovación, instituciones de aprendizaje— que es donde se encuentran los
neoschumpeterianos con la tradición de la CEPAL.

Y abre preguntas que cada quien puede responder distinto:

- ¿Es viable esa política dada la **restricción externa** (Diamand)? ¿Cómo se financia el cambio
  estructural sin divisas?
- ¿Qué sectores priorizar: **agregar capacidades sobre lo que ya sabemos hacer** (agro, software,
  biotecnología) o apostar a sectores nuevos?
- El camino de México/Malasia —atraer IED de alta tecnología— ¿es un atajo o una **trampa de
  ensamblaje**?
- ¿Qué papel para el tipo de cambio, la educación y el financiamiento de la innovación?

> ✍️ **Lo importante:** que la conclusión sea **tuya**, esté **fundamentada** y se conecte con lo que
> mostró el contraste del Bloque 6. No es repetir el análisis: es decir qué hacés con él."""
))

cells.append(md(
"""---
## Fuentes y ficha técnica

**Datos**
- Banco Mundial — *Research and development expenditure (% of GDP)*, `GB.XPD.RSDV.GD.ZS`.
  API: https://api.worldbank.org (descarga en vivo en este notebook).
- Banco Mundial — *High-technology exports (% of manufactured exports)*, `TX.VAL.TECH.MF.ZS`.
- Atlas of Economic Complexity, Harvard Growth Lab — *Economic Complexity Index (ECI)*, 2023,
  clasificación HS. https://atlas.hks.harvard.edu/rankings — valores transcriptos de
  https://en.wikipedia.org/wiki/Economic_Complexity_Index (consultada 10/06/2026), que cita al Atlas.

**Bibliografía (Unidad 4)**
- Hausmann, R., Hwang, J. & Rodrik, D. (2007). *What You Export Matters*. Journal of Economic Growth.
- Hidalgo, C. & Hausmann, R. (2009). *The Building Blocks of Economic Complexity*. PNAS.
- Cimoli, M. & Porcile, G. (2014). *Technology, Structural Change and BOP-Constrained Growth*. CJE.
- Prebisch, R. (1950); Ocampo, J.A. (2022) — visión centro-periferia.

**Declaración de uso de IA.** *(ejemplo)* Se usó una herramienta de IA para generar el código de
descarga y graficado a partir de consignas propias. La formulación de la pregunta, la hipótesis, la
interpretación de los gráficos y la conclusión son de elaboración propia."""
))

# ---------------------------------------------------------------------------
# Nota final al alumno
# ---------------------------------------------------------------------------
cells.append(md(
"""---
## 🧭 Antes de bajar datos: qué te dice tu teoría

Antes de buscar un solo dato, **la teoría que elegiste ya te dice qué datos necesitás.** El error más común es elegir una teoría de un nivel y traer datos de otro: si tu teoría habla de firmas y traés agregados de país, no estás testeando nada.

La teoría te responde **dos preguntas**:

1. **¿Qué TIPO de comercio explica?** — interindustrial, intraindustrial, intrafirma o de tareas → te dice si los datos son **agregados o desagregados**.
2. **¿Cuál es la UNIDAD de análisis?** — país, sector, producto, firma, región o eslabón → te dice el **nivel de agregación**.

> **Regla de oro:** la teoría y el dato tienen que estar en el **mismo nivel**.

### Cada teoría del curso → qué datos implica

| Teoría (unidad) | Tipo de comercio | Unidad / nivel | Datos que implica |
|---|---|---|---|
| **Smith / Ricardo — ventaja absoluta y comparativa** (U2) | Inter-industrial | País × sector | Productividad relativa por sector; especialización → RCA (Balassa) |
| **Heckscher-Ohlin** (U2) | Inter-industrial | País × sector (agregado) | Dotaciones de factores; intensidad factorial; contenido factorial del comercio |
| **Krugman / comercio intraindustrial** (U3) | Intra-industrial | Producto desagregado | Comercio bilateral por producto fino → índice de Grubel-Lloyd |
| **Vernon — ciclo del producto** (U3) | Dinámico | Producto en el tiempo | Serie temporal de un producto: del país innovador a la periferia |
| **Melitz — firmas heterogéneas** (U3) | Intra-industrial | **Firma (micro)** | Productividad por firma; quién exporta vs no; premio exportador |
| **Dumping** (U3) | Intra-industrial | Empresa × mercado | Precios del mismo bien en distintos mercados; márgenes |
| **Nueva Geografía Económica** (U3) | Aglomeración | Región | Concentración geográfica de producción/empleo; costos de transporte |
| **Prebisch-Singer — TDI** (U4) | Inserción primaria | País, serie larga | Serie larga de términos del intercambio / precios commodities vs manufacturas |
| **Diamand — EPD / estructuralismo** (U4) | Restricción externa | Dos sectores (agro/industria) | Balance de divisas por sector; tipo de cambio; composición sectorial |
| **Neoschumpeteriano / complejidad** (U4) | Capacidades | País × producto | I+D; intensidad tecnológica; ECI; sofisticación (este notebook) |
| **ETN / IED** (U5) | **Intra-firma** | Empresa multinacional | IED; comercio intrafirma; participación de filiales extranjeras |
| **CGV — Gereffi** (U5) | **Comercio de tareas** | Eslabón / valor agregado | Valor agregado en exportaciones (TiVA); contenido importado; posición en la cadena |
| **Política comercial / protección efectiva** (U6) | Instrumentos | Producto / sector | Aranceles nominales y efectivos; precios domésticos vs internacionales |
| **Integración — Viner** (U6) | Creación / desvío | Bloque, antes/después | Comercio intra vs extra bloque antes y después del acuerdo |

### El check (3 preguntas antes de bajar datos)

1. ¿Mi teoría explica comercio inter, intra, intrafirma o de tareas? → ¿agregados o desagregados?
2. ¿Mi unidad es país, sector, producto, firma, región o eslabón? → ese es el nivel del dato.
3. ¿El dato que conseguí está en ese nivel? Si no, no testea lo que decís.

> **Ejemplo del error:** un trabajo sobre cadenas de valor (CGV → valor agregado) que usa comercio **bruto** en vez de **valor agregado**; o uno sobre firmas (Melitz → micro) que usa agregados de país. La teoría pide un nivel y el dato está en otro."""
))

cells.append(md(
"""---
## 📌 Cómo replicar esto con TU tema

1. **Elegí UN modelo** del curso (Ricardo, H-O, Grubel-Lloyd/IIT, Prebisch-Singer, complejidad,
   CGV, ETN, etc.) y **UNA pregunta** testeable.
2. Escribí tu **hipótesis** antes de mirar los datos.
3. Conseguí los datos (Banco Mundial, INDEC, COMTRADE, OEC, CEPAL...) y **procesalos en el notebook**
   (no pegues un gráfico hecho por otro).
4. Construí **el gráfico** que muestra tu hecho estilizado. Sumá 1-2 más solo si refuerzan o matizan.
5. **Contrastá tu hipótesis** con el marco teórico: ¿los datos la confirman o la refutan? Tomate en
   serio las objeciones (contraejemplos, explicaciones rivales, causalidad) antes de dar el veredicto.
6. **Concluí aparte:** tu propuesta o discusión de política. Esa es tu voz, y es distinta del contraste.

> ✅ **Lo que se evalúa no es el código, es la interpretación económica.** Pero el procesamiento
> tiene que estar adentro del notebook para que se vea que el análisis es tuyo."""
))

cells.append(md(
"""---
## 📤 Cómo entregar

1. **Subí tu notebook a Google Colab** (Archivo → Subir notebook, o trabajalo directo ahí).
2. **Ejecutalo de principio a fin** (Entorno de ejecución → *Ejecutar todo*) y verificá que **no falle
   ninguna celda**. Si una da error, todavía no está para entregar.
3. **Compartí el link** con permiso de lectura para "cualquiera con el enlace" (botón *Compartir*,
   arriba a la derecha).

> ⚠️ **Tiene que correr para cualquiera, no solo para vos.** Hay dos formas válidas de cargar datos:
> **(1)** si son pocos (una tabla de pocas filas, como la mayoría), **escribilos directo en una celda**
> como un DataFrame o diccionario — son parte del notebook y corren siempre; **(2)** si están online,
> **leelos por URL** (una API como el Banco Mundial, o un Google Sheet *publicado como CSV* y leído con
> `pd.read_csv(url)`).
>
> **Lo que NO funciona:** subir un archivo (CSV/Excel) a tu sesión de Colab. Ese archivo **no se guarda**
> con el notebook, desaparece al cerrar la sesión, y cuando el docente abra el link le va a fallar.

> ✅ **Checklist final antes de mandar el link:** corrió *Ejecutar todo* sin errores · los gráficos se
> ven · los datos se bajan solos · el link está compartido como "cualquiera con el enlace"."""
))

# ---------------------------------------------------------------------------
# Ensamblar el notebook
# ---------------------------------------------------------------------------
notebook = {
    "cells": cells,
    "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"display_name": "Python 3", "name": "python3"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

destino = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "TP_modelo_insercion_tecnologica.ipynb")
with open(destino, "w", encoding="utf-8") as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f"Notebook generado: {destino}")
print(f"Total de celdas: {len(cells)}")
