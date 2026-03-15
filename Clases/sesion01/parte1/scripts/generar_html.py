"""
Genera HTML de presentación desde el JSON de slides.
Usa los patrones del HTML existente.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"
OUTPUT_HTML = BASE_DIR / "presentacion" / "index.html"

# ============== TEMPLATES ==============

HTML_HEAD = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Economía Internacional - Clases 1+2</title>
  <script>
    MathJax = {
      tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body {
      width: 100%;
      height: 100%;
      overflow: hidden;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }

    .slides-container {
      width: 100%;
      height: 100%;
      position: relative;
    }

    .slide {
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0;
      left: 0;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s ease;
    }

    .slide.active {
      opacity: 1;
      visibility: visible;
    }

    .footer {
      position: fixed;
      bottom: 15px;
      left: 0;
      right: 0;
      display: flex;
      justify-content: space-between;
      padding: 0 25px;
      font-size: 0.85rem;
      color: #4B5563;
      z-index: 100;
    }

    /* PRINT MODE */
    body.print-mode {
      overflow: auto !important;
      height: auto !important;
    }

    body.print-mode .slides-container {
      height: auto !important;
      position: relative !important;
      display: block !important;
    }

    body.print-mode .slide {
      position: relative !important;
      opacity: 1 !important;
      visibility: visible !important;
      page-break-after: always !important;
      break-after: page !important;
      margin-bottom: 20px !important;
      border: 1px solid #e5e7eb !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
      top: auto !important;
      left: auto !important;
    }

    body.print-mode .footer {
      display: none !important;
    }

    .print-banner {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: #1F4E79;
      color: white;
      padding: 10px 20px;
      text-align: center;
      z-index: 1000;
      font-size: 0.9rem;
    }

    body.print-mode .print-banner {
      display: block !important;
      position: relative !important;
    }

    @media print {
      * {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      html, body {
        overflow: visible !important;
        height: auto !important;
        width: 100% !important;
      }
      .slides-container {
        height: auto !important;
        display: block !important;
      }
      .slide {
        position: relative !important;
        opacity: 1 !important;
        visibility: visible !important;
        page-break-after: always !important;
        break-after: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        border: none !important;
        box-shadow: none !important;
        margin: 0 !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        height: 100vh !important;
      }
      .footer, .print-banner {
        display: none !important;
      }
    }

    :root {
      --primary: #1F4E79;
      --secondary: #0EA5E9;
      --accent: #10B981;
      --warning: #F59E0B;
      --danger: #EF4444;
      --text-dark: #111827;
      --text-muted: #4B5563;
      --white: #FFFFFF;
      --bg-light: #F3F4F6;
    }

    /* Utility classes */
    .warning-box {
      background-color: #FEF3C7;
      padding: 15px 20px;
      border-left: 4px solid #F59E0B;
      margin: 15px 0;
    }
    .info-box {
      background-color: #E0F2FE;
      padding: 15px 20px;
      border-left: 4px solid #0EA5E9;
      margin: 15px 0;
    }
    .success-box {
      background-color: #D1FAE5;
      padding: 15px 20px;
      border-left: 4px solid #10B981;
      margin: 15px 0;
    }
    .danger-box {
      background-color: #FEE2E2;
      padding: 15px 20px;
      border-left: 4px solid #EF4444;
      margin: 15px 0;
    }
  </style>
</head>
<body>

<div class="print-banner">
  MODO IMPRESIÓN - Presioná <strong>P</strong> para volver a modo presentación, o <strong>Ctrl+P</strong> para imprimir/guardar como PDF
</div>

<div class="slides-container">
'''

HTML_FOOTER = '''
</div>

<!-- Footer -->
<div class="footer">
  <span>Economía Internacional | UMET | Clase 1</span>
  <span id="slide-counter">1 / {total}</span>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const counter = document.getElementById('slide-counter');
  let current = 0;

  function showSlide(n) {{
    slides[current].classList.remove('active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('active');
    counter.textContent = `${{current + 1}} / ${{slides.length}}`;
  }}

  let printMode = false;
  const originalStyles = [];
  slides.forEach(s => {{
    originalStyles.push(s.getAttribute('style'));
  }});

  function togglePrintMode() {{
    printMode = !printMode;
    document.body.classList.toggle('print-mode', printMode);

    if (printMode) {{
      document.body.style.overflow = 'auto';
      document.body.style.height = 'auto';
      document.querySelector('.slides-container').style.height = 'auto';
      document.querySelector('.slides-container').style.position = 'relative';

      slides.forEach((s, i) => {{
        s.style.position = 'relative';
        s.style.opacity = '1';
        s.style.visibility = 'visible';
        s.style.top = 'auto';
        s.style.left = 'auto';
        s.style.marginBottom = '30px';
        s.style.border = '2px solid #1F4E79';
        s.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
        s.style.pageBreakAfter = 'always';
        s.style.breakAfter = 'page';
      }});
    }} else {{
      document.body.style.overflow = 'hidden';
      document.body.style.height = '100%';
      document.querySelector('.slides-container').style.height = '100%';
      document.querySelector('.slides-container').style.position = 'relative';

      slides.forEach((s, i) => {{
        s.setAttribute('style', originalStyles[i]);
        s.classList.remove('active');
      }});
      slides[current].classList.add('active');
    }}
  }}

  document.addEventListener('keydown', (e) => {{
    if (printMode) {{
      if (e.key === 'p' || e.key === 'P') {{
        togglePrintMode();
      }}
      return;
    }}

    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {{
      showSlide(current + 1);
    }} else if (e.key === 'ArrowLeft') {{
      showSlide(current - 1);
    }} else if (e.key === 'f' || e.key === 'F') {{
      document.documentElement.requestFullscreen?.();
    }} else if (e.key === 'Escape') {{
      document.exitFullscreen?.();
    }} else if (e.key === 'Home') {{
      showSlide(0);
    }} else if (e.key === 'End') {{
      showSlide(slides.length - 1);
    }} else if (e.key === 'p' || e.key === 'P') {{
      togglePrintMode();
    }}
  }});

  document.addEventListener('click', (e) => {{
    if (printMode) return;
    if (e.target.tagName !== 'A') {{
      if (e.clientX > window.innerWidth / 2) {{
        showSlide(current + 1);
      }} else {{
        showSlide(current - 1);
      }}
    }}
  }});
</script>

</body>
</html>
'''


def escape_html(text):
    """Escapa caracteres HTML pero preserva fórmulas matemáticas."""
    if not text:
        return ''
    # No escapar $ para MathJax
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


def render_portada(slide, is_first):
    titulo = slide['titulo']
    subtitulo = slide.get('subtitulo', '')
    active = ' active' if is_first else ''

    return f'''
  <!-- SLIDE {slide['numero']}: Portada -->
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 60px;
    text-align: center;
  ">
    <h1 style="color: #1F4E79; font-size: 3.2rem; font-weight: 600; margin: 0 0 20px 0;">
      {escape_html(titulo)}
    </h1>
    <div style="color: #111827; font-size: 1.5rem; margin: 0 0 30px 0;">
      {escape_html(subtitulo)}
    </div>
    <div style="color: #4B5563; font-size: 1.15rem;">
      UMET - Licenciatura en Economía | 2026
    </div>
  </section>
'''


def render_seccion(slide, is_first):
    titulo = slide['titulo']
    subtitulo = slide.get('subtitulo', '')
    active = ' active' if is_first else ''

    subtitulo_html = f'<div style="color: #E0F2FE; font-size: 1.5rem; margin-top: 20px;">{escape_html(subtitulo)}</div>' if subtitulo else ''

    return f'''
  <!-- SLIDE {slide['numero']}: Sección -->
  <section class="slide{active}" style="
    background-color: #1F4E79;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  ">
    <h1 style="color: #FFFFFF; font-size: 3.5rem; font-weight: 600; text-align: center; padding: 0 60px;">
      {escape_html(titulo)}
    </h1>
    {subtitulo_html}
  </section>
'''


def render_agenda(slide, is_first):
    titulo = slide['titulo']
    contenido = slide.get('contenido', [])
    active = ' active' if is_first else ''

    items_html = '\n'.join([f'        <li style="margin-bottom: 15px;">{escape_html(item)}</li>' for item in contenido])

    return f'''
  <!-- SLIDE {slide['numero']}: Agenda -->
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    padding: 50px 60px;
  ">
    <h2 style="color: #1F4E79; font-size: 2rem; font-weight: 600; margin: 0 0 30px 0;">
      {escape_html(titulo)}
    </h2>
    <ul style="font-size: 1.3rem; color: #111827; line-height: 1.6; padding-left: 1.5em;">
{items_html}
    </ul>
  </section>
'''


def render_formula(slide, is_first):
    titulo = slide['titulo']
    subtitulo = slide.get('subtitulo', '')
    contenido = slide.get('contenido', [])
    active = ' active' if is_first else ''

    subtitulo_html = f'<div style="color: #4B5563; font-size: 1.1rem; margin-bottom: 20px;">{escape_html(subtitulo)}</div>' if subtitulo else ''

    # Procesar contenido: detectar fórmulas
    items_html = []
    for item in contenido:
        if item.startswith('Fórmula:') or '=' in item and ('/' in item or '×' in item or '+' in item or '-' in item):
            # Es una fórmula - mostrar destacada
            items_html.append(f'<div style="font-size: 1.4rem; margin: 15px 0; padding: 10px; background: #F3F4F6; border-radius: 4px;">{escape_html(item)}</div>')
        else:
            items_html.append(f'<li style="margin-bottom: 10px;">{escape_html(item)}</li>')

    # Separar fórmulas de bullets
    formulas = [h for h in items_html if h.startswith('<div')]
    bullets = [h for h in items_html if h.startswith('<li')]

    formulas_html = '\n'.join(formulas)
    bullets_html = f'<ul style="font-size: 1.15rem; color: #111827; line-height: 1.6; padding-left: 1.5em; margin-top: 20px;">\n' + '\n'.join(bullets) + '\n</ul>' if bullets else ''

    return f'''
  <!-- SLIDE {slide['numero']}: Fórmula -->
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 50px 80px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.9rem; font-weight: 600; margin: 0 0 15px 0; text-align: center;">
      {escape_html(titulo)}
    </h2>
    {subtitulo_html}
    <div style="max-width: 900px; margin: 0 auto;">
      {formulas_html}
      {bullets_html}
    </div>
  </section>
'''


def render_texto(slide, is_first):
    titulo = slide['titulo']
    subtitulo = slide.get('subtitulo', '')
    contenido = slide.get('contenido', [])
    active = ' active' if is_first else ''

    subtitulo_html = f'<div style="color: #4B5563; font-size: 1.1rem; margin-bottom: 25px;">{escape_html(subtitulo)}</div>' if subtitulo else ''

    items_html = '\n'.join([f'        <li style="margin-bottom: 12px;">{escape_html(item)}</li>' for item in contenido])

    return f'''
  <!-- SLIDE {slide['numero']}: Texto -->
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    padding: 40px 60px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.8rem; font-weight: 600; margin: 0 0 20px 0;">
      {escape_html(titulo)}
    </h2>
    {subtitulo_html}
    <ul style="font-size: 1.15rem; color: #111827; line-height: 1.6; padding-left: 1.5em; flex-grow: 1;">
{items_html}
    </ul>
  </section>
'''


def render_grafico_texto(slide, is_first):
    titulo = slide['titulo']
    subtitulo = slide.get('subtitulo', '')
    contenido = slide.get('contenido', [])
    visual = slide.get('visual', '')
    fuente = slide.get('fuente', '')
    active = ' active' if is_first else ''

    # Ajustar path de imagen
    if visual:
        if not visual.startswith('../'):
            visual = '../' + visual

    items_html = '\n'.join([f'          <li style="margin-bottom: 8px;">{escape_html(item)}</li>' for item in contenido])
    fuente_html = f'<div style="font-size: 0.75rem; color: #4B5563; font-style: italic; text-align: center; margin-top: 8px;">Fuente: {escape_html(fuente)}</div>' if fuente else ''

    return f'''
  <!-- SLIDE {slide['numero']}: Gráfico + Texto -->
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    padding: 25px 40px 20px 40px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.7rem; font-weight: 600; margin: 0 0 15px 0;">
      {escape_html(titulo)}
    </h2>

    <div style="display: flex; flex-grow: 1; gap: 30px; min-height: 0;">
      <div style="flex: 0 0 64%; display: flex; flex-direction: column; min-height: 0;">
        <img src="{visual}" alt="{escape_html(titulo)}"
             style="max-width: 100%; max-height: calc(100vh - 160px); object-fit: contain; flex-grow: 1; min-height: 0;">
        {fuente_html}
      </div>

      <div style="flex: 0 0 34%; padding-top: 10px;">
        <ul style="font-size: 0.95rem; color: #111827; line-height: 1.5; margin: 0; padding-left: 1.2em;">
{items_html}
        </ul>
      </div>
    </div>
  </section>
'''


def render_cierre(slide, is_first):
    titulo = slide['titulo']
    subtitulo = slide.get('subtitulo', '')
    active = ' active' if is_first else ''

    subtitulo_html = f'<div style="color: #4B5563; font-size: 1.3rem; margin-top: 20px;">{escape_html(subtitulo)}</div>' if subtitulo else ''

    return f'''
  <!-- SLIDE {slide['numero']}: Cierre -->
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 60px;
    text-align: center;
  ">
    <h1 style="color: #1F4E79; font-size: 3.5rem; font-weight: 600;">
      {escape_html(titulo)}
    </h1>
    {subtitulo_html}
  </section>
'''


def render_slide(slide, is_first=False):
    """Renderiza un slide según su tipo."""
    tipo = slide.get('tipo', 'texto')

    renderers = {
        'portada': render_portada,
        'seccion': render_seccion,
        'agenda': render_agenda,
        'formula': render_formula,
        'texto': render_texto,
        'grafico_texto': render_grafico_texto,
        'cierre': render_cierre,
    }

    renderer = renderers.get(tipo, render_texto)
    return renderer(slide, is_first)


def main():
    # Primero actualizar la agenda automáticamente
    try:
        from actualizar_agenda import main as actualizar_agenda
        print("Actualizando agenda...")
        actualizar_agenda()
        print("")
    except ImportError:
        print("ADVERTENCIA: No se pudo importar actualizar_agenda.py")

    # Leer JSON
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    slides = data['slides']
    total = len(slides)

    # Generar HTML
    html_parts = [HTML_HEAD]

    for i, slide in enumerate(slides):
        is_first = (i == 0)
        html_parts.append(render_slide(slide, is_first))

    html_parts.append(HTML_FOOTER.format(total=total))

    # Escribir archivo
    html_content = '\n'.join(html_parts)

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML generado: {OUTPUT_HTML}")
    print(f"Total slides: {total}")


if __name__ == "__main__":
    main()
