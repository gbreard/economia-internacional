# Proyecto: Clases de Economía Internacional - UMET

## Descripción
Proyecto para diseñar y armar presentaciones de clases de Comercio Internacional para alumnos de la carrera de Economía de la UMET (Universidad Metropolitana para la Educación y el Trabajo).

## Datos del Curso
- **Carrera**: Licenciatura en Economía / Relaciones Internacionales
- **Carga horaria**: 44 horas de contenido + coloquio + recuperatorio
- **Duración**: 12 semanas (26/03 al 18/06), jueves 18 a 22hs
- **Frecuencia**: 1 sesión semanal de 4 horas
- **Correlativas**: Microeconomía, Macroeconomía

## Estructura del Proyecto

```
Economia Internacional/
├── CLAUDE.md                    # Este archivo de contexto
├── .gitignore                   # Exclusiones de git (caches, temporales)
├── index.html                   # Landing page del curso (GitHub Pages)
├── notebooks.html               # Subpágina: ejercicios con datos (instrucciones + links)
├── asistente-ia.html            # Subpágina: NotebookLM como asistente de estudio
│
├── programa/                    # Documentos del curso
│   ├── Programa de la Asignatura.docx
│   ├── Clases del programa.docx
│   └── Plan_de_clases.pdf
│
├── bibliografia/                # Bibliografía organizada por unidad
│   ├── index.html               # Página de descarga: manuales + links a unidades
│   ├── Krugman y Obstfeld - 9na edición.pdf   # Manual principal (compartido)
│   ├── Lugones-Teorias_del_Comercio_Internacional.pdf  # Lugones (compartido)
│   ├── LIC-PORTA-Integracion_Econo (1).pdf    # Porta (compartido)
│   ├── unidad1/               # index.html + README.md + PDFs específicos
│   ├── unidad2/               # index.html + README.md + PDFs específicos
│   ├── unidad3/               # index.html + README.md + PDFs específicos
│   ├── unidad4/               # index.html + README.md + PDFs específicos
│   ├── unidad5/               # index.html + README.md + PDFs específicos
│   ├── unidad6/               # index.html + README.md + PDFs específicos
│   └── unidad7/               # index.html + README.md + PDFs específicos
│
├── notebooks/                   # Ejercicios prácticos con Python (Google Colab)
│   └── NB1_indicadores_comercio_mundial.ipynb
│
├── evaluacion/                  # Evaluaciones por unidad
│   ├── evaluacion_unidad1.md    # 5 preguntas MC (3 conceptuales + 2 con datos)
│   ├── evaluacion_unidad2.md    # 5 preguntas MC (3 conceptuales + 2 con datos)
│   └── datos/                   # Excel con datos procesados y gráficos de verificación
│       ├── U1_P4_apertura_comercial.xlsx
│       ├── U1_P5_cuenta_corriente.xlsx
│       ├── U2_P4_importaciones_avicolas.xlsx
│       ├── U2_P5_tipo_cambio_real.xlsx
│       └── generar_U{N}_P{M}.py # Scripts que generan los Excel
│
├── docente/                     # ⚠️ EN .gitignore — NO se publica
│   └── NB1_RESUELTO_indicadores_comercio_mundial.ipynb
│
├── datos_compartidos/           # Datos reutilizables entre clases
│   └── [archivos FTWTHD por región: world, america, europe, asia, africa, oceania]
│
├── herramientas/                # Sistema de generación de slides (legacy JSON)
│   ├── generar_html.py          # Generador JSON → HTML (NO se usa, ver generar_desde_md.py)
│   ├── TEMPLATE.html            # Template manual
│   └── README.md                # Documentación (desactualizado)
│
├── Clases/                      # 12 carpetas de sesión (⚠️ C mayúscula)
│   ├── sesion01/              # Sesiones 1-3: dos partes (4hs = 2+2 con recreo)
│   │   ├── parte1/            # Ex clase01
│   │   │   ├── contenido.md
│   │   │   ├── scripts/generar_desde_md.py
│   │   │   ├── graficos/
│   │   │   ├── img/
│   │   │   └── presentacion/index.html
│   │   └── parte2/            # Ex clase02
│   │       └── (misma estructura)
│   ├── sesion04/              # Sesiones 4+: una sola presentación de 4hs
│   │   ├── contenido.md
│   │   ├── scripts/
│   │   ├── graficos/
│   │   ├── img/
│   │   └── presentacion/
│   ├── sesion06-11/           # Esqueletos creados (carpetas vacías)
│   └── sesion12/              # Coloquio
│       └── consignas.md
│
└── archivo/                     # Archivos antiguos (Quarto, PPT, etc.)
```

## Enfoque Pedagógico
- Combina teoría ortodoxa con **visión estructuralista latinoamericana** (Prebisch, CEPAL, Diamand)
- Énfasis en **América Latina y Argentina**
- Temas actuales: guerra comercial EEUU-China, slowbalization, transición energética
- Incluye aspectos de **tipo de cambio real** y política cambiaria

## Pregunta Central del Curso

> **¿Cómo se inserta un país en la economía mundial y qué consecuencias tiene eso para su desarrollo?**

Esta pregunta guía todo el curso y se aborda desde distintas perspectivas en cada unidad:

| Unidad | Sesiones | Perspectiva |
|--------|----------|-------------|
| 1 | S1 | ¿Qué pasó históricamente y cómo lo medimos? |
| 2 | S2-S3 | ¿Por qué los países comercian? (teorías clásicas y neoclásicas) |
| 3 | S4-S5 | ¿Por qué los países comercian? (nuevas teorías del comercio) |
| 4 | S6-S7 | ¿Quién gana y quién pierde? (visión estructuralista) |
| 5 | S8-S9 | ¿Quién organiza el comercio? (ETN, IED, CGV) |
| 6 | S10 | ¿Qué políticas hay? (instrumentos + integración) |
| 7 | S11 | ¿Dónde estamos hoy? (Argentina y transformaciones recientes) |

## Evaluación del Curso

### MC asincrónico en plataforma (7 evaluaciones)
- 5 preguntas MC por unidad (3 conceptuales + 2 con datos reales)
- Se abren al cerrar la unidad, deadline 1 semana
- "Parcial 1" = promedio evals U1-U3
- "Parcial 2" = promedio evals U4-U7
- **Para promocionar**: todas las evaluaciones con 7 o más

