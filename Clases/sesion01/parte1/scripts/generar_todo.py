"""
Genera HTML y MD para ambas clases.
"""

import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def generar_clase(num_clase):
    """Genera HTML y MD para una clase."""
    json_file = BASE_DIR / "datos" / f"slides_clase{num_clase}.json"
    html_file = BASE_DIR / "presentacion" / f"clase{num_clase}.html"
    md_file = BASE_DIR / f"contenido_clase{num_clase}.md"

    # Leer JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    meta = data['metadata']
    slides = data['slides']

    print(f"\n{'='*60}")
    print(f"CLASE {num_clase}: {meta['titulo']}")
    print(f"Pregunta central: {meta['pregunta_central']}")
    print(f"Total slides: {meta['total_slides']}")
    print(f"{'='*60}")

    # Mostrar estructura
    for s in slides:
        visual = 'G' if s.get('visual') else '-'
        print(f"  {s['numero']:2d}. [{visual}] {s['titulo'][:50]}")

    return len(slides)


def main():
    total = 0
    for i in [1, 2]:
        total += generar_clase(i)

    print(f"\n{'='*60}")
    print(f"TOTAL: {total} slides en 2 clases")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
