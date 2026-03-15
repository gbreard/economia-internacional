# -*- coding: utf-8 -*-
"""
Generador de presentaciones HTML desde JSON
Economía Internacional - UMET

Uso:
    python generar_html.py config/clase01.json clase01/index.html
"""

import json
import sys
import re
from pathlib import Path

# ============================================
# TEMPLATES HTML
# ============================================

HTML_HEAD = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo}</title>
  <script>
    MathJax = {{ tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }} }};
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html, body {{
      width: 100%;
      height: 100%;
      overflow: hidden;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }}
    .slides-container {{ width: 100%; height: 100%; position: relative; }}
    .slide {{
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0;
      left: 0;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s ease;
    }}
    .slide.active {{ opacity: 1; visibility: visible; }}
    .footer {{
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
    }}
    body.print-mode {{ overflow: auto !important; height: auto !important; }}
    body.print-mode .slides-container {{ height: auto !important; }}
    body.print-mode .slide {{
      position: relative !important;
      opacity: 1 !important;
      visibility: visible !important;
      margin-bottom: 20px !important;
      border: 1px solid #e5e7eb !important;
    }}
    body.print-mode .footer {{ display: none !important; }}
    .print-banner {{
      display: none;
      background: #1F4E79;
      color: white;
      padding: 10px 20px;
      text-align: center;
      font-size: 0.9rem;
    }}
    body.print-mode .print-banner {{ display: block !important; }}
    @media print {{
      * {{ -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
      .slide {{
        position: relative !important;
        opacity: 1 !important;
        visibility: visible !important;
        page-break-after: always !important;
      }}
      .footer, .print-banner {{ display: none !important; }}
    }}
  </style>
</head>
<body>

<div class="print-banner">
  MODO IMPRESIÓN - <strong>P</strong> para volver | <strong>Ctrl+P</strong> para PDF
</div>

<div class="slides-container">
'''

HTML_FOOT = '''
</div>

<div class="footer">
  <span>{footer}</span>
  <span id="slide-counter">1 / {total}</span>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const counter = document.getElementById('slide-counter');
  let current = 0;
  let printMode = false;
  const originalStyles = [];
  slides.forEach(s => originalStyles.push(s.getAttribute('style')));

  function showSlide(n) {{
    slides[current].classList.remove('active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('active');
    counter.textContent = `${{current + 1}} / ${{slides.length}}`;
  }}

  function togglePrintMode() {{
    printMode = !printMode;
    document.body.classList.toggle('print-mode', printMode);
    if (printMode) {{
      document.body.style.overflow = 'auto';
      document.body.style.height = 'auto';
      document.querySelector('.slides-container').style.height = 'auto';
      document.querySelector('.slides-container').style.position = 'relative';
      slides.forEach(s => {{
        s.style.position = 'relative';
        s.style.opacity = '1';
        s.style.visibility = 'visible';
        s.style.top = 'auto';
        s.style.left = 'auto';
        s.style.marginBottom = '30px';
        s.style.border = '2px solid #1F4E79';
        s.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
        s.style.pageBreakAfter = 'always';
      }});
    }} else {{
      document.body.style.overflow = 'hidden';
      document.body.style.height = '100%';
      document.querySelector('.slides-container').style.height = '100%';
      slides.forEach((s, i) => {{
        s.setAttribute('style', originalStyles[i]);
        s.classList.remove('active');
      }});
      slides[current].classList.add('active');
    }}
  }}

  document.addEventListener('keydown', (e) => {{
    if (printMode) {{ if (e.key === 'p' || e.key === 'P') togglePrintMode(); return; }}
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') showSlide(current + 1);
    else if (e.key === 'ArrowLeft') showSlide(current - 1);
    else if (e.key === 'f' || e.key === 'F') document.documentElement.requestFullscreen?.();
    else if (e.key === 'Escape') document.exitFullscreen?.();
    else if (e.key === 'Home') showSlide(0);
    else if (e.key === 'End') showSlide(slides.length - 1);
    else if (e.key === 'p' || e.key === 'P') togglePrintMode();
  }});

  document.addEventListener('click', (e) => {{
    if (printMode) return;
    if (e.target.tagName !== 'A') {{
      if (e.clientX > window.innerWidth / 2) showSlide(current + 1);
      else showSlide(current - 1);
    }}
  }});
</script>

</body>
</html>
'''

# ============================================
# SLIDE TEMPLATES
# ============================================

def md_to_html(text):
    """Convierte markdown básico a HTML"""
    if not text:
        return text
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def render_lista(items, numerada=False):
    """Genera HTML para una lista"""
    tag = 'ol' if numerada else 'ul'
    items_html = ''.join(f'<li style="margin-bottom: 6px;">{md_to_html(item)}</li>' for item in items)
    return f'<{tag} style="font-size: 0.92rem; color: #111827; line-height: 1.45; margin: 0 0 15px 0; padding-left: 1.2em;">{items_html}</{tag}>'

def render_destacado(data):
    """Genera caja destacada"""
    colores = {
        'warning': ('#FEF3C7', '#F59E0B'),
        'info': ('#E0F2FE', '#0EA5E9'),
        'success': ('#D1FAE5', '#10B981'),
        'error': ('#FEE2E2', '#EF4444')
    }
    bg, border = colores.get(data.get('tipo', 'info'), colores['info'])
    return f'''<div style="background-color: {bg}; padding: 15px 20px; border-left: 4px solid {border}; margin-top: 20px;">
      <p style="margin: 0; font-size: 1.05rem;">{md_to_html(data['texto'])}</p>
    </div>'''

def slide_portada(data, meta, is_first):
    active = ' active' if is_first else ''
    return f'''
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
      {meta['titulo']}
    </h1>
    <div style="color: #111827; font-size: 1.5rem; margin: 0 0 30px 0;">
      {meta['subtitulo']}
    </div>
    <div style="color: #4B5563; font-size: 1.15rem;">
      {meta['autor']}
    </div>
  </section>
'''

def slide_seccion(data, meta, is_first):
    active = ' active' if is_first else ''
    return f'''
  <section class="slide{active}" style="
    background-color: #1F4E79;
    display: flex;
    justify-content: center;
    align-items: center;
  ">
    <h1 style="color: #FFFFFF; font-size: 4.5rem; font-weight: 600; text-align: center; padding: 0 60px;">
      {data['titulo']}
    </h1>
  </section>
'''

def slide_centrado(data, meta, is_first):
    active = ' active' if is_first else ''

    pregunta = f'<div style="color: #1F4E79; font-size: 1.9rem; font-weight: 600; text-align: center; max-width: 90%; line-height: 1.4; margin-bottom: 40px;">{md_to_html(data.get("pregunta", ""))}</div>' if data.get('pregunta') else ''

    lista_html = ''
    if data.get('lista'):
        items = ''.join(f'<li style="margin-bottom: 12px; line-height: 1.5;">{md_to_html(item)}</li>' for item in data['lista'])
        lista_html = f'<ol style="display: inline-block; text-align: left; margin: 20px 0; padding-left: 1.5em;">{items}</ol>'

    texto = f'{md_to_html(data.get("texto", ""))}{lista_html}'

    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 60px 80px;
  ">
    <h2 style="color: #1F4E79; font-size: 2.2rem; font-weight: 600; margin: 0 0 30px 0; text-align: center;">
      {data['titulo']}
    </h2>
    {pregunta}
    <div style="color: #111827; font-size: 1.3rem; text-align: center; max-width: 80%;">
      {texto}
    </div>
  </section>
'''

def slide_texto(data, meta, is_first):
    active = ' active' if is_first else ''

    subtitulo = f'<h3 style="color: #1F4E79; font-size: 1.3rem; margin-bottom: 20px;">{md_to_html(data["subtitulo"])}</h3>' if data.get('subtitulo') else ''

    lista_html = ''
    if data.get('lista_numerada'):
        items = ''.join(f'<li style="margin-bottom: 15px;">{md_to_html(item)}</li>' for item in data['lista_numerada'])
        lista_html = f'<ol style="font-size: 1.2rem; color: #111827; line-height: 1.6; padding-left: 1.5em;">{items}</ol>'
    elif data.get('lista'):
        items = ''.join(f'<li style="margin-bottom: 12px;">{md_to_html(item)}</li>' for item in data['lista'])
        lista_html = f'<ul style="font-size: 1.15rem; color: #111827; line-height: 1.6; padding-left: 1.5em;">{items}</ul>'

    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    padding: 30px 50px 25px 50px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.7rem; font-weight: 600; margin: 0 0 25px 0;">
      {data['titulo']}
    </h2>
    <div style="flex-grow: 1;">
      {subtitulo}
      {lista_html}
    </div>
  </section>
'''

def slide_texto_tabla(data, meta, is_first):
    active = ' active' if is_first else ''

    intro = f'<p style="font-size: 1.15rem; color: #111827; line-height: 1.55; margin: 0 0 20px 0;">{md_to_html(data.get("texto_intro", ""))}</p>' if data.get('texto_intro') else ''

    # Tabla
    tabla = data.get('tabla', {})
    cols = tabla.get('columnas', [])
    filas = tabla.get('filas', [])

    header = ''.join(f'<th style="background-color: #1F4E79; color: #FFFFFF; padding: 12px 16px; text-align: left; font-weight: 600;">{col}</th>' for col in cols)

    rows_html = ''
    for i, fila in enumerate(filas):
        bg = ' style="background-color: #F3F4F6;"' if i % 2 == 1 else ''
        cells = ''.join(f'<td style="padding: 10px 16px; border-bottom: 1px solid #e5e7eb;">{md_to_html(cell)}</td>' for cell in fila)
        rows_html += f'<tr{bg}>{cells}</tr>'

    tabla_html = f'''<table style="width: 100%; border-collapse: collapse; font-size: 1rem; margin: 15px 0;">
        <thead><tr>{header}</tr></thead>
        <tbody>{rows_html}</tbody>
      </table>'''

    destacado = render_destacado(data['destacado']) if data.get('destacado') else ''

    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    padding: 30px 50px 25px 50px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.7rem; font-weight: 600; margin: 0 0 20px 0;">
      {data['titulo']}
    </h2>
    <div style="flex-grow: 1;">
      {intro}
      {tabla_html}
      {destacado}
    </div>
  </section>
'''

def slide_formula(data, meta, is_first):
    active = ' active' if is_first else ''

    donde = ''
    if data.get('donde'):
        items = ''.join(f'<li>{md_to_html(item)}</li>' for item in data['donde'])
        donde = f'<p>Donde:</p><ul style="margin: 15px 0; padding-left: 1.5em; line-height: 1.6;">{items}</ul>'

    interpretacion = ''
    if data.get('interpretacion'):
        items = ''.join(f'<li>{md_to_html(item)}</li>' for item in data['interpretacion'])
        interpretacion = f'<strong>Interpretación:</strong><ul style="margin: 15px 0; padding-left: 1.5em; line-height: 1.6;">{items}</ul>'

    nota = f'<p style="margin-top: 20px;">{md_to_html(data["nota"])}</p>' if data.get('nota') else ''

    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 60px 80px;
  ">
    <h2 style="color: #1F4E79; font-size: 2rem; font-weight: 600; margin: 0 0 30px 0; text-align: center;">
      {data['titulo']}
    </h2>
    <div style="margin: 20px 0; font-size: 1.5rem;">
      <strong>Definición:</strong>
      <div style="margin: 20px 0; font-size: 1.8rem; text-align: center;">
        $${data['formula']}$$
      </div>
    </div>
    <div style="color: #111827; font-size: 1.2rem; max-width: 80%; margin-top: 20px;">
      {donde}
      {interpretacion}
      {nota}
    </div>
  </section>
'''

def slide_grafico_texto(data, meta, is_first):
    active = ' active' if is_first else ''

    # Columna derecha
    col_derecha = ''
    for seccion in data.get('columna_derecha', {}).get('secciones', []):
        subtitulo_style = 'font-style: italic; color: #4B5563;' if seccion.get('estilo_subtitulo') == 'italic' else 'color: #1F4E79; font-weight: 600;'
        sub = f'<h3 style="font-size: 1.05rem; margin: 0 0 10px 0; {subtitulo_style}">{seccion["subtitulo"]}</h3>' if seccion.get('subtitulo') else ''

        texto = f'<p style="font-size: 0.92rem; color: #111827; line-height: 1.45; margin: 0 0 15px 0;">{md_to_html(seccion["texto"])}</p>' if seccion.get('texto') else ''

        lista = ''
        if seccion.get('lista'):
            items = ''.join(f'<li style="margin-bottom: 6px;">{md_to_html(item)}</li>' for item in seccion['lista'])
            lista = f'<ul style="font-size: 0.92rem; color: #111827; line-height: 1.45; margin: 0 0 15px 0; padding-left: 1.2em;">{items}</ul>'

        col_derecha += f'{sub}{texto}{lista}'

    destacado = ''
    if data.get('columna_derecha', {}).get('destacado'):
        destacado = render_destacado(data['columna_derecha']['destacado'])

    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex;
    flex-direction: column;
    padding: 25px 40px 20px 40px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.7rem; font-weight: 600; margin: 0 0 15px 0;">
      {data['titulo']}
    </h2>

    <div style="display: flex; flex-grow: 1; gap: 30px; min-height: 0;">
      <div style="flex: 0 0 64%; display: flex; flex-direction: column; min-height: 0;">
        <img src="{data['imagen']}" alt="{data['titulo']}"
             style="max-width: 100%; max-height: calc(100vh - 160px); object-fit: contain; flex-grow: 1; min-height: 0;">
        <div style="font-size: 0.75rem; color: #4B5563; font-style: italic; text-align: center; margin-top: 8px;">
          Fuente: {data.get('fuente', '')}
        </div>
      </div>

      <div style="flex: 0 0 34%; padding-top: 10px;">
        {col_derecha}
        {destacado}
      </div>
    </div>
  </section>
'''

# Mapeo de tipos a funciones
SLIDE_RENDERERS = {
    'portada': slide_portada,
    'seccion': slide_seccion,
    'centrado': slide_centrado,
    'texto': slide_texto,
    'texto_tabla': slide_texto_tabla,
    'formula': slide_formula,
    'grafico_texto': slide_grafico_texto,
}

def generar_html(config_path, output_path):
    """Genera HTML desde JSON config"""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    meta = config['metadata']
    slides = config['slides']

    # Generar slides
    slides_html = ''
    for i, slide in enumerate(slides):
        tipo = slide.get('tipo', 'texto')
        renderer = SLIDE_RENDERERS.get(tipo)
        if renderer:
            slides_html += renderer(slide, meta, i == 0)
        else:
            print(f"Advertencia: tipo de slide desconocido: {tipo}")

    # Ensamblar HTML
    html = HTML_HEAD.format(titulo=meta['titulo'])
    html += slides_html
    html += HTML_FOOT.format(footer=meta['footer'], total=len(slides))

    # Guardar
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ Generado: {output_path} ({len(slides)} slides)")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python generar_html.py config/clase01.json clase01/index.html")
        sys.exit(1)

    generar_html(sys.argv[1], sys.argv[2])