| Evaluación | Se abre después de | Deadline |
|------------|---------------------|----------|
| Eval U1 | Sesión 1 (26/03) | 02/04 |
| Eval U2 | Sesión 3 (16/04) | 23/04 |
| Eval U3 | Sesión 5 (30/04) | 07/05 |
| Eval U4 | Sesión 7 (14/05) | 21/05 |
| Eval U5 | Sesión 9 (28/05) | 04/06 |
| Eval U6 | Sesión 10 (04/06) | 11/06 |
| Eval U7 | Sesión 11 (11/06) | 18/06 |

### Coloquio final (Sesión 12 — 18/06)
- Presentaciones **grupales** de casos reales
- Asignar casos en sesión 9 o 10 (dar 2-3 semanas de preparación)
- Evaluativo: aprobado/desaprobado

### Recuperatorio (25/06)
- MC presencial para quienes reprobaron alguna evaluación

## Bibliografía por Unidad

Cada unidad tiene su carpeta en `bibliografia/unidadN/` con un `README.md` que lista lecturas obligatorias, complementarias y referencias del docente. Los PDFs están descargados en la misma carpeta.

### Manuales compartidos (en `bibliografia/`)
- **Krugman, Obstfeld & Melitz (9a ed.)** — Economía Internacional: Teoría y Política [ES]
- **Lugones, G. et al.** — Teorías del Comercio Internacional, UNQ [ES]
- **Porta, F. (comp.)** — Integración Económica: Teoría y Experiencia Latinoamericana, UNQ [ES]

### Lecturas clave por unidad

| Unidad | Clases | Lecturas obligatorias principales | Archivo README |
|--------|--------|----------------------------------|----------------|
| **1** | 1-2 | Krugman caps 1-2, CEPAL 2002 Globalización, Frenkel 2008 TC real | `bibliografia/unidad1/README.md` |
| **2** | 3-6 | Lugones cap 1, Krugman caps 3-5 | `bibliografia/unidad2/README.md` |
| **3** | 7-10 | Lugones cap 2.1, Krugman caps 6-8, Lucángeli 2007 IIT, Bernard et al 2007 | `bibliografia/unidad3/README.md` |
| **4** | 11-13 | Lugones caps 2.2-2.3+5, Prebisch 1950, Diamand 1972, Ocampo 2022, Hausmann et al 2007 | `bibliografia/unidad4/README.md` |
| **5** | 14-16 | Lugones cap 4, Gereffi 2001 cadenas productivas, Durán Lima 2013 CGV AL | `bibliografia/unidad5/README.md` |
| **6** | 17-18 | Lugones cap 3, Krugman caps 9-12, Porta (caps seleccionados), UNCTAD 2021 MNA | `bibliografia/unidad6/README.md` |
| **7** | 19-20 | CEPAL Perspectivas 2025, Rosales 2022 EEUU-China, CEP XXI radiografía, CBAM Argentina | `bibliografia/unidad7/README.md` |

### ⚠️ REGLA: Consultar bibliografía ANTES de preparar cada clase
Al iniciar una clase nueva, **SIEMPRE leer el README.md de la unidad correspondiente** para:
- Usar los marcos conceptuales correctos (no improvisar teoría)
- Citar a los autores que los alumnos están leyendo
- Incluir el slide de "Lecturas" con la bibliografía asignada
- Alinear los contenidos del slide con lo que dice la bibliografía

---

## Plan de 12 Sesiones (4 horas cada una)

### Calendario

| Sesión | Fecha | Unidad | Contenido | Estado |
|--------|-------|--------|-----------|--------|
| **S1** | 26/03 | **U1 completa** | Hechos estilizados + BdP + TC | LISTA (parte1+parte2) |
| — | 02/04 | **FERIADO** | — | — |
| **S2** | 09/04 | **U2 pt1** | Mercantilistas/Smith + Ricardo | LISTA (parte1+parte2) |
| **S3** | 16/04 | **U2 pt2** | Neoclásico estándar + H-O (cierra U2) | LISTA (parte1+parte2) |
| **S4** | 23/04 | **U3 pt1** | Krugman + IIT + GL + NGE | LISTA (30 slides, 4hs) |
| **S5** | 30/04 | **U3 pt2** | IIT profundización + Vernon + Melitz + Dumping (cierra U3) | LISTA (30 slides, 7 gráficos) |
| **S6** | 07/05 | **U4 pt1** | Prebisch + centro-periferia CEPAL | POR ARMAR |
| **S7** | 14/05 | **U4 pt2** | Intercambio desigual + ventajas dinámicas (cierra U4) | POR ARMAR |
| **S8** | 21/05 | **U5 pt1** | Movilidad de factores + ETN/IED + intro CGV | POR ARMAR |
| **S9** | 28/05 | **U5 pt2** | CGV en profundidad + CGV en AL/Argentina (cierra U5) | POR ARMAR |
| **S10** | 04/06 | **U6 completa** | Política comercial + Integración regional (cierra U6) | POR ARMAR |
| **S11** | 11/06 | **U7 completa** | Guerra comercial + transición verde + Argentina (cierra U7) | POR ARMAR |
| **S12** | 18/06 | **Coloquio** | Presentaciones grupales de casos | — |
| — | 25/06 | Recuperatorio | MC presencial | — |
| — | 02/07 | Libre | Consulta / cierre administrativo | — |

### Detalle por sesión

#### UNIDAD 1: Introducción, hechos estilizados, balanza de pagos y tipo de cambio

| Sesión | Contenido |
|--------|-----------|
| **S1** (4hs) | Presentación unificada (70 slides): historia del comercio mundial (5 etapas, marco T-R-P, convergencia/divergencia) + 9 indicadores de economía internacional + hechos estilizados y caso argentino |

#### UNIDAD 2: Teorías clásicas y neoclásicas del comercio internacional

| Sesión | Contenido |
|--------|-----------|
| **S2** (4hs) | Presentación unificada (34 slides): Mercantilistas, Smith (división del trabajo, ventaja absoluta, límites), Ricardo (Corn Laws, costos de oportunidad, ventaja comparativa, PPF, ganancias del comercio), RCA Balassa |
| **S3** (4hs) | **Parte 1**: Modelo neoclásico estándar, curvas de transformación, precios relativos. **Recreo**. **Parte 2**: H-O, Stolper-Samuelson, Rybczynski, paradoja de Leontief. Cierra U2 |

#### UNIDAD 3: Nuevas teorías del comercio, IIT, dumping, firmas heterogéneas

| Sesión | Contenido |
|--------|-----------|
| **S4** (4hs) | Tríada, competencia monopolística, modelo Krugman, IIT, Grubel-Lloyd, IIT H/V, evidencia comparada, caso Mercosur autos, home-market effect, NGE (centrípetas/centrífugas, bifurcación K-1991, Argentina) |
| **S5** (4hs) | Determinantes IIT, caso ARG-BRA profundización, Vernon (ciclo del producto), Melitz (firmas heterogéneas, selección de exportadores), Dumping (discriminación de precios, medidas antidumping, reglas OMC). Cierra U3 |

