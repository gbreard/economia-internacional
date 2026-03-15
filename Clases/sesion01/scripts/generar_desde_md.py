"""
Genera HTML de presentación directamente desde contenido.md
"""
import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
INPUT_MD = BASE_DIR / "contenido.md"
OUTPUT_HTML = BASE_DIR / "presentacion" / "index.html"


# ============== PARSER ==============

def parse_contenido_md(text):
    """Parsea contenido.md y devuelve lista de slides."""
    slides = []
    # Dividir por slides (#### Slide ...)
    parts = re.split(r'\n####\s+Slide\s+(?:NEW-\d+|\d+)\s*:', text)

    for part in parts[1:]:  # skip header
        slide = {}
        lines = part.strip().split('\n')

        # Título viene en la primera línea
        slide['titulo_header'] = lines[0].strip()

        # Parsear campos
        content_lines = []
        in_contenido = False
        in_notas = False
        notas_lines = []
        # Progressive steps (grafico_progresivo)
        pasos = []
        current_paso = None
        in_paso_contenido = False

        for line in lines[1:]:
            stripped = line.strip()

            # Check for **Paso N**: blocks (progressive slides)
            paso_match = re.match(r'\*\*Paso\s+\d+\*\*\s*:', stripped)
            if paso_match:
                if current_paso is not None:
                    pasos.append(current_paso)
                current_paso = {'contenido': [], 'visual': ''}
                in_paso_contenido = False
                in_contenido = False
                in_notas = False
                continue

            # If inside a paso block, handle paso-level fields
            if current_paso is not None:
                if stripped.startswith('**Gráfico**:') or stripped.startswith('**Imagen**:'):
                    current_paso['visual'] = stripped.split(':', 1)[1].strip()
                    in_paso_contenido = False
                elif stripped.startswith('**Contenido**:'):
                    in_paso_contenido = True
                elif stripped.startswith('**Fuente**:'):
                    pasos.append(current_paso)
                    current_paso = None
                    in_paso_contenido = False
                    slide['fuente'] = stripped.split(':', 1)[1].strip()
                elif stripped.startswith('**Notas docente**:'):
                    pasos.append(current_paso)
                    current_paso = None
                    in_paso_contenido = False
                    in_notas = True
                elif stripped == '---':
                    pasos.append(current_paso)
                    current_paso = None
                    break
                elif in_paso_contenido and stripped.startswith('- '):
                    current_paso['contenido'].append(stripped[2:])
                continue

            if stripped.startswith('**Tipo**:'):
                slide['tipo'] = stripped.split(':', 1)[1].strip()
                in_contenido = False
                in_notas = False
            elif stripped.startswith('**Título**:'):
                slide['titulo'] = stripped.split(':', 1)[1].strip()
                in_contenido = False
                in_notas = False
            elif stripped.startswith('**Subtítulo**:'):
                slide['subtitulo'] = stripped.split(':', 1)[1].strip()
                in_contenido = False
                in_notas = False
            elif stripped.startswith('**Fecha**:'):
                slide['fecha'] = stripped.split(':', 1)[1].strip()
                in_contenido = False
                in_notas = False
            elif stripped.startswith('**Layout**:'):
                slide['layout'] = stripped.split(':', 1)[1].strip().lower()
                in_contenido = False
                in_notas = False
            elif stripped.startswith('**Contenido**:'):
                in_contenido = True
                in_notas = False
            elif stripped.startswith('**Imagen**:') or stripped.startswith('**Gráfico**:'):
                slide['visual'] = stripped.split(':', 1)[1].strip()
                in_contenido = False
                in_notas = False
            elif stripped.startswith('**Fuente**:'):
                slide['fuente'] = stripped.split(':', 1)[1].strip()
                in_contenido = False
                in_notas = False
            elif stripped.startswith('**Notas docente**:'):
                in_notas = True
                in_contenido = False
            elif stripped == '---':
                break
            elif in_contenido and stripped.startswith('- '):
                content_lines.append(stripped[2:])
            elif in_notas:
                if stripped != '```':
                    notas_lines.append(line.rstrip())

        # Close any unclosed paso
        if current_paso is not None:
            pasos.append(current_paso)

        slide['contenido'] = content_lines
        slide['notas_docente'] = '\n'.join(notas_lines).strip()
        if pasos:
            slide['pasos'] = pasos

        if 'titulo' not in slide:
            slide['titulo'] = slide.get('titulo_header', '')

        slides.append(slide)

    return slides


