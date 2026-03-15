# Reglas para generar slides Quarto Revealjs - UMET

## Reglas obligatorias

### 1. Centrado vertical
- **NUNCA** uses `::: {.content-center}` como wrapper para centrar
- **USA** la clase en el H2: `## Título {.center-slide}`
- Esto funciona en fullscreen, el wrapper no

### 2. Estructura de slide con gráfico + texto

```markdown
## Título del slide

:::: {.columns}
::: {.column width="65%"}
```{python}
#| fig-width: 11
#| fig-height: 6.5
#| out-width: "100%"
#| out-height: "55vh"

# código del gráfico
```

::: {.fuente}
Fuente: NOMBRE
:::
:::

::: {.column width="35%"}
**Subtítulo:**

- Punto 1
- Punto 2
:::
::::
```

### 3. Opciones obligatorias para gráficos Python

Siempre incluir estas opciones en los bloques de código:
```
#| fig-width: 11
#| fig-height: 6.5
#| out-width: "100%"
#| out-height: "55vh"
```

El `out-height: "55vh"` es crítico para que no se desborde.

### 4. Fuentes de imágenes/gráficos

Siempre usar la clase `.fuente`:
```markdown
::: {.fuente}
Fuente: INDEC, 2023
:::
```

Va inmediatamente después del gráfico o imagen, dentro de la misma columna.

### 5. Tablas en lugar de ASCII art

**NO hagas esto:**
```
┌────────────┬───────────────────────────────┐
│   Fuerza   │        Pregunta clave         │
├────────────┼───────────────────────────────┤
```

**SÍ hacé esto:**
```markdown
| Fuerza | Pregunta clave | Ejemplos |
|--------|----------------|----------|
| Tecnología | ¿Cuánto cuesta...? | Vela → vapor |
```

### 6. Slides de sección

```markdown
# Nombre de sección {.section}
```

El `#` (H1) con `.section` crea slide de sección con fondo azul.

### 7. Imágenes estáticas

```markdown
![](img/mapa.png)

::: {.fuente}
Fuente: Atlas Histórico
:::
```

Para controlar tamaño:
```markdown
![](img/mapa.png){height="50vh"}
```

### 8. NO usar

- `<br>` para espaciado vertical
- `height: 100vh` en CSS
- Tablas ASCII
- `::: {.content-center}` como wrapper
- Tamaños en px para imágenes

### 9. Slides de definición/fórmula

Para slides donde querés mostrar una fórmula centrada con explicación:

```markdown
## Indicador X: Nombre {.center-slide}

**Definición:**

$$formula$$

**Interpretación:**

- Punto 1
- Punto 2
```

### 10. Columnas permitidas

Solo usar estos anchos:
- Gráfico/imagen: 65%, texto: 35%
- Dos columnas iguales: 50%, 50%

No inventar otros porcentajes.