#### UNIDAD 4: Comercio, estructura productiva y desarrollo (enfoques estructuralistas y dinámicos)

| Sesión | Contenido |
|--------|-----------|
| **S6** (4hs) | Visión estructuralista CEPAL, ISI, tesis deterioro TDI (Prebisch-Singer) |
| **S7** (4hs) | Emmanuel e intercambio desigual, diferencias salariales, learning by doing, capacidades tecnológicas, neoschumpeterianos, path dependence. Cierra U4 |

#### UNIDAD 5: Movilidad de factores, ETN, IED y cadenas globales de valor

| Sesión | Contenido |
|--------|-----------|
| **S8** (4hs) | Movilidad internacional de factores (retoma FPE → capital/IED + trabajo/migración), ETN e IED (motivaciones, modos, efectos), intro CGV (participación, posición, gobernanza, upgrading) |
| **S9** (4hs) | CGV en profundidad + CGV en AL y Argentina (inserción, oportunidades, límites, política productiva y cambiaria). Cierra U5 |

#### UNIDAD 6: Instrumentos de política comercial e integración económica regional

| Sesión | Contenido |
|--------|-----------|
| **S10** (4hs) | Aranceles, protección efectiva, cuotas, subsidios, MNA, antidumping, salvaguardias. Integración: ZLC, UA, MC, UE monetaria, creación/desviación de comercio, Mercosur. Cierra U6 |

#### UNIDAD 7: Transformaciones recientes, geopolítica e inserción argentina

| Sesión | Contenido |
|--------|-----------|
| **S11** (4hs) | Crisis 2008, slowbalization, nearshoring, friend-shoring, guerra comercial EEUU-China. Transición verde, minerales críticos, CBAM. Comercio exterior argentino, restricción externa. Cierra U7 |

---

## Estado de Avance

### Material listo
- [x] **Sesión 1** (U1 completa) — 73 slides unificados, 32 gráficos + 6 imágenes. Presentación continua de 4hs (parte1+parte2 integradas). Incluye: definiciones conceptuales con unidad de medida en los 9 indicadores, slide de Notebook 1, slide de NotebookLM, menciones al notebook en notas docente de indicadores 5-8
- [x] **Sesión 2** (U2 pt1) — 34 slides unificados, 15 gráficos + 2 imágenes. Presentación continua de 4hs (parte1+parte2 integradas)
- [x] **Sesión 3** (U2 pt2) — 43 slides unificados, 14 gráficos. Presentación continua de 4hs (parte1+parte2 integradas)
- [x] **Sesión 4** (U3 pt1) — 30 slides, 13 gráficos + retrato Krugman. Ya era de 4hs
- [x] **Sesión 5** (U3 pt2) — 30 slides, 7 gráficos. Vernon + Melitz + dumping + comercio de tareas (estructura narrativa continua). Cierra U3
- [x] Bibliografía — 7 unidades completas (READMEs + ~42 PDFs descargados)
- [x] Evaluación U1 — 5 MC (3 conceptuales + 2 con datos), Excel de verificación
- [x] Evaluación U2 — 5 MC (3 conceptuales + 2 con datos), caso Granja Tres Arroyos, Excel de verificación
- [x] Sistema de presentaciones HTML, notas docente, KaTeX configurados
- [x] Reorganización de carpetas: `claseNN/` → `sesionNN/` completada

- [x] Notebook 1 — Indicadores de comercio mundial (datos Banco Mundial, Google Colab)

### Por hacer
- [ ] Sesiones 6-11 — Por armar
- [ ] Evaluaciones U3-U7 — Pendientes
- [ ] Consignas del coloquio (sesión 12)
- [ ] Notebook 2 — Comercio intraindustrial / Grubel-Lloyd (para S5)
- [ ] Notebook 3 — Efecto de un arancel / integración (para S10)

---

## Notebooks con Python (ejercicios prácticos con datos)

### Filosofía

Los notebooks son ejercicios **formativos** (sin nota obligatoria) donde los alumnos trabajan con datos reales descargados de fuentes oficiales. **No necesitan saber programar**: la idea es que usen herramientas de IA (ChatGPT, Claude, etc.) para generar el código, y que lo importante sea **formular bien la pregunta** e **interpretar económicamente** los resultados.

### Plataforma

- **Ejecución**: Google Colab (cero instalación, gratis, funciona en celular)
- **Datos**: se descargan en tiempo real desde APIs oficiales (Banco Mundial, etc.), no desde archivos locales
- **Entrega**: los alumnos descargan el .ipynb resuelto y lo suben al campus de la UMET

### Estructura de cada notebook

```
BLOQUE 1 — Contexto (markdown)
  Qué teoría estamos viendo, qué pregunta queremos responder

BLOQUE 2 — Datos (código listo, ejecutable)
  Conexión a API oficial, descarga, vista previa, descripción

BLOQUE 3 — Desarrollo guiado (código + interpretación)
  4-5 celdas con cálculos + gráficos + texto explicativo del docente

BLOQUE 4 — TAREA (celdas vacías + consigna)
  Consigna económica → alumno pide código a la IA → pega → ejecuta → interpreta

BLOQUE 5 — Reflexión
  3 preguntas de interpretación económica que escriben en markdown
```

### Plan de 3 notebooks

| NB | Disponible con | Tema | Fuente de datos | Estado |
|----|---------------|------|-----------------|--------|
| **NB1** | Sesión 1 (U1) | Indicadores de comercio mundial | API Banco Mundial (10 países, 1960-2024) | **LISTO** |
| **NB2** | Sesión 5 (U3) | Comercio intraindustrial (Grubel-Lloyd) | Por definir (COMTRADE o CEPAL) | Pendiente |
| **NB3** | Sesión 10 (U6) | Efecto de un arancel + integración | Datos simulados/estilizados | Pendiente |

### Archivos

| Archivo | Ubicación | Público |
|---------|-----------|---------|
| Notebook para alumnos | `notebooks/NB1_indicadores_comercio_mundial.ipynb` | Sí (GitHub Pages + Colab) |
| Solucionario docente | `docente/NB1_RESUELTO_indicadores_comercio_mundial.ipynb` | **NO** (en .gitignore) |
| Subpágina de instrucciones | `notebooks.html` | Sí (GitHub Pages) |

### Solucionarios docentes (carpeta `docente/`)

