# Sistema de Presentaciones UMET

## Estructura

```
presentaciones/
├── generar_html.py      # Script que genera HTML desde JSON
├── TEMPLATE.html        # Template manual (opcional)
├── README.md            # Este archivo
├── config/              # Configuraciones JSON por clase
│   ├── clase01.json
│   ├── clase02.json
│   └── ...
├── clase01/             # Carpeta de salida por clase
│   ├── index.html       # Presentación generada
│   ├── graficos/        # PNGs de matplotlib
│   └── img/             # Imágenes estáticas
└── clase02/
    └── ...
```

## Workflow

### 1. Crear/editar el JSON de la clase

```json
{
  "metadata": {
    "titulo": "Economía Internacional",
    "subtitulo": "Clase 2 — Balanza de pagos",
    "autor": "UMET - Licenciatura en Economía | 2026",
    "footer": "Economía Internacional | UMET"
  },
  "slides": [
    {"tipo": "portada"},
    {"tipo": "seccion", "titulo": "Introducción"},
    ...
  ]
}
```

### 2. Generar el HTML

```bash
cd presentaciones
python generar_html.py config/clase02.json clase02/index.html
```

### 3. Copiar gráficos e imágenes

```bash
# Copiar desde la carpeta de Quarto si hay gráficos Python
cp ../output/clases/clase02_files/figure-revealjs/*.png clase02/graficos/
```

## Tipos de slides disponibles

| Tipo | Descripción | Campos principales |
|------|-------------|-------------------|
| `portada` | Slide de título | (usa metadata) |
| `seccion` | Fondo azul, título grande | `titulo` |
| `centrado` | Texto centrado | `titulo`, `pregunta`, `texto`, `lista` |
| `texto` | Solo texto/listas | `titulo`, `subtitulo`, `lista`, `lista_numerada` |
| `texto_tabla` | Texto con tabla | `titulo`, `texto_intro`, `tabla`, `destacado` |
| `formula` | Fórmula matemática | `titulo`, `formula`, `interpretacion`, `donde`, `nota` |
| `grafico_texto` | Imagen + texto 65/35 | `titulo`, `imagen`, `fuente`, `columna_derecha` |

## Controles de la presentación

| Tecla | Acción |
|-------|--------|
| `→` `Space` `Enter` | Siguiente slide |
| `←` | Slide anterior |
| `F` | Fullscreen |
| `P` | Modo impresión (ver todos) |
| `Ctrl+P` | Guardar como PDF (en modo P) |
| `Home` / `End` | Primera / última |

## Ejemplo de slide `grafico_texto`

```json
{
  "tipo": "grafico_texto",
  "titulo": "Índice de comercio mundial (1800-1938)",
  "imagen": "graficos/indice_comercio.png",
  "fuente": "FTWTHD",
  "columna_derecha": {
    "secciones": [
      {
        "subtitulo": "Cómo leer el índice:",
        "lista": ["Punto 1", "Punto 2", "Punto 3"]
      },
      {
        "subtitulo": "Datos clave:",
        "estilo_subtitulo": "italic",
        "lista": ["1913 = 100", "1932 = 95"]
      }
    ],
    "destacado": {
      "tipo": "warning",
      "texto": "**Nota importante**"
    }
  }
}
```

## Ejemplo de slide `formula`

```json
{
  "tipo": "formula",
  "titulo": "Indicador 1: Índice de comercio",
  "formula": "I_t = 100 \\times \\frac{Comercio_t}{Comercio_{1913}}",
  "interpretacion": [
    "Si $I_t = 50$ → la mitad del comercio de 1913",
    "Si $I_t = 200$ → el doble"
  ],
  "nota": "Evita problemas de inflación."
}
```

## Cajas destacadas

Tipos disponibles: `warning` (amarillo), `info` (azul), `success` (verde), `error` (rojo)

```json
"destacado": {
  "tipo": "warning",
  "texto": "**Idea clave:** Texto importante."
}
```

## Markdown soportado en textos

- `**texto**` → **negrita**
- `*texto*` → *cursiva*
- `$formula$` → LaTeX inline
