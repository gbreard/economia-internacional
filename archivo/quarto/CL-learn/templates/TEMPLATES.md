# Sistema de Templates para Slides UMET

## Instrucciones para Claude Code

Cada slide es un archivo HTML independiente o una sección dentro de un HTML único.
**NUNCA modifiques el CSS**. Solo reemplazá el contenido marcado con `<!-- CONTENIDO -->`.

Los templates están probados en fullscreen 1920x1080 y 1600x900.

---

## Variables de estilo (ya incluidas en cada template)

```css
--primary: #1F4E79;
--secondary: #0EA5E9;
--text-dark: #111827;
--text-muted: #4B5563;
--white: #FFFFFF;
--bg-light: #F3F4F6;
```

---

## TEMPLATE 1: Sección (fondo azul, título centrado)

Uso: `# Apertura {.section}` equivalente

```html
<section class="slide slide-section">
  <style>
    .slide-section {
      width: 100vw;
      height: 100vh;
      background-color: #1F4E79;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    .slide-section h1 {
      color: #FFFFFF;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      font-size: 4.5rem;
      font-weight: 600;
      text-align: center;
      margin: 0;
      padding: 0 60px;
    }
  </style>
  
  <!-- CONTENIDO: Solo cambiar el texto del h1 -->
  <h1>Apertura</h1>
</section>
```

---

## TEMPLATE 2: Texto centrado (definiciones, fórmulas, preguntas)

Uso: Slides con poco contenido que debe estar centrado

```html
<section class="slide slide-center">
  <style>
    .slide-center {
      width: 100vw;
      height: 100vh;
      background-color: #FFFFFF;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: 0;
      padding: 60px 80px;
      box-sizing: border-box;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }
    .slide-center h2 {
      color: #1F4E79;
      font-size: 2.2rem;
      font-weight: 600;
      margin: 0 0 30px 0;
      text-align: center;
    }
    .slide-center .pregunta {
      color: #1F4E79;
      font-size: 1.9rem;
      font-weight: 600;
      text-align: center;
      max-width: 90%;
      line-height: 1.4;
      margin-bottom: 40px;
    }
    .slide-center .contenido {
      color: #111827;
      font-size: 1.3rem;
      text-align: center;
      max-width: 80%;
    }
    .slide-center .contenido ol {
      display: inline-block;
      text-align: left;
      margin: 20px 0;
      padding-left: 1.5em;
    }
    .slide-center .contenido li {
      margin-bottom: 12px;
      line-height: 1.5;
    }
    .slide-center .formula {
      font-size: 1.8rem;
      margin: 30px 0;
      color: #111827;
    }
  </style>
  
  <!-- CONTENIDO -->
  <h2>Pregunta central de la clase</h2>
  
  <div class="pregunta">
    ¿Por qué el comercio mundial creció 40 veces entre 1800 y 1913, y luego colapsó en apenas 30 años?
  </div>
  
  <div class="contenido">
    Esta pregunta organiza todo lo que veremos hoy:
    <ol>
      <li>Medir ese crecimiento y colapso con datos</li>
      <li>Explicar qué fuerzas lo causaron</li>
      <li>Conectar historia con números</li>
    </ol>
  </div>
</section>
```

---

## TEMPLATE 3: Gráfico Python + Texto (65/35)

Uso: Slides con visualización de datos a la izquierda, explicación a la derecha