La carpeta `docente/` está en `.gitignore` y **nunca se sube a GitHub**. Contiene las versiones resueltas de los notebooks con:
- Código completo de todas las tareas
- Interpretaciones modelo (respuestas esperadas)
- Rúbrica de corrección (10 puntos, criterios por tarea)
- Tiempo estimado de corrección: 3-5 minutos por alumno

### Subpáginas web del curso

| Página | URL | Contenido |
|--------|-----|-----------|
| Landing page | `index.html` | Portal principal con sesiones, bibliografía, herramientas, evaluaciones, programa |
| Notebooks | `notebooks.html` | Qué son, cómo funcionan (8 pasos), FAQ, cards por notebook |
| Asistente IA | `asistente-ia.html` | NotebookLM con bibliografía del curso, ejemplos de preguntas, tips |
| Bibliografía raíz | `bibliografia/index.html` | Manuales compartidos + links a las 7 unidades |
| Bibliografía unidad N | `bibliografia/unidadN/index.html` | PDFs descargables de cada unidad |

---

## Repositorio Git y Publicación Web

### Repositorio

El proyecto tiene su propio repositorio git local, independiente de cualquier otro repo.

- **Ruta local**: `C:\Users\gbrea\OneDrive\Documentos\UMET\Economia Intenacional\.git`
- **Remote**: `https://github.com/gbreard/economia-internacional`
- **Repo público**: sí (necesario para GitHub Pages gratuito)

#### Branches

| Branch | Propósito | Estado |
|--------|-----------|--------|
| `master` | Snapshot base del proyecto al crear el repo | Estable, no se trabaja directamente acá |
| `publicacion-web` | Branch activo de trabajo, sirve GitHub Pages | **Branch por defecto para desarrollo** |

#### .gitignore

Excluye: `__pycache__/`, `*.pyc`, temporales de Office (`~$*`), `nul`, `.claude/`, archivos de IDE (`.vscode/`, `.idea/`)

Se incluyen todos los archivos del proyecto: PDFs de bibliografía, Excel de datos, PNGs, HTML, scripts.

#### Commit inicial

```
ba2213f feat: commit inicial - Economia Internacional UMET
         684 archivos, 264 MB total
         - 55 PDFs (125.7 MB), 342 PNGs (61.7 MB), 19 XLSX (7.4 MB)
         - 18 HTML, 60 scripts Python, 29 Markdown
```

### GitHub Pages

- **URL del sitio**: https://gbreard.github.io/economia-internacional/
- **Source**: branch `publicacion-web`, carpeta `/` (raíz)
- **Deploy**: automático con cada `git push origin publicacion-web`
- **Tiempo de build**: ~30 segundos

#### Landing page (`index.html`)

Portal de acceso para alumnos con:
- Cards para cada sesión (se habilitan progresivamente antes de cada clase)
- Sección de bibliografía con links a manuales principales y carpetas por unidad
- Tabla de evaluaciones con fechas de disponibilidad y deadline (links se agregan al liberar)
- Links al programa: Programa de la Asignatura (.docx), Clases del programa (.docx) y Plan de clases (.pdf)
- Responsive (se adapta a celulares)

**Estrategia de liberación progresiva**: solo se publica la sesión que corresponde a la clase siguiente. Las demás aparecen como "Próximamente" aunque el material ya esté listo. Esto se controla editando el `index.html` antes de cada clase (ver instrucciones abajo).

**⚠️ REGLA DE PUSH: Las presentaciones que incluyen quiz de lecturas (preguntas + respuestas al inicio) NO se pushean a GitHub hasta DESPUÉS de la fecha de la clase.** Si se pushean antes, los alumnos pueden ver las respuestas en el repo público. Workflow:
1. Commitear localmente (`git commit`) — OK
2. **NO pushear** (`git push`) hasta después de la clase
3. Una vez dada la clase, pushear y habilitar en `index.html`

#### URLs de acceso para alumnos

| Recurso | URL |
|---------|-----|
| Portal del curso | `https://gbreard.github.io/economia-internacional/` |
| Sesión N (presentación) | `.../Clases/sesionNN/presentacion/index.html` |
| Bibliografía unidad N | `.../bibliografia/unidadN/` |
| PDF específico | `.../bibliografia/unidadN/nombre_archivo.pdf` |
| Excel de evaluación | `.../evaluacion/datos/UN_PM_nombre.xlsx` |

#### Límites de GitHub Pages (plan gratuito)

| Concepto | Límite | Estado del proyecto |
|----------|--------|---------------------|
| Tamaño del sitio publicado | 1 GB | ~264 MB (26% usado) |
| Ancho de banda mensual | 100 GB/mes | Muy por debajo |
| Tamaño máximo por archivo | 100 MB (50 MB warning) | Max 17.2 MB (CEPAL Perspectivas) |
| Builds por hora | 10 | Más que suficiente |

#### Workflow de publicación

```
1. Trabajar en el branch publicacion-web
2. Hacer cambios (nueva sesión, actualizar material, etc.)
3. git add . && git commit -m "descripción del cambio"
4. git push origin publicacion-web
5. El sitio se actualiza automáticamente en ~30 segundos
6. Verificar en https://gbreard.github.io/economia-internacional/
```

#### Actualizar landing page al agregar sesiones nuevas

Cuando se complete una sesión nueva (ej: S6), actualizar `index.html`:
1. Buscar el `<div class="session-card disabled">` de la sesión correspondiente
2. Quitar la clase `disabled`
3. Reemplazar `<span class="tag pending">Proximamente</span>` por el link y tag de slides:
   ```html
   <a href="Clases/sesion06/presentacion/index.html">Ver presentacion &rarr;</a>
   <span class="tag">N slides</span>
   ```
4. Commit + push

#### Nota sobre copyright de bibliografía

Los PDFs están publicados en un repo **público**. Material de organismos internacionales (CEPAL, UNCTAD, OMC) y working papers académicos generalmente permiten distribución libre. Los libros editoriales (Krugman) están en zona gris — muchas cátedras los distribuyen así pero técnicamente hay riesgo de copyright. Si fuera necesario, se pueden excluir los PDFs editoriales del repo y distribuirlos por la plataforma de la UMET o Google Drive privado.

---

## FLUJO DE TRABAJO POR SESIÓN

### Workflow completo

