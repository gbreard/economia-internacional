"""
Transfiere notas docente de slides_clase2.json a contenido.md
"""
import json, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
JSON_FILE = BASE_DIR / "datos" / "slides_clase2.json"
MD_FILE = BASE_DIR / "contenido.md"

# Leer JSON
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

notas_por_numero = {}
for slide in data['slides']:
    notas_por_numero[slide['numero']] = slide.get('notas_docente', '')

# Leer contenido.md
md_text = MD_FILE.read_text(encoding='utf-8')

# Para cada slide, insertar notas docente antes del separador ---
# Pattern: #### Slide N: ... (contenido) ... ---
lines = md_text.split('\n')
output = []
current_slide_num = None
i = 0

while i < len(lines):
    line = lines[i]

    # Detectar inicio de slide
    slide_match = re.match(r'^####\s+Slide\s+(\d+)\s*:', line)
    if slide_match:
        current_slide_num = int(slide_match.group(1))

    # Detectar separador --- (fin del slide)
    if line.strip() == '---' and current_slide_num is not None:
        # Insertar notas docente antes del ---
        notas = notas_por_numero.get(current_slide_num, '')
        if notas:
            # Agregar línea en blanco si la anterior no lo es
            if output and output[-1].strip() != '':
                output.append('')
            output.append('**Notas docente**:')
            output.append(notas)
            output.append('')
        current_slide_num = None

    output.append(line)
    i += 1

# Escribir resultado
result = '\n'.join(output)
MD_FILE.write_text(result, encoding='utf-8')

# Verificar
count = result.count('**Notas docente**:')
print(f"Notas docente insertadas: {count}")
print(f"Slides en JSON: {len(data['slides'])}")