```html
<section class="slide slide-graph">
  <style>
    .slide-graph {
      width: 100vw;
      height: 100vh;
      background-color: #FFFFFF;
      display: flex;
      flex-direction: column;
      margin: 0;
      padding: 25px 40px 20px 40px;
      box-sizing: border-box;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }
    .slide-graph h2 {
      color: #1F4E79;
      font-size: 1.7rem;
      font-weight: 600;
      margin: 0 0 15px 0;
      flex-shrink: 0;
    }
    .slide-graph .columns {
      display: flex;
      flex-grow: 1;
      gap: 30px;
      min-height: 0;
    }
    .slide-graph .col-graph {
      flex: 0 0 64%;
      display: flex;
      flex-direction: column;
      min-height: 0;
    }
    .slide-graph .col-graph img {
      max-width: 100%;
      max-height: calc(100vh - 160px);
      object-fit: contain;
      flex-grow: 1;
      min-height: 0;
    }
    .slide-graph .col-graph .fuente {
      font-size: 0.75rem;
      color: #4B5563;
      font-style: italic;
      text-align: center;
      margin-top: 8px;
      flex-shrink: 0;
    }
    .slide-graph .col-text {
      flex: 0 0 34%;
      padding-top: 10px;
    }
    .slide-graph .col-text h3 {
      color: #1F4E79;
      font-size: 1.05rem;
      font-weight: 600;
      margin: 0 0 10px 0;
    }
    .slide-graph .col-text p {
      font-size: 0.92rem;
      color: #111827;
      line-height: 1.45;
      margin: 0 0 12px 0;
    }
    .slide-graph .col-text ul {
      font-size: 0.92rem;
      color: #111827;
      line-height: 1.45;
      margin: 0 0 15px 0;
      padding-left: 1.2em;
    }
    .slide-graph .col-text li {
      margin-bottom: 6px;
    }
    .slide-graph .col-text .label {
      font-size: 0.85rem;
      color: #4B5563;
      font-style: italic;
      margin-bottom: 5px;
    }
  </style>
  
  <!-- CONTENIDO -->
  <h2>Índice de comercio mundial (1800-1938)</h2>
  
  <div class="columns">
    <div class="col-graph">
      <!-- Reemplazar src con la ruta al gráfico generado -->
      <img src="graficos/indice_comercio.png" alt="Índice de comercio mundial">
      <div class="fuente">Fuente: FTWTHD</div>
    </div>
    
    <div class="col-text">
      <h3>Cómo leer el índice:</h3>
      <ul>
        <li>1913 = 100 (año base)</li>
        <li>Valor 50 = mitad del comercio de 1913</li>
        <li>Valor 200 = doble del de 1913</li>
      </ul>
      
      <p class="label">Puntos clave:</p>
      <ul>
        <li>1800: 2.4 (casi nada)</li>
        <li>1870: 25 (x10 en 70 años)</li>
        <li>1913: 100 (pico)</li>
        <li>1932: 95 (colapso -29%)</li>
      </ul>
    </div>
  </div>
</section>
```

---

## TEMPLATE 4: Imagen estática + Texto (65/35)

Uso: Slides con mapas, fotos, diagramas

```html
<section class="slide slide-image">
  <style>
    .slide-image {
      width: 100vw;
      height: 100vh;
      background-color: #FFFFFF;
      display: flex;
      flex-direction: column;
      margin: 0;
      padding: 25px 40px 20px 40px;
      box-sizing: border-box;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }
    .slide-image h2 {
      color: #1F4E79;
      font-size: 1.7rem;
      font-weight: 600;
      margin: 0 0 15px 0;
      flex-shrink: 0;
    }
    .slide-image .columns {
      display: flex;
      flex-grow: 1;
      gap: 30px;
      min-height: 0;
    }
    .slide-image .col-img {
      flex: 0 0 64%;
      display: flex;
      flex-direction: column;
      min-height: 0;
    }
    .slide-image .col-img img {
      max-width: 100%;
      max-height: calc(100vh - 160px);
      object-fit: contain;
      flex-grow: 1;
      min-height: 0;
      border-radius: 4px;
    }
    .slide-image .col-img .fuente {
      font-size: 0.75rem;
      color: #4B5563;
      font-style: italic;
      text-align: center;
      margin-top: 8px;
      flex-shrink: 0;
    }
    .slide-image .col-text {
      flex: 0 0 34%;
      padding-top: 10px;
    }
    .slide-image .col-text h3 {
      color: #1F4E79;
      font-size: 1.05rem;
      font-weight: 600;
      margin: 0 0 10px 0;
    }
    .slide-image .col-text p {
      font-size: 0.92rem;
      color: #111827;
      line-height: 1.5;
      margin: 0 0 12px 0;
    }
    .slide-image .col-text ul {
      font-size: 0.92rem;
      color: #111827;
      line-height: 1.45;
      margin: 0 0 15px 0;
      padding-left: 1.2em;
    }
    .slide-image .col-text li {
      margin-bottom: 6px;
    }
  </style>
  
  <!-- CONTENIDO -->
  <h2>Etapa 1: Economía-mundo ibérica (1500-1650)</h2>
  
  <div class="columns">
    <div class="col-img">
      <img src="img/mapa-rutas-ibericas.png" alt="Rutas comerciales ibéricas siglo XVI">
      <div class="fuente">Fuente: Mapas históricos</div>
    </div>
    
    <div class="col-text">
      <h3>Rutas ibéricas siglo XVI:</h3>
      <ul>
        <li>Portugal: ruta del Cabo → Asia</li>
        <li>España: Atlántico → América</li>
      </ul>
      
      <h3>Modelo de comercio:</h3>
      <p>Monopolios estatales (Casa de Contratación). El Estado absorbe riesgos y captura rentas.</p>
    </div>
  </div>
</section>
```

---

## TEMPLATE 5: Solo texto (bullets, tablas, explicaciones)

Uso: Slides de contenido teórico