```
0. BIBLIOGRAFÍA DE LA UNIDAD
   └── Leer bibliografia/unidadN/README.md (N = unidad de la sesión)
   └── Identificar lecturas obligatorias y complementarias asignadas
   └── Usar como marco conceptual para los contenidos
   └── El slide de "Lecturas" debe listar la bibliografía del README

1. WORD → contenido.md
   └── Usuario trae contenido en Word (Clase X.docx)
   └── Extraer a contenido.md: slides, tipos, contenido, notas docente
   └── contenido.md es la ÚNICA FUENTE DE VERDAD (no JSON)

2. INVESTIGACIÓN Y DATOS
   └── Definir gráficos necesarios (web search, discusión con usuario)
   └── Buscar datos: Banco Mundial API, Our World in Data, Maddison, FRED, UNCTAD, OMC
   └── Cuando no hay API: hardcodear de fuentes confiables. NUNCA inventar datos

3. GRÁFICOS (scripts Python en scripts/)
   └── Un script por bloque temático
   └── Paleta: #1F4E79, #2E75B6, #0EA5E9, #E8833A, #27AE60, #E74C3C
   └── 150 dpi, fondo blanco, bbox_inches='tight', etiquetas en español
   └── sys.stdout con encoding UTF-8 (Windows)
   └── Guardar PNGs en graficos/

4. INTEGRACIÓN EN contenido.md
   └── Slides con gráficos: tipo grafico_texto + bullets + notas docente
   └── Integrar narrativamente: secciones, transiciones, agenda, resumen
   └── Renumerar slides, actualizar tabla de recursos, "Para hacer"

5. generar_desde_md.py → HTML
   └── Copiar de sesión anterior, cambiar footer ("Clase N")
   └── Ejecutar: cd scripts/ && python generar_desde_md.py
   └── Genera presentacion/index.html
   └── Ctrl+F5 en navegador (cache)

6. EVALUACIÓN (al terminar la unidad)
   └── 5 preguntas MC: 3 conceptuales + 2 con procesamiento de datos
   └── Descargar datos reales → procesar → verificar respuestas → Excel
   └── Ver sección "Evaluaciones por Unidad" más abajo
```

### Estructura de carpetas

```
# Sesión 1 (integrada): presentación unificada de 4hs
Clases/sesion01/                   # ⚠️ "Clases" con C mayúscula
├── contenido.md           # FUENTE DE VERDAD (70 slides)
├── scripts/generar_desde_md.py
├── graficos/              # 32 PNGs (unificados de parte1+parte2)
├── img/                   # 6 imágenes históricas
├── presentacion/index.html
├── parte1/                # Archivo (originales, no se usan)
└── parte2/                # Archivo (originales, no se usan)

# Sesión 2 (integrada): presentación unificada de 4hs
Clases/sesion02/                   # ⚠️ "Clases" con C mayúscula
├── contenido.md           # FUENTE DE VERDAD (34 slides)
├── scripts/generar_desde_md.py
├── graficos/              # 15 PNGs (unificados de parte1+parte2)
├── img/                   # 2 imágenes (wealth_of_nations, ricardo_portrait)
├── presentacion/index.html
├── parte1/                # Archivo (originales, no se usan)
└── parte2/                # Archivo (originales, no se usan)

# Sesión 3 (integrada): presentación unificada de 4hs
Clases/sesion03/                   # ⚠️ "Clases" con C mayúscula
├── contenido.md           # FUENTE DE VERDAD (43 slides)
├── scripts/generar_desde_md.py
├── graficos/              # 14 PNGs (unificados de parte1+parte2)
├── presentacion/index.html
├── parte1/                # Archivo (originales, no se usan)
└── parte2/                # Archivo (originales, no se usan)

# Sesiones 4+ (material nuevo): una sola presentación de 4hs
Clases/sesionNN/
├── contenido.md           # FUENTE DE VERDAD
├── datos/
├── scripts/
│   ├── generar_desde_md.py
│   └── generar_graficos_*.py
├── graficos/
├── img/
└── presentacion/index.html
```

### Formato del contenido.md (formato validado)

```markdown
# Clase N: Título

## Metadata
- **Duración**: 2 horas
- **Pregunta central**: ...

## Estado
Borrador | En revisión | Listo

## Para hacer
- [ ] Tarea pendiente
- [x] Tarea completada

---

## Contenido

### Sección: Nombre del bloque

#### Slide 1: Portada
**Tipo**: portada
**Título**: Economía Internacional — Clase N
**Subtítulo**: Subtítulo de la clase

**Notas docente**:
APERTURA (3 minutos)
Texto de las notas...

---

#### Slide 2: Nombre del slide
**Tipo**: texto | formula | grafico_texto | seccion | centrado | agenda | cierre
**Título**: Título del slide
**Subtítulo**: (opcional)

**Contenido**:
- Bullet 1
- Bullet 2

**Gráfico**: graficos/nombre.png        (solo para grafico_texto)
**Imagen**: img/nombre.png              (solo para imágenes estáticas)
**Fuente**: Nombre de la fuente

**Notas docente**:
NOMBRE DEL TEMA (X minutos)
Texto expandido de las notas...

---

## Recursos

### Gráficos necesarios
| Archivo | Descripción | Estado |
|---------|-------------|--------|
| nombre.png | Descripción | ✓ Existe / Pendiente |

---

## Notas de investigación
...
```

### CAMPOS IMPORTANTES del formato
- `#### Slide N:` — SIEMPRE numerar secuencialmente
- `**Tipo**:` — define el renderizado del slide
- `**Contenido**:` — cada bullet con `- ` (espacio después del guión)
- `**Gráfico**:` o `**Imagen**:` — ruta relativa desde la carpeta de la clase
- `**Notas docente**:` — texto libre después de este campo (sin code blocks)
- `---` — separador entre slides (OBLIGATORIO)

### generar_desde_md.py — El generador HTML

- **Ubicación**: `Clases/sesionNN/scripts/generar_desde_md.py` (o `parte1/scripts/` / `parte2/scripts/` en S1-S3)
- **Origen**: copiar de la sesión anterior y cambiar solo el footer
- **Cambios necesarios**: buscar "Sesión N" en el script (aparece en `<title>` y en `<span>` del footer)
- **Ejecutar**: `cd Clases/sesionNN/scripts/ && python generar_desde_md.py`
- **Resultado**: genera `presentacion/index.html`
- **El parser acepta notas docente con o sin ``` code blocks** (strips ```)

### Controles de la presentación HTML

| Tecla | Acción |
|-------|--------|
| `→` `Space` `Enter` | Siguiente slide |
| `←` | Slide anterior |
| `F` | Fullscreen |
| `P` | Modo impresión (ver todos) |
| `Ctrl+P` | Guardar como PDF (en modo P) |
| `Home` / `End` | Primera / última |

### Tipos de slides disponibles

