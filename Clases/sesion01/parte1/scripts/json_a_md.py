"""
Script para convertir JSON de slides a contenido.md
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INPUT_JSON = BASE_DIR / "datos" / "slides_clase1y2.json"
OUTPUT_MD = BASE_DIR / "contenido.md"


def main():
    # Leer JSON
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Construir MD
    lines = []

    # Header
    meta = data['metadata']
    lines.append(f"# {meta['titulo']}")
    lines.append("")
    lines.append("## Metadata")
    lines.append(f"- **Clase**: {meta['clase']}")
    lines.append(f"- **Duración**: {meta['duracion']}")
    lines.append(f"- **Total slides**: {meta['total_slides']}")
    lines.append("")
    lines.append("## Estado")
    lines.append("En desarrollo")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sección de recursos
    lines.append("## Recursos de la Clase")
    lines.append("")
    lines.append("### Gráficos (graficos/)")
    lines.append("| Archivo | Script generador |")
    lines.append("|---------|------------------|")

    # Obtener lista de gráficos del JSON
    graficos_usados = set()
    for slide in data['slides']:
        visual = slide.get('visual')
        if visual and visual.startswith('graficos/'):
            graficos_usados.add(visual.replace('graficos/', ''))

    scripts_graficos = {
        'indice_comercio.png': 'pendiente',
        'participacion_regional.png': 'pendiente',
        'hhi.png': 'pendiente',
        'cobertura.png': 'pendiente',
        'indice_colapso.png': 'pendiente',
        'balanza_comercial_argentina.png': 'generar_graficos_indicadores.py',
        'balanza_comercial_comparativo.png': 'generar_graficos_indicadores.py',
        'apertura_comercial.png': 'generar_graficos_indicadores.py',
        'tot_argentina.png': 'generar_graficos_indicadores.py',
        'cc_argentina.png': 'generar_graficos_bp.py',
        'desequilibrios_globales.png': 'generar_graficos_bp.py',
        'tcr_argentina.png': 'generar_graficos_bp.py',
        'reservas_argentina.png': 'generar_graficos_bp.py',
    }

    for grafico in sorted(graficos_usados):
        script = scripts_graficos.get(grafico, 'desconocido')
        lines.append(f"| {grafico} | {script} |")

    lines.append("")
    lines.append("### Scripts (scripts/)")
    lines.append("- `actualizar_agenda.py` - Actualiza agenda automáticamente")
    lines.append("- `generar_html.py` - JSON → HTML")
    lines.append("- `json_a_md.py` - JSON → Markdown")
    lines.append("- `generar_graficos_bp.py` - Gráficos BP")
    lines.append("- `generar_graficos_indicadores.py` - Gráficos indicadores 5-7")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Slides
    current_section = None

    for slide in data['slides']:
        numero = slide['numero']
        tipo = slide['tipo']
        titulo = slide['titulo']
        subtitulo = slide.get('subtitulo')
        contenido = slide.get('contenido', [])
        visual = slide.get('visual')
        fuente = slide.get('fuente')
        notas = slide.get('notas_docente', '')

        # Separador de sección si es tipo seccion
        if tipo == 'seccion':
            lines.append("---")
            lines.append("")
            lines.append(f"# BLOQUE: {titulo}")
            if subtitulo:
                lines.append(f"*{subtitulo}*")
            lines.append("")
            current_section = titulo

            if notas:
                lines.append("### Notas docente")
                lines.append("```")
                lines.append(notas)
                lines.append("```")
                lines.append("")
            continue

        # Slide normal
        lines.append(f"## Slide {numero}: {titulo}")
        lines.append(f"**Tipo**: {tipo}")
        if subtitulo:
            lines.append(f"**Subtítulo**: {subtitulo}")
        lines.append("")

        # Contenido
        if contenido:
            lines.append("### Contenido")
            for item in contenido:
                lines.append(f"- {item}")
            lines.append("")

        # Visual
        if visual:
            lines.append("### Visual")
            lines.append(f"![{titulo}]({visual})")
            if fuente:
                lines.append(f"*Fuente: {fuente}*")
            lines.append("")

        # Notas docente
        if notas:
            lines.append("### Notas docente")
            lines.append("```")
            lines.append(notas)
            lines.append("```")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Escribir MD
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Convertido: {OUTPUT_MD}")
    print(f"Total slides: {len(data['slides'])}")


if __name__ == "__main__":
    main()