```html
<section class="slide slide-text">
  <style>
    .slide-text {
      width: 100vw;
      height: 100vh;
      background-color: #FFFFFF;
      display: flex;
      flex-direction: column;
      margin: 0;
      padding: 30px 50px 25px 50px;
      box-sizing: border-box;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }
    .slide-text h2 {
      color: #1F4E79;
      font-size: 1.7rem;
      font-weight: 600;
      margin: 0 0 20px 0;
      flex-shrink: 0;
    }
    .slide-text .content {
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }
    .slide-text p {
      font-size: 1.15rem;
      color: #111827;
      line-height: 1.55;
      margin: 0 0 15px 0;
      max-width: 90%;
    }
    .slide-text ul, .slide-text ol {
      font-size: 1.15rem;
      color: #111827;
      line-height: 1.55;
      margin: 0 0 20px 0;
      padding-left: 1.5em;
      max-width: 90%;
    }
    .slide-text li {
      margin-bottom: 10px;
    }
    .slide-text table {
      width: 100%;
      max-width: 95%;
      border-collapse: collapse;
      font-size: 1rem;
      margin: 15px 0;
    }
    .slide-text th {
      background-color: #1F4E79;
      color: #FFFFFF;
      padding: 12px 16px;
      text-align: left;
      font-weight: 600;
    }
    .slide-text td {
      padding: 10px 16px;
      border-bottom: 1px solid #e5e7eb;
      color: #111827;
    }
    .slide-text tr:nth-child(even) {
      background-color: #F3F4F6;
    }
    .slide-text .highlight {
      background-color: #FEF3C7;
      padding: 15px 20px;
      border-left: 4px solid #F59E0B;
      margin: 15px 0;
      max-width: 90%;
    }
    .slide-text .highlight p {
      margin: 0;
      font-size: 1.1rem;
    }
  </style>
  
  <!-- CONTENIDO -->
  <h2>Marco analítico: tres fuerzas</h2>
  
  <div class="content">
    <p>Para explicar cualquier período del comercio, preguntamos:</p>
    
    <table>
      <thead>
        <tr>
          <th>Fuerza</th>
          <th>Pregunta clave</th>
          <th>Ejemplos</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Tecnología</strong></td>
          <td>¿Cuánto cuesta mover bienes?</td>
          <td>Vela → vapor → contenedor</td>
        </tr>
        <tr>
          <td><strong>Reglas</strong></td>
          <td>¿Quién puede comerciar?</td>
          <td>Monopolios, aranceles, OMC</td>
        </tr>
        <tr>
          <td><strong>Poder</strong></td>
          <td>¿Quién garantiza estabilidad?</td>
          <td>Hegemonía, marina, moneda</td>
        </tr>
      </tbody>
    </table>
    
    <div class="highlight">
      <p><strong>Idea clave:</strong> Las tres operan juntas. Si una falla, el sistema se quiebra.</p>
    </div>
  </div>
</section>
```

---

## TEMPLATE 6: Portada / Título

```html
<section class="slide slide-title">
  <style>
    .slide-title {
      width: 100vw;
      height: 100vh;
      background-color: #FFFFFF;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: 0;
      padding: 60px;
      box-sizing: border-box;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      text-align: center;
    }
    .slide-title h1 {
      color: #1F4E79;
      font-size: 3.2rem;
      font-weight: 600;
      margin: 0 0 20px 0;
    }
    .slide-title .subtitle {
      color: #111827;
      font-size: 1.5rem;
      margin: 0 0 30px 0;
    }
    .slide-title .author {
      color: #4B5563;
      font-size: 1.15rem;
    }
  </style>
  
  <!-- CONTENIDO -->
  <h1>Economía Internacional</h1>
  <div class="subtitle">Clase 1 — El comercio mundial: auge, colapso y preguntas abiertas</div>
  <div class="author">UMET - Licenciatura en Economía | 2026</div>
</section>
```

---

## Cómo usar estos templates

### Para Claude Code:

1. **Elegir el template** según el tipo de contenido
2. **Copiar el HTML completo** (incluyendo el `<style>`)
3. **Reemplazar SOLO el contenido** dentro de los tags marcados
4. **NO tocar el CSS** bajo ninguna circunstancia

### Estructura de archivo recomendada:

```
clase01/
├── index.html          # Todas las slides concatenadas
├── graficos/           # PNGs generados por Python
│   ├── indice_comercio.png
│   └── participacion_regional.png
├── img/                # Imágenes estáticas
│   └── mapa-rutas-ibericas.png
└── datos/              # Scripts Python que generan gráficos
    └── generar_graficos.py
```

### Para navegación entre slides:

Podemos agregar un wrapper con Reveal.js mínimo o usar teclas de flecha con JavaScript vanilla. ¿Querés que agregue eso?