| Tipo | Uso | Renderer |
|------|-----|----------|
| `portada` | Título de la clase | Centrado, UMET 2026 |
| `seccion` | División de bloque | Fondo azul #1F4E79 |
| `centrado` | Preguntas, definiciones | Centrado con bullets |
| `texto` | Explicación conceptual | Bullets izquierda |
| `formula` | Indicadores, ecuaciones | Igual que texto |
| `agenda` | Índice de la clase | Bullets grandes |
| `grafico_texto` | Gráfico + explicación | 65% imagen / 35% texto |
| `cierre` | Slide final | Centrado grande |

### Paleta de colores (presentaciones y gráficos)

| Uso | Color | Hex |
|-----|-------|-----|
| Principal / headers | Azul oscuro | `#1F4E79` |
| Líneas secundarias | Azul medio | `#2E75B6` |
| Acento / highlight | Azul celeste | `#0EA5E9` |
| Alerta / contraste | Naranja | `#E8833A` |
| Positivo | Verde | `#27AE60` |
| Negativo / crisis | Rojo | `#E74C3C` |
| Texto principal | Casi negro | `#111827` |
| Texto secundario | Gris | `#4B5563` |

---

## Datos disponibles para análisis

| Fuente | Período | Temas | Acceso |
|--------|---------|-------|--------|
| FTWTHD (datos_compartidos/) | 1800-1938 | Comercio histórico por país/región | Excel local |
| Maddison Project Database | 1000-2018 | PIB per cápita por país/región | Excel local |
| Banco Mundial (API) | 1960-2023 | Comercio/PIB, IED, CC, apertura, BC | `api.worldbank.org/v2/country/{ISO}/indicator/{ID}?format=json` |
| Our World in Data | Varios | Costos transporte, comercio, desarrollo | CSV descargable |
| FRED (Fed St. Louis) | Varios | Reservas de oro EEUU, series monetarias | API o hardcoded |
| UNCTAD | 1970-2023 | IED global, comercio de servicios | Reportes/hardcoded |
| OMC | 1948-2023 | Exportaciones mundiales, rondas GATT | Reportes/hardcoded |
| INDEC | Varios | Comercio exterior, BP, IPC Argentina | indec.gob.ar |
| BCRA | Varios | TCR (ITCRM), reservas, tipo de cambio | bcra.gob.ar |

### Indicadores del Banco Mundial usados

| Código | Indicador | Usado en |
|--------|-----------|----------|
| NE.TRD.GNFS.ZS | Trade (% of GDP) — apertura comercial | Clase 2, Eval U1 P4 |
| BN.CAB.XOKA.GD.ZS | Current account balance (% of GDP) | Clase 2, Eval U1 P5 |
| NE.RSB.GNFS.ZS | External balance on goods and services (% GDP) | Clase 2 |

---

## Notas para Claude (Agente)

### Qué SÍ hacer
- **SIEMPRE leer `bibliografia/unidadN/README.md` ANTES de preparar una clase** — consultar lecturas asignadas, autores clave, marcos conceptuales
- **SIEMPRE leer contenido.md ANTES de editar** — verificar estado actual, no asumir
- **SIEMPRE consultar al usuario ANTES de armar slides** — mostrar agenda del Word, discutir contenido, recién después construir
- Trabajar iterativamente: contenido primero, HTML después
- Usar datos reales (nunca inventar)
- Mantener equilibrio teoría ortodoxa + estructuralismo
- Incluir ejemplos de Argentina/Latam
- Preguntar cuando haya dudas
- **Verificar flujo conceptual**: cada concepto/valor debe estar explicado ANTES de usarse en un ejemplo
- **Revisar PNGs después de generar**: leer cada imagen y verificar que no hay textos superpuestos
- **Incluir en cada clase**: slide de biografía del autor principal, slide de material complementario (documentales/películas), slide de lecturas

### Qué NO hacer
- Generar HTML desde JSON (usar SOLO generar_desde_md.py)
- Insertar slides sin integrarlos narrativamente
- Modificar CSS de los templates
- Asumir el estado del archivo sin leerlo
- Inventar datos o estadísticas
- **Construir toda la clase sin consultarlo con el usuario** — no presentar hechos consumados
- **Usar un concepto antes de explicarlo** — verificar orden lógico de los slides
- **Olvidar slides recurrentes** — cada clase DEBE tener: Material Complementario, Lecturas, Próxima clase, Preguntas
- **Usar `clases/` en minúscula** — la carpeta real es `Clases/` con C mayúscula. Carpetas son `sesionNN/` (no `claseNN/`)
- **Preparar una clase sin consultar la bibliografía de la unidad** — SIEMPRE leer `bibliografia/unidadN/README.md` primero

### Checklist post-inserción de slides

Cada vez que se agregan slides nuevos a contenido.md:
```
- [ ] Slides renumerados secuencialmente
- [ ] Sección (### Sección:) creada si es bloque temático nuevo
- [ ] Transición en notas del slide anterior ("Ahora vamos a ver...")
- [ ] Transición en notas del último slide nuevo ("Pasemos a...")
- [ ] Agenda actualizada con nuevo punto
- [ ] Resumen/cierre actualizado
- [ ] Tabla de recursos actualizada
- [ ] "Para hacer" actualizado
- [ ] HTML regenerado con generar_desde_md.py
- [ ] Verificado en navegador (Ctrl+F5)
```

### Lecciones de Clase 4 (reutilizables)

#### Solapamiento en gráficos matplotlib
Los textos en matplotlib se posicionan con coordenadas absolutas. Si hay muchos elementos, se superponen. **Después de generar cada PNG, leerlo y verificar visualmente.** Problemas comunes y soluciones:

| Problema | Solución |
|----------|----------|
| Anotación sobre borde de caja | Mover coordenadas (x,y) alejándose del borde |
| Etiqueta de extremo sobre línea de datos | Mover fuera del área de datos o usar `ha='center'` con offset |
| Textos en dos niveles superpuestos (ej: subtítulo + label) | Separar en eje Y (subir uno, bajar otro) o reducir fontsize |
| Muchas cajas en fila que se tocan | Aumentar figsize, box_w, gap; o reducir fontsize |
| Texto cortado al borde de la figura | Ampliar xlim/ylim |

#### Slides tipo recurrentes (incluir en cada clase)
1. **Biografía del autor principal**: tipo `grafico_texto`, retrato en `img/`, layout portrait (33% imagen). Bullets: fechas, origen, obra principal, contexto histórico, cita memorable
2. **Material complementario**: tipo `texto`, 4-5 recomendaciones con emoji 🎬/📺. Documentales, videos de YouTube, películas. Incluir link si es accesible
3. **Lecturas**: tipo `texto`, bibliografía obligatoria y complementaria del programa