# ============== HTML RENDERERS ==============

def esc(text):
    if not text:
        return ''
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def format_md(text):
    """Convert inline markdown (bold, italic) to HTML after escaping."""
    if not text:
        return ''
    t = esc(text)
    t = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    return t


def render_formula_content(text):
    """Render text with inline $...$ LaTeX formulas and markdown bold/italic."""
    if not text:
        return ''
    escaped = esc(text)
    parts = escaped.split('$')
    if len(parts) >= 3:
        result = []
        for i, part in enumerate(parts):
            if i % 2 == 0:
                result.append(part)
            else:
                result.append(f'<span class="katex-inline">\\({part}\\)</span>')
        out = ''.join(result)
    else:
        out = escaped
    out = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', out)
    out = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', out)
    out = re.sub(r'\*(.+?)\*', r'<em>\1</em>', out)
    return out


def render_portada(s, active):
    fecha_html = f'<div style="color: #4B5563; font-size: 1.2rem; margin: 0 0 15px 0;">{esc(s.get("fecha", ""))}</div>' if s.get('fecha') else ''
    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    padding: 60px; text-align: center;
  ">
    <h1 style="color: #1F4E79; font-size: 3.2rem; font-weight: 600; margin: 0 0 20px 0;">
      {esc(s.get('titulo', ''))}
    </h1>
    <div style="color: #111827; font-size: 1.5rem; margin: 0 0 30px 0;">
      {esc(s.get('subtitulo', ''))}
    </div>
    {fecha_html}
    <div style="color: #4B5563; font-size: 1.15rem;">
      UMET - Licenciatura en Economía | 2026
    </div>
  </section>'''


def render_centrado(s, active):
    items = '\n'.join(f'        <li style="margin-bottom: 12px;">{render_formula_content(c)}</li>' for c in s.get('contenido', []))
    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    padding: 60px 80px;
  ">
    <h2 style="color: #1F4E79; font-size: 2.2rem; font-weight: 600; margin: 0 0 30px 0; text-align: center;">
      {esc(s.get('titulo', ''))}
    </h2>
    <ul style="font-size: 1.2rem; color: #111827; line-height: 1.7; padding-left: 1.5em; text-align: left; max-width: 80%;">
{items}
    </ul>
  </section>'''


def render_texto(s, active):
    sub = f'<div style="color: #4B5563; font-size: 1.1rem; margin-bottom: 25px;">{esc(s.get("subtitulo", ""))}</div>' if s.get('subtitulo') else ''
    items = '\n'.join(f'        <li style="margin-bottom: 12px;">{render_formula_content(c)}</li>' for c in s.get('contenido', []))
    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column;
    padding: 40px 60px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.8rem; font-weight: 600; margin: 0 0 20px 0;">
      {esc(s.get('titulo', ''))}
    </h2>
    {sub}
    <ul style="font-size: 1.15rem; color: #111827; line-height: 1.6; padding-left: 1.5em; flex-grow: 1;">
{items}
    </ul>
  </section>'''


def render_formula(s, active):
    sub = f'<div style="color: #4B5563; font-size: 1.1rem; margin-bottom: 25px;">{esc(s.get("subtitulo", ""))}</div>' if s.get('subtitulo') else ''
    items = '\n'.join(f'        <li style="margin-bottom: 14px;">{render_formula_content(c)}</li>' for c in s.get('contenido', []))
    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column;
    padding: 40px 60px;
  ">
    <h2 style="color: #1F4E79; font-size: 1.8rem; font-weight: 600; margin: 0 0 20px 0;">
      {esc(s.get('titulo', ''))}
    </h2>
    {sub}
    <ul style="font-size: 1.15rem; color: #111827; line-height: 1.8; padding-left: 1.5em; flex-grow: 1;">
{items}
    </ul>
  </section>'''