#### Soporte KaTeX en generar_desde_md.py
- Fórmulas entre `$...$` se renderizan con KaTeX (CDN en el HTML)
- Usar en slides tipo `formula` para ecuaciones (PPF, indicadores, modelos)
- Funciona tanto en contenido principal como en bullets

#### format_md() para markdown en bullets
- La función `format_md()` convierte `**bold**` y `*italic*` a `<strong>`/`<em>` en el HTML

### Lecciones de Clase 5 (reutilizables)

#### ⚠️ Ruta de carpetas: `Clases/` con C MAYÚSCULA
- La carpeta real en disco es `Clases/` (mayúscula), no `clases/` (minúscula)
- Glob y Read fallan silenciosamente si se usa la ruta incorrecta
- **SIEMPRE usar**: `Clases/sesionNN/` — "Clases" con C mayúscula, "sesionNN" en minúscula
- Para sesiones 1-3: `Clases/sesionNN/parte1/` y `Clases/sesionNN/parte2/`

#### Material complementario es OBLIGATORIO en cada clase
- El usuario espera que CADA clase tenga un slide de Material Complementario (documentales, videos, películas)
- No olvidarlo — es un slide tipo recurrente como Biografía y Lecturas
- Checklist de slides recurrentes por clase:
  1. **Portada** (siempre slide 1)
  2. **Agenda** (siempre slide 2 o 3)
  3. **Biografía** del autor principal (si aplica)
  4. **Material complementario** (4-5 recomendaciones con 🎬/📺) — **NO OLVIDAR**
  5. **Lecturas** (bibliografía obligatoria y complementaria)
  6. **Próxima clase** (anticipar siguiente tema)
  7. **Preguntas** (cierre)

#### Fallback cuando no se encuentra retrato/imagen
- Si no se encuentra una imagen (ej: retrato de un economista), NO dejar el slide roto
- Solución: cambiar el tipo del slide de `grafico_texto` a `texto`
- Eliminar las líneas `**Imagen**:` y `**Fuente**:` del contenido.md
- El contenido biográfico se mantiene como bullets de texto sin imagen

#### Gráficos tipo tabla con matplotlib (patches)
- Los headers de tabla se posicionan ARRIBA de las filas de datos
- Fórmula correcta: `header_y = y_start + row_h + offset` (NO `y_start + offset`)
- Usar `zorder=5` para patches de header y `zorder=6` para texto de header
- Si headers quedan ocultos: están debajo de las filas de datos por z-order

#### Verificación de gráficos en dos pasadas
- **Pasada 1**: Generar todos los PNGs → leer cada uno visualmente → anotar problemas
- **Pasada 2**: Corregir todos los problemas en batch → regenerar → verificar
- Problemas típicos encontrados en Clase 5:
  - Flechas de anotación fuera del área visible (ampliar xlim/ylim)
  - Labels superpuestos en ejes Y (usar annotate con xytext en vez de text)
  - Puntos de equilibrio demasiado al borde (mover índices hacia el centro de la curva)
  - Textos de export/import fuera del plot (calcular mid-points dentro del área)
- Ya está incluida en generar_desde_md.py desde Clase 4
- Se aplica en: bullets de slides, contenido de agenda, fórmulas

#### Layout de grafico_texto
- Imágenes en `img/` (retratos, fotos): **33% imagen / resto texto** (portrait layout)
- Gráficos en `graficos/` (charts matplotlib): **62% imagen / resto texto**
- Detección automática por path (`'img/' in visual`)

#### Flujo conceptual — regla de precedencia
Antes de numerar slides definitivamente, verificar:
- ¿El slide N usa un concepto/valor que se explica en slide N+k? → Invertir orden
- Ejemplo: no usar P=1.6 en un ejemplo antes de explicar qué es el precio mundial y de dónde sale (rango de autarquías)

---

## Evaluaciones por Unidad

### Estructura

```
evaluacion/
├── evaluacion_unidad1.md           # Preguntas MC + respuestas + justificaciones
├── evaluacion_unidad2.md           # (una por unidad, 7 en total)
└── datos/
    ├── U1_P4_apertura_comercial.xlsx   # Excel verificación pregunta 4
    ├── U1_P5_cuenta_corriente.xlsx     # Excel verificación pregunta 5
    └── generar_U1_P4.py               # Script que genera el Excel
```

### Convenciones de nombres
- Evaluaciones: `evaluacion_unidadN.md`
- Excel de datos: `U{N}_P{M}_nombre_descriptivo.xlsx` (N = unidad, M = número de pregunta)
- Scripts: `generar_U{N}_P{M}.py`

### Formato de cada evaluación
- **5 preguntas multiple choice** por unidad
- **3 conceptuales**: cubren temas de las clases de la unidad
- **2 con procesamiento de datos**: requieren descargar datos de fuentes reales y procesar
  - Incluyen instrucciones paso a paso para navegar el portal de datos (ej: Banco Mundial)
  - Las opciones combinan el **resultado numérico** + la **explicación del dato**
  - Así puede estar bien el número pero mal la interpretación (o viceversa)
  - Es imposible responder correctamente sin haber procesado los datos
- Cada pregunta tiene: enunciado, opciones, respuesta correcta y justificación detallada

### Excel de verificación (para el docente)
Cada Excel tiene 3 hojas:
1. **Datos**: serie completa descargada, con formato condicional
2. **Cálculos**: promedios, conteos, diferencias — lo que el alumno debe calcular
3. **Gráfico**: visualización de los datos con las respuestas marcadas

### Workflow para crear una evaluación

```
1. Revisar contenido.md de TODAS las clases de la unidad
2. Diseñar 3 preguntas conceptuales (temas clave, debates, conexiones)
3. Diseñar 2 preguntas con datos:
   a. Elegir indicadores relevantes de la unidad
   b. Descargar datos reales (Banco Mundial API u otra fuente)
   c. Procesar los datos para verificar las respuestas
   d. Diseñar opciones que combinen dato + explicación
   e. Generar Excel de verificación (script Python → .xlsx)
4. Escribir instrucciones de descarga paso a paso (links, filtros, formato)
5. Guardar en evaluacion/evaluacion_unidadN.md
6. Guardar Excel en evaluacion/datos/U{N}_P{M}_nombre.xlsx
```

---

## Notas del Docente - Formato Expandido

### Filosofía
Las notas del docente NO son un resumen del slide. Son un **guión de clase** que ayuda al docente a:
- Explicar el concepto con profundidad
- Dar ejemplos concretos y actuales
- Generar participación de los estudiantes
- Conectar con otros temas del curso
- Manejar el tiempo de clase

### Estructura de una Nota Docente

Cada nota debe incluir (según aplique al tipo de slide):