def render_agenda(s, active):
    items = '\n'.join(f'        <li style="margin-bottom: 15px;">{format_md(c)}</li>' for c in s.get('contenido', []))
    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column;
    padding: 50px 60px;
  ">
    <h2 style="color: #1F4E79; font-size: 2rem; font-weight: 600; margin: 0 0 30px 0;">
      {esc(s.get('titulo', ''))}
    </h2>
    <ul style="font-size: 1.3rem; color: #111827; line-height: 1.6; padding-left: 1.5em;">
{items}
    </ul>
  </section>'''


def render_seccion(s, active):
    sub = f'<div style="color: #E0F2FE; font-size: 1.5rem; margin-top: 20px;">{esc(s.get("subtitulo", ""))}</div>' if s.get('subtitulo') else ''
    return f'''
  <section class="slide{active}" style="
    background-color: #1F4E79;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
  ">
    <h1 style="color: #FFFFFF; font-size: 3.5rem; font-weight: 600; text-align: center; padding: 0 60px;">
      {esc(s.get('titulo', ''))}
    </h1>
    {sub}
  </section>'''


def render_grafico_texto(s, active):
    visual = s.get('visual', '')
    if visual and not visual.startswith('../'):
        visual = '../' + visual
    fuente = s.get('fuente', '')
    fuente_html = f'<div style="font-size: 0.7rem; color: #4B5563; font-style: italic; text-align: center; margin-top: 4px; flex-shrink: 0;">Fuente: {esc(fuente)}</div>' if fuente else ''
    items = '\n'.join(f'          <li style="margin-bottom: 6px;">{render_formula_content(c)}</li>' for c in s.get('contenido', []))
    layout = s.get('layout', '')
    if layout == 'portrait':
        img_pct = '33'
    else:
        img_pct = '62'
    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column;
    padding: 20px 35px 15px 35px;
    overflow: hidden;
    height: 100vh; width: 100vw;
  ">
    <h2 style="color: #1F4E79; font-size: 1.6rem; font-weight: 600; margin: 0 0 10px 0; flex-shrink: 0;">
      {esc(s.get('titulo', ''))}
    </h2>
    <div style="display: flex; flex: 1 1 auto; gap: 25px; min-height: 0; overflow: hidden;">
      <div style="width: {img_pct}%; flex-shrink: 0; display: flex; flex-direction: column; min-height: 0; overflow: hidden;">
        <img src="{visual}" alt="{esc(s.get('titulo', ''))}"
             style="max-width: 100%; flex: 1 1 auto; object-fit: contain; min-height: 0;">
        {fuente_html}
      </div>
      <div style="flex: 1 1 auto; min-width: 0; overflow-y: auto; padding-top: 5px;">
        <ul style="font-size: 0.9rem; color: #111827; line-height: 1.45; margin: 0; padding-left: 1.2em;">
{items}
        </ul>
      </div>
    </div>
  </section>'''


def render_cierre(s, active):
    sub = f'<div style="color: #4B5563; font-size: 1.3rem; margin-top: 20px;">{esc(s.get("subtitulo", ""))}</div>' if s.get('subtitulo') else ''
    return f'''
  <section class="slide{active}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    padding: 60px; text-align: center;
  ">
    <h1 style="color: #1F4E79; font-size: 3.5rem; font-weight: 600;">
      {esc(s.get('titulo', ''))}
    </h1>
    {sub}
  </section>'''