```
1. TIEMPO SUGERIDO
   - Cuántos minutos dedicar al slide
   - Ejemplo: "(10 minutos)"

2. EXPLICACIÓN EXTENDIDA
   - Desarrollo conceptual más allá de los bullets
   - Contexto que no entra en el slide
   - Sutilezas y matices

3. EJEMPLOS CONCRETOS
   - Ejemplos numéricos para hacer en pizarrón
   - Casos de la actualidad argentina/mundial
   - Analogías para facilitar comprensión

4. PREGUNTAS PARA ESTUDIANTES
   - Preguntas disparadoras para debate
   - Respuestas sugeridas entre paréntesis
   - Preguntas retóricas para generar reflexión

5. CONFUSIONES COMUNES
   - Errores típicos de interpretación
   - Aclaraciones sobre qué NO dice el concepto
   - "Ojo con..." / "Cuidado con..."

6. DATOS ADICIONALES
   - Estadísticas que no entran en el slide
   - Fuentes para ampliar
   - Referencias históricas

7. CONEXIONES
   - Con otros slides de la misma clase
   - Con clases anteriores o posteriores
   - Con la bibliografía del curso
```

### Longitud Esperada
- **Mínimo**: 300 caracteres (slides simples: transición, cierre)
- **Promedio**: 800-1200 caracteres (slides de contenido)
- **Máximo**: 1500+ caracteres (conceptos clave, casos de estudio)

### Plantillas por Tipo de Slide

#### Para slides de FÓRMULA/INDICADOR:
```
INDICADOR X: [NOMBRE] ([tiempo] minutos)

CONCEPTO CLAVE: [explicar qué mide y por qué importa]

FÓRMULA EXPLICADA:
[desglosar cada componente de la fórmula]

EJEMPLO NUMÉRICO EN PIZARRÓN:
[caso concreto con números para calcular en clase]

INTERPRETACIÓN:
- Si el indicador sube → [qué significa]
- Si el indicador baja → [qué significa]

DATOS PARA COMPARAR:
- País A: X%
- País B: Y%
- Argentina: Z%

PREGUNTA PARA ESTUDIANTES: "[pregunta]"
RESPUESTA: [respuesta sugerida]

CONFUSIÓN COMÚN: "[error típico]"
ACLARACIÓN: [corrección]

CONEXIÓN: [relacionar con otros temas del curso]
```

#### Para slides de GRÁFICO:
```
LECTURA DEL GRÁFICO ([tiempo] minutos)

GUÍA PARA LEER:
- Eje Y: [qué mide]
- Eje X: [período]
- Identificar: [qué buscar]

DATOS CLAVE PARA MENCIONAR:
- Año X: valor Y (contexto)
- Año X: valor Y (contexto)
- Punto de quiebre: [explicar]

PREGUNTAS PARA DISCUSIÓN:
1. "[pregunta sobre el gráfico]"
   RESPUESTA: [explicación]

2. "[pregunta de análisis]"
   RESPUESTA: [explicación]

FUENTE: [explicar brevemente la fuente y su confiabilidad]

CONEXIÓN ACTUAL: [relacionar con situación presente]
```

#### Para slides de CASO/HISTORIA:
```
[NOMBRE DEL CASO] ([tiempo] minutos)

CONTEXTO HISTÓRICO:
- [fecha]: [evento]
- [fecha]: [evento]

EXPLICACIÓN:
[desarrollo del caso con más detalle que el slide]

DATOS QUE IMPACTAN:
- [dato concreto]
- [dato concreto]

ANÉCDOTA/CITA:
"[cita relevante]" - [autor]

LECCIÓN CLAVE:
"[frase resumen que pueden recordar]"

PREGUNTA CONTRAFACTUAL:
"¿Qué hubiera pasado si...?"
RESPUESTA: [análisis]

CONEXIÓN CON ARGENTINA:
[paralelo con caso local]
```

#### Para slides de TRANSICIÓN/SECCIÓN:
```
TRANSICIÓN ([tiempo] minutos)

RECAPITULACIÓN:
- Lo que ya vimos: [resumen]
- Lo que viene: [anticipar]

CONEXIÓN:
[explicar cómo se relaciona lo anterior con lo siguiente]

PREGUNTA PUENTE:
"[pregunta que conecta los temas]"
```

### Ejemplo Completo

**Slide**: Indicador 8: Cuenta corriente (% PIB)

**Notas docente**:
```
INDICADOR 8: CUENTA CORRIENTE (12 minutos)

FÓRMULA COMPLETA:
CC = (X - M) + Rentas + Transferencias
Expresada como % del PIB: CC/PIB × 100

INTERPRETACIÓN:
- CC > 0: SUPERÁVIT → El país produce más de lo que consume
  → Ahorra más de lo que invierte → PRESTA al resto del mundo
- CC < 0: DÉFICIT → El país consume más de lo que produce
  → Invierte más de lo que ahorra → Se ENDEUDA con el mundo

¿DÉFICIT ES MALO? ¡DEPENDE!

DÉFICIT "BUENO":
- Si financia INVERSIÓN productiva
- Ejemplo: Chile en los 90s tenía déficit pero invertía en minería

DÉFICIT "MALO":
- Si financia CONSUMO
- Ejemplo: Argentina en los 90s tenía déficit y no invertía

LA IDENTIDAD FUNDAMENTAL:
CC = S - I (Ahorro nacional menos Inversión nacional)

DATOS PARA COMPARAR:
- EEUU: -3% del PIB (déficit persistente)
- Alemania: +7% del PIB (superávit persistente)
- China: +2% del PIB (superávit moderado)
- Argentina: oscila entre +5% y -5% dependiendo del ciclo

PREGUNTA: "¿Por qué EEUU puede tener déficit persistente sin crisis?"
(Respuesta: privilegio del dólar - ver slide siguiente)

CONEXIÓN: Esta es LA variable clave de macroeconomía abierta.
Un déficit persistente financiando consumo es insostenible.
```

---

## Checklist de Calidad para Notas Docente

Antes de dar por terminadas las notas de una clase, verificar:

- [ ] Cada slide tiene notas de al menos 300 caracteres
- [ ] Los slides de indicadores tienen ejemplo numérico
- [ ] Los slides de gráficos tienen guía de lectura
- [ ] Hay al menos 5 preguntas para estudiantes en toda la clase
- [ ] Se mencionan conexiones con otras clases
- [ ] Hay ejemplos de Argentina/Latinoamérica
- [ ] Los tiempos sugeridos suman aproximadamente la duración de la clase
- [ ] Las notas usan lenguaje coloquial (como hablaría el docente)