def render_grafico_progresivo(s, active):
    """Render progressive graphic slide with clickable steps."""
    pasos = s.get('pasos', [])
    if not pasos:
        return render_grafico_texto(s, active)
    fuente = s.get('fuente', '')
    fuente_html = f'<div style="font-size: 0.7rem; color: #4B5563; font-style: italic; text-align: center; margin-top: 4px;">Fuente: {esc(fuente)}</div>' if fuente else ''
    sub = f'<div style="color: #4B5563; font-size: 1rem; margin-bottom: 8px; flex-shrink: 0;">{esc(s.get("subtitulo", ""))}</div>' if s.get('subtitulo') else ''
    steps_html = []
    for i, paso in enumerate(pasos):
        visual = paso.get('visual', '')
        if visual and not visual.startswith('../'):
            visual = '../' + visual
        items = '\n'.join(f'            <li style="margin-bottom: 6px;">{render_formula_content(c)}</li>' for c in paso.get('contenido', []))
        display = 'flex' if i == 0 else 'none'
        steps_html.append(f'''      <div class="prog-step" data-step="{i}" style="display: {display}; flex: 1 1 auto; gap: 25px; min-height: 0; overflow: hidden;">
        <div style="width: 62%; flex-shrink: 0; display: flex; flex-direction: column; min-height: 0; overflow: hidden;">
          <img src="{visual}" alt="Paso {i+1}" style="max-width: 100%; flex: 1 1 auto; object-fit: contain; min-height: 0;">
          {fuente_html}
        </div>
        <div style="flex: 1 1 auto; min-width: 0; overflow-y: auto; padding-top: 5px;">
          <ul style="font-size: 0.9rem; color: #111827; line-height: 1.45; margin: 0; padding-left: 1.2em;">
{items}
          </ul>
        </div>
      </div>''')
    total_steps = len(pasos)
    return f'''
  <section class="slide{active}" data-steps="{total_steps}" style="
    background-color: #FFFFFF;
    display: flex; flex-direction: column;
    padding: 20px 35px 15px 35px;
    overflow: hidden;
    height: 100vh; width: 100vw;
  ">
    <h2 style="color: #1F4E79; font-size: 1.6rem; font-weight: 600; margin: 0 0 5px 0; flex-shrink: 0;">
      {esc(s.get('titulo', ''))}
    </h2>
    {sub}
{''.join(steps_html)}
    <div class="step-indicator" style="text-align: center; font-size: 0.8rem; color: #2E75B6; padding-top: 4px; flex-shrink: 0;">
      Paso <span class="step-current">1</span> / {total_steps}
    </div>
  </section>'''


RENDERERS = {
    'portada': render_portada,
    'centrado': render_centrado,
    'texto': render_texto,
    'formula': render_formula,
    'agenda': render_agenda,
    'seccion': render_seccion,
    'grafico_texto': render_grafico_texto,
    'grafico_progresivo': render_grafico_progresivo,
    'cierre': render_cierre,
}


# ============== HTML TEMPLATE ==============

HTML_HEAD = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Economía Internacional - Clase 1</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '\\\\(', right: '\\\\)', display: false}, {left: '\\\\[', right: '\\\\]', display: true}]});"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body {
      width: 100%; height: 100%; overflow: hidden;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }
    .slides-container { width: 100%; height: 100%; position: relative; }
    .slide {
      width: 100vw; height: 100vh;
      position: absolute; top: 0; left: 0;
      opacity: 0; visibility: hidden;
      transition: opacity 0.3s ease;
    }
    .slide.active { opacity: 1; visibility: visible; }
    .footer {
      position: fixed; bottom: 15px; left: 0; right: 0;
      display: flex; justify-content: space-between;
      padding: 0 25px; font-size: 0.85rem; color: #4B5563; z-index: 100;
    }
    body.print-mode { overflow: auto !important; height: auto !important; }
    body.print-mode .slides-container { height: auto !important; position: relative !important; }
    body.print-mode .slide {
      position: relative !important; opacity: 1 !important; visibility: visible !important;
      page-break-after: always !important; margin-bottom: 20px !important;
      border: 1px solid #e5e7eb !important; top: auto !important; left: auto !important;
    }
    body.print-mode .footer { display: none !important; }
    body.print-mode .prog-step { display: flex !important; }
    body.print-mode .step-indicator { display: none !important; }
    .print-banner {
      display: none; background: #1F4E79; color: white;
      padding: 10px 20px; text-align: center; font-size: 0.9rem;
    }
    body.print-mode .print-banner { display: block !important; position: relative !important; }
    @media print {
      * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
      html, body { overflow: visible !important; height: auto !important; }
      .slides-container { height: auto !important; display: block !important; }
      .slide {
        position: relative !important; opacity: 1 !important; visibility: visible !important;
        page-break-after: always !important; border: none !important; margin: 0 !important;
        top: auto !important; left: auto !important; width: 100% !important; height: 100vh !important;
      }
      .footer, .print-banner { display: none !important; }
      .prog-step { display: flex !important; }
      .step-indicator { display: none !important; }
    }
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
  <span>Economía Internacional | UMET | Clase 1</span>
  <span id="slide-counter">1 / {total}</span>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const counter = document.getElementById('slide-counter');
  let current = 0;
  let currentStep = 0;
  let printMode = false;
  const originalStyles = [];
  slides.forEach(s => originalStyles.push(s.getAttribute('style')));

  function getTotalSteps(idx) {{
    const attr = slides[idx].getAttribute('data-steps');
    return attr ? parseInt(attr) : 0;
  }}

  function showStep(slideIdx, stepIdx) {{
    const steps = slides[slideIdx].querySelectorAll('.prog-step');
    if (steps.length === 0) return;
    steps.forEach((s, i) => {{
      s.style.display = i === stepIdx ? 'flex' : 'none';
    }});
    const cur = slides[slideIdx].querySelector('.step-current');
    if (cur) cur.textContent = stepIdx + 1;
  }}

  function showSlide(n, fromEnd) {{
    slides[current].classList.remove('active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('active');
    const totalSteps = getTotalSteps(current);
    if (totalSteps > 0) {{
      currentStep = fromEnd ? totalSteps - 1 : 0;
      showStep(current, currentStep);
    }} else {{
      currentStep = 0;
    }}
    counter.textContent = `${{current + 1}} / ${{slides.length}}`;
  }}

  function advance() {{
    const totalSteps = getTotalSteps(current);
    if (totalSteps > 0 && currentStep < totalSteps - 1) {{
      currentStep++;
      showStep(current, currentStep);
      return;
    }}
    showSlide(current + 1, false);
  }}

  function goBack() {{
    const totalSteps = getTotalSteps(current);
    if (totalSteps > 0 && currentStep > 0) {{
      currentStep--;
      showStep(current, currentStep);
      return;
    }}
    showSlide(current - 1, true);
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
        s.style.position = 'relative'; s.style.opacity = '1'; s.style.visibility = 'visible';
        s.style.top = 'auto'; s.style.left = 'auto'; s.style.marginBottom = '30px';
        s.style.border = '2px solid #1F4E79'; s.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
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
      const totalSteps = getTotalSteps(current);
      if (totalSteps > 0) showStep(current, currentStep);
    }}
  }}

  document.addEventListener('keydown', (e) => {{
    if (printMode) {{ if (e.key === 'p' || e.key === 'P') togglePrintMode(); return; }}
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') advance();
    else if (e.key === 'ArrowLeft') goBack();
    else if (e.key === 'f' || e.key === 'F') document.documentElement.requestFullscreen?.();
    else if (e.key === 'Escape') document.exitFullscreen?.();
    else if (e.key === 'Home') showSlide(0, false);
    else if (e.key === 'End') showSlide(slides.length - 1, true);
    else if (e.key === 'p' || e.key === 'P') togglePrintMode();
  }});

  document.addEventListener('click', (e) => {{
    if (printMode) return;
    if (e.target.tagName !== 'A') {{
      if (e.clientX > window.innerWidth / 2) advance();
      else goBack();
    }}
  }});
</script>

</body>
</html>
'''


def main():
    md_text = INPUT_MD.read_text(encoding='utf-8')
    slides = parse_contenido_md(md_text)

    print(f"Slides parseados desde contenido.md: {len(slides)}")
    for i, s in enumerate(slides):
        tipo = s.get('tipo', '?')
        titulo = s.get('titulo', s.get('titulo_header', '?'))
        visual = s.get('visual', '')
        v = f'  [{visual}]' if visual else ''
        print(f"  {i+1:2d}. ({tipo}) {titulo}{v}")

    # Generar HTML
    parts = [HTML_HEAD]
    for i, s in enumerate(slides):
        tipo = s.get('tipo', 'texto')
        renderer = RENDERERS.get(tipo, render_texto)
        active = ' active' if i == 0 else ''
        parts.append(f'\n  <!-- SLIDE {i+1}: {esc(s.get("titulo", ""))} -->')
        parts.append(renderer(s, active))

    parts.append(HTML_FOOT.format(total=len(slides)))

    html = '\n'.join(parts)
    OUTPUT_HTML.write_text(html, encoding='utf-8')

    print(f"\nHTML generado: {OUTPUT_HTML}")
    print(f"Total slides: {len(slides)}")


if __name__ == "__main__":
    main()
